#!/usr/bin/env python3
"""Score employer-facing public positioning against the Tier 1 hireability contract.

This is a deterministic release checklist, not a semantic judge. It makes the quality
model executable and flags common defensive leakage for human review.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

WEIGHTS = {
    "truth_evidence": 20,
    "role_alignment": 15,
    "intended_communication": 10,
    "jared_voice": 10,
    "truth_to_value": 15,
    "persuasion": 15,
    "specificity_proof": 10,
    "clarity_economy": 5,
}

DEFENSIVE_PATTERNS = [
    r"\bi do not overstate\b",
    r"\bi am not positioning myself as\b",
    r"\bdo not invent\b",
    r"\bwithout overstating causality\b",
    r"\bnot a claim that\b",
    r"\bfail closed\b",
]
VALUE_SIGNALS = [
    r"\bresult\b", r"\bimpact\b", r"\bvalue\b", r"\bscale\b", r"\blead\w*\b",
    r"\bdecision\w*\b", r"\binvestment\b", r"\bcapital\b", r"\bgrowth\b",
]
PROOF_SIGNALS = [r"\$\d", r"\d+%", r"\d+\+", r"\bcase stud", r"\bevidence\b"]


def heuristic_review(text: str) -> tuple[int, list[str]]:
    score = 100
    notes: list[str] = []
    lower = text.lower()

    defensive_hits = sum(len(re.findall(p, lower)) for p in DEFENSIVE_PATTERNS)
    if defensive_hits:
        penalty = min(20, defensive_hits * 4)
        score -= penalty
        notes.append(f"defensive/internal-governance leakage: {defensive_hits} hit(s), -{penalty}")

    value_hits = sum(bool(re.search(p, lower)) for p in VALUE_SIGNALS)
    if value_hits < 3:
        score -= 10
        notes.append("weak employer-value translation, -10")

    proof_hits = sum(bool(re.search(p, lower)) for p in PROOF_SIGNALS)
    if proof_hits < 2:
        score -= 10
        notes.append("limited specificity/proof signals, -10")

    if len(text.split()) > 2500:
        score -= 5
        notes.append("front-door artifact may be too long, -5")

    return max(0, score), notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()

    failed = False
    for raw in args.paths:
        path = Path(raw)
        text = path.read_text(encoding="utf-8")
        score, notes = heuristic_review(text)
        tier = "Tier 1" if score >= 80 else "REWRITE REQUIRED"
        print(f"{path}: {score}/100 — {tier}")
        for note in notes:
            print(f"  - {note}")
        if score < 80:
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
