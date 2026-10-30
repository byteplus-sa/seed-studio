import json
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / ".agents" / "skills"
COMPILER = SKILLS / "seedance-prompt-25"
REVIEW = SKILLS / "prompt-review" / "references"


class CompilerCreativeFreedomTests(unittest.TestCase):
    def text(self, path):
        return " ".join(path.read_text(encoding="utf-8").lower().split())

    def review(self):
        split = REVIEW / "checklist-seedance-25.md"
        return split if split.exists() else REVIEW / "review-checklists.md"

    def test_motion_axes_are_selective_not_exhaustive(self):
        for path in [COMPILER / "references/scene-action.md", self.review()]:
            with self.subTest(path=path):
                text = self.text(path)
                self.assertNotRegex(text, r"full motion grammar|each moving element.*?takes states motion type|every moving element has motion grammar")
                self.assertIn("only the", text)
                self.assertIn("intended repetition", text)
                self.assertIn("stillness", text)

    def test_ordered_actions_do_not_require_single_event_stages(self):
        for path in [COMPILER / "SKILL.md", COMPILER / "references/scene-action.md",
                     COMPILER / "references/shot-staging.md", self.review()]:
            with self.subTest(path=path):
                text = self.text(path)
                self.assertNotRegex(text, r"one primary (?:state change|event or sustained state)|each stage is one (?:state change|event)")
                self.assertIn("ordered", text)

    def test_counts_preserve_hidden_subjects(self):
        for path in [COMPILER / "references/scene-action.md", self.review()]:
            with self.subTest(path=path):
                text = self.text(path)
                self.assertNotRegex(text, r"(?:put every counted item|is) in open view from the first frame")
                self.assertIn("visible count", text)
                self.assertIn("hidden", text)
                self.assertIn("contradict", text)

    def test_delegated_camera_paths_are_not_limited_by_move_count(self):
        for path in [COMPILER / "references/shot-staging.md", self.review()]:
            with self.subTest(path=path):
                text = self.text(path)
                self.assertNotIn("at most one secondary move", text)
                self.assertNotIn("use one or two clear camera movements", text)
                self.assertIn("requested or delegated choreography", text)
                self.assertIn("readable", text)
                self.assertIn("static", text)

    def test_audio_routes_follow_ownership(self):
        for path in [COMPILER / "references/audio-performance-camera.md", self.review(),
                     REVIEW / "author-self-check.md"]:
            with self.subTest(path=path):
                text = self.text(path)
                self.assertNotIn("ambient-only means no native audio", text)
                self.assertNotRegex(text, r"ambience-only, score-driven(?: or|,) speech-free")
                for concept in ["ownership", "wordless", "silence", "master", "unwanted"]:
                    self.assertIn(concept, text)

    def test_audio_keeps_capability_and_listening_guards(self):
        for path in [COMPILER / "references/audio-performance-camera.md", self.review()]:
            with self.subTest(path=path):
                text = self.text(path)
                for concept in ["supported", "rights", "listening", "promot", "unresolved"]:
                    self.assertIn(concept, text)

    def music_review(self):
        text = (REVIEW / "review-checklists.md").read_text(encoding="utf-8")
        section = text.split("## Seedance music video\n", 1)[1].split(
            "\n## UGC hooks and scripts", 1
        )[0]
        return " ".join(section.lower().split())

    def test_music_review_preserves_ordered_events_and_sustained_attention(self):
        text = self.music_review()
        self.assertNotIn("one event per section", text)
        self.assertNotIn("one primary visual assignment", text)
        for concept in ["ordered", "sustained", "readab", "locked"]:
            self.assertIn(concept, text)

    def test_music_review_uses_measured_timing_not_genre(self):
        text = self.music_review()
        self.assertNotIn("applies to rap, fast vocal delivery", text)
        for concept in ["measured", "audio", "provisional", "ordered cues",
                        "unavailable", "no paraphrasing", "no line skipped"]:
            self.assertIn(concept, text)

    def test_music_review_allows_optional_hybrid_treatment_summaries(self):
        text = self.music_review()
        for concept in ["brief-derived", "optional", "hybrid", "transitions",
                        "approved", "not compulsory locks"]:
            self.assertIn(concept, text)
        self.assertNotRegex(text, r"genre lock (?:required|present)|single recipe")

    def test_offline_behavior_fixtures_cover_positive_and_failure_cases(self):
        data = json.loads((COMPILER / "evals/creative-freedom.json").read_text())
        self.assertEqual(data["skill_name"], "seedance-prompt-25")
        cases = data["evals"]
        identifiers = {case["id"] for case in cases}
        self.assertEqual(len(identifiers), len(cases))
        self.assertEqual(identifiers, set(range(201, 211)))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"].strip())
                self.assertTrue(case["expected_output"].strip())
                self.assertEqual(case["files"], [])
                self.assertGreaterEqual(len(case["expectations"]), 3)


if __name__ == "__main__":
    unittest.main()
