from __future__ import annotations

"""Independent frozen-evidence reviewer for the task-local R1.6H S1 attempt."""

import hashlib
import json
from typing import Any


def _event_tag(event: dict[str, Any]) -> str:
    kind = event.get("kind")
    if kind == "IPC_SENT":
        return f"IPC_SENT:{event.get('command')}"
    if kind == "IPC_RECEIVED":
        return f"IPC_RECEIVED:{(event.get('worker_event') or {}).get('event')}"
    return str(kind)


def _issue(issues: list[dict[str, str]], severity: str, reason: str) -> None:
    issues.append({"severity": severity, "reason": reason})


def _controls_valid(value: Any, phase: str, issues: list[dict[str, str]]) -> None:
    if not isinstance(value, dict) or value.get("phase") != phase:
        _issue(issues, "MISSING", f"HELPER_{phase}_CONTROLS_MISSING")
        return
    for channel in ("unix", "tcp"):
        row = value.get(channel) or {}
        if row.get("matched_control") is not True or row.get("response_bytes") != 14:
            _issue(issues, "FAIL", f"HELPER_{phase}_{channel.upper()}_POSITIVE_CONTROL_FAILED")
        if len(row.get("accepted") or []) != 1:
            _issue(issues, "FAIL", f"HELPER_{phase}_{channel.upper()}_UNEXPECTED_CONNECTIONS")


def review_direct_wait_cleanup(binding: dict[str, Any], security: dict[str, Any], exit_receipt: dict[str, Any], wrapper_return_code: int | None, readers_stopped: bool) -> dict[str, Any]:
    """Review lifecycle exit independently from whether the access-policy snapshot passed."""
    reasons: list[str] = []
    exact_fields = (
        "instance_id", "receipt_nonce", "worker_pid", "worker_start_ticks", "waiter_pid", "waiter_start_ticks",
        "pid_namespace", "network_namespace", "mount_namespace", "worker_sha256", "launcher_sha256",
    )
    for name, record in (("binding", binding), ("security", security), ("exit", exit_receipt)):
        if record.get("_receipt_record_type") != "TRUSTED_PARENT_RECEIPT" or record.get("_receipt_channel") != "PARENT_ONLY_STDERR_V1":
            reasons.append(f"{name.upper()}_PROVENANCE_INVALID")
    if binding.get("binding_source") != "TRUSTED_DIRECT_FORK_PARENT" or binding.get("wait_source") != "POSIX_WAITPID_CHILD":
        reasons.append("BINDING_SOURCE_INVALID")
    if exit_receipt.get("binding_source") != "TRUSTED_DIRECT_FORK_PARENT" or exit_receipt.get("wait_source") != "POSIX_WAITPID_CHILD":
        reasons.append("EXIT_WAIT_SOURCE_INVALID")
    for field in exact_fields:
        if exit_receipt.get(field) != binding.get(field):
            reasons.append(f"EXIT_BINDING_MISMATCH:{field}")
    if exit_receipt.get("security_receipt_sha256") != security.get("security_receipt_sha256"):
        reasons.append("SECURITY_LINK_MISMATCH")
    if wrapper_return_code is None or exit_receipt.get("return_code") != wrapper_return_code:
        reasons.append("RETURN_CODE_MISMATCH_OR_UNKNOWN")
    if readers_stopped is not True:
        reasons.append("READERS_NOT_STOPPED")
    return {
        "reviewer": "INDEPENDENT_DIRECT_WAIT_CLEANUP_REVIEWER",
        "status": "PROVEN" if not reasons else "UNPROVEN",
        "reasons": reasons,
        "access_policy_snapshot_accepted": None,
        "scope": "exact child binding plus parent-only POSIX waitpid exit only",
    }


def review_s1_evidence(bundle: dict[str, Any]) -> dict[str, Any]:
    issues: list[dict[str, str]] = []
    plan = bundle.get("plan") or {}
    expected = bundle.get("expected") or {}
    events = bundle.get("events") or []
    helper = bundle.get("helper") or {}
    if plan.get("task_id") != "CGDR_SELECTED_PROCESS_ACCESS_BOUNDARY_S1_R1_6H":
        _issue(issues, "FAIL", "PLAN_TASK_BINDING_MISMATCH")
    canonical_plan_hash = hashlib.sha256(json.dumps(plan, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if canonical_plan_hash != bundle.get("plan_canonical_sha256"):
        _issue(issues, "FAIL", "PLAN_CANONICAL_HASH_MISMATCH")
    if bundle.get("plan_file_sha256") != expected.get("plan_file_sha256"):
        _issue(issues, "FAIL", "PLAN_FILE_HASH_MISMATCH")
    if plan.get("attempt_id") != expected.get("attempt_id"):
        _issue(issues, "FAIL", "PLAN_ATTEMPT_BINDING_MISMATCH")
    fixture_manifest = bundle.get("fixture_manifest") or {}
    if fixture_manifest.get("task_id") != plan.get("task_id") or fixture_manifest.get("attempt_id") != plan.get("attempt_id"):
        _issue(issues, "FAIL", "FIXTURE_MANIFEST_BINDING_MISMATCH")

    required = [
        "PROCESS_START_REQUESTED", "PROCESS_HANDLE_OBTAINED", "OS_CHILD_BOUND", "OS_CHILD_SECURITY_BOUND",
        "IPC_RECEIVED:READY", "IPC_SENT:PING", "IPC_RECEIVED:PONG", "IPC_SENT:S1_RUN",
        "IPC_RECEIVED:S1_PROBE_BATCH_RESULT", "IPC_SENT:STOP", "IPC_RECEIVED:STOP_ACK", "EXIT_OBSERVED",
    ]
    by_tag: dict[str, dict[str, Any]] = {}
    cursor = -1
    for wanted in required:
        found = None
        for index in range(cursor + 1, len(events)):
            if _event_tag(events[index]) == wanted:
                found = index
                break
        if found is None:
            _issue(issues, "MISSING", f"MISSING_REQUIRED_EVENT:{wanted}")
        else:
            cursor = found
            by_tag[wanted] = events[found]
    instance_id = expected.get("instance_id")
    for tag, event in by_tag.items():
        if event.get("instance_id") != instance_id:
            _issue(issues, "FAIL", f"WRONG_INSTANCE:{tag}")

    binding = (by_tag.get("OS_CHILD_BOUND") or {}).get("binding") or {}
    security = (by_tag.get("OS_CHILD_SECURITY_BOUND") or {}).get("security") or {}
    exit_event = by_tag.get("EXIT_OBSERVED") or {}
    exit_receipt = exit_event.get("inner_exit_receipt") or {}
    for record_name, record in (("BINDING", binding), ("SECURITY", security), ("EXIT", exit_receipt)):
        if record.get("_receipt_record_type") != "TRUSTED_PARENT_RECEIPT" or record.get("_receipt_channel") != "PARENT_ONLY_STDERR_V1":
            _issue(issues, "FAIL", f"{record_name}_RECEIPT_PROVENANCE_INVALID")
        if record.get("receipt_channel") != "PARENT_ONLY_STDERR_V1":
            _issue(issues, "FAIL", f"{record_name}_RECEIPT_CHANNEL_INVALID")
    for field, wanted in {
        "instance_id": instance_id,
        "receipt_nonce": expected.get("receipt_nonce"),
        "worker_sha256": expected.get("worker_sha256"),
        "launcher_sha256": expected.get("launcher_sha256"),
        "binding_source": "TRUSTED_DIRECT_FORK_PARENT",
        "wait_source": "POSIX_WAITPID_CHILD",
        "worker_stderr_route": "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT",
        "trusted_receipt_route": "PARENT_ONLY_STDERR_V1",
    }.items():
        if binding.get(field) != wanted:
            _issue(issues, "FAIL", f"CHILD_BINDING_MISMATCH:{field}")
    for field in ("worker_pid", "worker_start_ticks", "waiter_pid", "waiter_start_ticks"):
        if not isinstance(binding.get(field), int):
            _issue(issues, "MISSING", f"CHILD_BINDING_MISSING:{field}")
    for field in ("instance_id", "worker_pid", "worker_start_ticks", "pid_namespace", "network_namespace", "mount_namespace"):
        wanted = instance_id if field == "instance_id" else binding.get(field)
        if security.get(field) != wanted:
            _issue(issues, "FAIL", f"SECURITY_BINDING_MISMATCH:{field}")
        if exit_receipt.get(field) != wanted:
            _issue(issues, "FAIL", f"EXIT_BINDING_MISMATCH:{field}")
    if exit_receipt.get("security_receipt_sha256") != security.get("security_receipt_sha256"):
        _issue(issues, "FAIL", "EXIT_SECURITY_RECEIPT_LINK_MISMATCH")

    status = (security.get("status") or {}).get("status_fields") or {}
    security_for_hash = {key: value for key, value in security.items() if key not in {"security_receipt_sha256", "_receipt_record_type", "_receipt_channel"}}
    observed_security_hash = hashlib.sha256(json.dumps(security_for_hash, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if observed_security_hash != security.get("security_receipt_sha256"):
        _issue(issues, "FAIL", "SECURITY_RECEIPT_HASH_MISMATCH")
    for field in ("CapInh", "CapPrm", "CapEff", "CapBnd", "CapAmb"):
        if status.get(field) != "0000000000000000":
            _issue(issues, "FAIL", f"NONZERO_CHILD_CAPABILITY:{field}")
    if status.get("NoNewPrivs") != "1":
        _issue(issues, "FAIL", "NO_NEW_PRIVS_NOT_SET")
    fds = [item.get("fd") for item in ((security.get("status") or {}).get("fds") or []) if isinstance(item, dict)]
    if fds != [0, 1, 2]:
        _issue(issues, "FAIL", f"UNEXPECTED_CHILD_FDS:{fds!r}")
    mounts = {row.get("mount_point"): row for row in security.get("mounts", []) if isinstance(row, dict)}
    stage_dir = plan.get("stage_dir")
    helper_dir = (plan.get("endpoint_binding") or {}).get("helper_dir")
    for path, mode, filesystem in (
        (stage_dir, "ro", None),
        (f"{stage_dir}/scratch", "rw", "tmpfs"),
        (f"{stage_dir}/private", None, "tmpfs"),
        (helper_dir, None, "tmpfs"),
    ):
        row = mounts.get(path) or {}
        if not row or (mode and mode not in row.get("mount_options", [])) or (filesystem and row.get("filesystem") != filesystem):
            _issue(issues, "MISSING", f"MOUNT_POLICY_NOT_OBSERVED:{path}")

    ready = ((by_tag.get("IPC_RECEIVED:READY") or {}).get("worker_event") or {})
    for field, wanted in {
        "instance_id": instance_id,
        "pid": binding.get("worker_pid"),
        "proc_start_ticks": binding.get("worker_start_ticks"),
        "pid_namespace": binding.get("pid_namespace"),
        "network_namespace": binding.get("network_namespace"),
        "mount_namespace": binding.get("mount_namespace"),
        "s1_mode": True,
        "s1_plan_sha256": expected.get("plan_file_sha256"),
    }.items():
        if ready.get(field) != wanted:
            _issue(issues, "FAIL", f"READY_BINDING_MISMATCH:{field}")
    ready_security = ready.get("security_metadata") or {}
    if ready_security.get("open_fds") != [0, 1, 2]:
        _issue(issues, "FAIL", "WORKER_REPORTED_FD_POLICY_MISMATCH")
    allowed_environment = {"CGDR_INSTANCE_ID", "CGDR_PDEATHSIG_SET", "CGDR_S1_ATTEMPT_ID", "CGDR_S1_MODE", "CGDR_S1_PLAN", "CGDR_S1_PLAN_SHA256", "LANG", "LC_CTYPE", "PATH", "PYTHONHASHSEED"}
    environment_keys = set(ready_security.get("environment_keys") or [])
    if not {"CGDR_INSTANCE_ID", "CGDR_S1_ATTEMPT_ID", "CGDR_S1_MODE", "CGDR_S1_PLAN", "CGDR_S1_PLAN_SHA256", "PATH", "LANG"}.issubset(environment_keys) or not environment_keys.issubset(allowed_environment):
        _issue(issues, "FAIL", "WORKER_ENVIRONMENT_ALLOWLIST_MISMATCH")
    if ready_security.get("securebits") != 207:
        _issue(issues, "FAIL", "WORKER_SECUREBITS_POLICY_MISMATCH")
    ready_fields = ready_security.get("status_fields") or {}
    for field in ("Uid", "Gid", "Groups", "CapInh", "CapPrm", "CapEff", "CapBnd", "CapAmb", "NoNewPrivs"):
        if ready_fields.get(field) != status.get(field):
            _issue(issues, "FAIL", f"WORKER_PARENT_SECURITY_VIEW_MISMATCH:{field}")

    pong = ((by_tag.get("IPC_RECEIVED:PONG") or {}).get("worker_event") or {})
    if pong.get("nonce") != expected.get("ping_nonce") or pong.get("message_id") != expected.get("ping_message_id") or pong.get("instance_id") != instance_id:
        _issue(issues, "FAIL", "PING_PONG_BINDING_MISMATCH")
    batch = ((by_tag.get("IPC_RECEIVED:S1_PROBE_BATCH_RESULT") or {}).get("worker_event") or {})
    if batch.get("attempt_id") != expected.get("attempt_id") or batch.get("plan_sha256") != expected.get("plan_file_sha256"):
        _issue(issues, "FAIL", "PROBE_BATCH_BINDING_MISMATCH")
    result = batch.get("result") or {}
    actual_rows = result.get("rows") or []
    actual_by_id = {row.get("probe_id"): row for row in actual_rows if isinstance(row, dict)}
    if len(actual_by_id) != len(actual_rows):
        _issue(issues, "FAIL", "DUPLICATE_OR_MISSING_ACTUAL_PROBE_ID")
    allow_count = 0
    deny_count = 0
    for planned in plan.get("probes", []):
        probe_id = planned.get("probe_id")
        row = actual_by_id.get(probe_id)
        if row is None:
            _issue(issues, "MISSING", f"PROBE_NOT_OBSERVED:{probe_id}")
            continue
        for field in ("object_id", "operation", "expectation", "target"):
            if row.get(field) != planned.get(field):
                _issue(issues, "FAIL", f"PROBE_BINDING_MISMATCH:{probe_id}:{field}")
        if row.get("syscall_attempted") is not True:
            _issue(issues, "MISSING", f"SYSCALL_NOT_OBSERVED:{probe_id}")
        if planned.get("expectation") == "EXPECT_ALLOW":
            if row.get("allowed") is not True:
                _issue(issues, "FAIL", f"ALLOWED_CONTROL_DENIED:{probe_id}")
            else:
                allow_count += 1
            if planned.get("expected_sha256") and row.get("observed_sha256") != planned.get("expected_sha256"):
                _issue(issues, "FAIL", f"ALLOWED_CONTENT_HASH_MISMATCH:{probe_id}")
            if planned.get("write_payload"):
                digest = hashlib.sha256(planned["write_payload"].encode()).hexdigest()
                if row.get("observed_sha256") != digest:
                    _issue(issues, "FAIL", f"SCRATCH_READBACK_HASH_MISMATCH:{probe_id}")
        else:
            if row.get("allowed") is True:
                _issue(issues, "FAIL", f"FORBIDDEN_ACCESS_SUCCEEDED:{probe_id}")
            elif row.get("errno") not in planned.get("accepted_errno", []):
                _issue(issues, "MISSING", f"DENIAL_ERRNO_UNBOUND:{probe_id}:{row.get('errno')}")
            else:
                deny_count += 1
    if result.get("stopped_after_forbidden_success") is not None:
        _issue(issues, "FAIL", f"RUNTIME_STOPPED_AFTER_FORBIDDEN_SUCCESS:{result.get('stopped_after_forbidden_success')}")

    pre_paths = (bundle.get("pre_snapshot") or {}).get("paths") or {}
    post_paths = (bundle.get("post_snapshot") or {}).get("paths") or {}
    if expected.get("fixture_manifest_sha256") != bundle.get("fixture_manifest_file_sha256"):
        _issue(issues, "FAIL", "FIXTURE_MANIFEST_HASH_MISMATCH")
    for fixture in fixture_manifest.get("files", []):
        relative = str(fixture.get("relative_path", ""))
        if fixture.get("destination") == "STAGE":
            target = f"{stage_dir}/{relative}"
        elif fixture.get("destination") == "HELPER" and relative.startswith("parent_service/"):
            target = f"{helper_dir}/{relative.split('/', 1)[1]}"
        else:
            _issue(issues, "FAIL", f"FIXTURE_DESTINATION_INVALID:{relative}")
            continue
        before = pre_paths.get(target) or {}
        after = post_paths.get(target) or {}
        for phase, snapshot in (("PRE", before), ("POST", after)):
            if snapshot.get("sha256") != fixture.get("sha256") or snapshot.get("bytes") != fixture.get("bytes"):
                _issue(issues, "FAIL", f"FIXTURE_{phase}_HASH_OR_SIZE_MISMATCH:{relative}")
    for planned in plan.get("probes", []):
        if planned.get("operation") not in {"FILE_READ", "FILE_APPEND"}:
            continue
        target = planned.get("target")
        before = pre_paths.get(target)
        after = post_paths.get(target)
        if not before or not after:
            _issue(issues, "MISSING", f"TARGET_SNAPSHOT_MISSING:{planned.get('probe_id')}")
        elif before != after:
            _issue(issues, "FAIL", f"TARGET_CHANGED:{planned.get('probe_id')}")
    scratch_snapshot = exit_receipt.get("s1_scratch_snapshot") or {}
    scratch_plan = next((row for row in plan.get("probes", []) if row.get("operation") == "SCRATCH_WRITE_READBACK"), {})
    if scratch_snapshot.get("sha256") != hashlib.sha256(str(scratch_plan.get("write_payload", "")).encode()).hexdigest():
        _issue(issues, "MISSING", "TRUSTED_SCRATCH_POST_SNAPSHOT_MISMATCH")

    helper_binding = helper.get("binding") or {}
    helper_ready = helper.get("ready") or {}
    helper_exit = helper.get("exit_receipt") or {}
    for record_name, record in (("HELPER_BINDING", helper_binding), ("HELPER_EXIT", helper_exit)):
        if record.get("_receipt_record_type") != "TRUSTED_PARENT_RECEIPT" or record.get("_receipt_channel") != "PARENT_ONLY_STDERR_V1":
            _issue(issues, "FAIL", f"{record_name}_PROVENANCE_INVALID")
    for field, wanted in {"binding_source":"TRUSTED_DIRECT_FORK_PARENT","wait_source":"POSIX_WAITPID_CHILD","receipt_channel":"PARENT_ONLY_STDERR_V1","helper_sha256":expected.get("helper_sha256")}.items():
        if helper_binding.get(field) != wanted:
            _issue(issues, "FAIL", f"HELPER_BINDING_MISMATCH:{field}")
    for field in ("instance_id", "receipt_nonce", "helper_pid", "helper_start_ticks", "network_namespace", "mount_namespace", "helper_sha256"):
        wanted = expected.get("helper_instance_id") if field == "instance_id" else expected.get("helper_receipt_nonce") if field == "receipt_nonce" else helper_binding.get(field)
        if helper_exit.get(field) != wanted or helper_binding.get(field) != wanted:
            _issue(issues, "FAIL", f"HELPER_EXIT_BINDING_MISMATCH:{field}")
    if helper_ready.get("pid") != helper_binding.get("helper_pid") or helper_ready.get("proc_start_ticks") != helper_binding.get("helper_start_ticks"):
        _issue(issues, "FAIL", "HELPER_READY_BINDING_MISMATCH")
    if helper_ready.get("network_namespace") == binding.get("network_namespace"):
        _issue(issues, "FAIL", "HELPER_AND_WORKER_NETWORK_NAMESPACE_NOT_SEPARATED")
    _controls_valid(helper_ready.get("pre_controls"), "PRE", issues)
    _controls_valid((helper.get("post_control") or {}).get("controls"), "POST", issues)
    if helper.get("cleanup_status") != "PROVEN" or helper_exit.get("return_code") != 0:
        _issue(issues, "MISSING", "HELPER_CLEANUP_NOT_PROVEN")
    if exit_event.get("cleanup_status") != "PROVEN" or exit_event.get("inner_exit_confirmed") is not True or exit_event.get("reader_threads_stopped") is not True:
        _issue(issues, "MISSING", "WORKER_CLEANUP_NOT_PROVEN")
    commands = [event.get("command") for event in events if event.get("kind") == "IPC_SENT"]
    if commands != ["PING", "S1_RUN", "STOP"]:
        _issue(issues, "FAIL", f"UNEXPECTED_WORKER_COMMANDS:{commands!r}")

    if any(issue["severity"] == "FAIL" for issue in issues):
        verdict = "FAIL"
    elif issues:
        verdict = "INCONCLUSIVE"
    else:
        verdict = "PASS_SCOPED_S1"
    return {
        "reviewer": "INDEPENDENT_R1_6H_S1_EVIDENCE_REVIEWER",
        "verdict": verdict,
        "issues": issues,
        "planned_probe_count": len(plan.get("probes", [])),
        "observed_probe_count": len(actual_rows),
        "allowed_controls_verified": allow_count,
        "denied_access_checks_verified": deny_count,
        "required_lifecycle_order": required,
        "actual_lifecycle_order": [_event_tag(event) for event in events],
        "claim_ceiling": "Exact task-local synthetic objects, operations, bytes, namespaces, and bounded observation window only.",
    }
