"""Shadow-only C-L4 companion for local fixture smoke runs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from .append_log import append_jsonl
from .material_change import detect_material_change
from .models import NonFormationReceipt, TransitionWitness
from .non_formation import build_non_formation_receipt, validate_non_formation_receipt
from .replay import assess_continuity_reset, compare_digest, sha256_digest
from .validator import validate_transition_witness

def load_fixture(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def process_fixture(data: Mapping[str, Any], output_dir: str | Path) -> dict[str, Any]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    witness = TransitionWitness.from_mapping(data["witness"])
    validation = validate_transition_witness(witness)
    replay_anchor = sha256_digest(witness)
    witness.replay_anchor = replay_anchor
    append_jsonl(output / "transition_witness.jsonl", witness)

    result: dict[str, Any] = {
        "fixture": data.get("fixture_id"),
        "permission_state": validation.permission_state.value,
        "receipt": validation.receipt.value,
        "replay_anchor": replay_anchor,
        "validation": validation.to_dict(),
    }

    receipt_data = data.get("non_formation_receipt")
    if receipt_data:
        receipt = NonFormationReceipt.from_mapping(receipt_data)
        receipt.replay_anchor = sha256_digest(receipt)
        receipt_result = validate_non_formation_receipt(receipt)
        append_jsonl(output / "non_formation_receipts.jsonl", receipt)
        result["non_formation"] = receipt_result.to_dict()
    elif validation.permission_state.value != "PASS":
        receipt = build_non_formation_receipt(witness, reason="validation_not_pass")
        receipt_result = validate_non_formation_receipt(receipt)
        if receipt_result.valid:
            append_jsonl(output / "non_formation_receipts.jsonl", receipt)
        result["non_formation"] = receipt_result.to_dict()

    material = data.get("material_change")
    if material:
        previous = TransitionWitness.from_mapping(material["previous"])
        current = TransitionWitness.from_mapping(material["current"])
        event = detect_material_change(previous, current)
        append_jsonl(output / "material_change_events.jsonl", event)
        result["material_change"] = event.to_dict()

    replay = data.get("replay")
    if replay:
        replay_result = compare_digest(str(replay["expected"]), str(replay["actual"]))
        append_jsonl(output / "replay_results.jsonl", replay_result)
        result["replay"] = replay_result

    continuity = data.get("continuity_reset")
    if continuity:
        assessment = assess_continuity_reset(continuity)
        append_jsonl(output / "replay_results.jsonl", {"continuity_reset": assessment.to_dict()})
        result["continuity_reset"] = assessment.to_dict()

    return result
