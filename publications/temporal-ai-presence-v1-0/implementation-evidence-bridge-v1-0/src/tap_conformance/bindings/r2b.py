"""R2B static discovery and binding closure without importing the Ester runtime."""

from __future__ import annotations

import ast
import hashlib
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from .ester import discover_agent_surfaces, discover_cloud_call_sites


BACKGROUND_CALLS = {
    "asyncio.create_task": "ASYNC_TASK",
    "asyncio.ensure_future": "ASYNC_TASK",
    "threading.Thread": "THREAD",
    "Thread": "THREAD",
    "threading.Timer": "TIMER",
    "Timer": "TIMER",
}
SCHEDULER_TAILS = {"add_job", "add_task", "register_job", "schedule_job"}
BACKGROUND_CLASSES = {
    "BOUND",
    "DISABLED_BY_DEFAULT",
    "TEST_ONLY",
    "LEGACY_INACTIVE",
    "DEPLOYMENT_EXTERNAL",
    "OUT_OF_SCOPE_WITH_REASON",
    "UNRESOLVED",
}
T06_ROUTE_CLASSES = {
    "CLOUD_AI_ORACLE",
    "LOCAL_LOOPBACK_MODEL",
    "LOCAL_SERVICE",
    "NON_AI_EXTERNAL_NETWORK",
    "UPDATE_OR_METADATA",
    "TEST_ONLY",
    "LEGACY_INACTIVE",
    "UNREACHABLE",
    "OTHER_EXPLICIT",
}
T07_CLASSES = {
    "INVENTORIED",
    "DISABLED_BY_DEFAULT",
    "TEST_ONLY",
    "LEGACY_INACTIVE",
    "OUT_OF_SCOPE_WITH_REASON",
    "HIDDEN",
    "UNRESOLVED",
}

_BOUND_BACKGROUND_MODULES = {
    "modules/dreams/dream_engine.py": "dream-candidate-preparation",
    "modules/garage/agent_supervisor.py": "agent-supervisor-tick",
    "modules/volition/pulse.py": "volition-pulse",
}
_LEGACY_CLOUD_MODULES = {
    "modules/providers/openai_adapter.py",
    "modules/providers/gemini_adapter.py",
    "modules/providers/xai_adapter.py",
}
_CLOUD_AI_MARKERS = (
    "api.openai.com",
    "generativelanguage.googleapis.com",
    "api.x.ai",
    "chat/completions",
    "generatecontent",
)
_NON_AI_PATH_MARKERS = (
    "/adapters/telegram_",
    "/channels/telegram_",
    "/market/",
    "/media/",
    "/messenger_",
    "/opps/",
    "/search/",
    "/social/",
    "/sos/",
    "/web_search.py",
    "google_cse",
    "webhook",
)
_UPDATE_PATH_MARKERS = (
    "/diagnostics/",
    "/ester/selfmod_",
    "/survival/",
    "/video/metadata/",
)
_LOCAL_SERVICE_MODULES = {
    "modules/kg/autolink.py",
    "modules/kg/linker.py",
    "modules/llm/selector.py",
    "modules/mem/affect_priority.py",
    "modules/ops/cost_fence.py",
    "modules/policy/cautious_ethos.py",
    "modules/self/autonomy.py",
    "modules/self/papa_locator.py",
    "modules/sister_autochat.py",
    "modules/sisters/registry.py",
    "modules/synaps/codex_coordination_cycle.py",
    "modules/thinking/action_registry.py",
}
_NON_AI_EXTERNAL_MODULES = {
    "modules/garage/jobs.py",
    "modules/garage/pipeline.py",
    "modules/html_extract.py",
    "modules/judge/adapters.py",
    "modules/net_bridge.py",
    "modules/proactive/video_autorunner.py",
}


def _dotted_name(node: ast.AST) -> str:
    parts: list[str] = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def _source_files(repo_root: Path) -> list[Path]:
    root = Path(repo_root).resolve()
    excluded = {".git", ".venv", "venv", "__pycache__", "node_modules"}
    return sorted(
        path
        for path in root.rglob("*.py")
        if not any(part in excluded for part in path.relative_to(root).parts)
    )


def _parse(path: Path) -> tuple[ast.Module, str] | None:
    try:
        source = path.read_text(encoding="utf-8-sig")
        return ast.parse(source, filename=str(path)), source
    except (SyntaxError, UnicodeDecodeError, OSError):
        return None


def _enclosing_symbol(tree: ast.AST, target: ast.AST) -> str:
    line = int(getattr(target, "lineno", 0) or 0)
    best = "<module>"
    span = 10**9
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        start = int(getattr(node, "lineno", 0) or 0)
        end = int(getattr(node, "end_lineno", start) or start)
        if start <= line <= end and end - start < span:
            best = node.name
            span = end - start
    return best


def _source_line(source: str, node: ast.AST) -> str:
    lines = source.splitlines()
    line = int(getattr(node, "lineno", 0) or 0)
    if not line or line > len(lines):
        return ""
    return lines[line - 1].strip()


def _has_sleep(loop: ast.While) -> bool:
    for node in ast.walk(loop):
        if not isinstance(node, ast.Call):
            continue
        name = _dotted_name(node.func)
        if name.endswith("sleep") or name.endswith("wait") or name.endswith("join"):
            return True
    return False


def _thread_subclass(node: ast.ClassDef) -> bool:
    return any(_dotted_name(base).split(".")[-1] == "Thread" for base in node.bases)


def _background_nodes(tree: ast.Module) -> Iterable[tuple[ast.AST, str, str]]:
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _dotted_name(node.func)
            if name in BACKGROUND_CALLS:
                yield node, BACKGROUND_CALLS[name], name
            elif name.split(".")[-1] in SCHEDULER_TAILS:
                yield node, "SCHEDULED_JOB", name
        elif isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and node.test.value is True and _has_sleep(node):
                yield node, "POLL_LOOP", "while True with wait/sleep"
        elif isinstance(node, ast.ClassDef) and _thread_subclass(node):
            yield node, "THREAD_SUBCLASS", node.name
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for deco in node.decorator_list:
                if isinstance(deco, ast.Call) and _dotted_name(deco.func).endswith("on_event"):
                    if deco.args and isinstance(deco.args[0], ast.Constant) and deco.args[0].value == "startup":
                        yield node, "STARTUP_HOOK", node.name


def _is_main_guarded(source: str) -> bool:
    return 'if __name__ == "__main__"' in source or "if __name__ == '__main__'" in source


def _background_classification(rel: str, symbol: str, source: str) -> tuple[str, str]:
    rel_lower = rel.lower()
    if rel.startswith("tests/") or rel.startswith("test_"):
        return "TEST_ONLY", "surface is reachable only from a test module"
    if "legacy" in rel_lower or rel_lower.endswith(".py1.py"):
        return "LEGACY_INACTIVE", "preserved legacy source is not a current primary entry point"
    if rel in _BOUND_BACKGROUND_MODULES:
        return "BOUND", f"surface is declared as {_BOUND_BACKGROUND_MODULES[rel]} in the R2A TAP task declaration"
    if rel.startswith("tools/"):
        return "TEST_ONLY", "tool surface requires explicit command invocation and is not imported by the primary runtime"
    if rel.startswith(("scripts/", "windows/")) or _is_main_guarded(source):
        return "DEPLOYMENT_EXTERNAL", "standalone entry point requires an external process or service launcher"
    if rel.startswith(("listeners/", "cloud/")) or rel in {
        "ambient_proactive.py",
        "energy_logger.py",
        "ester_oneclick.py",
        "group_evening.py",
        "group_digest.py",
        "ingestion.py",
        "orchestrator.py",
        "processing_worker.py",
        "run_ester_fixed.py",
        "telegram_adapter.py",
    }:
        return "DEPLOYMENT_EXTERNAL", "activation depends on the selected deployment entry point or owner-launched process"
    if symbol != "<module>":
        return "DISABLED_BY_DEFAULT", "creation is nested in an explicit callable and no import-time activation occurs at this site"
    return "DEPLOYMENT_EXTERNAL", "module-level activation requires selection of this module by a deployment entry point"


def discover_background_surfaces(repo_root: Path) -> list[dict[str, Any]]:
    root = Path(repo_root).resolve()
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in _source_files(root):
        parsed = _parse(path)
        if parsed is None:
            continue
        tree, source = parsed
        rel = path.relative_to(root).as_posix()
        for node, surface_type, creation in _background_nodes(tree):
            symbol = _enclosing_symbol(tree, node)
            surface_id = f"background:{rel}:{getattr(node, 'lineno', 0)}:{surface_type}"
            if surface_id in seen:
                continue
            seen.add(surface_id)
            classification, reason = _background_classification(rel, symbol, source)
            owner = "external deployment controller" if classification == "DEPLOYMENT_EXTERNAL" else symbol
            pause = "external process control" if classification == "DEPLOYMENT_EXTERNAL" else "explicit callable/control gate"
            rows.append(
                {
                    "id": surface_id,
                    "source_path": rel,
                    "symbol": symbol,
                    "surface_type": surface_type,
                    "creation_route": creation,
                    "activation_route": f"{rel}:{symbol}",
                    "default_activation_state": "DEPLOYMENT_DEPENDENT" if classification == "DEPLOYMENT_EXTERNAL" else ("ENABLED_WHEN_DECLARED" if classification == "BOUND" else "INACTIVE_UNTIL_CALLED"),
                    "owner_or_controller": owner,
                    "frequency_or_trigger": _source_line(source, node),
                    "memory_classes_touched": ["DECLARATION_BOUND"] if classification == "BOUND" else [],
                    "tool_privileges": ["DECLARATION_BOUND"] if classification == "BOUND" else [],
                    "cloud_capability": "DECLARATION_BOUND" if classification == "BOUND" else "NOT_ESTABLISHED_BY_ACTIVATION_SITE",
                    "stop_route": pause,
                    "pause_route": pause,
                    "revoke_route": pause,
                    "witness_or_log_route": "TAP_BACKGROUND_TASKS.json" if classification == "BOUND" else "DEPLOYMENT_OR_MODULE_LOG",
                    "classification": classification,
                    "classification_reason": reason,
                    "evidence_refs": [f"{rel}:{getattr(node, 'lineno', 0)}"],
                }
            )
    return sorted(rows, key=lambda row: row["id"])


def validate_background_inventory(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    required = {
        "id", "source_path", "symbol", "surface_type", "creation_route", "activation_route",
        "default_activation_state", "owner_or_controller", "frequency_or_trigger", "memory_classes_touched",
        "tool_privileges", "cloud_capability", "stop_route", "pause_route", "revoke_route",
        "witness_or_log_route", "classification", "classification_reason", "evidence_refs",
    }
    for row in rows:
        if set(row) != required:
            errors.append("TAP-R2B-T03-INCOMPLETE-SURFACE")
        if row.get("id") in ids:
            errors.append("TAP-R2B-T03-DUPLICATE-SURFACE")
        ids.add(str(row.get("id")))
        if row.get("classification") not in BACKGROUND_CLASSES:
            errors.append("TAP-R2B-T03-INVALID-CLASSIFICATION")
        if row.get("classification") == "UNRESOLVED":
            errors.append("TAP-R2B-T03-UNRESOLVED-SURFACE")
    return errors


def _route_class(row: dict[str, Any], source: str) -> tuple[str, str, str]:
    rel = row["module"]
    rel_marked = f"/{rel.lower()}"
    lowered = source.lower()
    if rel == "modules/llm/providers_openai_oracle.py":
        return "CLOUD_AI_ORACLE", "BOUND", "fixed OpenAI oracle route is gated by approved request, oracle window, budget and deny logging"
    if rel in _LEGACY_CLOUD_MODULES:
        return "LEGACY_INACTIVE", "OUT_OF_SCOPE_WITH_REASON", "direct provider adapter has no production import; only debug-import custody references exist"
    if rel == "modules/llm/broker.py":
        return "OTHER_EXPLICIT", "BOUND", "shared broker transport applies net_guard and rejects direct cloud-AI hosts before urlopen"
    if rel in _LOCAL_SERVICE_MODULES:
        return "LOCAL_SERVICE", "OUT_OF_SCOPE_WITH_REASON", "site is an in-process, peer, local-daemon or repository service route with explicit caller activation"
    if rel in _NON_AI_EXTERNAL_MODULES:
        return "NON_AI_EXTERNAL_NETWORK", "OUT_OF_SCOPE_WITH_REASON", "site transports a URL fetch, evaluator, outreach, search or feed payload rather than AI identity/continuity state"
    if any(marker in rel_marked for marker in _UPDATE_PATH_MARKERS):
        return "UPDATE_OR_METADATA", "OUT_OF_SCOPE_WITH_REASON", "site transports update, diagnostic, metadata or custody material rather than an AI prompt/continuity state"
    if any(marker in rel_marked for marker in _NON_AI_PATH_MARKERS):
        return "NON_AI_EXTERNAL_NETWORK", "OUT_OF_SCOPE_WITH_REASON", "site is an explicitly named messaging, search, media, market or webhook transport rather than an AI oracle"
    if "127.0.0.1" in lowered or "localhost" in lowered:
        route = "LOCAL_LOOPBACK_MODEL" if any(token in rel_marked for token in ("/llm/", "lmstudio", "image_caption", "chat_api")) else "LOCAL_SERVICE"
        return route, "OUT_OF_SCOPE_WITH_REASON", "endpoint construction has a loopback default or explicit local-url guard; it is not a cloud oracle"
    symbol = str(row.get("function_class") or "").lower()
    local_context = "\n".join(line for line in source.splitlines() if symbol and symbol in line.lower())
    ai_semantics = any(marker in lowered for marker in _CLOUD_AI_MARKERS) and any(token in lowered for token in ("prompt", "messages", "model"))
    if ai_semantics:
        return "CLOUD_AI_ORACLE", "UNRESOLVED", "AI-model transport is not proven to pass through the approved oracle authority boundary"
    if rel.startswith("modules/thinking/actions_"):
        return "LOCAL_SERVICE", "OUT_OF_SCOPE_WITH_REASON", "action adapter calls a repository-local HTTP service route under the action registry authority surface"
    return "OTHER_EXPLICIT", "OUT_OF_SCOPE_WITH_REASON", f"static call in {row.get('function_class')} has no model/prompt ownership semantics; it remains inventoried as a non-oracle transport"


def discover_t06_call_sites(repo_root: Path) -> list[dict[str, Any]]:
    root = Path(repo_root).resolve()
    rows: list[dict[str, Any]] = []
    for base in discover_cloud_call_sites(root):
        if base["route"] in {"client.get", "client.post"}:
            # R2A's lexical matcher caught Flask test_client.get and dict.get;
            # neither is a network primitive. R2B records both as discovery removals.
            continue
        path = root / base["module"]
        parsed = _parse(path)
        source = parsed[1] if parsed else ""
        route_class, classification, reason = _route_class(base, source)
        is_oracle = route_class == "CLOUD_AI_ORACLE"
        bound_oracle = is_oracle and classification == "BOUND"
        rows.append(
            {
                "id": base["call_site_id"],
                "source_path": base["module"],
                "symbol": base["function_class"],
                "call_type": base["route"],
                "endpoint_construction": "module constants, request object, or caller-provided URL; see evidence_refs",
                "route_class": route_class,
                "activation_route": f"{base['module']}:{base['function_class']}",
                "caller_identity": "Ester module caller; exact runtime principal is caller-bound",
                "memory_classes_possible": ["T-M2", "T-M3", "T-M4", "T-M5"] if is_oracle else [],
                "tool_or_agent_context": "oracle-request caller" if is_oracle else "module/action caller",
                "authority_gate": "oracle_window+approved_request" if bound_oracle else ("modules.net_guard or explicit caller" if classification != "UNRESOLVED" else "UNRESOLVED"),
                "budget_route": "oracle_window.authorize_call" if bound_oracle else "caller or route-local budget",
                "retention_boundary": "provider policy plus prompt-digest log; plaintext logging opt-in" if bound_oracle else "no AI-oracle retention claim",
                "data_minimization_boundary": "bounded prompt and digest-first logging" if bound_oracle else "route payload is caller-scoped",
                "deny_route": "fail closed before network" if bound_oracle or base["module"] == "modules/llm/broker.py" else "network/route failure returned to caller",
                "failure_behavior": "no silent continuity or authority transfer",
                "logging_or_witness_route": "oracle_window.note_call" if bound_oracle else "module/action log where configured",
                "classification": classification,
                "classification_reason": reason,
                "evidence_refs": [f"{base['module']}:{base['call_site_id'].split(':')[-2]}"],
            }
        )
    return sorted(rows, key=lambda row: row["id"])


def discover_t06_route_authority_map(repo_root: Path) -> list[dict[str, Any]]:
    root = Path(repo_root).resolve()
    broker = root / "modules/llm/broker.py"
    return [
        {
            "route_id": "tap-cloud-openai-oracle",
            "provider": "OpenAI",
            "status": "BOUND",
            "approval_path": "oracle_requests.validate_approved_request",
            "oracle_window_required": True,
            "memory_classes_possible": ["T-M2", "T-M3", "T-M4", "T-M5"],
            "data_minimization_rule": "bounded prompt; digest-first logging; plaintext opt-in only",
            "retention_policy": "provider policy; local receipt excludes plaintext by default",
            "budget_control_route": "oracle_window.authorize_call",
            "deny_path": "providers_openai_oracle._deny_and_note",
            "fail_closed": True,
            "logging_witness_route": "oracle_window.note_call",
            "caller_identity": "actor, agent_id, plan_id, step_index and request_id",
            "evidence_refs": ["modules/llm/providers_openai_oracle.py:133"],
        },
        {
            "route_id": "legacy-broker-openai-direct",
            "provider": "OpenAI",
            "status": "EXPLICITLY_DISABLED",
            "approval_path": "central oracle route required",
            "oracle_window_required": True,
            "memory_classes_possible": [],
            "data_minimization_rule": "no payload leaves through this route",
            "retention_policy": "not applicable; request denied before network",
            "budget_control_route": "not applicable; denied",
            "deny_path": "modules.llm.broker._http_json",
            "fail_closed": True,
            "logging_witness_route": "returned denial receipt",
            "caller_identity": "broker caller",
            "evidence_refs": [f"{broker.relative_to(root).as_posix()}:122"],
        },
        {
            "route_id": "legacy-broker-gemini-direct",
            "provider": "Google Gemini",
            "status": "EXPLICITLY_DISABLED",
            "approval_path": "no approved central route exists",
            "oracle_window_required": True,
            "memory_classes_possible": [],
            "data_minimization_rule": "no payload leaves through this route",
            "retention_policy": "not applicable; request denied before network",
            "budget_control_route": "not applicable; denied",
            "deny_path": "modules.llm.broker._http_json",
            "fail_closed": True,
            "logging_witness_route": "returned denial receipt",
            "caller_identity": "broker caller",
            "evidence_refs": [f"{broker.relative_to(root).as_posix()}:122"],
        },
    ]


def validate_t06_inventory(rows: list[dict[str, Any]], authority_map: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids = [row.get("id") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("TAP-R2B-T06-DUPLICATE-SITE")
    for row in rows:
        if row.get("route_class") not in T06_ROUTE_CLASSES:
            errors.append("TAP-R2B-T06-INVALID-ROUTE-CLASS")
        if row.get("classification") == "UNRESOLVED":
            errors.append("TAP-R2B-T06-UNRESOLVED-SITE")
    for route in authority_map:
        required = {
            "route_id", "provider", "status", "approval_path", "oracle_window_required",
            "memory_classes_possible", "data_minimization_rule", "retention_policy",
            "budget_control_route", "deny_path", "fail_closed", "logging_witness_route",
            "caller_identity", "evidence_refs",
        }
        if set(route) != required or not route.get("fail_closed"):
            errors.append("TAP-R2B-T06-INCOMPLETE-AUTHORITY-MAP")
    return errors


def discover_t07_agent_surfaces(repo_root: Path) -> list[dict[str, Any]]:
    root = Path(repo_root).resolve()
    rows: list[dict[str, Any]] = []
    disabled = {
        "modules/agents/desktop_agent.py": "explicit DesktopAgent construction; no module-level instance or startup hook",
        "modules/agents/game_mate_agent.py": "explicit GameMateAgent construction; no module-level instance or startup hook",
        "modules/agents/installer_agent.py": "explicit InstallerAgent construction; no module-level instance or startup hook",
        "modules/judge/evo_judge.py": "explicit EvoJudgeRunner construction by tooling; no default runtime registration",
    }
    for base in discover_agent_surfaces(root):
        rel = base["module"]
        classification = base["status"]
        reason = base["reason"]
        if rel in disabled:
            classification, reason = "DISABLED_BY_DEFAULT", disabled[rel]
        elif rel == "modules/synergy/models.py":
            classification = "OUT_OF_SCOPE_WITH_REASON"
            reason = "Pydantic Agent record is data only and exposes no execute/start lifecycle"
        elif "legacy" in rel:
            classification = "LEGACY_INACTIVE"
            reason = "preserved legacy runtime is not imported by the reconciled primary agent runtime"
        inventoried = classification == "INVENTORIED"
        rows.append(
            {
                "id": base["surface_id"],
                "source_path": rel,
                "symbol": base["symbol"],
                "role": "declared bounded executor" if inventoried else "static candidate or data surface",
                "creator": "explicit runtime factory/caller",
                "creation_route": f"{rel}:{base['symbol']}",
                "activation_trigger": "declared bounded invocation" if inventoried else "explicit construction only",
                "default_activation_state": "DECLARED" if inventoried else "INACTIVE",
                "lifecycle": "declared create/run/pause/revoke" if inventoried else "not active by default",
                "memory_access": ["DECLARATION_BOUND"] if inventoried else [],
                "tool_access": ["DECLARATION_BOUND"] if inventoried else [],
                "network_or_cloud_access": "DECLARATION_BOUND" if inventoried else "NONE_ESTABLISHED",
                "authority_source": "TAP_AGENT_INVENTORY and runtime gates" if inventoried else "none until explicit construction",
                "stop_route": "declared runtime control" if inventoried else "not active",
                "pause_route": "declared runtime control" if inventoried else "not active",
                "revoke_route": "declared runtime control" if inventoried else "not active",
                "inventory_visibility": "TAP_AGENT_INVENTORY.json" if inventoried else "R2B static surface inventory",
                "logging_or_witness_route": "declared runtime receipts" if inventoried else "not applicable while inactive",
                "classification": classification,
                "classification_reason": reason,
                "evidence_refs": [f"{rel}:{base['surface_id'].split(':')[-2]}"],
            }
        )
    return sorted(rows, key=lambda row: row["id"])


def validate_t07_inventory(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids = [row.get("id") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("TAP-R2B-T07-DUPLICATE-SURFACE")
    for row in rows:
        if row.get("classification") not in T07_CLASSES:
            errors.append("TAP-R2B-T07-INVALID-CLASSIFICATION")
        if row.get("classification") == "HIDDEN":
            errors.append("TAP-R2B-T07-HIDDEN-EXECUTOR")
        if row.get("classification") == "UNRESOLVED":
            errors.append("TAP-R2B-T07-UNRESOLVED-SURFACE")
    return errors


def inventory_summary(rows: list[dict[str, Any]], key: str = "classification") -> dict[str, int]:
    return dict(sorted(Counter(str(row.get(key) or "MISSING") for row in rows).items()))


def deterministic_inventory_id(rows: list[dict[str, Any]]) -> str:
    material = "\n".join(str(row.get("id")) for row in rows).encode("utf-8")
    return hashlib.sha256(material).hexdigest()
