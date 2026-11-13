import json
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / ".agents/skills"


class SeedanceFamilyContractsTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

    def test_studio_02_adapter_and_review_never_promote_board_origin_to_conditioning(self):
        paths = (
            "seedance-prompt-25/SKILL.md",
            "seedance-prompt-25/references/parameter-reference.md",
            "seedance-prompt-25/references/keyframes-storyboards-blockouts.md",
            "prompt-review/references/review-checklists.md",
        )
        for path in paths:
            with self.subTest(path=path):
                text = self.text(path)
                for concept in ("grids", "panels", "crops", "animatics",
                                "planning-only", "independent", "production still",
                                "selection", "hash", "origin"):
                    self.assertIn(concept, text)
                for stale in ("submit only the promoted panel",
                              "submit the approved panel",
                              "eligible storyboard conditioning",
                              "optional monochrome conditioning",
                              "@image 1 is a planning sheet",
                              "intentional conditioning exception"):
                    self.assertNotIn(stale, text)

    def test_studio_03_full_take_preserves_separate_picture_and_sound_spans(self):
        text = self.text("seedance-motion-recast/references/audio-and-lipsync.md")
        for concept in ("picture", "sound", "independent", "fractional",
                        "offset", "audio tail", "full", "delivery", "unresolved",
                        "retain", "original", "explicit", "derivative"):
            self.assertIn(concept, text)
        self.assertNotIn("trim the saved audio to the exact span bound", text)
        self.assertIn("do not use `-shortest`", text)
        self.assertIn("do not pad", text)
        self.assertIn("matching excerpt", text)
        self.assertIn("exact authorized", text)
        self.assertIn("listening", text)
        self.assertIn("voice consent", text)

    def test_studio_03_audio_span_evals_cover_tails_equal_shorter_and_authorized_probe(self):
        data = json.loads((SKILLS / "seedance-motion-recast/evals/evals.json").read_text())
        cases = {case["id"]: case for case in data["evals"]}
        scenarios = {
            104: ("8.375", "9.000", "no probe"),
            105: ("8.375", "8.375", "equal"),
            106: ("9.000", "8.375", "no padding"),
            107: ("2.125", "4.500", "only"),
            108: ("full take", "probe", "not authorized"),
        }
        for case_id, concepts in scenarios.items():
            with self.subTest(case=case_id):
                self.assertIn(case_id, cases)
                case = cases[case_id]
                for concept in concepts:
                    self.assertIn(concept, case["prompt"].lower())
                expectations = " ".join(case["expectations"]).lower()
                self.assertIn("original", expectations)
                self.assertIn("no", expectations)
                self.assertTrue(case["expected_output"].strip())
                self.assertEqual(case["files"], [])
                self.assertGreaterEqual(len(case["expectations"]), 3)

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
