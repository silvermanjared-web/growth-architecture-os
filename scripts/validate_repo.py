#!/usr/bin/env python3
"""Repository validation guardrail.

Checks for common secret patterns, tracked credential-like files, required
repository documentation, the public claim-governance contract, and local
working-tree state.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CLAIMS_DIR = ROOT / "00-positioning" / "claims"
SECRET_PATTERNS = [
    re.compile(r"GOCSPX-[A-Za-z0-9_-]+"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"BEGIN (RSA|OPENSSH|PRIVATE) KEY"),
]
SENSITIVE_NAME = re.compile(
    r"(^|/)(\.env(\..*)?|\.env\.keys|client_secret.*\.json|credentials.*\.json|token.*\.json|tokens.*\.json|google[-_]ads\.ya?ml)$",
    re.IGNORECASE,
)
ALLOW_TRACKED = {
    ".envrc",
    ".env.example",
}
SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
TEXT_SUFFIXES = {".py", ".md", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".toml", ".sh", ".css", ".js", ".ts", ".html"}
ALLOWED_CAUSAL_STATES = {"directly_supported", "associated_after_change", "scope_only", "contextual"}
ALLOWED_SG_TIERS = {"SG0", "SG1", "SG2", "SG3"}
REQUIRED_CLAIM_FIELDS = {
    "id",
    "company",
    "competencies",
    "canonical_public_wording",
    "metric",
    "funnel_level",
    "causal_state",
    "confidence",
    "source_refs",
    "prohibited_inference",
}
REQUIRED_ROUTE_FIELDS = {
    "route_id",
    "tier",
    "primary_claim_ids",
    "supporting_claim_ids",
    "closure_axes",
    "decision_rule",
}


def git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=False)


def tracked_files() -> list[str]:
    result = git(["ls-files"])
    return [line for line in result.stdout.splitlines() if line.strip()]


def is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"Makefile", "README", "CLAUDE.md", ".envrc"}


def load_json(path: Path, failures: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - diagnostic detail matters more than branch coverage here.
        failures.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return None


def validate_claim_system(failures: list[str]) -> None:
    required_paths = {
        "claim registry": CLAIMS_DIR / "claims-registry.json",
        "semantic routes": CLAIMS_DIR / "semantic-routes.jsonl",
        "intent aliases": CLAIMS_DIR / "intent-aliases.json",
        "semantic governance": CLAIMS_DIR / "semantic-governance.md",
        "claims README": CLAIMS_DIR / "README.md",
        "human proof-point entry": ROOT / "00-positioning" / "proof-points.md",
    }
    for label, path in required_paths.items():
        if not path.exists():
            failures.append(f"Missing {label}: {path.relative_to(ROOT)}")
    if any(not path.exists() for path in required_paths.values()):
        return

    registry = load_json(required_paths["claim registry"], failures)
    aliases = load_json(required_paths["intent aliases"], failures)
    if registry is None or aliases is None:
        return

    if registry.get("schema_version") != "growth-architecture.claim-registry/v1":
        failures.append("Claim registry schema_version must be growth-architecture.claim-registry/v1")

    resume_sha = registry.get("canonical_resume_binding", {}).get("sha256", "")
    if not re.fullmatch(r"[a-f0-9]{64}", str(resume_sha)):
        failures.append("Claim registry canonical resume binding must include a 64-character lowercase sha256")

    claims = registry.get("claims")
    if not isinstance(claims, list) or not claims:
        failures.append("Claim registry must contain a non-empty claims array")
        return

    claim_ids: set[str] = set()
    for claim in claims:
        if not isinstance(claim, dict):
            failures.append("Every claim must be an object")
            continue
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            failures.append("Every claim must have a non-empty string id")
            continue
        if claim_id in claim_ids:
            failures.append(f"Duplicate claim id: {claim_id}")
        claim_ids.add(claim_id)

        missing = REQUIRED_CLAIM_FIELDS - set(claim)
        if missing:
            failures.append(f"Claim {claim_id} missing required fields: {', '.join(sorted(missing))}")
        if claim.get("causal_state") not in ALLOWED_CAUSAL_STATES:
            failures.append(f"Claim {claim_id} has unsupported causal_state: {claim.get('causal_state')}")
        if not isinstance(claim.get("competencies"), list) or not all(isinstance(v, str) and v for v in claim.get("competencies", [])):
            failures.append(f"Claim {claim_id} competencies must be a non-empty list of strings")
        if not isinstance(claim.get("canonical_public_wording"), str) or not claim.get("canonical_public_wording", "").strip():
            failures.append(f"Claim {claim_id} needs canonical_public_wording")
        if not isinstance(claim.get("source_refs"), list) or not claim.get("source_refs"):
            failures.append(f"Claim {claim_id} needs source_refs")
        if not isinstance(claim.get("prohibited_inference"), list) or not claim.get("prohibited_inference"):
            failures.append(f"Claim {claim_id} needs prohibited_inference controls")

    route_ids: set[str] = set()
    routes_path = required_paths["semantic routes"]
    for line_no, raw in enumerate(routes_path.read_text().splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            route = json.loads(raw)
        except json.JSONDecodeError as exc:
            failures.append(f"Invalid JSONL route at semantic-routes.jsonl:{line_no}: {exc}")
            continue
        if not isinstance(route, dict):
            failures.append(f"Route at line {line_no} must be an object")
            continue
        missing = REQUIRED_ROUTE_FIELDS - set(route)
        route_id = route.get("route_id", f"line-{line_no}")
        if missing:
            failures.append(f"Route {route_id} missing required fields: {', '.join(sorted(missing))}")
        if not isinstance(route_id, str) or not route_id:
            failures.append(f"Route at line {line_no} has invalid route_id")
        elif route_id in route_ids:
            failures.append(f"Duplicate route_id: {route_id}")
        else:
            route_ids.add(route_id)
        if route.get("tier") not in ALLOWED_SG_TIERS:
            failures.append(f"Route {route_id} has unsupported tier: {route.get('tier')}")
        for key in ("primary_claim_ids", "supporting_claim_ids"):
            values = route.get(key)
            if not isinstance(values, list) or (key == "primary_claim_ids" and not values):
                failures.append(f"Route {route_id} {key} must be a list; primary_claim_ids cannot be empty")
                continue
            for claim_id in values:
                if claim_id not in claim_ids:
                    failures.append(f"Route {route_id} references unknown claim id: {claim_id}")
        if not isinstance(route.get("closure_axes"), list) or not route.get("closure_axes"):
            failures.append(f"Route {route_id} needs closure_axes")
        if not isinstance(route.get("decision_rule"), str) or not route.get("decision_rule", "").strip():
            failures.append(f"Route {route_id} needs decision_rule")

    if not isinstance(aliases, dict):
        failures.append("intent-aliases.json must be an object mapping route_id to aliases")
    else:
        for route_id, alias_list in aliases.items():
            if route_id not in route_ids:
                failures.append(f"Intent aliases reference unknown route_id: {route_id}")
            if not isinstance(alias_list, list) or not alias_list:
                failures.append(f"Intent aliases for {route_id} must be a non-empty list")
            elif not all(isinstance(alias, str) and alias.strip() for alias in alias_list):
                failures.append(f"Intent aliases for {route_id} must all be non-empty strings")


def main() -> int:
    failures: list[str] = []
    tracked = tracked_files()

    if not (ROOT / "README.md").exists():
        failures.append("Missing README.md")

    for rel in tracked:
        base = Path(rel).name
        if SENSITIVE_NAME.search(rel) and base not in ALLOW_TRACKED:
            normalized = rel.replace("\\", "/")
            if not (
                normalized.startswith("design-tokens/")
                or normalized.startswith("design-system/")
                or normalized.startswith("examples/example-token")
                or "token-output" in normalized
            ):
                failures.append(f"Tracked sensitive-looking file: {rel}")

    for rel in tracked:
        path = ROOT / rel
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.exists() or not path.is_file() or not is_text_candidate(path):
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                failures.append(f"Secret-like pattern in {rel}: {pattern.pattern}")
                break

    validate_claim_system(failures)

    status = git(["status", "--short"]).stdout.strip()
    if status:
        failures.append("Working tree is not clean")

    if failures:
        print("VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
