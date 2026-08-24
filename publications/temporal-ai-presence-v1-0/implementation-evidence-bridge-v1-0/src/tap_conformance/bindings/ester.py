"""Static Ester discovery adapters; importing this module does not import Ester."""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any


NETWORK_CALL_NAMES = {
    "urlopen",
    "requests.get",
    "requests.post",
    "requests.put",
    "requests.delete",
    "requests.request",
    "httpx.get",
    "httpx.post",
    "client.get",
    "client.post",
    "provider.call",
}
AGENT_CLASS_SUFFIXES = ("Agent", "Runner", "Executor", "Supervisor", "Worker")
AGENT_FUNCTIONS = {"create_agent", "run_agent_once", "disable_agent", "pause_run", "resume_run"}


def _dotted_name(node: ast.AST) -> str:
    parts: list[str] = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def _source_files(repo_root: Path) -> list[Path]:
    roots = (repo_root / "modules", repo_root / "growth_engine")
    return sorted(path for root in roots for path in root.rglob("*.py") if "__pycache__" not in path.parts)


def discover_cloud_call_sites(repo_root: Path) -> list[dict[str, Any]]:
    root = Path(repo_root).resolve()
    rows: list[dict[str, Any]] = []
    for path in _source_files(root):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError):
            continue
        source = path.read_text(encoding="utf-8-sig")
        rel = path.relative_to(root).as_posix()
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = _dotted_name(node.func)
            tail = ".".join(name.split(".")[-2:])
            if name not in NETWORK_CALL_NAMES and tail not in NETWORK_CALL_NAMES and not name.endswith(".urlopen"):
                continue
            line = source.splitlines()[node.lineno - 1].strip() if node.lineno else ""
            site_id = f"cloud:{rel}:{node.lineno}:{name}"
            lowered = line.lower()
            if rel == "modules/llm/providers_openai_oracle.py":
                status, binding, reason = "BOUND", "tap-cloud-openai-oracle", "gated provider uses oracle request and window controls"
            elif "127.0.0.1" in lowered or "localhost" in lowered or "lmstudio" in rel.lower():
                status, binding, reason = "OUT_OF_SCOPE_WITH_REASON", None, "loopback/local-model transport is not a cloud oracle"
            else:
                status, binding, reason = "UNRESOLVED", None, "network-capable call site requires a later route-specific authority review"
            rows.append({
                "call_site_id": site_id,
                "module": rel,
                "function_class": _enclosing_symbol(tree, node),
                "route": name,
                "status": status,
                "binding": binding,
                "reason": reason,
                "memory_classes": [],
                "authority_surface": "UNRESOLVED" if status == "UNRESOLVED" else ("oracle_window+approved_request" if status == "BOUND" else "not-applicable"),
            })
    return sorted(rows, key=lambda row: row["call_site_id"])


def _enclosing_symbol(tree: ast.AST, target: ast.AST) -> str:
    best = "<module>"
    best_span = 10**9
    target_line = getattr(target, "lineno", 0)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        start = getattr(node, "lineno", 0)
        end = getattr(node, "end_lineno", start)
        if start <= target_line <= end and end - start < best_span:
            best = node.name
            best_span = end - start
    return best


def discover_agent_surfaces(repo_root: Path) -> list[dict[str, Any]]:
    root = Path(repo_root).resolve()
    rows: list[dict[str, Any]] = []
    bound_modules = {
        "modules/agents/runtime.py",
        "modules/garage/agent_factory.py",
        "modules/garage/agent_runner.py",
        "modules/garage/agent_supervisor.py",
        "modules/dreams/dream_engine.py",
    }
    for path in _source_files(root):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError):
            continue
        rel = path.relative_to(root).as_posix()
        for node in ast.walk(tree):
            is_class = isinstance(node, ast.ClassDef) and node.name.endswith(AGENT_CLASS_SUFFIXES)
            is_function = isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in AGENT_FUNCTIONS
            if not (is_class or is_function):
                continue
            surface_id = f"agent:{rel}:{node.lineno}:{node.name}"
            if rel in bound_modules:
                status, binding, reason = "INVENTORIED", "ester-primary-agent-controls", "primary runtime surface is represented in TAP_AGENT_INVENTORY.json"
            elif "legacy" in rel:
                status, binding, reason = "OUT_OF_SCOPE_WITH_REASON", None, "preserved legacy implementation is not the reconciled primary runtime"
            else:
                status, binding, reason = "UNRESOLVED", None, "executor-like surface requires later activation and lifecycle review"
            rows.append({
                "surface_id": surface_id,
                "module": rel,
                "symbol": node.name,
                "kind": "class" if is_class else "function",
                "status": status,
                "binding": binding,
                "reason": reason,
            })
    return sorted(rows, key=lambda row: row["surface_id"])


def discover_registered_action_ids(repo_root: Path) -> list[str]:
    path = Path(repo_root).resolve() / "modules" / "thinking" / "action_registry.py"
    tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
    actions: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or _dotted_name(node.func).split(".")[-1] != "register" or not node.args:
            continue
        first = node.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            actions.add(first.value)
    return sorted(actions)


def validate_binding_map(repo_root: Path, binding_map: dict[str, Any]) -> list[str]:
    root = Path(repo_root).resolve()
    errors: list[str] = []
    for row in binding_map.get("bindings", []):
        targets = [{"implementation_module": row.get("implementation_module"), "symbols": row.get("symbols", [])}]
        targets.extend(row.get("additional_bindings", []))
        for target in targets:
            module = root / str(target.get("implementation_module") or "")
            if not module.is_file():
                errors.append(f"{row.get('test_id')}: missing implementation module {module}")
                continue
            if module.suffix != ".py":
                continue
            try:
                tree = ast.parse(module.read_text(encoding="utf-8-sig"), filename=str(module))
            except SyntaxError as exc:
                errors.append(f"{row.get('test_id')}: cannot parse {module}: {exc}")
                continue
            symbols = {node.name for node in ast.walk(tree) if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))}
            for symbol in target.get("symbols", []):
                if symbol not in symbols:
                    errors.append(f"{row.get('test_id')}: missing symbol {symbol} in {module.relative_to(root)}")
    return errors
