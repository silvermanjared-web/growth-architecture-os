from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.reference_runtime import execute


class SecurityTests(unittest.TestCase):
    def test_path_traversal_is_rejected(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp) / "sandbox"
            with self.assertRaises(ValueError):
                execute(
                    "artifact.write",
                    root=root,
                    relative_path="../escape.txt",
                    content="no",
                    confirm=True,
                )

    def test_write_without_confirmation_does_not_touch_disk(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = execute(
                "artifact.write",
                root=root,
                relative_path="blocked.txt",
                content="no",
            )
            self.assertEqual(result["status"], "refused")
            self.assertFalse((root / "blocked.txt").exists())


if __name__ == "__main__":
    unittest.main()
