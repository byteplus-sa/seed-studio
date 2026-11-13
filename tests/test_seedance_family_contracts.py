import json
import re
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / ".agents/skills"


class SeedanceFamilyContractsTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

    def factory_storyboard_delegate(self):
        entrypoint = (SKILLS / "template-factory/SKILL.md").read_text()
        link = re.search(
            r"Author storyboard prompts per \[storyboard-prompts\.md\]\(([^)]+)\)",
            entrypoint,
        )
        self.assertIsNotNone(link)
        delegate = SKILLS / "template-factory" / link.group(1)
        self.assertEqual(
            delegate, SKILLS / "template-factory/references/storyboard-prompts.md",
        )
        return " ".join(delegate.read_text().lower().split())

    def assert_factory_planning_handoff(self, text):
        board = r"(?:panel|storyboard|board|grid cell|thumbnail)"
        redraw = r"(?:re-?author|redraw|repaint|rebuild|regenerat\w*|fresh render)"
        anchor = (
            r"(?:video keyframe|first[- ]frame|last[- ]frame|"
            r"opening reference|closing anchor|r2v|motion reference)"
        )
        routes = (
            (
                rf"{board}[^.!?]*\b(?:must|should|can|may)\b[^.!?]*"
                rf"(?:become|serve|use|{redraw})[^.!?]*{anchor}"
            ),
            rf"{redraw}[^.!?]*{board}[^.!?]*\b(?:as|for|into)\b[^.!?]*{anchor}",
            (
                rf"\b(?:attach|bind|feed|upload|use)\b[^.!?]*{redraw}"
                rf"[^.!?]*\b(?:as|for|into)\b[^.!?]*{anchor}"
            ),
        )
        for route in routes:
            self.assertIsNone(re.search(route, text), "board-redraw conditioning route")
        for concept in (
            "planning-image authoring only", "regenerating from a panel prompt",
            "preserves planning origin", "planning-only", "animatics",
            "first/last-frame", "r2v", "motion", "translate", "text",
        ):
            self.assertIn(concept, text)

    def test_factory_loaded_delegate_matches_board_owner_and_video_slot_handoff(self):
        delegate = self.factory_storyboard_delegate()
        self.assert_factory_planning_handoff(delegate)
        for path in (
            "seedream-storyboard/SKILL.md",
            "template-factory/references/slot-mapping.md",
        ):
            with self.subTest(path=path):
                owner = self.text(path)
                for concept in ("planning-only", "panels", "grids", "crops",
                                "translate", "text", "production still"):
                    self.assertIn(concept, owner)
        self.assertIn(
            "regenerating a standalone from its panel prompt is not independence",
            self.text("seedream-storyboard/SKILL.md"),
        )

    def test_factory_handoff_rejects_alternate_redraw_routes_even_with_origin_fence(self):
        delegate = self.factory_storyboard_delegate()
        self.assert_factory_planning_handoff(delegate)
        for directive in (
            "Repaint the selected thumbnail without labels as the opening reference.",
            "Rebuild the grid cell in full color for a last-frame closing anchor.",
            "A cleaned board may serve as an R2V reference after selection.",
            "Regenerate the panel from its saved prompt as the motion reference.",
            "Attach the fresh render from the recorded beat as the first-frame image.",
        ):
            with (
                self.subTest(directive=directive),
                self.assertRaisesRegex(AssertionError, "board-redraw conditioning route"),
            ):
                self.assert_factory_planning_handoff(
                    f"{delegate} {directive.lower()}",
                )

    def test_factory_preserves_independent_stills_and_blockouts_with_existing_gates(self):
        delegate = self.factory_storyboard_delegate()
        self.assert_factory_planning_handoff(delegate)
        for text in (delegate, self.text("seedream-storyboard/SKILL.md")):
            for concept in (
                "independently authored", "selected", "text-free", "non-board",
                "production still", "independent animated blockout", "exact",
                "model", "operation", "transport", "role", "rights", "consent",
                "current canonical hashes", "source lineage", "artifact-specific qa",
                "motion and appearance", "preserve historical",
            ):
                self.assertIn(concept, text)

    def test_remaining_board_owners_reject_origin_laundering(self):
        for path in (
            "seedance-prompt-20/SKILL.md",
            "seedream-storyboard/SKILL.md",
            "seedream-storyboard/references/scene-density.md",
        ):
            with self.subTest(path=path):
                text = self.text(path)
                for concept in (
                    "grids", "panels", "crops", "animatics", "planning-only",
                    "crop", "cleanup", "approval", "selection", "hash",
                    "board-derived regeneration", "do not change planning origin",
                    "translate", "text", "historical",
                ):
                    self.assertIn(concept, text)
                for stale in (
                    "submit only the promoted panel",
                    "submit only the two promoted panels",
                    "submit the approved panel",
                    "promote only approved panels to video keyframes",
                    "a storyboard panel may later become a keyframe",
                    "bind the whole grid in a seedance prompt only when",
                    "when a board is bound to a seedance prompt",
                    "hand a board that conditions a seedance prompt",
                    "approved-panel and explicit supported-conditioning rules",
                ):
                    self.assertNotIn(stale, text)

    def test_remaining_board_owners_preserve_independent_eligible_inputs(self):
        for path in (
            "seedance-prompt-20/SKILL.md",
            "seedream-storyboard/SKILL.md",
            "seedream-storyboard/references/scene-density.md",
        ):
            with self.subTest(path=path):
                text = self.text(path)
                for concept in (
                    "independently authored", "text-free", "non-board",
                    "production still", "independent animated blockout",
                    "exact", "model", "operation", "transport", "role",
                    "rights", "source lineage", "qa",
                ):
                    self.assertIn(concept, text)
                self.assertIn("preserve historical", text)

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
