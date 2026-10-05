from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.reference_runtime import discover, execute


class ReferenceRuntimeTests(unittest.TestCase):
    def test_discovery_is_explicit(self):
        capabilities = discover()
        self.assertEqual(capabilities["system.inspect"]["effect"], "read")
        self.assertEqual(capabilities["artifact.write"]["effect"], "write")

    def test_write_requires_confirmation_and_returns_receipt(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            refused = execute(
                "artifact.write",
                root=root,
                relative_path="reports/today.md",
                content="hello",
            )
            self.assertEqual(refused["status"], "refused")
            result = execute(
                "artifact.write",
                root=root,
                relative_path="reports/today.md",
                content="hello",
                confirm=True,
            )
            self.assertEqual(result["status"], "executed")
            self.assertEqual(result["effect"], "write")
            self.assertTrue(result["run_id"])
            self.assertEqual((root / "reports/today.md").read_text(), "hello")

    def test_unknown_capability_refuses(self):
        with TemporaryDirectory() as tmp:
            result = execute("shell.run", root=Path(tmp), confirm=True)
            self.assertEqual(result["status"], "refused")


if __name__ == "__main__":
    unittest.main()
