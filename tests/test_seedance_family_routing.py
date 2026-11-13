import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
CALLERS = (
    "seedance-camera-presets", "seedance-pacing-presets",
    "seedance-music-video", "seedance-motion-design",
    "seedance-shot-design", "seedance-lens-presets",
    "seedance-lighting-presets",
)


class SeedanceFamilyRoutingTests(unittest.TestCase):
    def test_generic_craft_callers_name_neutral_leaf(self):
        for skill in CALLERS:
            with self.subTest(skill=skill):
                text = (SKILLS / skill / "SKILL.md").read_text()
                self.assertIn("`seedance-prompt`", text)
                self.assertNotIn("never stack more than two", text)

    def test_legacy_adapters_have_explicit_not_generic_routing(self):
        for version in ("20", "25"):
            with self.subTest(version=version):
                text = (SKILLS / f"seedance-prompt-{version}/SKILL.md").read_text()
                self.assertIn("`seedance-prompt`", text)
                self.assertIn("explicit", text.lower())

    def test_review_resolves_model_before_language_without_automatic_repairs(self):
        text = (SKILLS / "prompt-review/SKILL.md").read_text().lower()
        self.assertIn("model and operation first", text)
        self.assertIn("findings-only by default", text)
        self.assertIn("repair requires separate explicit authorization", text)
        self.assertNotIn("seedance 2.5 + universal checklists", text)
        self.assertIn("disable-model-invocation: true", text)

    def test_routing_evals_cover_should_near_and_should_not(self):
        data = json.loads((SKILLS / "prompt-review/evals/evals.json").read_text())
        cases = [case for case in data["evals"] if "routing_class" in case]
        self.assertEqual({case["routing_class"] for case in cases},
                         {"should", "near", "should-not"})
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["expected_output"].strip())
                self.assertGreaterEqual(len(case["expectations"]), 3)
        prompts = " ".join(case["prompt"].lower() for case in cases)
        for scenario in ("2.0", "filipino", "unknown", "no prompt", "seedream"):
            self.assertIn(scenario, prompts)


if __name__ == "__main__":
    unittest.main()
