"""Guardrails for the Arch Privacy Policy page."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVACY = (ROOT / "privacy" / "index.html").read_text()
ALIAS = (ROOT / "arch" / "privacy" / "index.html").read_text()


class PrivacyPageTests(unittest.TestCase):
    def test_privacy_is_a_real_policy(self):
        self.assertIn("Privacy Policy", PRIVACY)
        self.assertIn("Effective Date", PRIVACY)
        self.assertIn("Last Updated", PRIVACY)
        self.assertNotIn("coming soon", PRIVACY.lower())

    def test_discloses_live_collection_surfaces(self):
        for needle in (
            "API key",
            "magic link",
            "Stripe",
            "api@tnvolman.com",
            "X-API-Key",
            "/v1/review",
            "arch_dash",
            "SendGrid",
        ):
            self.assertIn(needle, PRIVACY, f"missing {needle!r}")

    def test_no_cross_branding(self):
        lowered = PRIVACY.lower()
        for brand in ("journey digital", "journeydigital", "typewright", "freeborn"):
            self.assertNotIn(brand, lowered)

    def test_footer_privacy_does_not_404_itself(self):
        self.assertIn('href="/privacy"', PRIVACY)
        self.assertNotIn('href="/terms"', PRIVACY)

    def test_arch_privacy_alias_points_at_canonical(self):
        self.assertIn("/privacy", ALIAS)
        self.assertIn("canonical", ALIAS)


if __name__ == "__main__":
    unittest.main()
