from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from .common import canonical_hash
from .signing import verify


SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE authority(singleton INTEGER PRIMARY KEY CHECK(singleton=1), epoch TEXT NOT NULL,
  version INTEGER NOT NULL, grant_id TEXT NOT NULL, status TEXT NOT NULL, lease TEXT NOT NULL,
  scope TEXT NOT NULL, action TEXT NOT NULL, instance_id TEXT NOT NULL, source_hash TEXT NOT NULL,
  policy_hash TEXT NOT NULL);
CREATE TABLE operations(operation_id TEXT PRIMARY KEY, proposal_hash TEXT NOT NULL, result TEXT NOT NULL);
CREATE TABLE effects(effect_id TEXT PRIMARY KEY, operation_id TEXT UNIQUE NOT NULL, cell_id TEXT NOT NULL, payload TEXT NOT NULL);
CREATE TABLE promotions(promotion_id TEXT PRIMARY KEY, cell_id TEXT NOT NULL, payload TEXT NOT NULL);
CREATE TABLE revocations(seq INTEGER PRIMARY KEY AUTOINCREMENT, grant_id TEXT NOT NULL, ack_event_seq INTEGER NOT NULL);
CREATE TABLE source_bindings(seq INTEGER PRIMARY KEY AUTOINCREMENT, source_id TEXT UNIQUE NOT NULL,
  source_hash TEXT UNIQUE NOT NULL, predecessor_source_hash TEXT, transition TEXT NOT NULL);
"""


def build_operation_intent(
    operation_id: str,
    cell_id: str,
    proposal_hash: str,
    source: dict[str, Any],
    instance_id: str,
    attempt_id: str,
    checkpoint: str,
    commit_record_id: str,
    *,
    expect_effect: bool,
) -> dict[str, Any]:
    """Freeze the authorized operation and expected row before SQL readback.

    The returned object is derived from trusted source/proposal context only.  It
    never accepts an observed database row as input.
    """
    policy = source["trusted_policy"]
    resolution = source.get("resolution")
    scope = {
        "task_id": policy["task_id"],
        "action": policy["protected_action"],
        "operation_id": operation_id,
        "cell_id": cell_id,
        "attempt_id": attempt_id,
        "checkpoint": checkpoint,
        "instance_id": instance_id,
        "commit_record_id": commit_record_id,
    }
    basis = {
        "proposal_hash": proposal_hash,
        "source_id": source["source_id"],
        "source_hash": source["source_hash"],
        "source_resolution_hash": canonical_hash(resolution) if isinstance(resolution, dict) else None,
        "policy_hash": canonical_hash(policy),
    }
    payload = {
        "kind": "SYNTHETIC_ACCEPT",
        **scope,
        **basis,
    }
    expected_effect_row = {
        "effect_id": f"effect:{operation_id}",
        "operation_id": operation_id,
        "cell_id": cell_id,
        "payload": payload,
    } if expect_effect else None
    return {
        "intent_version": "CGDR_OPERATION_INTENT_V1",
        "capture_stage": "PRE_COMMIT",
        "effect_expectation": "EXACTLY_ONE" if expect_effect else "NO_EFFECT",
        "scope": scope,
        "basis": basis,
        "expected_effect_row": expected_effect_row,
    }


class Broker:
    def __init__(self, path: Path):
        self.path = path
        if path.exists():
            raise FileExistsError(f"refusing existing broker database: {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, isolation_level=None)
        self.db.executescript(SCHEMA)

    def bind_instance(self, source: dict[str, Any], instance_id: str) -> None:
        r, policy = source["registry"], source["trusted_policy"]
        self.db.execute("BEGIN IMMEDIATE")
        try:
            self.db.execute(
                "INSERT INTO authority VALUES(1,?,?,?,?,?,?,?,?,?,?)",
                (r["epoch"], r["authority_version"], r["grant_id"], r["grant_status"], r["lease"],
                 r["scope"], r["task"], instance_id, source["source_hash"], canonical_hash(policy)),
            )
            self.db.execute(
                "INSERT INTO source_bindings(source_id,source_hash,predecessor_source_hash,transition) VALUES(?,?,?,?)",
                (source["source_id"], source["source_hash"], None, "INITIAL_SOURCE_FREEZE"),
            )
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def advance_source(self, source: dict[str, Any], instance_id: str) -> None:
        """Append one source-derived clarification without changing authority or instance scope."""
        self.db.execute("BEGIN IMMEDIATE")
        try:
            row = self.db.execute(
                "SELECT epoch,version,grant_id,status,lease,scope,action,instance_id,source_hash,policy_hash "
                "FROM authority WHERE singleton=1"
            ).fetchone()
            registry, policy = source["registry"], source["trusted_policy"]
            lineage = source.get("source_lineage") or {}
            expected_prefix = (
                registry["epoch"], registry["authority_version"], registry["grant_id"], "VALID",
                registry["lease"], registry["scope"], registry["task"], instance_id,
            )
            if (
                row is None
                or row[:8] != expected_prefix
                or row[9] != canonical_hash(policy)
                or lineage.get("predecessor_source_hash") != row[8]
                or lineage.get("transition") != "SCOPED_CLARIFICATION_APPEND"
            ):
                raise ValueError("SOURCE_ADVANCE_BINDING_MISMATCH")
            self.db.execute(
                "INSERT INTO source_bindings(source_id,source_hash,predecessor_source_hash,transition) VALUES(?,?,?,?)",
                (source["source_id"], source["source_hash"], row[8], lineage["transition"]),
            )
            self.db.execute("UPDATE authority SET source_hash=? WHERE singleton=1", (source["source_hash"],))
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def revoke(self, grant_id: str, ack_event_seq: int) -> dict[str, Any]:
        self.db.execute("BEGIN IMMEDIATE")
        try:
            self.db.execute("UPDATE authority SET status='REVOKED' WHERE grant_id=?", (grant_id,))
            cursor = self.db.execute("INSERT INTO revocations(grant_id,ack_event_seq) VALUES(?,?)", (grant_id, ack_event_seq))
            self.db.commit()
            return {"seq": cursor.lastrowid, "grant_id": grant_id, "ack_event_seq": ack_event_seq}
        except Exception:
            self.db.rollback()
            raise

    def atomic_commit(
        self,
        operation_id: str,
        cell_id: str,
        proposal_hash: str,
        decision: dict[str, Any],
        source: dict[str, Any],
        instance_id: str,
        *,
        operation_context: dict[str, Any] | None = None,
        proposal_envelope: dict[str, Any] | None = None,
        public_signer_map: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        self.db.execute("BEGIN IMMEDIATE")
        try:
            duplicate = self.db.execute("SELECT result FROM operations WHERE operation_id=?", (operation_id,)).fetchone()
            if duplicate:
                self.db.commit()
                return {"result": "DUPLICATE_NO_EFFECT", "effect_delta": 0, "atomic_revalidation": True,
                        "final_action_gate": "HOLD"}
            row = self.db.execute(
                "SELECT epoch,version,grant_id,status,lease,scope,action,instance_id,source_hash,policy_hash FROM authority WHERE singleton=1"
            ).fetchone()
            r, policy = source["registry"], source["trusted_policy"]
            expected = (r["epoch"], r["authority_version"], r["grant_id"], "VALID", r["lease"],
                        r["scope"], r["task"], instance_id, source["source_hash"], canonical_hash(policy))
            binding = decision.get("verified_binding") or {}
            resolution = source.get("resolution")
            context = operation_context or {}
            proposal = (proposal_envelope or {}).get("payload") or {}
            attempt_id = proposal.get("attempt_id")
            checkpoint = proposal.get("checkpoint")
            commit_record_id = proposal.get("commit_record_id")
            expected_intent = build_operation_intent(
                operation_id,
                cell_id,
                proposal_hash,
                source,
                instance_id,
                attempt_id,
                checkpoint,
                commit_record_id,
                expect_effect=decision.get("action_gate") == "ALLOW",
            ) if all(isinstance(value, str) and value for value in (attempt_id, checkpoint, commit_record_id)) else {}
            expected_scope = expected_intent.get("scope") or {}
            required_scope_fields = {
                "task_id", "action", "operation_id", "cell_id", "attempt_id",
                "checkpoint", "instance_id", "commit_record_id",
            }
            scope_complete = set(expected_scope) == required_scope_fields and all(
                isinstance(value, str) and value for value in expected_scope.values()
            )
            expected_binding = {
                "task_id": policy["task_id"], "action": policy["protected_action"], "source_hash": source["source_hash"],
                "source_resolution_hash": canonical_hash(resolution) if isinstance(resolution, dict) else None,
                "checkpoint": expected_scope.get("checkpoint"), "attempt_id": expected_scope.get("attempt_id"),
                "instance_id": instance_id, "operation_id": operation_id,
                "commit_record_id": expected_scope.get("commit_record_id"),
                "proposal_hash": proposal_hash, "policy_hash": canonical_hash(policy),
            }
            signed_ok, signed_reason = verify(proposal_envelope or {}, public_signer_map or {})
            unhashed = dict(proposal) if isinstance(proposal, dict) else {}
            unhashed.pop("proposal_hash", None)
            proposal_scope_ok = bool(
                signed_ok
                and proposal.get("proposal_hash") == proposal_hash
                and canonical_hash(unhashed) == proposal_hash
                and all(
                    proposal.get(name) == expected_scope[name]
                    for name in (
                        "task_id", "action", "cell_id", "attempt_id", "checkpoint",
                        "instance_id", "operation_id", "commit_record_id",
                    )
                )
                and proposal.get("source_hash") == source["source_hash"]
                and binding.get("verified_approval_roots") == sorted(set(binding.get("verified_approval_roots", [])))
            )
            binding_ok = bool(
                scope_complete
                and context == expected_intent
                and proposal_scope_ok
                and all(binding.get(name) == value for name, value in expected_binding.items())
            )
            authority_fields = (
                "epoch", "version", "grant_id", "status", "lease", "scope",
                "action", "instance_id", "source_hash", "policy_hash",
            )
            # Both readbacks occur inside this existing BEGIN IMMEDIATE.
            # Context agreement alone cannot attest current authority.
            authority_at_bind = None if row is None else dict(zip(authority_fields, row))
            revocations_at_bind = [
                {"seq": seq, "grant_id": grant, "ack_event_seq": ack}
                for seq, grant, ack in self.db.execute(
                    "SELECT seq,grant_id,ack_event_seq FROM revocations ORDER BY seq"
                ).fetchall()
            ]
            failures: list[dict[str, Any]] = []
            for valid, reason in (
                (scope_complete, "OPERATION_SCOPE_INCOMPLETE"),
                (context == expected_intent, "OPERATION_INTENT_MISMATCH"),
                (signed_ok, "SIGNED_PROPOSAL_INVALID"),
                (proposal_scope_ok, "PROPOSAL_SCOPE_MISMATCH"),
                (all(binding.get(name) == value for name, value in expected_binding.items()), "RECEIVER_BINDING_MISMATCH"),
            ):
                if not valid:
                    failures.append({"plane": "OPERATION_BINDING", "reason": reason})
            if row is None:
                failures.append({"plane": "CURRENT_AUTHORITY", "reason": "AUTHORITY_ROW_MISSING"})
            elif row != expected:
                changed = [name for name, actual, required in zip(authority_fields, row, expected) if actual != required]
                reason = "CURRENT_GRANT_REVOKED_AT_BIND" if changed == ["status"] and row[3] == "REVOKED" else "CURRENT_AUTHORITY_BINDING_MISMATCH"
                failures.append({"plane": "CURRENT_AUTHORITY", "reason": reason, "fields": changed})
            gate, result, delta = decision.get("action_gate"), "HELD", 0
            if gate == "ALLOW" and row == expected and binding_ok:
                intended_row = expected_intent["expected_effect_row"]
                self.db.execute(
                    "INSERT INTO effects VALUES(?,?,?,?)",
                    (
                        intended_row["effect_id"],
                        operation_id,
                        cell_id,
                        json.dumps(intended_row["payload"], sort_keys=True, separators=(",", ":")),
                    ),
                )
                result, delta = "BOUND", 1
            elif gate == "ALLOW":
                result = "DENIED_ATOMIC_REVALIDATION"
            elif gate == "DENY":
                result = "DENIED"
            self.db.execute("INSERT INTO operations VALUES(?,?,?)", (operation_id, proposal_hash, result))
            self.db.commit()
            return {
                "result": result,
                "effect_delta": delta,
                "atomic_revalidation": True,
                "binding_revalidated": binding_ok,
                "operation_binding_revalidated": binding_ok,
                "current_authority_binding": row == expected,
                "revalidation_failures": failures,
                "authority_at_bind": authority_at_bind,
                "revocations_at_bind": revocations_at_bind,
                "precommit_action_gate": gate,
                "final_action_gate": "ALLOW" if result == "BOUND" else ("HOLD" if result == "HELD" else "DENY"),
                "signed_proposal_status": "VALID" if signed_ok else signed_reason,
                "operation_context": expected_scope,
                "operation_intent": expected_intent,
                "operation_intent_hash": canonical_hash(expected_intent) if expected_intent else None,
            }
        except Exception:
            self.db.rollback()
            raise

    def counts(self) -> dict[str, int]:
        return {"effects": self.db.execute("SELECT count(*) FROM effects").fetchone()[0],
                "promotions": self.db.execute("SELECT count(*) FROM promotions").fetchone()[0]}

    def snapshot(self) -> dict[str, Any]:
        effects = []
        for effect_id, operation_id, cell_id, payload in self.db.execute(
            "SELECT effect_id,operation_id,cell_id,payload FROM effects ORDER BY effect_id"
        ).fetchall():
            effects.append({
                "effect_id": effect_id,
                "operation_id": operation_id,
                "cell_id": cell_id,
                "payload": json.loads(payload),
            })
        return {
            "authority": self.db.execute("SELECT * FROM authority ORDER BY singleton").fetchall(),
            "operations": self.db.execute("SELECT * FROM operations ORDER BY operation_id").fetchall(),
            "effects": effects,
            "promotions": self.db.execute("SELECT * FROM promotions ORDER BY promotion_id").fetchall(),
            "revocations": self.db.execute("SELECT * FROM revocations ORDER BY seq").fetchall(),
            "source_bindings": [
                {"seq": row[0], "source_id": row[1], "source_hash": row[2], "predecessor_source_hash": row[3], "transition": row[4]}
                for row in self.db.execute(
                    "SELECT seq,source_id,source_hash,predecessor_source_hash,transition FROM source_bindings ORDER BY seq"
                ).fetchall()
            ],
        }

    def close(self) -> None:
        self.db.close()
