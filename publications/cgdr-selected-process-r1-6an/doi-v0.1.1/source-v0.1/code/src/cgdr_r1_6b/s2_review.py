from __future__ import annotations

import base64
from typing import Any

from .common import canonical_hash
from .s2_handoff import (
    PROTECTED_CARRIAGE_FIELDS,
    TASK_ID,
    inventory_issues,
    sha256_bytes,
)
from .signing import verify
from .state_transfer import decode_state_b64, validate_state_bytes


REVIEWER_ID = "INDEPENDENT_R1_6I_S2_EVIDENCE_REVIEWER"
REQUIRED_STEPS = (
    "W0_START_REQUEST",
    "W0_CHILD_BOUND",
    "W0_SECURITY_BOUND",
    "W0_READY",
    "W0_PONG",
    "W0_DELTA_CONTROLS",
    "W0_LOAD_ACK",
    "W0_CHECKPOINT",
    "W0_SHAM_WAIT",
    "W0_RELEASE",
    "W0_CONTINUE",
    "E0_FENCED",
    "W0_STOP_ACK",
    "W0_OS_WAIT_EXIT",
    "W1_START_REQUEST",
    "W1_CHILD_BOUND",
    "W1_SECURITY_BOUND",
    "W1_READY",
    "W1_PONG",
    "W1_DELTA_CONTROLS",
    "W1_RESTORE",
    "W1_CHECKPOINT",
    "E1_ISSUED",
    "W1_ADMISSION",
    "W1_BROKER_HOLD",
    "W1_STOP_ACK",
    "W1_OS_WAIT_EXIT",
)


def _event_ok(event: Any, kind: str, instance_id: str) -> bool:
    return isinstance(event, dict) and event.get("event") == kind and event.get("instance_id") == instance_id


def _security_issues(role: str, worker: dict[str, Any]) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    diagnostics = worker.get("diagnostics") or {}
    binding = diagnostics.get("child_binding") or {}
    security = diagnostics.get("child_security") or {}
    runtime = diagnostics.get("staged_runtime") or {}
    instance_id = worker.get("instance_id")
    if not binding or binding.get("instance_id") != instance_id:
        issues.append((f"{role}_TRUSTED_CHILD_BINDING_MISSING_OR_WRONG", "UNKNOWN"))
        return issues
    exact = ("worker_pid", "worker_start_ticks", "pid_namespace", "network_namespace", "mount_namespace")
    if not security or any(security.get(name) != binding.get(name) for name in exact):
        issues.append((f"{role}_TRUSTED_SECURITY_BINDING_MISMATCH", "UNKNOWN"))
        return issues
    if security.get("worker_stderr_route") != "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT" or security.get("trusted_receipt_route") != "PARENT_ONLY_STDERR_V1":
        issues.append((f"{role}_RECEIPT_ROUTE_NOT_SEPARATE", "FAIL"))
    status = security.get("status") or {}
    fields = status.get("status_fields") or {}
    if any(fields.get(name) != "0000000000000000" for name in ("CapInh", "CapPrm", "CapEff", "CapBnd", "CapAmb")):
        issues.append((f"{role}_CAPABILITY_SET_NOT_ZERO", "FAIL"))
    if fields.get("NoNewPrivs") != "1":
        issues.append((f"{role}_NO_NEW_PRIVS_NOT_SET", "FAIL"))
    fds = [row.get("fd") for row in status.get("fds", []) if isinstance(row, dict)]
    if fds != [0, 1, 2]:
        issues.append((f"{role}_INHERITED_FD_SET_MISMATCH", "FAIL"))
    mounts = {row.get("mount_point"): row for row in security.get("mounts", []) if isinstance(row, dict)}
    stage_dir = runtime.get("stage_dir")
    stage = mounts.get(stage_dir) or {}
    scratch = mounts.get(f"{str(stage_dir).rstrip('/')}/scratch") or {}
    private = mounts.get(f"{str(stage_dir).rstrip('/')}/private") or {}
    host_mask = mounts.get("/mnt") or {}
    if "ro" not in stage.get("mount_options", []):
        issues.append((f"{role}_STAGE_NOT_READ_ONLY", "FAIL"))
    if "rw" not in scratch.get("mount_options", []):
        issues.append((f"{role}_SCRATCH_NOT_WRITABLE_PRIVATE_MOUNT", "FAIL"))
    if private.get("filesystem") != "tmpfs" or host_mask.get("filesystem") != "tmpfs":
        issues.append((f"{role}_PRIVATE_OR_HOST_MASK_MISSING", "FAIL"))
    if runtime.get("mode") != "S2":
        issues.append((f"{role}_RUNTIME_MODE_NOT_S2", "FAIL"))
    ready = worker.get("ready") or {}
    expected_environment = {
        "CGDR_INSTANCE_ID", "CGDR_PDEATHSIG_SET", "CGDR_S1_MODE", "CGDR_S2_MODE",
        "CGDR_S2_PLAN", "CGDR_S2_PLAN_SHA256", "CGDR_S2_ATTEMPT_ID", "CGDR_S2_WORKER_ROLE",
        "LANG", "PATH", "PYTHONHASHSEED",
    }
    observed_environment = set((ready.get("security_metadata") or {}).get("environment_keys") or [])
    if observed_environment != expected_environment:
        issues.append((f"{role}_WORKER_REPORTED_ENV_ALLOWLIST_MISMATCH", "FAIL"))
    inner_exit = diagnostics.get("inner_exit") or {}
    exact_exit_fields = ("instance_id", "worker_pid", "worker_start_ticks", "waiter_pid", "waiter_start_ticks", "pid_namespace", "network_namespace", "mount_namespace", "worker_sha256", "launcher_sha256")
    if (
        inner_exit.get("marker") != "CGDR_INNER_EXIT"
        or inner_exit.get("binding_source") != "TRUSTED_DIRECT_FORK_PARENT"
        or inner_exit.get("wait_source") != "POSIX_WAITPID_CHILD"
        or inner_exit.get("receipt_channel") != "PARENT_ONLY_STDERR_V1"
        or inner_exit.get("return_code") != 0
        or any(inner_exit.get(name) != binding.get(name) for name in exact_exit_fields)
        or inner_exit.get("security_receipt_sha256") != security.get("security_receipt_sha256")
        or (diagnostics.get("launch_outcome") or {}).get("cleanup_status") != "PROVEN"
    ):
        issues.append((f"{role}_DIRECT_WAIT_EXIT_BINDING_INVALID", "UNKNOWN"))
    return issues


def _delta_issues(role: str, plan: dict[str, Any], expected_plan_sha256: Any, event: Any) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    if not isinstance(event, dict) or event.get("event") != "S2_DELTA_RESULT":
        return [(f"{role}_DELTA_RESULT_MISSING", "UNKNOWN")]
    if event.get("worker_role") != role or not isinstance(expected_plan_sha256, str) or event.get("plan_sha256") != expected_plan_sha256:
        issues.append((f"{role}_DELTA_PLAN_BINDING_MISMATCH", "FAIL"))
    result = event.get("result") or {}
    rows = result.get("rows")
    probes = plan.get("probes")
    if not isinstance(rows, list) or not isinstance(probes, list) or len(rows) != len(probes):
        return issues + [(f"{role}_DELTA_RESULT_INCOMPLETE", "UNKNOWN")]
    by_id = {row.get("probe_id"): row for row in rows if isinstance(row, dict)}
    for probe in probes:
        probe_id = probe.get("probe_id")
        row = by_id.get(probe_id)
        if not row:
            issues.append((f"{role}_MISSING_DELTA_PROBE:{probe_id}", "UNKNOWN"))
            continue
        if row.get("operation") != probe.get("operation") or row.get("target") != probe.get("target"):
            issues.append((f"{role}_DELTA_TARGET_BINDING_MISMATCH:{probe_id}", "FAIL"))
            continue
        expected = probe.get("expectation")
        allowed = row.get("allowed")
        if expected == "EXPECT_ALLOW":
            if allowed is not True:
                issues.append((f"{role}_ALLOWED_CONTROL_FAILED:{probe_id}", "FAIL"))
            if probe.get("operation") == "FILE_READ" and (
                row.get("observed_sha256") != probe.get("expected_sha256")
                or row.get("bytes") != probe.get("expected_bytes")
            ):
                issues.append((f"{role}_INPUT_READBACK_MISMATCH:{probe_id}", "FAIL"))
        elif expected == "EXPECT_DENY":
            if allowed is True:
                issues.append((f"{role}_FORBIDDEN_ACCESS_SUCCEEDED:{probe_id}", "FAIL"))
            elif allowed is not False or not isinstance(row.get("errno"), int):
                issues.append((f"{role}_DENIAL_OBSERVATION_INCOMPLETE:{probe_id}", "UNKNOWN"))
        else:
            issues.append((f"{role}_DELTA_EXPECTATION_UNKNOWN:{probe_id}", "FAIL"))
    if result.get("stopped_after_forbidden_success") is not None:
        issues.append((f"{role}_DELTA_STOPPED_AFTER_FORBIDDEN_SUCCESS", "FAIL"))
    return issues


def review_s2_evidence(bundle: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []

    def add(code: str, severity: str) -> None:
        item = {"code": code, "severity": severity}
        if item not in findings:
            findings.append(item)

    if bundle.get("task_id") != TASK_ID:
        add("OUTER_TASK_BINDING_MISMATCH", "FAIL")
    scope = bundle.get("evidence_scope")
    attempt_id = bundle.get("attempt_id")
    chronology = bundle.get("chronology")
    if not isinstance(chronology, list):
        chronology = []
        add("CHRONOLOGY_MISSING", "UNKNOWN")
    positions: dict[str, int] = {}
    for index, row in enumerate(chronology):
        if isinstance(row, dict) and isinstance(row.get("step"), str) and row["step"] not in positions:
            positions[row["step"]] = index
    for step in REQUIRED_STEPS:
        if step not in positions:
            add(f"MISSING_CAUSAL_STEP:{step}", "UNKNOWN")
    present = [step for step in REQUIRED_STEPS if step in positions]
    for left, right in zip(present, present[1:]):
        if positions[left] > positions[right]:
            add(f"CAUSAL_ORDER_INVALID:{left}_BEFORE_{right}", "FAIL")

    w0, w1 = bundle.get("w0") or {}, bundle.get("w1") or {}
    w0_id, w1_id = w0.get("instance_id"), w1.get("instance_id")
    if not isinstance(w0_id, str) or not isinstance(w1_id, str):
        add("WORKER_INSTANCE_BINDING_MISSING", "UNKNOWN")
    elif w0_id == w1_id:
        add("WORKER_INSTANCES_NOT_DISTINCT", "FAIL")
    for row in chronology:
        if not isinstance(row, dict):
            continue
        step, instance_id = row.get("step"), row.get("instance_id")
        if isinstance(step, str) and step.startswith("W0_") and step not in {"W0_START_REQUEST"} and instance_id not in {None, w0_id}:
            add(f"FOREIGN_W0_INSTANCE:{step}", "FAIL")
        if isinstance(step, str) and step.startswith("W1_") and step not in {"W1_START_REQUEST"} and instance_id not in {None, w1_id}:
            add(f"FOREIGN_W1_INSTANCE:{step}", "FAIL")
    for code, severity in _security_issues("W0", w0):
        add(code, severity)
    for code, severity in _security_issues("W1", w1):
        add(code, severity)

    plans = bundle.get("delta_plans") or {}
    plan_hashes = bundle.get("delta_plan_hashes") or {}
    for role, worker in (("W0", w0), ("W1", w1)):
        plan = plans.get(role)
        if not isinstance(plan, dict):
            add(f"{role}_DELTA_PLAN_MISSING", "UNKNOWN")
        else:
            for code, severity in _delta_issues(role, plan, plan_hashes.get(role), worker.get("delta_result")):
                add(code, severity)

    prestate, inventory = bundle.get("prestate") or {}, bundle.get("inventory") or {}
    disk = bundle.get("checkpoint_disk") or {}
    try:
        checkpoint_raw = base64.b64decode(str(disk.get("readback_b64", "")).encode("ascii"), validate=True)
    except Exception:
        checkpoint_raw = b""
        add("CHECKPOINT_DISK_READBACK_INVALID", "UNKNOWN")
    if checkpoint_raw:
        if disk.get("write_raw_sha256") != sha256_bytes(checkpoint_raw) or disk.get("readback_raw_sha256") != sha256_bytes(checkpoint_raw):
            add("CHECKPOINT_DISK_RAW_HASH_MISMATCH", "FAIL")
        if disk.get("write_b64") != disk.get("readback_b64"):
            add("CHECKPOINT_DISK_BYTES_MISMATCH", "FAIL")
        state_check = validate_state_bytes(checkpoint_raw, prestate, stated_hash=disk.get("canonical_sha256"))
        for issue in state_check.get("issues", []):
            add(f"W0_DISK_STATE:{issue}", "FAIL")
        state = state_check.get("state") if isinstance(state_check.get("state"), dict) else {}
        for issue in inventory_issues(state, inventory):
            add(f"W0_INVENTORY:{issue}", "FAIL")
    else:
        state = {}
        add("CHECKPOINT_DISK_BYTES_MISSING", "UNKNOWN")

    w0_checkpoint = w0.get("checkpoint") or {}
    if not _event_ok(w0.get("load_ack"), "LOAD_ACK", str(w0_id)):
        add("W0_LOAD_ACK_INVALID", "UNKNOWN")
    elif w0.get("load_ack", {}).get("state_sha256") != disk.get("canonical_sha256"):
        add("W0_LOAD_ACK_HASH_MISMATCH", "FAIL")
    if not _event_ok(w0_checkpoint, "CHECKPOINT", str(w0_id)):
        add("W0_CHECKPOINT_EVENT_INVALID", "UNKNOWN")
    else:
        raw, _, decode_issues = decode_state_b64(w0_checkpoint.get("state_b64"))
        for issue in decode_issues:
            add(f"W0_CHECKPOINT:{issue}", "FAIL")
        if raw != checkpoint_raw or w0_checkpoint.get("checkpoint_seq") != 1:
            add("W0_CHECKPOINT_BYTES_OR_SEQUENCE_MISMATCH", "FAIL")
    if not _event_ok(w0.get("sham_wait"), "SHAM_WAITING", str(w0_id)):
        add("W0_SHAM_WAIT_INVALID", "FAIL")
    if not _event_ok(w0.get("release"), "RELEASED", str(w0_id)):
        add("W0_RELEASE_INVALID", "FAIL")
    if not _event_ok(w0.get("continued"), "CONTINUED", str(w0_id)):
        add("W0_CONTINUE_INVALID", "FAIL")

    restore = w1.get("restore") or {}
    w1_checkpoint = w1.get("checkpoint") or {}
    if not _event_ok(restore, "RESTORED", str(w1_id)):
        add("W1_RESTORE_ACK_INVALID", "UNKNOWN")
    elif restore.get("state_sha256") != sha256_bytes(checkpoint_raw) or restore.get("checkpoint_seq") != 1:
        add("W1_RESTORE_HASH_OR_SEQUENCE_MISMATCH", "FAIL")
    raw_w1, state_w1, decode_w1 = decode_state_b64(w1_checkpoint.get("state_b64"))
    if not _event_ok(w1_checkpoint, "CHECKPOINT", str(w1_id)) or decode_w1:
        add("W1_FULL_CHECKPOINT_INVALID", "UNKNOWN" if not w1_checkpoint else "FAIL")
    elif raw_w1 != checkpoint_raw or w1_checkpoint.get("checkpoint_seq") != 1:
        add("W1_RESTORED_BYTES_OR_SEQUENCE_MISMATCH", "FAIL")
    if isinstance(state_w1, dict):
        for issue in inventory_issues(state_w1, inventory):
            add(f"W1_INVENTORY:{issue}", "FAIL")

    public_map = bundle.get("public_signer_map") or {}
    authority = bundle.get("authority") or {}
    fence, e1 = authority.get("e0_fence") or {}, authority.get("e1_current") or {}
    for label, envelope in (("E0_FENCE", fence), ("E1", e1)):
        valid, reason = verify(envelope, public_map)
        if not valid:
            add(f"{label}_SIGNATURE_INVALID:{reason}", "FAIL")
    fence_payload, e1_payload = fence.get("payload") or {}, e1.get("payload") or {}
    w0_binding = (w0.get("diagnostics") or {}).get("child_binding") or {}
    w1_binding = (w1.get("diagnostics") or {}).get("child_binding") or {}
    if fence_payload.get("epoch") != "E0" or fence_payload.get("instance_id") != w0_id or fence_payload.get("worker_start_ticks") != w0_binding.get("worker_start_ticks"):
        add("E0_FENCE_SCOPE_MISMATCH", "FAIL")
    if (
        e1_payload.get("epoch") != "E1"
        or e1_payload.get("outer_task_id") != TASK_ID
        or e1_payload.get("attempt_id") != attempt_id
        or e1_payload.get("instance_id") != w1_id
        or e1_payload.get("worker_start_ticks") != w1_binding.get("worker_start_ticks")
        or e1_payload.get("checkpoint_raw_sha256") != sha256_bytes(checkpoint_raw)
        or e1_payload.get("fence_envelope_sha256") != canonical_hash(fence)
    ):
        add("E1_CURRENT_SCOPE_MISMATCH_OR_E0_REUSED", "FAIL")

    current_source = authority.get("current_source_view") or {}
    transition = authority.get("epoch_transition") or {}
    if current_source.get("current_attestation", {}).get("epoch") != "E1" or current_source.get("registry", {}).get("epoch") != "E1":
        add("CURRENT_AUTHORITY_NOT_E1", "FAIL")
    if transition.get("e0_status") != "HISTORICAL_NOT_CURRENT_AFTER_FENCE" or transition.get("e1_status") != "CURRENT_FOR_W1_SCOPED_ADMISSION":
        add("EPOCH_TRANSITION_STATUS_INVALID", "FAIL")
    if isinstance(state_w1, dict):
        for field in PROTECTED_CARRIAGE_FIELDS:
            if current_source.get(field) != state_w1.get(field):
                add(f"E1_OVERLAY_CHANGED_CARRIED_MATERIAL:{field}", "FAIL")
    source_body = {key: value for key, value in current_source.items() if key != "source_hash"}
    if current_source.get("source_hash") != canonical_hash(source_body):
        add("CURRENT_SOURCE_HASH_INVALID", "FAIL")

    gate = bundle.get("gate") or {}
    decision, broker = gate.get("decision") or {}, gate.get("broker_result") or {}
    intent = gate.get("operation_intent")
    intent_hash = gate.get("operation_intent_hash")
    if not isinstance(intent, dict) or intent.get("capture_stage") != "PRE_COMMIT" or intent_hash != canonical_hash(intent):
        add("INDEPENDENT_OPERATION_INTENT_MISSING_OR_INVALID", "FAIL")
    elif intent.get("expected_effect_row") is not None or intent.get("effect_expectation") != "NO_EFFECT":
        add("OPEN_HOLD_INTENT_EXPECTS_EFFECT", "FAIL")
    if decision.get("admission") != "ADMITTED":
        add("W1_CURRENT_ADMISSION_NOT_ADMITTED", "FAIL")
    if decision.get("q_state") != "OPEN" or decision.get("action_gate") != "HOLD":
        add("PROTECTED_ACTION_NOT_OPEN_HOLD", "FAIL")
    if decision.get("memory_promotion_authorized") is not False:
        add("MEMORY_PROMOTION_AUTHORIZED", "FAIL")
    if broker.get("result") != "HELD" or broker.get("effect_delta") != 0 or broker.get("binding_revalidated") is not True:
        add("BROKER_DID_NOT_ENFORCE_BOUND_OPEN_HOLD", "FAIL")

    before, after = gate.get("sink_before"), gate.get("sink_after")
    if not isinstance(before, dict) or not isinstance(after, dict) or not all(
        isinstance(snapshot.get(name), list) for snapshot in (before, after) for name in ("effects", "promotions")
    ):
        add("S2_SINK_OBSERVATION_UNKNOWN", "UNKNOWN")
        effect_delta = promotion_delta = None
    else:
        effect_delta = len(after["effects"]) - len(before["effects"])
        promotion_delta = len(after["promotions"]) - len(before["promotions"])
        if effect_delta != 0:
            add("UNEXPECTED_S2_EFFECT", "FAIL")
        if promotion_delta != 0:
            add("UNEXPECTED_S2_PROMOTION", "FAIL")
        operation_id = gate.get("operation_id")
        own = [list(row) for row in after.get("operations", []) if isinstance(row, (list, tuple)) and row and row[0] == operation_id]
        if own != [[operation_id, gate.get("packet_projection", {}).get("proposal_hash"), "HELD"]]:
            add("EXACT_HELD_OPERATION_READBACK_MISMATCH", "FAIL")

    canaries = bundle.get("canary_snapshots") or {}
    for name in ("checkpoint_store_canary", "private_canary"):
        pair = canaries.get(name) or {}
        if pair.get("before") is None or pair.get("after") is None:
            add(f"CANARY_SNAPSHOT_MISSING:{name}", "UNKNOWN")
        elif pair.get("before") != pair.get("after"):
            add(f"CANARY_CHANGED:{name}", "FAIL")

    delta = bundle.get("s1_to_s2_delta") or {}
    if delta.get("status") != "STATIC_CONFIG_VERIFIED_FOR_S2_OBJECT_DELTA":
        add("S1_TO_S2_DELTA_NOT_VERIFIED", "FAIL")
    native = bundle.get("native_validation") or {}
    layers = native.get("layer_status") or {}
    for layer in ("shape", "record_semantics", "registered_evidence", "bundle_links"):
        if layers.get(layer) != "PASS":
            add(f"NATIVE_LAYER_NOT_PASS:{layer}", "FAIL" if layer in layers else "UNKNOWN")
    expected_native_scope = "ACTUAL_S2_PREFLIGHT" if scope == "ACTUAL_S2_PREFLIGHT" else "SYNTHETIC_REGRESSION"
    if native.get("scope") != expected_native_scope or native.get("accepted") is not True:
        add("NATIVE_RESULT_NOT_ACCEPTED_ACTUAL_PREFLIGHT", "FAIL" if native else "UNKNOWN")

    has_fail = any(item["severity"] == "FAIL" for item in findings)
    has_unknown = any(item["severity"] == "UNKNOWN" for item in findings)
    if has_fail:
        verdict = "FAIL"
    elif has_unknown:
        verdict = "INCONCLUSIVE"
    elif scope == "ACTUAL_S2_PREFLIGHT":
        verdict = "PASS_SCOPED_S2"
    else:
        verdict = "PASS_SYNTHETIC_REVIEW_CONTROL"
    return {
        "reviewer": REVIEWER_ID,
        "evidence_scope": scope,
        "verdict": verdict,
        "issues": sorted(findings, key=lambda item: (item["severity"], item["code"])),
        "required_steps": list(REQUIRED_STEPS),
        "observed_positions": positions,
        "observed_effect_delta": effect_delta,
        "observed_promotion_delta": promotion_delta,
        "claim_ceiling": "One task-local W0-to-W1 OPEN-state handoff, scoped admission, HOLD gate, and declared sink window only; not full conformance, same-c, B5 superiority, or live readiness.",
    }
