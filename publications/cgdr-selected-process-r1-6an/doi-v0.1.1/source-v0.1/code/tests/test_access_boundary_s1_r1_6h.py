from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cgdr_r1_6b.s1_review import review_direct_wait_cleanup, review_s1_evidence
from cgdr_r1_6b.supervisor import StagedRuntime, WorkerProcess, _worker_command
from cgdr_r1_6b.worker import _s1_file_operation


def _receipt(payload: dict) -> dict:
    return {**payload, "_receipt_record_type": "TRUSTED_PARENT_RECEIPT", "_receipt_channel": "PARENT_ONLY_STDERR_V1"}


def valid_bundle() -> dict:
    plan_path = ROOT / "S1_ACCESS_PLAN.json"
    raw = plan_path.read_bytes()
    plan = json.loads(raw)
    plan_hash = hashlib.sha256(raw).hexdigest()
    manifest = json.loads((ROOT / "S1_FIXTURE_MANIFEST.json").read_text(encoding="utf-8"))
    instance = "worker-instance"
    helper_instance = "helper-instance"
    security_sha = "9" * 64
    binding = _receipt({
        "marker": "CGDR_CHILD_BOUND", "binding_source": "TRUSTED_DIRECT_FORK_PARENT", "wait_source": "POSIX_WAITPID_CHILD",
        "receipt_channel": "PARENT_ONLY_STDERR_V1", "instance_id": instance, "receipt_nonce": "worker-receipt",
        "worker_pid": 22, "worker_start_ticks": 2200, "waiter_pid": 11, "waiter_start_ticks": 1100,
        "pid_namespace": "pid:[2]", "network_namespace": "net:[2]", "mount_namespace": "mnt:[2]",
        "worker_sha256": "a" * 64, "launcher_sha256": "b" * 64,
        "worker_stderr_route": "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT", "trusted_receipt_route": "PARENT_ONLY_STDERR_V1",
    })
    security = _receipt({
        "marker": "CGDR_CHILD_SECURITY", "binding_source": "TRUSTED_DIRECT_FORK_PARENT_POST_EXEC_PROCFS",
        "receipt_channel": "PARENT_ONLY_STDERR_V1", "instance_id": instance, "receipt_nonce": "worker-receipt",
        "worker_pid": 22, "worker_start_ticks": 2200, "pid_namespace": "pid:[2]", "network_namespace": "net:[2]", "mount_namespace": "mnt:[2]",
        "worker_stderr_route": "DEDICATED_PIPE_WRAPPED_BY_TRUSTED_PARENT", "trusted_receipt_route": "PARENT_ONLY_STDERR_V1",
        "security_receipt_sha256": security_sha,
        "status": {"status_fields": {"Uid":"0 0 0 0","Gid":"0 0 0 0","Groups":"0","CapInh":"0000000000000000","CapPrm":"0000000000000000","CapEff":"0000000000000000","CapBnd":"0000000000000000","CapAmb":"0000000000000000","NoNewPrivs":"1"}, "fds":[{"fd":0},{"fd":1},{"fd":2}]},
        "mounts": [
            {"mount_point":plan["stage_dir"],"mount_options":["ro"],"filesystem":"ext4"},
            {"mount_point":plan["stage_dir"]+"/scratch","mount_options":["rw"],"filesystem":"tmpfs"},
            {"mount_point":plan["stage_dir"]+"/private","mount_options":["rw"],"filesystem":"tmpfs"},
            {"mount_point":plan["endpoint_binding"]["helper_dir"],"mount_options":["rw"],"filesystem":"tmpfs"},
        ],
    })
    security_sha = hashlib.sha256(json.dumps({key:value for key,value in security.items() if key not in {"security_receipt_sha256","_receipt_record_type","_receipt_channel"}},sort_keys=True,separators=(",",":")).encode()).hexdigest()
    security["security_receipt_sha256"] = security_sha
    rows = []
    for item in plan["probes"]:
        row = {key:item[key] for key in ("probe_id","object_id","operation","expectation","target")}
        row["syscall_attempted"] = True
        if item["expectation"] == "EXPECT_ALLOW":
            row["allowed"] = True
            row["observed_sha256"] = item.get("expected_sha256") or hashlib.sha256(item["write_payload"].encode()).hexdigest()
        else:
            row.update({"allowed":False,"errno":item["accepted_errno"][0],"error_class":"PermissionError"})
        rows.append(row)
    ready_security = {
        "open_fds":[0,1,2],
        "environment_keys":["CGDR_INSTANCE_ID","CGDR_PDEATHSIG_SET","CGDR_S1_ATTEMPT_ID","CGDR_S1_MODE","CGDR_S1_PLAN","CGDR_S1_PLAN_SHA256","LANG","LC_CTYPE","PATH","PYTHONHASHSEED"],
        "securebits":207,
        "status_fields":copy.deepcopy(security["status"]["status_fields"]),
    }
    exit_receipt = _receipt({
        **{key:binding[key] for key in ("instance_id","receipt_nonce","worker_pid","worker_start_ticks","waiter_pid","waiter_start_ticks","pid_namespace","network_namespace","mount_namespace","worker_sha256","launcher_sha256")},
        "marker":"CGDR_INNER_EXIT","binding_source":"TRUSTED_DIRECT_FORK_PARENT","wait_source":"POSIX_WAITPID_CHILD",
        "receipt_channel":"PARENT_ONLY_STDERR_V1","security_receipt_sha256":security_sha,"return_code":0,
        "s1_scratch_snapshot":{"exists":True,"regular_file":True,"sha256":hashlib.sha256(next(row["write_payload"] for row in plan["probes"] if row["operation"]=="SCRATCH_WRITE_READBACK").encode()).hexdigest()},
    })
    ping_nonce = "ping-nonce"
    ping_id = "ping-id"
    stop_id = "stop-id"
    events = [
        {"local_seq":1,"kind":"PROCESS_START_REQUESTED","instance_id":instance},
        {"local_seq":2,"kind":"PROCESS_HANDLE_OBTAINED","instance_id":instance},
        {"local_seq":3,"kind":"OS_CHILD_BOUND","instance_id":instance,"binding":binding},
        {"local_seq":4,"kind":"OS_CHILD_SECURITY_BOUND","instance_id":instance,"security":security},
        {"local_seq":5,"kind":"IPC_RECEIVED","instance_id":instance,"worker_event":{"event":"READY","instance_id":instance,"pid":22,"proc_start_ticks":2200,"pid_namespace":"pid:[2]","network_namespace":"net:[2]","mount_namespace":"mnt:[2]","s1_mode":True,"s1_plan_sha256":plan_hash,"security_metadata":ready_security}},
        {"local_seq":6,"kind":"IPC_SENT","instance_id":instance,"command":"PING","nonce":ping_nonce,"message_id":ping_id},
        {"local_seq":7,"kind":"IPC_RECEIVED","instance_id":instance,"worker_event":{"event":"PONG","instance_id":instance,"nonce":ping_nonce,"message_id":ping_id}},
        {"local_seq":8,"kind":"IPC_SENT","instance_id":instance,"command":"S1_RUN"},
        {"local_seq":9,"kind":"IPC_RECEIVED","instance_id":instance,"worker_event":{"event":"S1_PROBE_BATCH_RESULT","instance_id":instance,"attempt_id":plan["attempt_id"],"plan_sha256":plan_hash,"result":{"rows":rows,"stopped_after_forbidden_success":None,"planned_count":len(rows)}}},
        {"local_seq":10,"kind":"IPC_SENT","instance_id":instance,"command":"STOP","message_id":stop_id},
        {"local_seq":11,"kind":"IPC_RECEIVED","instance_id":instance,"worker_event":{"event":"STOP_ACK","instance_id":instance,"stop_id":stop_id}},
        {"local_seq":12,"kind":"EXIT_OBSERVED","instance_id":instance,"return_code":0,"inner_exit_receipt":exit_receipt,"inner_exit_confirmed":True,"reader_threads_stopped":True,"cleanup_status":"PROVEN"},
    ]
    snapshot = {"paths":{item["target"]:{"exists":True,"regular_file":True,"bytes":8,"mode":"0o400","sha256":"f"*64} for item in plan["probes"] if item["operation"] in {"FILE_READ","FILE_APPEND"}}}
    for fixture in manifest["files"]:
        relative=fixture["relative_path"]
        target=plan["stage_dir"]+"/"+relative if fixture["destination"]=="STAGE" else plan["endpoint_binding"]["helper_dir"]+"/"+relative.split("/",1)[1]
        snapshot["paths"][target]={"exists":True,"regular_file":True,"bytes":fixture["bytes"],"mode":"0o400","sha256":fixture["sha256"]}
    controls = lambda phase: {"phase":phase,"unix":{"matched_control":True,"response_bytes":14,"accepted":[{}]},"tcp":{"matched_control":True,"response_bytes":14,"accepted":[{}]}}
    helper_binding = _receipt({"marker":"CGDR_HELPER_BOUND","binding_source":"TRUSTED_DIRECT_FORK_PARENT","wait_source":"POSIX_WAITPID_CHILD","receipt_channel":"PARENT_ONLY_STDERR_V1","instance_id":helper_instance,"receipt_nonce":"helper-receipt","helper_pid":33,"helper_start_ticks":3300,"waiter_pid":31,"waiter_start_ticks":3100,"pid_namespace":"pid:[1]","network_namespace":"net:[1]","mount_namespace":"mnt:[1]","helper_sha256":"c"*64})
    helper_exit = _receipt({**{k:v for k,v in helper_binding.items() if not k.startswith("_")},"marker":"CGDR_HELPER_EXIT","return_code":0})
    expected = {"attempt_id":plan["attempt_id"],"plan_file_sha256":plan_hash,"fixture_manifest_sha256":hashlib.sha256((ROOT/"S1_FIXTURE_MANIFEST.json").read_bytes()).hexdigest(),"instance_id":instance,"receipt_nonce":"worker-receipt","worker_sha256":"a"*64,"launcher_sha256":"b"*64,"helper_instance_id":helper_instance,"helper_receipt_nonce":"helper-receipt","helper_sha256":"c"*64,"ping_nonce":ping_nonce,"ping_message_id":ping_id,"stop_id":stop_id}
    return {
        "plan":plan,"fixture_manifest":manifest,"fixture_manifest_file_sha256":expected["fixture_manifest_sha256"],"plan_file_sha256":plan_hash,
        "plan_canonical_sha256":hashlib.sha256(json.dumps(plan,sort_keys=True,separators=(",",":")).encode()).hexdigest(),
        "expected":expected,"events":events,"pre_snapshot":copy.deepcopy(snapshot),"post_snapshot":copy.deepcopy(snapshot),
        "helper":{"binding":helper_binding,"ready":{"event":"HELPER_READY","instance_id":helper_instance,"pid":33,"proc_start_ticks":3300,"network_namespace":"net:[1]","pre_controls":controls("PRE")},"post_control":{"controls":controls("POST")},"exit_receipt":helper_exit,"cleanup_status":"PROVEN"},
    }


class ReviewerTests(unittest.TestCase):
    def test_valid_scoped_evidence_passes(self) -> None:
        result = review_s1_evidence(valid_bundle())
        self.assertEqual(result["verdict"], "PASS_SCOPED_S1", result)
        self.assertEqual((result["allowed_controls_verified"], result["denied_access_checks_verified"]), (2, 14))

    def test_each_required_fault_reaches_its_reason(self) -> None:
        cases = {}
        missing = valid_bundle(); target = missing["plan"]["probes"][0]["target"]; missing["pre_snapshot"]["paths"].pop(target); cases["missing_fixture"]=(missing,"TARGET_SNAPSHOT_MISSING")
        endpoint = valid_bundle(); endpoint["helper"]["ready"]["pre_controls"]["tcp"]["matched_control"]=False; cases["dead_endpoint"]=(endpoint,"POSITIVE_CONTROL_FAILED")
        binding = valid_bundle(); binding["events"][8]["worker_event"]["result"]["rows"][0]["target"]="/wrong"; cases["target_binding"]=(binding,"PROBE_BINDING_MISMATCH")
        unknown = valid_bundle(); unknown["events"][8]["worker_event"]["result"]["rows"][2]["errno"]=999; cases["unknown_errno"]=(unknown,"DENIAL_ERRNO_UNBOUND")
        forbidden = valid_bundle(); forbidden["events"][8]["worker_event"]["result"]["rows"][2]["allowed"]=True; cases["forbidden_success"]=(forbidden,"FORBIDDEN_ACCESS_SUCCEEDED")
        blanket = valid_bundle(); blanket["events"][8]["worker_event"]["result"]["rows"][0].update({"allowed":False,"errno":13}); cases["blanket_deny"]=(blanket,"ALLOWED_CONTROL_DENIED")
        missing_wait = valid_bundle(); missing_wait["events"] = missing_wait["events"][:-1]; cases["missing_wait"]=(missing_wait,"MISSING_REQUIRED_EVENT:EXIT_OBSERVED")
        for name,(bundle,reason) in cases.items():
            with self.subTest(name=name):
                result=review_s1_evidence(bundle)
                self.assertNotEqual(result["verdict"],"PASS_SCOPED_S1",result)
                self.assertTrue(any(reason in row["reason"] for row in result["issues"]),result)

    def test_worker_marker_cannot_be_substituted_for_parent_receipt(self) -> None:
        bundle=valid_bundle()
        bundle["events"][2]["binding"].pop("_receipt_channel")
        result=review_s1_evidence(bundle)
        self.assertEqual(result["verdict"],"FAIL",result)
        self.assertTrue(any("BINDING_RECEIPT_PROVENANCE_INVALID" == row["reason"] for row in result["issues"]))


class CandidateTests(unittest.TestCase):
    def test_s1_direct_argv_contains_frozen_bindings_and_no_shell(self) -> None:
        plan=json.loads((ROOT/"S1_ACCESS_PLAN.json").read_text(encoding="utf-8"))
        rt=StagedRuntime(stage_dir=plan["stage_dir"],worker=plan["stage_dir"]+"/worker.py",worker_sha256="a"*64,launcher=plan["stage_dir"]+"/s0_launcher.py",launcher_sha256="b"*64,stage_receipt={},mode="S1",s1_plan=plan["stage_dir"]+"/S1_ACCESS_PLAN.json",s1_plan_sha256="c"*64,s1_fixture_manifest=plan["stage_dir"]+"/S1_FIXTURE_MANIFEST.json",s1_fixture_manifest_sha256="d"*64,s1_attempt_id=plan["attempt_id"],helper_dir=plan["endpoint_binding"]["helper_dir"],helper=plan["endpoint_binding"]["helper_dir"]+"/s1_endpoint_helper.py",helper_sha256="e"*64)
        command,_config=_worker_command("Ubuntu",rt,"literal-$(not-shell)","nonce;data")
        self.assertNotIn("sh",command); self.assertNotIn("-c",command); self.assertIn("--s1-mode",command); self.assertIn("nonce;data",command)

    def test_worker_security_receipt_rejects_nonzero_capabilities(self) -> None:
        bundle=valid_bundle(); plan=bundle["plan"]
        rt=StagedRuntime(stage_dir=plan["stage_dir"],worker=plan["stage_dir"]+"/worker.py",worker_sha256="a"*64,launcher=plan["stage_dir"]+"/s0_launcher.py",launcher_sha256="b"*64,stage_receipt={},mode="S1",s1_plan="p",s1_plan_sha256=bundle["plan_file_sha256"],s1_fixture_manifest="m",s1_fixture_manifest_sha256="d"*64,s1_attempt_id=plan["attempt_id"],helper_dir=plan["endpoint_binding"]["helper_dir"])
        worker=WorkerProcess("TEST",rt,Path(tempfile.gettempdir())/"not-written.jsonl","S1","TEST",receipt_nonce="worker-receipt")
        worker.instance_id="worker-instance"
        binding=bundle["events"][2]["binding"]
        security=bundle["events"][3]["security"]
        self.assertTrue(worker._valid_child_security(security,binding))
        changed=copy.deepcopy(security); changed["status"]["status_fields"]["CapEff"]="0000000000000001"
        self.assertFalse(worker._valid_child_security(changed,binding))

    def test_direct_wait_cleanup_is_independent_of_security_policy_acceptance(self) -> None:
        bundle=valid_bundle()
        binding=bundle["events"][2]["binding"]
        security=copy.deepcopy(bundle["events"][3]["security"])
        security["status"]["status_fields"]["CapEff"]="0000000000000001"
        exit_receipt=bundle["events"][-1]["inner_exit_receipt"]
        result=review_direct_wait_cleanup(binding,security,exit_receipt,0,True)
        self.assertEqual(result["status"],"PROVEN",result)

    def test_bounded_file_allow_operations_use_actual_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); source=root/"source.bin"; source.write_bytes(b"abc")
            read=_s1_file_operation({"operation":"FILE_READ","target":str(source)})
            self.assertTrue(read["allowed"]); self.assertEqual(read["observed_sha256"],hashlib.sha256(b"abc").hexdigest())
            scratch=root/"scratch.bin"; payload="bounded\n"
            write=_s1_file_operation({"operation":"SCRATCH_WRITE_READBACK","target":str(scratch),"write_payload":payload})
            self.assertTrue(write["allowed"]); self.assertEqual(write["observed_sha256"],hashlib.sha256(payload.encode()).hexdigest())


if __name__ == "__main__":
    unittest.main(verbosity=2)
