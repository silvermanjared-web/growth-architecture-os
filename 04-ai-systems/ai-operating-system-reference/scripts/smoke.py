from pathlib import Path
from tempfile import TemporaryDirectory
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.reference_runtime import discover, execute


def main() -> int:
    capabilities = discover()
    assert "system.inspect" in capabilities
    assert "artifact.write" in capabilities
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        observed = execute("system.inspect", root=root)
        assert observed["status"] == "observed"
        refused = execute(
            "artifact.write",
            root=root,
            relative_path="proof.txt",
            content="bounded",
        )
        assert refused["status"] == "refused"
        written = execute(
            "artifact.write",
            root=root,
            relative_path="proof.txt",
            content="bounded",
            confirm=True,
        )
        assert written["status"] == "executed"
        assert (root / "proof.txt").read_text() == "bounded"
    print("AI operating system reference smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
