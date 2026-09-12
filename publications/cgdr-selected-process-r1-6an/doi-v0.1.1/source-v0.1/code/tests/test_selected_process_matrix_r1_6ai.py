from __future__ import annotations

import ast
import copy
import hashlib
import inspect
import json
import os
import tempfile
import unittest
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from cgdr_r1_6b import observer, producer, run_batch
from cgdr_r1_6b.broker import Broker
from cgdr_r1_6b.common import canonical_hash
from cgdr_r1_6b.receiver import evaluate
from cgdr_r1_6b.signing import TestKeyStore, sign
from cgdr_r1_6b.observer_fixtures import positive_trace
from cgdr_r1_6b.logic_path import execute as logic_execute
from cgdr_r1_6b.prospective_observation import review_observation_evidence


NEGATIVE_CELLS = ("T1", "T2Q", "T2D", "T3", "T4S", "T4R", "T5A", "T5E", "T6", "T7", "T8", "T9", "T10", "T11W", "T11E")


class MemoryKeys(TestKeyStore):
    def __init__(self):
        self.keys = {}

    def ensure(self, name):
        if name not in self.keys:
            self.keys[name] = Ed25519PrivateKey.generate()
        return self.keys[name]


class SelectedProcessMatrixR16AITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input = Path(os.environ["CGDR_AI_INPUT"]).resolve()
        matrix_path = cls.input / "profile/TRANSITION_TEST_MATRIX.json"
        assert hashlib.sha256(matrix_path.read_bytes()).hexdigest() == "7288a4e60501d1c8209308dacc4450e3d046f20b51ad5a8ad05f9010b4239a60"
        cls.matrix = json.loads(matrix_path.read_text())
        cls.expected = {(cell["cell_id"], row["checkpoint"]): row for cell in cls.matrix["cells"] for row in cell["expected_checkpoints"]}
        cls.roots = {p.name.split("_", 1)[1]: p for p in (cls.input / "ag_episode_evidence").iterdir() if p.is_dir()}
        cls.keys = MemoryKeys()
        cls.public = cls.keys.public_map({"producer-alpha": "root:alpha", "approver-beta": "root:beta", "alias-alpha-1": "root:alpha", "alias-alpha-2": "root:alpha"})
        cls.results = []

    @classmethod
    def tearDownClass(cls):
        output = os.environ.get("CGDR_AI_SEMANTIC_RESULT")
        if output:
            Path(output).write_text(json.dumps({"status": "PROCESS_FREE_TEST_RECORDS_ONLY", "records": cls.results, "historical_ag_score": "13_PASS_5_FAIL", "adjusted_score": "NOT_COMPUTED", "new_runtime": 0}, indent=2) + "\n", encoding="utf-8")

    def raw(self, cell, checkpoint=None):
        paths = list((self.roots[cell] / "raw").glob("*.json"))
        if checkpoint is not None:
            paths = [p for p in paths if p.stem == checkpoint]
        self.assertEqual(len(paths), 1)
        return json.loads(paths[0].read_text(encoding="utf-8"))

    def record(self, cell):
        return json.loads((self.roots[cell] / "EPISODE_RESULT.json").read_text(encoding="utf-8"))

    def rules(self, e):
        return {r["requirement_id"]: r for r in observer.inspect_checkpoint(e)["assertions"]}

    def sign_proposal(self, proposal, aliases=False):
        proposal = copy.deepcopy(proposal)
        proposal.pop("proposal_hash", None)
        proposal["proposal_hash"] = canonical_hash(proposal)
        envelope = sign(proposal, "producer-alpha", self.keys.ensure("producer-alpha"), "root:alpha")
        approvals = []
        resolution = proposal.get("resolution")
        if isinstance(resolution, dict) and resolution:
            payload = {name: proposal[name] for name in ("task_id", "action", "checkpoint", "instance_id", "attempt_id", "operation_id", "commit_record_id")}
            payload["source_resolution_hash"] = canonical_hash(resolution)
            bindings = [("producer-alpha", "root:alpha"), ("alias-alpha-1", "root:alpha"), ("alias-alpha-2", "root:alpha")] if aliases else [("producer-alpha", "root:alpha"), ("approver-beta", "root:beta")]
            approvals = [sign(payload, name, self.keys.ensure(name), root) for name, root in bindings]
        body = {"envelope": envelope, "approvals": approvals}
        return {**body, "transport_hash": canonical_hash(body)}

    def make(self, cell, neutral=False, checkpoint=None, context_mutator=None):
        """Counterfactual in memory + disposable SQLite, never a matrix episode."""
        e = self.raw(cell, checkpoint)
        source = copy.deepcopy(e["source_inventory"])
        if neutral:
            if cell == "T4R": source["registry"]["grant_status"] = "VALID"
            elif cell == "T9": source["semantic_clock"]["tick"] = 10
            elif cell == "T11W": source["a6_conditions"]["window"]["status"] = "CLOSED"
            elif cell == "T11E": source["a6_conditions"]["escalation"]["status"] = "RESOLVED_BY_COMPETENT_SOURCE"
            source.pop("source_hash", None)
            source["source_hash"] = canonical_hash(source)
        args = (source, cell, e["checkpoint"], e["active_instance_id"], e["attempt_id"], e["operation_id"], e["commit_record_id"])
        if neutral:
            packet = self.sign_proposal(producer._projection(*args))
        else:
            packet = producer.make_packet(cell, source, self.keys, e["checkpoint"], instance_id=e["active_instance_id"], attempt_id=e["attempt_id"], operation_id=e["operation_id"], commit_record_id=e["commit_record_id"])
        proposal = packet["envelope"]["payload"]
        decision = evaluate(packet, source, self.public)
        intent = run_batch.precommit_operation_intent(proposal, source, decision)
        submitted = copy.deepcopy(intent)
        if context_mutator:
            context_mutator(submitted)
        timeline = []
        start = e["observation_interval"]["start_ns"]
        end = e["observation_interval"]["end_ns"]
        self.assertGreater(end - start, 2)
        with tempfile.TemporaryDirectory(prefix="ai-causal-sqlite-") as temporary:
            broker = Broker(Path(temporary) / "control.sqlite3")
            try:
                broker.bind_instance(source, e["active_instance_id"])
                before = broker.snapshot()
                if cell == "T10" and not neutral:
                    revocation = broker.revoke(source["registry"]["grant_id"], 7)
                    timeline.append({"kind": "REVOCATION_ACKNOWLEDGED", "host_ns": start + 1, "scope": copy.deepcopy(intent["scope"]), "revocation": revocation})
                commit = broker.atomic_commit(e["operation_id"], cell, proposal["proposal_hash"], decision, source, e["active_instance_id"], operation_context=submitted, proposal_envelope=packet["envelope"], public_signer_map=self.public)
                if timeline:
                    timeline.append({"kind": "ATOMIC_BIND_COMPLETED", "host_ns": end - 1, "scope": copy.deepcopy(intent["scope"])})
                after = broker.snapshot()
            finally:
                broker.close()
        e.update(
            source_inventory=source, current_registry=copy.deepcopy(source["registry"]),
            materialized_packet=proposal, materialized_packet_hash=canonical_hash(proposal),
            proposal_hash=proposal["proposal_hash"], proposal_envelope=packet["envelope"],
            approval_envelopes=packet["approvals"], public_signer_map=self.public,
            supplied_decision=decision, precommit_receiver_decision=copy.deepcopy(decision),
            final_action_gate=run_batch.final_action_outcome(decision, commit),
            operation_intent=submitted, operation_intent_hash=canonical_hash(submitted),
            commit_evidence=commit, broker_before_snapshot=before, broker_after_snapshot=after,
            atomic_transition_chronology=timeline,
            sink_before_snapshot={k: before[k] for k in ("operations", "effects", "promotions")},
            sink_after_snapshot={k: after[k] for k in ("operations", "effects", "promotions")},
            counterfactual_origin="AI_PROCESS_FREE_CONTROL_USING_SAVED_AG_COORDINATES",
        )
        return e

    def alignment(self, e):
        cell = e["cell_id"]
        mode = e["lifecycle_mode"]
        opened = observer.inspect_checkpoint(e)
        return {
            "matrix_run_id": e["matrix_run_id"], "cell_id": cell, "attempt_id": e["attempt_id"], "checkpoint": e["checkpoint"],
            "lifecycle_mode": mode, "lifecycle_steps": self.record(cell)["lifecycle_steps"],
            "w0_instance_id": e["expected_w0_lifecycle_binding"]["instance_id"],
            "w1_instance_id": e["active_instance_id"] if mode == "REPLACE_PROCESS" else None,
            "active_instance_id": e["active_instance_id"], "w0_cleanup": "PROVEN", "state_carriage": "PASS",
            "current_epoch": "E1", "e0_status": "HISTORICAL_FENCED" if mode == "REPLACE_PROCESS" else "NOT_APPLICABLE",
            "readiness": "READY", "implementation_freeze": "BEFORE_FIRST_WORKER_START", "capture_gaps": [],
            "writer_admission": "ADMITTED", "expected_effect_delta": self.expected[(cell, e["checkpoint"])]["protected_effect_delta"],
            "actual_effect_delta": opened["actual_effect_delta"], "expected_promotion_delta": 0,
            "actual_promotion_delta": opened["actual_promotion_delta"], "approval_roots": opened["derived_gate"]["approvals"].get("roots", []),
            "required_approval_roots": e["source_inventory"]["trusted_policy"]["required_approval_roots"],
            "q_state": opened["derived_gate"]["q_state"], "qcr_valid": bool(e["source_inventory"].get("resolution")),
            "expected_obligations": e["source_inventory"]["duty"]["liabilities"],
            "carried_obligations": (e["materialized_packet"].get("duty") or {}).get("liabilities"),
            "evidence_binding": {k: e[k] for k in ("matrix_run_id", "cell_id", "attempt_id", "checkpoint")},
            "attempt_coverage_complete": True, "registry_coverage_complete": True,
            "surface_inventory": e["surface_observations"],
        }

    def review(self, e, *, linked=None, expected=None, alignment=None, prospective=True, cleanup=None):
        cell = e["cell_id"]
        observation = json.loads((self.roots[cell] / "prospective_observation/OBSERVATION_EVIDENCE.json").read_text(encoding="utf-8")) if prospective else None
        cleanup = cleanup or {"scope": {k: e[k] for k in ("task_id", "attempt_id", "active_instance_id")}, "w0": "PROVEN", "w1": "PROVEN" if e["lifecycle_mode"] == "REPLACE_PROCESS" else None}
        result = run_batch.review_profile_assertion(e, expected or self.expected[(cell, e["checkpoint"])], alignment or self.alignment(e), prospective_evidence=observation, cleanup=cleanup, linked_evidence=linked)
        self.results.append({"test": self.id(), "cell": cell, "checkpoint": e["checkpoint"], "profile_assertion": result["profile_assertion"], "fault_detection": result["fault_detection"], "actual": result["actual"], "candidate_fails": [r["requirement_id"] for r in result["candidate_assertions"]["assertions"] if r["value"] == "FAIL"]})
        return result

    def assert_profile(self, cell, neutral=False):
        e = self.make(cell, neutral)
        result = self.review(e)
        if neutral:
            self.assertEqual(result["profile_assertion"]["verdict"], "FAIL", result)
            self.assertIn("EXPECTED_FAULT_NOT_OBSERVED", result["profile_assertion"]["issues"], result)
        else:
            self.assertEqual(result["profile_assertion"]["verdict"], "PASS", result)
            self.assertEqual(result["fault_detection"]["status"], "OBSERVED_AND_CONTAINED", result)
            self.assertEqual(result["actual"], {k: self.expected[(cell, e["checkpoint"])][k] for k in result["actual"]})
        return e, result

    def assert_n1_bad(self, mutate):
        e = self.raw("N1", "OPEN_CHECK")
        mutate(e)
        self.assertEqual(self.rules(e)["R06"]["value"], "FAIL")

    def assert_atomic_bad(self, mutate):
        e = self.make("T10")
        mutate(e)
        result = observer.inspect_checkpoint(e)
        self.assertNotEqual(result["atomic_denial_review"]["status"], "PASS", result)
        self.assertNotEqual(self.review(e)["profile_assertion"]["verdict"], "PASS")

    def test_ai01_exact_n1_open(self):
        result = observer.inspect_checkpoint(self.raw("N1", "OPEN_CHECK"))
        self.assertEqual(result["observer_status"], "INCONCLUSIVE")
        self.assertEqual(result["problems"], [])
        self.assertEqual([(r["requirement_id"],r["reason"]) for r in result["assertions"] if r["value"] == "UNKNOWN"], [("R28","RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD")])
        self.assertFalse([r for r in result["assertions"] if r["value"] == "FAIL"])

    def test_ai02_exact_n1_resolved(self):
        result = observer.inspect_checkpoint(self.raw("N1", "RESOLVED_CHECK"))
        self.assertEqual(result["observer_status"], "PASS")
        self.assertEqual(result["problems"], [])

    def test_ai03_exact_n1_linked_profile(self):
        pair = (self.raw("N1","OPEN_CHECK"), self.raw("N1","RESOLVED_CHECK"))
        linked = observer.inspect_logic_path(*pair)
        self.assertEqual(linked["offline_logic_path_status"], "PASS")
        self.assertTrue(all(linked["checks"].values()))
        for e in pair:
            self.assertEqual(self.review(e,linked=pair)["profile_assertion"]["verdict"], "PASS")

    def test_ai04_missing_released(self):
        self.assert_n1_bad(lambda e: e.__setitem__("trusted_chronology", [x for x in e["trusted_chronology"] if (x.get("worker_event") or {}).get("event") != "RELEASED"]))

    def test_ai05_missing_continued(self):
        self.assert_n1_bad(lambda e: e.__setitem__("trusted_chronology", [x for x in e["trusted_chronology"] if (x.get("worker_event") or {}).get("event") != "CONTINUED"]))

    def test_ai06_wrong_ack_order(self):
        def mutate(e):
            events = e["trusted_chronology"]
            a = next(i for i,x in enumerate(events) if (x.get("worker_event") or {}).get("event") == "RELEASED")
            b = next(i for i,x in enumerate(events) if (x.get("worker_event") or {}).get("event") == "CONTINUED")
            events[a], events[b] = events[b], events[a]
        self.assert_n1_bad(mutate)

    def test_ai07_sent_commands_not_acknowledgements(self):
        def mutate(e):
            for x in e["trusted_chronology"]:
                if (x.get("worker_event") or {}).get("event") in {"RELEASED","CONTINUED"}:
                    x["kind"] = "IPC_SENT"
        self.assert_n1_bad(mutate)

    def test_ai08_wrong_wrapper_nested_event(self):
        def mutate(e):
            for x in e["trusted_chronology"]:
                if (x.get("worker_event") or {}).get("event") == "RELEASED":
                    x["kind"] = "UNRELATED_LIFECYCLE_RECORD"
        self.assert_n1_bad(mutate)

    def test_ai09_foreign_ack_scope_or_instance(self):
        for field in ("task_id","attempt_id","checkpoint","instance_id"):
            def mutate(e):
                x = next(x for x in e["trusted_chronology"] if (x.get("worker_event") or {}).get("event") == "RELEASED")
                x[field] = "foreign"
            self.assert_n1_bad(mutate)
        def inner(e):
            next(x for x in e["trusted_chronology"] if (x.get("worker_event") or {}).get("event") == "RELEASED")["worker_event"]["instance_id"] = "foreign"
        self.assert_n1_bad(inner)

    def test_ai10_t1_exact_discriminating_profile(self):
        self.assert_profile("T1")

    def test_ai11_t2q_exact_discriminating_profile(self):
        self.assert_profile("T2Q")

    def test_ai12_t2d_exact_discriminating_profile(self):
        self.assert_profile("T2D")

    def test_ai13_t3_exact_discriminating_profile(self):
        self.assert_profile("T3")

    def test_ai14_t4s_exact_discriminating_profile(self):
        self.assert_profile("T4S")

    def test_ai15_t4r_exact_discriminating_profile(self):
        self.assert_profile("T4R")

    def test_ai16_t5a_exact_discriminating_profile(self):
        self.assert_profile("T5A")

    def test_ai17_t5e_exact_discriminating_profile(self):
        self.assert_profile("T5E")

    def test_ai18_t6_exact_discriminating_profile(self):
        self.assert_profile("T6")

    def test_ai19_t7_exact_discriminating_profile(self):
        self.assert_profile("T7")

    def test_ai20_t8_exact_discriminating_profile(self):
        self.assert_profile("T8")

    def test_ai21_t9_exact_discriminating_profile(self):
        self.assert_profile("T9")

    def test_ai22_t10_exact_discriminating_profile(self):
        self.assert_profile("T10")

    def test_ai23_t11w_exact_discriminating_profile(self):
        self.assert_profile("T11W")

    def test_ai24_t11e_exact_discriminating_profile(self):
        self.assert_profile("T11E")

    def test_ai25_t1_neutralized_intervention(self):
        self.assert_profile("T1", neutral=True)

    def test_ai26_t2q_neutralized_intervention(self):
        self.assert_profile("T2Q", neutral=True)

    def test_ai27_t2d_neutralized_intervention(self):
        self.assert_profile("T2D", neutral=True)

    def test_ai28_t3_neutralized_intervention(self):
        self.assert_profile("T3", neutral=True)

    def test_ai29_t4s_neutralized_intervention(self):
        self.assert_profile("T4S", neutral=True)

    def test_ai30_t4r_neutralized_intervention(self):
        self.assert_profile("T4R", neutral=True)

    def test_ai31_t5a_neutralized_intervention(self):
        self.assert_profile("T5A", neutral=True)

    def test_ai32_t5e_neutralized_intervention(self):
        self.assert_profile("T5E", neutral=True)

    def test_ai33_t6_neutralized_intervention(self):
        self.assert_profile("T6", neutral=True)

    def test_ai34_t7_neutralized_intervention(self):
        self.assert_profile("T7", neutral=True)

    def test_ai35_t8_neutralized_intervention(self):
        self.assert_profile("T8", neutral=True)

    def test_ai36_t9_neutralized_intervention(self):
        self.assert_profile("T9", neutral=True)

    def test_ai37_t10_neutralized_intervention(self):
        self.assert_profile("T10", neutral=True)

    def test_ai38_t11w_neutralized_intervention(self):
        self.assert_profile("T11W", neutral=True)

    def test_ai39_t11e_neutralized_intervention(self):
        self.assert_profile("T11E", neutral=True)

    def test_ai40_expected_vector_without_fault(self):
        e = self.make("T3", neutral=True)
        e["supplied_decision"].update(admission="WITHHELD", action_gate="HOLD", failures=["DUTY_CARRIAGE_MISMATCH"])
        result = self.review(e)
        self.assertEqual(result["actual"], {k:self.expected[("T3","fault")][k] for k in result["actual"]})
        self.assertEqual(result["profile_assertion"]["verdict"], "FAIL")
        self.assertIn("EXPECTED_FAULT_NOT_OBSERVED", result["profile_assertion"]["issues"])

    def test_ai41_expected_fault_plus_extra_issue(self):
        e = self.make("T3"); e["forbidden_identity_claims"] = True
        result = self.review(e)
        self.assertEqual(result["profile_assertion"]["verdict"], "FAIL")
        self.assertIn("CANDIDATE_ASSERTION_SIGNATURE_MISMATCH", result["profile_assertion"]["issues"])

    def test_ai42_expected_fault_plus_effect_leakage(self):
        e = self.make("T3"); e["sink_after_snapshot"]["effects"].append({"operation_id":"foreign"})
        result = self.review(e)
        self.assertEqual(result["profile_assertion"]["verdict"], "FAIL")
        self.assertIn("FORBIDDEN_EFFECT_OR_PROMOTION", result["profile_assertion"]["issues"])

    def test_ai43_missing_observation_inconclusive(self):
        e = self.make("T3"); e["sink_before_snapshot"] = None
        self.assertEqual(self.review(e)["profile_assertion"]["verdict"], "INCONCLUSIVE")

    def test_ai44_nonpositive_r28_not_applicable(self):
        for cell in NEGATIVE_CELLS:
            self.assertEqual(self.rules(self.make(cell))["R28"]["value"], "NOT_APPLICABLE", cell)

    def test_ai45_t5e_admitted_claim_rejected_held(self):
        e = self.make("T5E"); d = e["supplied_decision"]
        self.assertEqual((d["admission"],d["q_state"],d["action_gate"]), ("ADMITTED","OPEN","HOLD"))
        self.assertEqual(d["failures"], [])
        self.assertEqual(d["rejected_claims"], ["SOURCE_RESOLUTION_BINDING_MISMATCH","EVIDENCE_PATH_MULTIPLICATION"])
        self.assertIsNone(d["verified_binding"]["source_resolution_hash"])
        self.assertEqual(d["candidate_resolution_hash"], canonical_hash(e["materialized_packet"]["resolution"]))
        self.assertEqual((e["commit_evidence"]["result"],e["commit_evidence"]["binding_revalidated"]), ("HELD",True))

    def test_ai46_t5e_candidate_r08_r20(self):
        rules = self.rules(self.make("T5E"))
        self.assertEqual((rules["R08"]["value"],rules["R08"]["reason"]), ("FAIL","CANDIDATE_RESOLUTION_CLAIM_INVALID"))
        self.assertEqual((rules["R20"]["value"],rules["R20"]["reason"]), ("FAIL","EVIDENCE_PATH_MULTIPLICATION"))

    def test_ai47_resolved_source_claim_mismatch_denied(self):
        e = self.raw("T0","RESOLVED_CHECK")
        p = producer.make_packet("T5E",e["source_inventory"],self.keys,e["checkpoint"],instance_id=e["active_instance_id"],attempt_id=e["attempt_id"],operation_id=e["operation_id"],commit_record_id=e["commit_record_id"])
        d = evaluate(p,e["source_inventory"],self.public)
        self.assertEqual((d["admission"],d["action_gate"]), ("WITHHELD","DENY"))
        self.assertIn("SOURCE_RESOLUTION_BINDING_MISMATCH",d["failures"])

    def test_ai48_resolution_null_absent_malformed_controls(self):
        e = self.make("T5E")
        for mode in ("null","absent","malformed"):
            proposal = copy.deepcopy(e["materialized_packet"])
            if mode == "absent": proposal.pop("resolution")
            else: proposal["resolution"] = None if mode == "null" else {}
            d = evaluate(self.sign_proposal(proposal),e["source_inventory"],self.public)
            self.assertEqual(d["rejected_claims"], [])
            if mode == "null": self.assertEqual(d["action_gate"], "HOLD")
            else:
                self.assertEqual(d["action_gate"], "DENY")
                self.assertIn("CANDIDATE_RESOLUTION_UNOBSERVABLE_OR_MALFORMED", d["failures"])

    def test_ai49_hidden_duplicate_claim_fails(self):
        e = self.make("T5E")
        e["materialized_packet"].pop("resolution")
        e["materialized_packet_hash"] = canonical_hash(e["materialized_packet"])
        self.assertNotEqual(self.review(e)["profile_assertion"]["verdict"], "PASS")

    def test_ai50_valid_resolved_positive_controls(self):
        for cell in ("N0","N1","T0"):
            e = self.make(cell,checkpoint="RESOLVED_CHECK")
            self.assertEqual(e["supplied_decision"]["action_gate"], "ALLOW", cell)
            self.assertEqual((e["commit_evidence"]["result"],e["commit_evidence"]["effect_delta"]), ("BOUND",1))
            self.assertEqual(observer.inspect_checkpoint(e)["observer_status"], "PASS")

    def test_ai51_t5a_distinct_roots_remain_denied(self):
        e = self.make("T5A")
        self.assertEqual(e["supplied_decision"]["action_gate"], "DENY")
        self.assertEqual(e["supplied_decision"]["distinct_approval_roots"], 1)
        self.assertEqual(self.rules(e)["R19"]["value"], "FAIL")

    def test_ai52_t8_request_explicitly_rejected(self):
        e = self.make("T8")
        self.assertEqual(e["supplied_decision"]["rejected_memory_requests"], ["PROMOTE_QUARANTINED_TO_CONFIRMED_EA"])
        self.assertEqual(self.rules(e)["R23"]["reason"], "FORBIDDEN_MEMORY_PROMOTION_REQUEST")

    def test_ai53_no_promotion_control_has_no_signal(self):
        e = self.make("T8",neutral=True)
        self.assertEqual(e["supplied_decision"]["rejected_memory_requests"], [])
        self.assertEqual(self.rules(e)["R23"]["value"], "PASS")

    def test_ai54_t8_mutated_control_evidence_differs(self):
        a,b = self.make("T8"),self.make("T8",neutral=True)
        self.assertEqual({k:a["supplied_decision"][k] for k in ("admission","q_state","action_gate")}, {k:b["supplied_decision"][k] for k in ("admission","q_state","action_gate")})
        self.assertNotEqual(a["supplied_decision"]["rejected_memory_requests"],b["supplied_decision"]["rejected_memory_requests"])
        self.assertNotEqual(self.rules(a)["R23"]["value"],self.rules(b)["R23"]["value"])

    def test_ai55_t8_promotion_row_fails(self):
        e = self.make("T8"); e["sink_after_snapshot"]["promotions"].append({"promotion_id":"forbidden"})
        self.assertEqual(self.review(e)["profile_assertion"]["verdict"], "FAIL")
        self.assertEqual(self.rules(e)["R10"]["value"], "FAIL")

    def test_ai56_t8_promotion_authorized_true_fails(self):
        e = self.make("T8"); e["supplied_decision"]["memory_promotion_authorized"] = True
        self.assertEqual(self.review(e)["profile_assertion"]["verdict"], "FAIL")

    def test_ai57_t10_no_revocation_binds_one_effect(self):
        e = self.make("T10",neutral=True); c = e["commit_evidence"]
        self.assertIs(c["current_authority_binding"],True)
        self.assertEqual(c["result"],"BOUND"); self.assertEqual(c["effect_delta"],1)
        self.assertEqual(e["operation_intent"]["effect_expectation"],"EXACTLY_ONE")
        self.assertEqual(c["revalidation_failures"],[])

    def test_ai58_t10_late_revocation_denies_zero_effect(self):
        e = self.make("T10"); c = e["commit_evidence"]
        self.assertIs(c["operation_binding_revalidated"],True)
        self.assertIs(c["current_authority_binding"],False)
        self.assertEqual(c["result"],"DENIED_ATOMIC_REVALIDATION")
        self.assertEqual(c["effect_delta"],0)
        self.assertEqual(c["revalidation_failures"],[{"plane":"CURRENT_AUTHORITY","reason":"CURRENT_GRANT_REVOKED_AT_BIND","fields":["status"]}])

    def test_ai59_gold_mutation_cannot_change_intent_or_broker(self):
        a = self.make("T10",neutral=True)
        gold = copy.deepcopy(self.expected[("T10","LATE_COMMIT_CHECK")]); gold["protected_effect_delta"] = 999
        b = self.make("T10",neutral=True)
        self.assertEqual(a["operation_intent"],b["operation_intent"])
        self.assertEqual((a["commit_evidence"]["result"],a["commit_evidence"]["effect_delta"]), (b["commit_evidence"]["result"],b["commit_evidence"]["effect_delta"]))
        self.assertNotEqual(self.review(b,expected=gold)["profile_assertion"]["verdict"],"PASS")
        tree = ast.parse(inspect.getsource(run_batch.precommit_operation_intent))
        self.assertNotIn("expected",{n.id for n in ast.walk(tree) if isinstance(n,ast.Name)})
        checkpoint_tree = ast.parse(inspect.getsource(run_batch._checkpoint_evidence))
        calls = [n for n in ast.walk(checkpoint_tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=="precommit_operation_intent"]
        self.assertEqual(len(calls),1)
        self.assertEqual([n.id for n in calls[0].args],["proposal","source","decision"])

    def test_ai60_unrelated_intent_mismatch_not_revocation_proof(self):
        e = self.make("T10",context_mutator=lambda intent:intent["scope"].__setitem__("attempt_id","foreign"))
        self.assertEqual(e["commit_evidence"]["result"],"DENIED_ATOMIC_REVALIDATION")
        self.assertIs(e["commit_evidence"]["operation_binding_revalidated"],False)
        self.assertNotEqual(observer.inspect_checkpoint(e)["atomic_denial_review"]["status"],"PASS")
        self.assertNotEqual(self.review(e)["profile_assertion"]["verdict"],"PASS")

    def test_ai61_missing_revocation_evidence_fails(self):
        self.assert_atomic_bad(lambda e:e["broker_after_snapshot"].pop("revocations"))

    def test_ai62_wrong_grant_revocation_fails(self):
        def mutate(e):
            e["broker_after_snapshot"]["revocations"] = [[1,"foreign-grant",7]]
        self.assert_atomic_bad(mutate)

    def test_ai63_revocation_after_bind_fails(self):
        self.assert_atomic_bad(lambda e:e["commit_evidence"].__setitem__("revocations_at_bind",[]))

    def test_ai64_final_gate_comes_from_commit(self):
        decision={"action_gate":"ALLOW"}
        self.assertEqual(run_batch.final_action_outcome(decision,{"result":"DENIED_ATOMIC_REVALIDATION","effect_delta":0}),"DENY")
        self.assertEqual(decision,{"action_gate":"ALLOW"})
        self.assertEqual(run_batch.final_action_outcome(decision,{"result":"BOUND","effect_delta":1}),"ALLOW")

    def test_ai65_both_precommit_and_final_retained(self):
        e = self.make("T10")
        self.assertEqual(e["supplied_decision"]["action_gate"],"ALLOW")
        self.assertEqual(e["precommit_receiver_decision"]["action_gate"],"ALLOW")
        self.assertEqual(e["final_action_gate"],"DENY")
        self.assertEqual(self.review(e)["actual"]["protected_action_gate"],"DENY")

    def test_ai66_atomic_denial_r24_r26_r27_pass(self):
        e = self.make("T10"); result=observer.inspect_checkpoint(e)
        self.assertEqual(result["atomic_denial_review"],{"status":"PASS","reason":"EXACT_LATE_GRANT_REVOCATION"})
        rules=self.rules(e)
        for requirement in ("R24","R26","R27"):
            self.assertEqual(rules[requirement]["value"],"PASS",rules[requirement])
        self.assertEqual(result["observer_status"],"PASS")

    def test_ai67_effect_under_revocation_fails(self):
        self.assert_atomic_bad(lambda e:e["sink_after_snapshot"]["effects"].append({"operation_id":"unexpected"}))

    def test_ai68_absent_authority_never_passes(self):
        self.assert_atomic_bad(lambda e:e["broker_before_snapshot"].__setitem__("authority",[]))

    def test_ai69_reversed_atomic_order_fails(self):
        self.assert_atomic_bad(lambda e:e["atomic_transition_chronology"].reverse())

    def test_ai70_foreign_atomic_scope_fails(self):
        self.assert_atomic_bad(lambda e:e["atomic_transition_chronology"][0]["scope"].__setitem__("attempt_id","foreign"))

    def test_ai71_fabricated_final_deny_fails(self):
        self.assert_atomic_bad(lambda e:e["commit_evidence"].__setitem__("result","BOUND"))

    def test_ai72_missing_zero_effect_coverage_never_passes(self):
        e=self.make("T10"); e["sink_before_snapshot"]=None
        self.assertEqual(self.review(e)["profile_assertion"]["verdict"],"INCONCLUSIVE")

    def test_ai73_n0_t0_linked_preserved(self):
        for cell in ("N0","T0"):
            pair=(self.raw(cell,"OPEN_CHECK"),self.raw(cell,"RESOLVED_CHECK"))
            linked=observer.inspect_logic_path(*pair)
            self.assertEqual(linked["offline_logic_path_status"],"PASS",linked)
            self.assertTrue(all(linked["checks"].values()))
            for e in pair: self.assertEqual(self.review(e,linked=pair)["profile_assertion"]["verdict"],"PASS")

    def test_ai74_explicit_no_run_compatibility(self):
        r=observer.review_execution_scope({"measured_matrix_started":False,"matrix_canary_started":False})
        self.assertEqual((r.value,r.reason),("PASS","NO_MATRIX_OR_NEW_ARCHITECTURE"))

    def test_ai75_legacy_synthetic_compatibility(self):
        with tempfile.TemporaryDirectory(prefix="ai-legacy-") as temporary:
            e=positive_trace(Path(temporary)/"keys")
            self.assertEqual(observer.inspect_checkpoint(e)["observer_status"],"PASS")
            self.assertEqual(observer.review_execution_scope(e).value,"PASS")

    def test_ai76_valid_full_matrix_binding_preserved(self):
        e=self.raw("N1","OPEN_CHECK")
        self.assertEqual(observer.review_execution_scope(e).value,"PASS")
        self.assertIs(e["final_matrix_credit"],True)

    def test_ai77_valid_canary_binding_preserved(self):
        e=self.raw("T0","OPEN_CHECK")
        b=copy.deepcopy(e["execution_scope_binding"])
        b.update(mode="CANARY",allowed_cells=["T0"],allowed_checkpoints=[{"cell_id":"T0","checkpoint":"OPEN_CHECK"},{"cell_id":"T0","checkpoint":"RESOLVED_CHECK"}],final_matrix_credit=False)
        e.update(observer.execution_scope_evidence(b,matrix_run_id=e["matrix_run_id"],matrix_sha256=e["actual_matrix_sha256"],successor_baseline_sha256=e["actual_successor_baseline_sha256"]))
        self.assertEqual(observer.review_execution_scope(e).value,"PASS")
        self.assertIs(e["final_matrix_credit"],False)

    def test_ai78_invalid_scope_binding_stays_closed(self):
        e=self.raw("T0","OPEN_CHECK"); e["execution_scope_binding_hash"]="0"*64
        self.assertEqual(observer.review_execution_scope(e).value,"FAIL")

    def test_ai79_prospective_positive_verdict_unchanged(self):
        e=json.loads((self.roots["T0"]/"prospective_observation/OBSERVATION_EVIDENCE.json").read_text())
        result=review_observation_evidence(e)
        self.assertEqual(result["verdict"],"OBSERVED_COMMITTED_CHANGE")
        self.assertEqual(result["issues"],[])
        self.assertEqual(e["gaps"],[])

    def test_ai80_protected_logic_path_eight_checks(self):
        with tempfile.TemporaryDirectory(prefix="ai-protected-logic-") as temporary:
            result=logic_execute(Path(temporary) / "logic")
            controls=json.loads((Path(temporary)/"logic/observer_d02_d05.json").read_text())
            self.results.append({"test":self.id(),"protected_logic_path":result,"d02_d05":controls})
            self.assertEqual(result["offline_logic_path_status"],"PASS",result)
            self.assertEqual(len(result["checks"]),8)
            self.assertTrue(all(result["checks"].values()))

    def test_ai81_t5e_core_admission_failure_stays_denied(self):
        e=self.make("T5E"); p=copy.deepcopy(e["materialized_packet"]); p.pop("receiver_basis")
        d=evaluate(self.sign_proposal(p),e["source_inventory"],self.public)
        self.assertEqual((d["admission"],d["action_gate"]),("WITHHELD","DENY"))
        self.assertIn("SOURCE_RESOLUTION_BINDING_MISMATCH",d["failures"])

    def test_ai82_t5e_invalid_approval_scope_stays_denied(self):
        e=self.make("T5E"); packet=self.sign_proposal(e["materialized_packet"])
        approval=packet["approvals"][0]["payload"]; approval["attempt_id"]="foreign"
        packet["approvals"][0]=sign(approval,"producer-alpha",self.keys.ensure("producer-alpha"),"root:alpha")
        packet["transport_hash"]=canonical_hash({k:packet[k] for k in ("envelope","approvals")})
        d=evaluate(packet,e["source_inventory"],self.public)
        self.assertEqual(d["action_gate"],"DENY"); self.assertIn("APPROVAL_SCOPE_MISMATCH",d["failures"])

    def test_ai83_extra_material_intervention_fails(self):
        e=self.make("T3")
        e["materialized_packet"]["quarantined_memory"]["id"]="different"
        e["materialized_packet_hash"]=canonical_hash(e["materialized_packet"])
        result=self.review(e)
        self.assertEqual(result["profile_assertion"]["verdict"],"FAIL")
        self.assertIn("UNDECLARED_OR_MISSING_INTERVENTION",result["profile_assertion"]["issues"])

    def test_ai84_missing_prospective_observation_inconclusive(self):
        e=self.make("T3")
        self.assertEqual(self.review(e,prospective=False)["profile_assertion"]["verdict"],"INCONCLUSIVE")

    def test_ai85_foreign_positive_pair_fails_profile(self):
        opened=self.raw("N1","OPEN_CHECK"); resolved=self.raw("N1","RESOLVED_CHECK")
        resolved["matrix_run_id"]="foreign-run"
        result=self.review(opened,linked=(opened,resolved))
        self.assertEqual(result["profile_assertion"]["verdict"],"FAIL")
        self.assertIn("LINKED_POSITIVE_PATH_INVALID",result["profile_assertion"]["issues"])

    def test_ai86_boolean_authority_cannot_match_integer_intervention(self):
        e=self.make("T4S")
        e["materialized_packet"]["authority_version"]=True
        p=self.sign_proposal(e["materialized_packet"])
        e.update(materialized_packet=p["envelope"]["payload"],materialized_packet_hash=canonical_hash(p["envelope"]["payload"]),proposal_envelope=p["envelope"],proposal_hash=p["envelope"]["payload"]["proposal_hash"])
        result=self.review(e)
        self.assertEqual(result["profile_assertion"]["verdict"],"FAIL")
        self.assertIn("UNDECLARED_OR_MISSING_INTERVENTION",result["profile_assertion"]["issues"])

    def test_ai87_rebound_wrong_intent_payload_fails_atomic_proof(self):
        e=self.make("T10")
        e["operation_intent"]["expected_effect_row"]["payload"]["kind"]="FOREIGN"
        e["operation_intent_hash"]=canonical_hash(e["operation_intent"])
        e["commit_evidence"]["operation_intent"]=copy.deepcopy(e["operation_intent"])
        e["commit_evidence"]["operation_intent_hash"]=e["operation_intent_hash"]
        result=observer.inspect_checkpoint(e)
        self.assertEqual(result["atomic_denial_review"]["status"],"FAIL")
        for requirement in ("R24","R26"):
            self.assertEqual(self.rules(e)[requirement]["value"],"FAIL")

    def test_ai88_foreign_proposal_context_fails_independent_witness(self):
        e=self.make("T8")
        e["materialized_packet"]["attempt_id"]="foreign"
        p=self.sign_proposal(e["materialized_packet"])
        e.update(materialized_packet=p["envelope"]["payload"],materialized_packet_hash=canonical_hash(p["envelope"]["payload"]),proposal_envelope=p["envelope"],proposal_hash=p["envelope"]["payload"]["proposal_hash"])
        self.assertIn("CANDIDATE_PROPOSAL_CONTEXT_INVALID",observer.inspect_checkpoint(e)["problems"])
        self.assertEqual(self.rules(e)["R26"]["value"],"FAIL")

    def test_ai89_foreign_prospective_episode_fails_profile(self):
        e=self.make("T3")
        foreign=json.loads((self.roots["T2D"]/"prospective_observation/OBSERVATION_EVIDENCE.json").read_text())
        cleanup={"scope":{k:e[k] for k in ("task_id","attempt_id","active_instance_id")},"w0":"PROVEN","w1":"PROVEN"}
        result=run_batch.review_profile_assertion(e,self.expected[("T3","fault")],self.alignment(e),prospective_evidence=foreign,cleanup=cleanup)
        self.assertEqual(result["profile_assertion"]["verdict"],"FAIL")
        self.assertIn("PROSPECTIVE_COORDINATE_BINDING_MISMATCH",result["profile_assertion"]["issues"])

    def test_ai90_foreign_received_release_identifier_fails(self):
        def mutate(e):
            for event in e["trusted_chronology"]:
                if event.get("worker_event",{}).get("event")=="RELEASED":
                    event["worker_event"]["release_id"]="release:foreign"
        self.assert_n1_bad(mutate)

    def test_ai91_protected_legacy_d05_pending_preserved(self):
        from cgdr_r1_6b.observer_fixtures import lawful_open_phase
        with tempfile.TemporaryDirectory(prefix="ai-legacy-d05-") as temporary:
            e=lawful_open_phase(Path(temporary)/"keys")
            rule=self.rules(e)["R28"]
            self.assertEqual((rule["value"],rule["reason"]),("UNKNOWN","RESOLUTION_PROGRESS_PENDING_AFTER_LAWFUL_OPEN_HOLD"))
            e["cell_id"]="T8"
            self.assertEqual(self.rules(e)["R28"]["value"],"NOT_APPLICABLE")

    def test_ai92_prospective_plan_never_reads_matrix_gold(self):
        tree=ast.parse(inspect.getsource(run_batch._run_episode))
        plan=next(n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="plan" for t in n.targets))
        before=[n for n in tree.body[0].body if n.lineno <= plan.lineno]
        reads=[n for statement in before for n in ast.walk(statement) if isinstance(n,ast.Name) and isinstance(n.ctx,ast.Load) and n.id=="expected"]
        self.assertEqual(reads,[])
        outcome=next(k.value for k in plan.value.keywords if k.arg=="expected_outcome")
        self.assertEqual(ast.unparse(outcome),"'ALLOW_EXACTLY_ONE' if planned_effect else 'HOLD_NO_EFFECT'")
