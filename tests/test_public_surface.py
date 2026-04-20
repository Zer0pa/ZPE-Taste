import unittest

from zpe_taste.reference import get_repo_root
from zpe_taste.verify import assert_readme_contract, scan_for_disallowed_paths


class PublicSurfaceTests(unittest.TestCase):
    def test_readme_contract(self) -> None:
        repo_root = get_repo_root()
        readme_text = (repo_root / "README.md").read_text(encoding="utf-8")

        assert_readme_contract(readme_text)

    def test_public_surface_is_clean(self) -> None:
        repo_root = get_repo_root()

        self.assertEqual(scan_for_disallowed_paths(repo_root), [])

    def test_proof_anchor_paths_exist(self) -> None:
        repo_root = get_repo_root()
        paths = [
            repo_root / "proofs" / "artifacts" / "taste_negative_reference.json",
            repo_root / "proofs" / "manifests" / "CURRENT_REFERENCE_PACKET.md",
            repo_root / "validation" / "results" / "reference_validation.json",
            repo_root / "PUBLICATION_BOUNDARY_REPORT.md",
        ]

        for path in paths:
            self.assertTrue(path.exists(), f"Missing path: {path.relative_to(repo_root)}")


if __name__ == "__main__":
    unittest.main()
