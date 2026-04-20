import unittest

from zpe_taste.reference import load_manifest_text, load_reference_packet


class ReferencePacketTests(unittest.TestCase):
    def test_reference_packet_preserves_negative_scope(self) -> None:
        packet = load_reference_packet()

        self.assertEqual(packet["state_label"], "evidenced_negative")
        self.assertIn("not geometry-bearing", packet["public_statement"]["claim"])
        self.assertTrue(
            any(
                "biological taste coding is impossible" in item
                for item in packet["public_statement"]["non_claims"]
            )
        )

    def test_manifest_preserves_required_non_claim(self) -> None:
        manifest_text = load_manifest_text()

        self.assertIn(
            "does not claim that biological taste coding is impossible",
            manifest_text,
        )


if __name__ == "__main__":
    unittest.main()
