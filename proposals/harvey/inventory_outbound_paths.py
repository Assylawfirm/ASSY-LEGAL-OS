"""Offline inventory of potentially outbound Python code paths; not a security verdict."""
import ast
import json
import pathlib
import sys

root = pathlib.Path(sys.argv[1]).resolve()
if not root.is_dir():
    raise SystemExit("Missing upstream source tree")
keywords = ("smtp", "email", "mail", "linkedin", "requests", "httpx", "urllib", "socket", "playwright", "browser", "send", "post", "oauth", "webhook")
findings = []
for path in sorted(root.rglob("*.py")):
    if any(part in {".venv", "venv", ".git", "node_modules", "tests"} for part in path.parts):
        continue
    try:
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
    except (UnicodeError, SyntaxError) as exc:
        findings.append({"path": str(path.relative_to(root)), "parse_error": str(exc)})
        continue
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or ""]
            for name in names:
                if any(k in name.lower() for k in keywords):
                    findings.append({"path": str(path.relative_to(root)), "line": node.lineno, "kind": "import", "symbol": name})
        elif isinstance(node, ast.Call):
            try:
                name = ast.unparse(node.func)
            except Exception:
                continue
            if any(k in name.lower() for k in keywords):
                findings.append({"path": str(path.relative_to(root)), "line": node.lineno, "kind": "call", "symbol": name})
print(json.dumps({"scanned_root": root.name, "potential_outbound_paths": findings, "count": len(findings)}, indent=2))
