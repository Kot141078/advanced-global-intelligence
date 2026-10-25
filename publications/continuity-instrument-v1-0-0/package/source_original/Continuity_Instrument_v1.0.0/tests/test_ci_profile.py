from __future__ import annotations

import ast
import copy
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
IMPLEMENTATION_DIR = ROOT / "REFERENCE_IMPLEMENTATION"
SCHEMA_DIR = IMPLEMENTATION_DIR / "schemas"
sys.path.insert(0, str(IMPLEMENTATION_DIR))

import ci_profile  # noqa: E402


MANDATORY_NON_CLAIMS = [
    "authority_or_permission",
    "biological_age",
    "metaphysical_or_legal_identity",
    "personhood",
    "uninterrupted_existence",
    "wall_clock_age",
]


def _witness(
    witness_id: str,
    lower: int,
    upper: int,
    status: str = "admitted",
) -> dict:
    return {
        "witness_id": witness_id,
        "observation_ref": f"observation:{witness_id}",
        "time": {"lower": lower, "upper": upper},
        "admission_status": status,
        "witness_ref": f"witness:{witness_id}",
        "authority_ref": "authority:bounded",
        "evidence_refs": [f"evidence:{witness_id}"],
        "uncertainty": ["bounded_source_time"],
    }


def _interval(interval_id: str, start: int, end: int, status: str = "admitted") -> dict:
    return {
        "interval_id": interval_id,
        "start": start,
        "end": end,
        "participation_predicate": "bounded_test_participation",
        "evidence_refs": [f"evidence:{interval_id}:b", f"evidence:{interval_id}:a"],
        "witness_refs": ["witness:z", "witness:a"],
        "authority_refs": ["authority:bounded"],
        "admission_status": status,
        "eligible_for_duration": status == "admitted",
        "uncertainty": ["predicate_scope_limited"],
    }


def _pause(pause_id: str, start: int, end: int) -> dict:
    return {
        "pause_id": pause_id,
        "start": start,
        "end": end,
        "classification": "evidenced_unavailable",
        "evidence_refs": [f"evidence:{pause_id}"],
        "uncertainty": ["pause_scope_limited"],
    }


def _event(event_id: str, event_type: str, tick: int) -> dict:
    return {
        "event_id": event_id,
        "event_type": event_type,
        "time": {"lower": tick, "upper": tick},
        "source_branch_ref": "branch:source",
        "target_branch_ref": "branch:target",
        "predecessor_refs": ["state:b", "state:a"],
        "successor_refs": ["state:d", "state:c"],
        "witness_refs": ["witness:z", "witness:a"],
        "authority_refs": ["authority:bounded"],
        "affected_lineages": ["witness", "memory"],
        "evidence_refs": [f"evidence:{event_id}"],
        "supported_interpretation": f"bounded {event_type} event",
        "exclusions": ["uninterrupted_existence", "entity_identity"],
        "uncertainty": ["event_scope_limited"],
        "review_status": "scope_limited_review",
    }


def _lineage(transition_id: str, tick: int, state: str) -> dict:
    return {
        "transition_id": transition_id,
        "time": {"lower": tick, "upper": tick},
        "state": state,
        "predecessor_ref": f"state:{transition_id}:before",
        "successor_ref": f"state:{transition_id}:after",
        "evidence_refs": [f"evidence:{transition_id}"],
        "uncertainty": ["lineage_scope_limited"],
    }


def sample_input() -> dict:
    return {
        "schema_version": "ci-profile-input/v1",
        "profile_id": "profile:test-v1",
        "subject_ref": "declared-subject:test",
        "branch_ref": "branch:test",
        "time_axis": {
            "unit": "tick",
            "origin": "fixture-origin",
            "basis": "fixture-monotonic-index",
        },
        "observation_window": {"start": 0, "end": 100},
        "witnesses": [
            _witness("w-last", 90, 95),
            _witness("w-excluded", 0, 0, "excluded"),
            _witness("w-first", 5, 5),
        ],
        "verified_intervals": [
            _interval("i-three", 50, 60),
            _interval("i-two", 10, 30),
            _interval("i-one", 0, 20),
        ],
        "known_pauses": [
            _pause("p-two", 70, 80),
            _pause("p-one", 30, 40),
        ],
        "events": [
            _event("event-restore", "restore", 68),
            _event("event-replay", "replay", 41),
            _event("event-cold", "cold_wake", 81),
            _event("event-fork", "fork", 65),
        ],
        "lineages": {
            "memory": [
                _lineage("memory-later", 75, "changed_with_bound_record"),
                _lineage("memory-earlier", 25, "preserved_with_evidence"),
            ],
            "governance": [
                _lineage("governance-one", 35, "changed_with_bound_record")
            ],
            "witness": [_lineage("witness-one", 45, "preserved_with_evidence")],
            "authority": [_lineage("authority-one", 55, "broken_with_evidence")],
        },
        "irreversible_transitions": [
            {
                "transition_id": "irreversible:test",
                "time": {"lower": 85, "upper": 85},
                "scope": "fixture-governance-scope",
                "decision_rule": "bound_record_declares_no_reversal_in_scope",
                "evidence_refs": ["evidence:irreversible"],
                "witness_refs": ["witness:z", "witness:a"],
                "authority_refs": ["authority:bounded"],
                "uncertainty": ["only_within_declared_scope"],
            }
        ],
        "uncertainty": {
            "missing_evidence": ["outside_observation_window", "unobserved_gap_causes"],
            "clock_uncertainty": ["fixture_tick_not_wall_clock"],
            "classification_uncertainty": ["event_labels_caller_supplied"],
            "branch_uncertainty": ["no_cross_branch_aggregation"],
            "lineage_uncertainty": ["lineages_independently_scoped"],
            "witness_uncertainty": ["witness_independence_not_established"],
            "authority_uncertainty": ["authority_truth_not_attested"],
            "review_uncertainty": "not_assessed",
        },
        "claim_ceiling": {
            "status": "specified",
            "allowed_claims": [
                "deterministic_transformation_of_caller_supplied_fixture",
                "structure_only",
            ],
            "prohibited_inferences": MANDATORY_NON_CLAIMS
            + ["scientific_validation", "r160_qualification"],
            "basis_refs": ["CI_SPECIFICATION.md", "CONTINUITY_OBSERVABLES.md"],
        },
    }


class CIProfileTests(unittest.TestCase):
    def test_vector_is_evidence_bound_and_does_not_use_witness_span_as_age(self) -> None:
        output = ci_profile.build_profile(sample_input())
        vector = output["formation_depth_vector"]

        self.assertEqual(vector["W_first"]["witness_id"], "w-first")
        self.assertEqual(vector["W_last"]["witness_id"], "w-last")
        self.assertEqual(vector["D_verified"]["value"], 40)
        self.assertNotEqual(
            vector["D_verified"]["value"],
            vector["W_last"]["time"]["upper"]
            - vector["W_first"]["time"]["lower"],
        )
        self.assertEqual(
            vector["G_unexplained"],
            [
                {
                    "start": 40,
                    "end": 50,
                    "reason": "no_admitted_verified_participation_or_known_pause",
                },
                {
                    "start": 60,
                    "end": 70,
                    "reason": "no_admitted_verified_participation_or_known_pause",
                },
                {
                    "start": 80,
                    "end": 100,
                    "reason": "no_admitted_verified_participation_or_known_pause",
                },
            ],
        )

    def test_all_event_lineage_transition_uncertainty_and_ceiling_coordinates_survive(self) -> None:
        output = ci_profile.build_profile(sample_input())
        vector = output["formation_depth_vector"]

        self.assertEqual([item["event_type"] for item in vector["E_replay"]], ["replay"])
        self.assertEqual([item["event_type"] for item in vector["E_fork"]], ["fork"])
        self.assertEqual([item["event_type"] for item in vector["E_restore"]], ["restore"])
        self.assertEqual([item["event_type"] for item in vector["E_cold_wake"]], ["cold_wake"])
        self.assertEqual(
            [item["transition_id"] for item in vector["L_memory"]],
            ["memory-earlier", "memory-later"],
        )
        self.assertEqual(len(vector["L_governance"]), 1)
        self.assertEqual(len(vector["L_witness"]), 1)
        self.assertEqual(len(vector["L_authority"]), 1)
        self.assertEqual(len(vector["T_irreversible"]), 1)
        self.assertEqual(vector["U"]["review_uncertainty"], "not_assessed")
        self.assertTrue(
            set(MANDATORY_NON_CLAIMS).issubset(
                output["claim_ceiling"]["prohibited_inferences"]
            )
        )

    def test_permutations_produce_identical_output_and_vector_digest(self) -> None:
        source = sample_input()
        permuted = copy.deepcopy(source)
        for key in (
            "witnesses",
            "verified_intervals",
            "known_pauses",
            "events",
            "irreversible_transitions",
        ):
            permuted[key].reverse()
        for lineage_records in permuted["lineages"].values():
            lineage_records.reverse()
        permuted["claim_ceiling"]["allowed_claims"].reverse()
        permuted["claim_ceiling"]["prohibited_inferences"].reverse()
        permuted["claim_ceiling"]["basis_refs"].reverse()
        permuted["uncertainty"]["missing_evidence"].reverse()

        first = ci_profile.build_profile(source)
        second = ci_profile.build_profile(permuted)
        self.assertEqual(first, second)
        self.assertEqual(ci_profile.canonical_json(first), ci_profile.canonical_json(second))
        expected_digest = hashlib.sha256(
            ci_profile.canonical_json(first["formation_depth_vector"]).encode("utf-8")
        ).hexdigest()
        self.assertEqual(first["formation_depth_vector_sha256"], expected_digest)

    def test_contradictory_pause_overlap_is_rejected(self) -> None:
        source = sample_input()
        source["known_pauses"].append(_pause("p-overlap", 19, 21))
        with self.assertRaisesRegex(
            ci_profile.ProfileValidationError, "overlaps known pause"
        ):
            ci_profile.build_profile(source)

    def test_mandatory_claim_exclusions_are_required(self) -> None:
        source = sample_input()
        source["claim_ceiling"]["prohibited_inferences"].remove("personhood")
        with self.assertRaisesRegex(
            ci_profile.ProfileValidationError, "missing mandatory values"
        ):
            ci_profile.build_profile(source)

    def test_cli_writes_canonical_utf8_json_and_accepts_schema_integer_forms(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / "input.json"
            output_path = Path(temporary_directory) / "output.json"
            source = sample_input()
            source["subject_ref"] = "declared-subject:тест"
            source["observation_window"]["end"] = 100.0
            input_path.write_text(
                json.dumps(source, ensure_ascii=False), encoding="utf-8"
            )
            self.assertEqual(
                ci_profile.main([str(input_path), "--output", str(output_path)]), 0
            )
            output_text = output_path.read_text(encoding="utf-8")
            output = json.loads(output_text)
            self.assertEqual(output_text, ci_profile.canonical_json(output) + "\n")
            self.assertNotIn("generated_at", output)

            stdout_capture = mock.Mock()
            stdout_capture.buffer = io.BytesIO()
            with mock.patch.object(ci_profile.sys, "stdout", stdout_capture):
                self.assertEqual(ci_profile.main([str(input_path)]), 0)
            self.assertEqual(
                stdout_capture.buffer.getvalue(),
                (ci_profile.canonical_json(output) + "\n").encode("utf-8"),
            )

    def test_versioned_schemas_are_valid_json_and_match_constants(self) -> None:
        input_schema = json.loads(
            (SCHEMA_DIR / "ci-profile-input-v1.schema.json").read_text(encoding="utf-8")
        )
        output_schema = json.loads(
            (SCHEMA_DIR / "ci-profile-output-v1.schema.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            input_schema["properties"]["schema_version"]["const"],
            ci_profile.INPUT_SCHEMA_VERSION,
        )
        self.assertEqual(
            output_schema["properties"]["schema_version"]["const"],
            ci_profile.OUTPUT_SCHEMA_VERSION,
        )
        self.assertEqual(
            output_schema["properties"]["generated_by"]["const"],
            ci_profile.IMPLEMENTATION_VERSION,
        )

    def test_implementation_imports_only_standard_library_modules(self) -> None:
        tree = ast.parse((IMPLEMENTATION_DIR / "ci_profile.py").read_text(encoding="utf-8"))
        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])
        self.assertTrue(imported_roots.issubset(sys.stdlib_module_names))


if __name__ == "__main__":
    unittest.main()
