import json
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / ".agents/skills"


class SeedanceFamilyContractsTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

    def test_recast_preserves_fractional_source_and_audio_tail(self):
        for relative in ("seedance-motion-recast/SKILL.md",
                         "seedance-motion-recast/references/recast-grammar.md"):
            with self.subTest(relative=relative):
                text = self.text(relative)
                self.assertIn("fractional", text)
                self.assertIn("audio tail", text)
                self.assertNotIn("trim to whole seconds", text)
                self.assertNotIn("whole-second source length", text)

    def test_recast_probes_require_explicit_selection(self):
        text = self.text("seedance-motion-recast/SKILL.md")
        self.assertIn("probes are opt-in", text)
        self.assertNotIn("start them with their own 480p probe", text)
        self.assertNotIn("starts with its own 480p probe", text)
        self.assertIn("full-duration", text)

    def test_restoration_first_draft_is_not_final_resolution(self):
        text = self.text("seedance-restoration/SKILL.md")
        self.assertNotIn("`resolution` 1080p", text)
        self.assertIn("first-pass", text)
        self.assertIn("final delivery target", text)
        self.assertIn('`resolution: "480p"`', text)
        self.assertIn("`draft: true`", text)
        self.assertIn("draft_task_id", text)

    def test_restoration_does_not_accept_blanket_timing_drift(self):
        text = self.text("seedance-restoration/SKILL.md")
        self.assertIn("fractional", text)
        self.assertIn("measured", text)
        self.assertNotIn("trim to ≤29s", text)
        self.assertNotIn("±0.3s", text)

    def test_preservation_evals_cover_empty_denied_and_changed_inputs(self):
        for skill in ("seedance-motion-recast", "seedance-restoration"):
            with self.subTest(skill=skill):
                data = json.loads((SKILLS / skill / "evals/evals.json").read_text())
                cases = data["evals"]
                self.assertEqual(data["skill_name"], skill)
                self.assertEqual(len(cases), len({case["id"] for case in cases}))
                prompts = " ".join(case["prompt"].lower() for case in cases)
                for scenario in ("fractional", "no source", "no probe", "changed"):
                    self.assertIn(scenario, prompts)
                for case in cases:
                    self.assertTrue(case["expected_output"].strip())
                    self.assertEqual(case["files"], [])
                    self.assertGreaterEqual(len(case["expectations"]), 3)
                if skill == "seedance-motion-recast":
                    crowded = next(case for case in cases if case["id"] == 4)
                    self.assertNotIn("exceed the recommended",
                                     crowded["expected_output"].lower())
                    self.assertIn("evidence", crowded["expected_output"].lower())


if __name__ == "__main__":
    unittest.main()
