#!/usr/bin/env python3
"""Deterministic, inert CI formation-depth reference implementation.

The module transforms an already-admitted evidence description into the
inspectable Continuity Instrument (CI) vector defined by this publication
draft.  It does not collect evidence, contact services, inspect the host, or
decide personhood, identity, wall-clock age, biological age, or authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


INPUT_SCHEMA_VERSION = "ci-profile-input/v1"
OUTPUT_SCHEMA_VERSION = "ci-profile-output/v1"
IMPLEMENTATION_VERSION = "ci-profile-reference/1.0.0"

ADMISSION_STATUSES = ("admitted", "excluded", "unresolved")
EVENT_TYPES = ("cold_wake", "fork", "replay", "restore")
LINEAGE_NAMES = ("authority", "governance", "memory", "witness")
LINEAGE_STATES = (
    "broken_with_evidence",
    "changed_with_bound_record",
    "conflicted",
    "preserved_with_evidence",
    "unknown",
)
REVIEW_STATUSES = (
    "independent_review_complete",
    "not_reviewed",
    "pending_independent_review",
    "scope_limited_review",
)
CLAIM_STATUSES = (
    "excluded",
    "not_established",
    "pending_independent_review",
    "specified",
    "supported_within_bound",
)
MANDATORY_PROHIBITED_INFERENCES = (
    "authority_or_permission",
    "biological_age",
    "metaphysical_or_legal_identity",
    "personhood",
    "uninterrupted_existence",
    "wall_clock_age",
)
UNCERTAINTY_FIELDS = (
    "authority_uncertainty",
    "branch_uncertainty",
    "classification_uncertainty",
    "clock_uncertainty",
    "lineage_uncertainty",
    "missing_evidence",
    "review_uncertainty",
    "witness_uncertainty",
)


class ProfileValidationError(ValueError):
    """Raised when an input does not satisfy the v1 input contract."""


def _object(value: Any, path: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise ProfileValidationError(f"{path} must be an object")
    return value


def _array(value: Any, path: str) -> Sequence[Any]:
    if not isinstance(value, list):
        raise ProfileValidationError(f"{path} must be an array")
    return value


def _string(value: Any, path: str) -> str:
    if not isinstance(value, str) or not value:
        raise ProfileValidationError(f"{path} must be a non-empty string")
    return value


def _integer(value: Any, path: str) -> int:
    if isinstance(value, bool):
        raise ProfileValidationError(f"{path} must be an integer")
    if isinstance(value, int):
        return value
    if isinstance(value, Decimal):
        if value.is_finite() and value == value.to_integral_value():
            return int(value)
        raise ProfileValidationError(f"{path} must be an integer")
    if isinstance(value, float) and value.is_integer():
        return int(value)
    raise ProfileValidationError(f"{path} must be an integer")


def _boolean(value: Any, path: str) -> bool:
    if not isinstance(value, bool):
        raise ProfileValidationError(f"{path} must be a boolean")
    return value


def _exact_keys(
    value: Mapping[str, Any], required: Iterable[str], path: str
) -> None:
    required_set = set(required)
    actual_set = set(value)
    missing = sorted(required_set - actual_set)
    extra = sorted(actual_set - required_set)
    if missing:
        raise ProfileValidationError(f"{path} missing required keys: {missing}")
    if extra:
        raise ProfileValidationError(f"{path} has unknown keys: {extra}")


def _enum(value: Any, allowed: Sequence[str], path: str) -> str:
    result = _string(value, path)
    if result not in allowed:
        raise ProfileValidationError(
            f"{path} must be one of {list(allowed)}, got {result!r}"
        )
    return result


def _unique_strings(value: Any, path: str, *, allow_empty: bool = True) -> list[str]:
    members = _array(value, path)
    result = [_string(member, f"{path}[{index}]") for index, member in enumerate(members)]
    if not allow_empty and not result:
        raise ProfileValidationError(f"{path} must contain at least one item")
    if len(set(result)) != len(result):
        raise ProfileValidationError(f"{path} must not contain duplicates")
    return sorted(result)


def _time_range(value: Any, path: str, window: tuple[int, int]) -> dict[str, int]:
    record = _object(value, path)
    _exact_keys(record, ("lower", "upper"), path)
    lower = _integer(record["lower"], f"{path}.lower")
    upper = _integer(record["upper"], f"{path}.upper")
    if lower > upper:
        raise ProfileValidationError(f"{path}.lower must be <= {path}.upper")
    if lower < window[0] or upper > window[1]:
        raise ProfileValidationError(f"{path} must be inside observation_window")
    return {"lower": lower, "upper": upper}


def _closed_open_interval(
    value: Mapping[str, Any], path: str, window: tuple[int, int]
) -> tuple[int, int]:
    start = _integer(value["start"], f"{path}.start")
    end = _integer(value["end"], f"{path}.end")
    if start >= end:
        raise ProfileValidationError(f"{path} requires start < end")
    if start < window[0] or end > window[1]:
        raise ProfileValidationError(f"{path} must be inside observation_window")
    return start, end


def _record_uncertainty(value: Any, path: str) -> list[str]:
    return _unique_strings(value, path, allow_empty=False)


def _structured_uncertainty(value: Any, path: str) -> dict[str, Any]:
    record = _object(value, path)
    _exact_keys(record, UNCERTAINTY_FIELDS, path)
    normalized: dict[str, Any] = {}
    for field in UNCERTAINTY_FIELDS:
        member = record[field]
        member_path = f"{path}.{field}"
        if member == "not_assessed":
            normalized[field] = "not_assessed"
        else:
            normalized[field] = _unique_strings(member, member_path, allow_empty=False)
    return normalized


def _normalize_witnesses(
    value: Any, window: tuple[int, int]
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    required = (
        "admission_status",
        "authority_ref",
        "evidence_refs",
        "observation_ref",
        "time",
        "uncertainty",
        "witness_id",
        "witness_ref",
    )
    records: list[dict[str, Any]] = []
    counts = {status: 0 for status in ADMISSION_STATUSES}
    seen: set[str] = set()
    for index, raw in enumerate(_array(value, "$.witnesses")):
        path = f"$.witnesses[{index}]"
        item = _object(raw, path)
        _exact_keys(item, required, path)
        witness_id = _string(item["witness_id"], f"{path}.witness_id")
        if witness_id in seen:
            raise ProfileValidationError(f"duplicate witness_id: {witness_id!r}")
        seen.add(witness_id)
        status = _enum(item["admission_status"], ADMISSION_STATUSES, f"{path}.admission_status")
        counts[status] += 1
        record = {
            "admission_status": status,
            "authority_ref": _string(item["authority_ref"], f"{path}.authority_ref"),
            "evidence_refs": _unique_strings(item["evidence_refs"], f"{path}.evidence_refs", allow_empty=False),
            "observation_ref": _string(item["observation_ref"], f"{path}.observation_ref"),
            "time": _time_range(item["time"], f"{path}.time", window),
            "uncertainty": _record_uncertainty(item["uncertainty"], f"{path}.uncertainty"),
            "witness_id": witness_id,
            "witness_ref": _string(item["witness_ref"], f"{path}.witness_ref"),
        }
        records.append(record)
    return records, counts


def _normalize_verified_intervals(
    value: Any, window: tuple[int, int]
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    required = (
        "admission_status",
        "authority_refs",
        "eligible_for_duration",
        "end",
        "evidence_refs",
        "interval_id",
        "participation_predicate",
        "start",
        "uncertainty",
        "witness_refs",
    )
    records: list[dict[str, Any]] = []
    counts = {status: 0 for status in ADMISSION_STATUSES}
    counts["eligible_for_duration"] = 0
    seen: set[str] = set()
    for index, raw in enumerate(_array(value, "$.verified_intervals")):
        path = f"$.verified_intervals[{index}]"
        item = _object(raw, path)
        _exact_keys(item, required, path)
        interval_id = _string(item["interval_id"], f"{path}.interval_id")
        if interval_id in seen:
            raise ProfileValidationError(f"duplicate interval_id: {interval_id!r}")
        seen.add(interval_id)
        start, end = _closed_open_interval(item, path, window)
        status = _enum(item["admission_status"], ADMISSION_STATUSES, f"{path}.admission_status")
        eligible = _boolean(item["eligible_for_duration"], f"{path}.eligible_for_duration")
        if eligible and status != "admitted":
            raise ProfileValidationError(
                f"{path} cannot be eligible_for_duration unless admitted"
            )
        counts[status] += 1
        if eligible:
            counts["eligible_for_duration"] += 1
        records.append(
            {
                "admission_status": status,
                "authority_refs": _unique_strings(item["authority_refs"], f"{path}.authority_refs"),
                "eligible_for_duration": eligible,
                "end": end,
                "evidence_refs": _unique_strings(item["evidence_refs"], f"{path}.evidence_refs", allow_empty=False),
                "interval_id": interval_id,
                "participation_predicate": _string(item["participation_predicate"], f"{path}.participation_predicate"),
                "start": start,
                "uncertainty": _record_uncertainty(item["uncertainty"], f"{path}.uncertainty"),
                "witness_refs": _unique_strings(item["witness_refs"], f"{path}.witness_refs", allow_empty=False),
            }
        )
    records.sort(key=lambda item: (item["start"], item["end"], item["interval_id"]))
    return records, counts


def _normalize_pauses(value: Any, window: tuple[int, int]) -> list[dict[str, Any]]:
    required = (
        "classification",
        "end",
        "evidence_refs",
        "pause_id",
        "start",
        "uncertainty",
    )
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(_array(value, "$.known_pauses")):
        path = f"$.known_pauses[{index}]"
        item = _object(raw, path)
        _exact_keys(item, required, path)
        pause_id = _string(item["pause_id"], f"{path}.pause_id")
        if pause_id in seen:
            raise ProfileValidationError(f"duplicate pause_id: {pause_id!r}")
        seen.add(pause_id)
        start, end = _closed_open_interval(item, path, window)
        records.append(
            {
                "classification": _string(item["classification"], f"{path}.classification"),
                "end": end,
                "evidence_refs": _unique_strings(item["evidence_refs"], f"{path}.evidence_refs", allow_empty=False),
                "pause_id": pause_id,
                "start": start,
                "uncertainty": _record_uncertainty(item["uncertainty"], f"{path}.uncertainty"),
            }
        )
    records.sort(key=lambda item: (item["start"], item["end"], item["pause_id"]))
    return records


def _normalize_events(value: Any, window: tuple[int, int]) -> list[dict[str, Any]]:
    required = (
        "affected_lineages",
        "authority_refs",
        "event_id",
        "event_type",
        "evidence_refs",
        "exclusions",
        "predecessor_refs",
        "review_status",
        "source_branch_ref",
        "successor_refs",
        "supported_interpretation",
        "target_branch_ref",
        "time",
        "uncertainty",
        "witness_refs",
    )
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(_array(value, "$.events")):
        path = f"$.events[{index}]"
        item = _object(raw, path)
        _exact_keys(item, required, path)
        event_id = _string(item["event_id"], f"{path}.event_id")
        if event_id in seen:
            raise ProfileValidationError(f"duplicate event_id: {event_id!r}")
        seen.add(event_id)
        affected = _unique_strings(item["affected_lineages"], f"{path}.affected_lineages")
        unknown_lineages = sorted(set(affected) - set(LINEAGE_NAMES))
        if unknown_lineages:
            raise ProfileValidationError(
                f"{path}.affected_lineages has unknown values: {unknown_lineages}"
            )
        records.append(
            {
                "affected_lineages": affected,
                "authority_refs": _unique_strings(item["authority_refs"], f"{path}.authority_refs"),
                "event_id": event_id,
                "event_type": _enum(item["event_type"], EVENT_TYPES, f"{path}.event_type"),
                "evidence_refs": _unique_strings(item["evidence_refs"], f"{path}.evidence_refs", allow_empty=False),
                "exclusions": _unique_strings(item["exclusions"], f"{path}.exclusions", allow_empty=False),
                "predecessor_refs": _unique_strings(item["predecessor_refs"], f"{path}.predecessor_refs"),
                "review_status": _enum(item["review_status"], REVIEW_STATUSES, f"{path}.review_status"),
                "source_branch_ref": _string(item["source_branch_ref"], f"{path}.source_branch_ref"),
                "successor_refs": _unique_strings(item["successor_refs"], f"{path}.successor_refs"),
                "supported_interpretation": _string(item["supported_interpretation"], f"{path}.supported_interpretation"),
                "target_branch_ref": _string(item["target_branch_ref"], f"{path}.target_branch_ref"),
                "time": _time_range(item["time"], f"{path}.time", window),
                "uncertainty": _record_uncertainty(item["uncertainty"], f"{path}.uncertainty"),
                "witness_refs": _unique_strings(item["witness_refs"], f"{path}.witness_refs"),
            }
        )
    records.sort(
        key=lambda item: (
            item["time"]["lower"],
            item["time"]["upper"],
            item["event_id"],
        )
    )
    return records


def _normalize_lineages(value: Any, window: tuple[int, int]) -> dict[str, list[dict[str, Any]]]:
    root = _object(value, "$.lineages")
    _exact_keys(root, LINEAGE_NAMES, "$.lineages")
    required = (
        "evidence_refs",
        "predecessor_ref",
        "state",
        "successor_ref",
        "time",
        "transition_id",
        "uncertainty",
    )
    normalized: dict[str, list[dict[str, Any]]] = {}
    for lineage_name in LINEAGE_NAMES:
        records: list[dict[str, Any]] = []
        seen: set[str] = set()
        for index, raw in enumerate(_array(root[lineage_name], f"$.lineages.{lineage_name}")):
            path = f"$.lineages.{lineage_name}[{index}]"
            item = _object(raw, path)
            _exact_keys(item, required, path)
            transition_id = _string(item["transition_id"], f"{path}.transition_id")
            if transition_id in seen:
                raise ProfileValidationError(
                    f"duplicate transition_id in {lineage_name}: {transition_id!r}"
                )
            seen.add(transition_id)
            records.append(
                {
                    "evidence_refs": _unique_strings(item["evidence_refs"], f"{path}.evidence_refs", allow_empty=False),
                    "predecessor_ref": _string(item["predecessor_ref"], f"{path}.predecessor_ref"),
                    "state": _enum(item["state"], LINEAGE_STATES, f"{path}.state"),
                    "successor_ref": _string(item["successor_ref"], f"{path}.successor_ref"),
                    "time": _time_range(item["time"], f"{path}.time", window),
                    "transition_id": transition_id,
                    "uncertainty": _record_uncertainty(item["uncertainty"], f"{path}.uncertainty"),
                }
            )
        records.sort(
            key=lambda item: (
                item["time"]["lower"],
                item["time"]["upper"],
                item["transition_id"],
            )
        )
        normalized[lineage_name] = records
    return normalized


def _normalize_irreversible_transitions(
    value: Any, window: tuple[int, int]
) -> list[dict[str, Any]]:
    required = (
        "authority_refs",
        "decision_rule",
        "evidence_refs",
        "scope",
        "time",
        "transition_id",
        "uncertainty",
        "witness_refs",
    )
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(_array(value, "$.irreversible_transitions")):
        path = f"$.irreversible_transitions[{index}]"
        item = _object(raw, path)
        _exact_keys(item, required, path)
        transition_id = _string(item["transition_id"], f"{path}.transition_id")
        if transition_id in seen:
            raise ProfileValidationError(
                f"duplicate irreversible transition_id: {transition_id!r}"
            )
        seen.add(transition_id)
        records.append(
            {
                "authority_refs": _unique_strings(item["authority_refs"], f"{path}.authority_refs"),
                "decision_rule": _string(item["decision_rule"], f"{path}.decision_rule"),
                "evidence_refs": _unique_strings(item["evidence_refs"], f"{path}.evidence_refs", allow_empty=False),
                "scope": _string(item["scope"], f"{path}.scope"),
                "time": _time_range(item["time"], f"{path}.time", window),
                "transition_id": transition_id,
                "uncertainty": _record_uncertainty(item["uncertainty"], f"{path}.uncertainty"),
                "witness_refs": _unique_strings(item["witness_refs"], f"{path}.witness_refs"),
            }
        )
    records.sort(
        key=lambda item: (
            item["time"]["lower"],
            item["time"]["upper"],
            item["transition_id"],
        )
    )
    return records


def _normalize_claim_ceiling(value: Any) -> dict[str, Any]:
    path = "$.claim_ceiling"
    record = _object(value, path)
    required = ("allowed_claims", "basis_refs", "prohibited_inferences", "status")
    _exact_keys(record, required, path)
    prohibited = _unique_strings(
        record["prohibited_inferences"],
        f"{path}.prohibited_inferences",
        allow_empty=False,
    )
    missing = sorted(set(MANDATORY_PROHIBITED_INFERENCES) - set(prohibited))
    if missing:
        raise ProfileValidationError(
            f"{path}.prohibited_inferences missing mandatory values: {missing}"
        )
    return {
        "allowed_claims": _unique_strings(record["allowed_claims"], f"{path}.allowed_claims"),
        "basis_refs": _unique_strings(record["basis_refs"], f"{path}.basis_refs"),
        "prohibited_inferences": prohibited,
        "status": _enum(record["status"], CLAIM_STATUSES, f"{path}.status"),
    }


def _merge_intervals(intervals: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    ordered = sorted(intervals)
    merged: list[list[int]] = []
    for start, end in ordered:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [(start, end) for start, end in merged]


def _assert_no_pause_participation_overlap(
    verified: Sequence[dict[str, Any]], pauses: Sequence[dict[str, Any]]
) -> None:
    eligible = [
        item
        for item in verified
        if item["admission_status"] == "admitted" and item["eligible_for_duration"]
    ]
    for interval in eligible:
        for pause in pauses:
            if max(interval["start"], pause["start"]) < min(interval["end"], pause["end"]):
                raise ProfileValidationError(
                    "admitted duration interval "
                    f"{interval['interval_id']!r} overlaps known pause {pause['pause_id']!r}"
                )


def _unexplained_gaps(
    window: tuple[int, int], covered: Iterable[tuple[int, int]]
) -> list[dict[str, Any]]:
    merged = _merge_intervals(covered)
    gaps: list[dict[str, Any]] = []
    cursor = window[0]
    for start, end in merged:
        if cursor < start:
            gaps.append(
                {
                    "end": start,
                    "reason": "no_admitted_verified_participation_or_known_pause",
                    "start": cursor,
                }
            )
        cursor = max(cursor, end)
    if cursor < window[1]:
        gaps.append(
            {
                "end": window[1],
                "reason": "no_admitted_verified_participation_or_known_pause",
                "start": cursor,
            }
        )
    return gaps


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_json(value: Any) -> str:
    """Return canonical UTF-8 JSON text without a trailing newline."""

    return _canonical_bytes(value).decode("utf-8")


def build_profile(source: Mapping[str, Any]) -> dict[str, Any]:
    """Validate *source* and return a deterministic CI v1 profile result."""

    root = _object(source, "$")
    required = (
        "branch_ref",
        "claim_ceiling",
        "events",
        "irreversible_transitions",
        "known_pauses",
        "lineages",
        "observation_window",
        "profile_id",
        "schema_version",
        "subject_ref",
        "time_axis",
        "uncertainty",
        "verified_intervals",
        "witnesses",
    )
    _exact_keys(root, required, "$")
    if root["schema_version"] != INPUT_SCHEMA_VERSION:
        raise ProfileValidationError(
            f"$.schema_version must be {INPUT_SCHEMA_VERSION!r}"
        )

    time_axis = _object(root["time_axis"], "$.time_axis")
    _exact_keys(time_axis, ("basis", "origin", "unit"), "$.time_axis")
    normalized_time_axis = {
        "basis": _string(time_axis["basis"], "$.time_axis.basis"),
        "origin": _string(time_axis["origin"], "$.time_axis.origin"),
        "unit": _string(time_axis["unit"], "$.time_axis.unit"),
    }

    window_record = _object(root["observation_window"], "$.observation_window")
    _exact_keys(window_record, ("end", "start"), "$.observation_window")
    window_start = _integer(window_record["start"], "$.observation_window.start")
    window_end = _integer(window_record["end"], "$.observation_window.end")
    if window_start >= window_end:
        raise ProfileValidationError("$.observation_window requires start < end")
    window = (window_start, window_end)

    witnesses, witness_counts = _normalize_witnesses(root["witnesses"], window)
    verified, interval_counts = _normalize_verified_intervals(
        root["verified_intervals"], window
    )
    pauses = _normalize_pauses(root["known_pauses"], window)
    events = _normalize_events(root["events"], window)
    lineages = _normalize_lineages(root["lineages"], window)
    irreversible = _normalize_irreversible_transitions(
        root["irreversible_transitions"], window
    )
    uncertainty = _structured_uncertainty(root["uncertainty"], "$.uncertainty")
    claim_ceiling = _normalize_claim_ceiling(root["claim_ceiling"])

    _assert_no_pause_participation_overlap(verified, pauses)
    admitted_witnesses = [
        witness for witness in witnesses if witness["admission_status"] == "admitted"
    ]
    first_witness = min(
        admitted_witnesses,
        key=lambda item: (
            item["time"]["lower"],
            item["time"]["upper"],
            item["witness_id"],
        ),
        default=None,
    )
    last_witness = min(
        admitted_witnesses,
        key=lambda item: (
            -item["time"]["upper"],
            -item["time"]["lower"],
            item["witness_id"],
        ),
        default=None,
    )

    eligible_intervals = [
        interval
        for interval in verified
        if interval["admission_status"] == "admitted"
        and interval["eligible_for_duration"]
    ]
    merged_verified = _merge_intervals(
        (item["start"], item["end"]) for item in eligible_intervals
    )
    verified_duration = sum(end - start for start, end in merged_verified)
    coverage = list(merged_verified)
    coverage.extend((pause["start"], pause["end"]) for pause in pauses)

    event_coordinates = {
        f"E_{event_type}": [
            event for event in events if event["event_type"] == event_type
        ]
        for event_type in EVENT_TYPES
    }
    vector: dict[str, Any] = {
        "D_verified": {
            "method": "union_of_admitted_eligible_closed_open_intervals",
            "unit": normalized_time_axis["unit"],
            "value": verified_duration,
        },
        **event_coordinates,
        "G_unexplained": _unexplained_gaps(window, coverage),
        "I_verified": eligible_intervals,
        "L_authority": lineages["authority"],
        "L_governance": lineages["governance"],
        "L_memory": lineages["memory"],
        "L_witness": lineages["witness"],
        "P_known": pauses,
        "T_irreversible": irreversible,
        "U": uncertainty,
        "W_first": first_witness,
        "W_last": last_witness,
    }

    output = {
        "branch_ref": _string(root["branch_ref"], "$.branch_ref"),
        "calculation_policy": {
            "duration": "union_without_double_counting",
            "event_order": "time_lower_then_time_upper_then_identifier",
            "gap": "observation_window_minus_verified_union_and_known_pause_union",
            "interval_semantics": "closed_open",
            "witness_order": "first_lower_asc_upper_asc_id_last_upper_desc_lower_desc_id",
        },
        "claim_ceiling": claim_ceiling,
        "evidence_counts": {
            "verified_intervals": interval_counts,
            "witnesses": witness_counts,
        },
        "formation_depth_vector": vector,
        "formation_depth_vector_sha256": hashlib.sha256(
            _canonical_bytes(vector)
        ).hexdigest(),
        "generated_by": IMPLEMENTATION_VERSION,
        "input_schema_version": INPUT_SCHEMA_VERSION,
        "observation_window": {"end": window_end, "start": window_start},
        "profile_id": _string(root["profile_id"], "$.profile_id"),
        "schema_version": OUTPUT_SCHEMA_VERSION,
        "subject_ref": _string(root["subject_ref"], "$.subject_ref"),
        "time_axis": normalized_time_axis,
    }
    return output


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ProfileValidationError(f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def load_input(path: Path) -> Mapping[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(
                handle,
                object_pairs_hook=_reject_duplicate_keys,
                parse_float=Decimal,
            )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ProfileValidationError(f"cannot read input JSON: {exc}") from exc
    return _object(value, "$")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build an inert, deterministic CI formation-depth vector."
    )
    parser.add_argument("input", type=Path, help="v1 input JSON path")
    parser.add_argument(
        "--output",
        type=Path,
        help="write canonical JSON here instead of stdout",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        profile = build_profile(load_input(args.input))
        rendered = canonical_json(profile) + "\n"
        if args.output is None:
            sys.stdout.buffer.write(rendered.encode("utf-8"))
        else:
            args.output.write_text(rendered, encoding="utf-8", newline="\n")
    except (OSError, ProfileValidationError) as exc:
        sys.stderr.write(f"ci_profile: error: {exc}\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
