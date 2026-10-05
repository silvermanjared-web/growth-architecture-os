from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "docs/executive-portfolio-index.md",
    "docs/proof-ledger.md",
    "docs/capability-catalog.md",
    "docs/federation-status.md",
    "docs/private-scale-public-proof.md",
    "scenarios/README.md",
    "architecture-decisions/README.md",
    "assets/jared-growth-systems-architecture.svg",
    "assets/portfolio-status-strip.svg",
    "data/capability-catalog.json",
    "RELEASE.md",
]

missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    raise SystemExit(f"missing portfolio proof artifacts: {missing}")

catalog = json.loads((ROOT / "data/capability-catalog.json").read_text())
members = catalog.get("members", [])
if len(members) != 6:
    raise SystemExit(f"expected 6 federation members, found {len(members)}")

names = {member["member"] for member in members}
if len(names) != len(members):
    raise SystemExit("duplicate federation member")

for member in members:
    if not member.get("capabilities"):
        raise SystemExit(f"member has no capabilities: {member['member']}")

print("portfolio proof layer validation passed")
