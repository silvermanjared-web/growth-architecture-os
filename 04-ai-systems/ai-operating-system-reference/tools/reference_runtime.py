from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
import uuid


CAPABILITIES = {
    "system.inspect": {
        "description": "Inspect the admitted sandbox root.",
        "effect": "read",
        "requires_confirmation": False,
    },
    "artifact.write": {
        "description": "Write a UTF-8 text artifact inside the admitted sandbox root.",
        "effect": "write",
        "requires_confirmation": True,
    },
}


@dataclass(frozen=True)
class Receipt:
    run_id: str
    capability: str
    effect: str
    status: str
    evidence: dict[str, Any]
    reason: str | None = None


def discover() -> dict[str, dict[str, Any]]:
    return {name: dict(spec) for name, spec in CAPABILITIES.items()}


def _resolve_under(root: Path, relative_path: str) -> Path:
    root = root.resolve()
    candidate = (root / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError("target escapes admitted sandbox")
    return candidate


def execute(
    capability: str,
    *,
    root: Path,
    confirm: bool = False,
    **kwargs: Any,
) -> dict[str, Any]:
    spec = CAPABILITIES.get(capability)
    if spec is None:
        return asdict(
            Receipt(
                run_id=str(uuid.uuid4()),
                capability=capability,
                effect="read",
                status="refused",
                evidence={},
                reason="unknown capability",
            )
        )

    if spec["requires_confirmation"] and not confirm:
        return asdict(
            Receipt(
                run_id=str(uuid.uuid4()),
                capability=capability,
                effect=spec["effect"],
                status="refused",
                evidence={},
                reason="explicit confirmation required",
            )
        )

    root = root.resolve()
    root.mkdir(parents=True, exist_ok=True)

    if capability == "system.inspect":
        entries = sorted(p.name for p in root.iterdir())
        receipt = Receipt(
            run_id=str(uuid.uuid4()),
            capability=capability,
            effect="read",
            status="observed",
            evidence={"root": str(root), "entries": entries},
        )
        return asdict(receipt)

    if capability == "artifact.write":
        target = _resolve_under(root, str(kwargs.get("relative_path", "")))
        content = str(kwargs.get("content", ""))
        if not target.name:
            raise ValueError("relative_path must name a file")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        receipt = Receipt(
            run_id=str(uuid.uuid4()),
            capability=capability,
            effect="write",
            status="executed",
            evidence={
                "relative_path": str(target.relative_to(root)),
                "bytes_written": len(content.encode("utf-8")),
            },
        )
        return asdict(receipt)

    raise AssertionError("declared capability missing implementation")
