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
    def test_legacy_and_storyboard_handoffs_have_no_board_reference_tokens(self):
        for skill, end in (
            ("seedance-prompt-20", "### Model IDs"),
            ("seedream-storyboard", "## Render style"),
        ):
            content = (SKILLS / skill / "SKILL.md").read_text()
            heading = (
                "### Storyboard-to-video handoff"
                if skill == "seedance-prompt-20" else "### Seedance handoff"
            )
            handoff = content.split(heading, 1)[1].split(end, 1)[0].lower()
            with self.subTest(skill=skill):
                self.assertIn("translate", handoff)
                self.assertIn("planning-only", handoff)
                self.assertIn("first", handoff)
                self.assertIn("r2v", handoff)
                self.assertNotIn("@image 1: approved storyboard panel", handoff)
                self.assertNotIn("bind the grid", handoff)
                self.assertNotIn("promoted panel", handoff)

    def test_remaining_board_narrative_evals_cover_positive_edge_and_failure_cases(self):
        scenarios = {
            101: ("selected", "crop", "first-frame", "hash"),
            102: ("selected", "grid", "r2v", "hash"),
            103: ("board-derived regeneration", "cleanup", "text-free"),
            104: ("independently authored", "non-board", "production still"),
            105: ("independent animated blockout", "motion", "source lineage"),
            106: ("historical", "records"),
            107: ("no assets", "unknown", "no generation"),
            108: ("independent", "wrong", "rights", "unresolved"),
        }
        for skill in ("seedance-prompt-20", "seedream-storyboard"):
            data = json.loads((SKILLS / skill / "evals/evals.json").read_text())
            cases = {case["id"]: case for case in data["evals"]}
            self.assertEqual(len(cases), len(data["evals"]))
            for case_id, concepts in scenarios.items():
                with self.subTest(skill=skill, case=case_id):
                    self.assertIn(case_id, cases)
                    case = cases[case_id]
                    for concept in concepts:
                        self.assertIn(concept, case["prompt"].lower())
                    self.assertEqual(case["files"], [])
                    self.assertTrue(case["expected_output"].strip())
                    self.assertGreaterEqual(len(case["expectations"]), 3)
                    expectations = " ".join(case["expectations"]).lower()
                    self.assertIn("no", expectations)
                    self.assertIn("planning-only", expectations)

    def test_studio_02_board_guidance_routes_to_text_not_uploaded_planning_assets(self):
        parameter = (SKILLS / "seedance-prompt-25/references/parameter-reference.md").read_text()
        handoff = parameter.split("### Storyboard-to-video handoff", 1)[1].split(
            "## Native draft first", 1
        )[0].lower()
        self.assertIn("planning-only", handoff)
        self.assertIn("independently authored", handoff)
        self.assertIn("first-frame", handoff)
        self.assertIn("r2v", handoff)
        self.assertNotIn("promoted panel", handoff)
        self.assertNotIn("@image 1: approved storyboard panel", handoff)
        reference = (SKILLS / "seedance-prompt-25/references/keyframes-storyboards-blockouts.md").read_text()
        board = reference.split("### Storyboard grids", 1)[1].split(
            "### Blockout references", 1
        )[0].lower()
        self.assertIn("translate", board)
        self.assertNotIn("@image", board)
        self.assertIn("historical", board)
        self.assertIn("@Video 1 is a coarse blockout reference", reference)

    def test_studio_02_board_evals_include_selected_crop_grid_independent_still_and_history(self):
        data = json.loads((SKILLS / "seedance-prompt-25/evals/evals.json").read_text())
        cases = {case["id"]: case for case in data["evals"]}
        scenarios = {
            306: ("selected", "crop", "first-frame", "hash"),
            307: ("selected", "grid", "r2v", "hash"),
            308: ("independently authored", "production still", "first-frame"),
            309: ("historical", "panel", "records"),
        }
        for case_id, concepts in scenarios.items():
            with self.subTest(case=case_id):
                self.assertIn(case_id, cases)
                case = cases[case_id]
                for concept in concepts:
                    self.assertIn(concept, case["prompt"].lower())
                self.assertEqual(case["files"], [])
                self.assertTrue(case["expected_output"].strip())
                self.assertGreaterEqual(len(case["expectations"]), 3)
        self.assertEqual(len(data["evals"]), len(cases))

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
