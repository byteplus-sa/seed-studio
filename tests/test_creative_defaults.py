import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"


class CreativeDefaultsTests(unittest.TestCase):
    def text(self, relative):
        return (ROOT / relative).read_text()

    def assert_no_rule(self, text, pattern):
        match = re.search(pattern, " ".join(text.lower().split()))
        self.assertIsNone(match, f"Conflicting rule: {match.group() if match else ''}")

    def test_compilers_and_review_do_not_soften_body_energy(self):
        paths = [
            "seedance-prompt-25/references/scene-action.md",
            "seedance-prompt-20/SKILL.md",
            "prompt-review/references/review-checklists.md",
        ]
        for relative in paths:
            with self.subTest(path=relative):
                text = (SKILLS / relative).read_text()
                self.assert_no_rule(
                    text, r"(?i)prefer(?:s)? slow, gentle, continuous motion"
                )
                self.assertIn("interruptions", text)
                self.assertIn("recovery", text)

    def test_burst_remedies_are_not_universal_caps(self):
        paths = [
            "seedance-acting-console/SKILL.md",
            "seedance-acting-console/references/restraint-and-shape.md",
            "prompt-review/references/review-checklists.md",
        ]
        for relative in paths:
            with self.subTest(path=relative):
                text = (SKILLS / relative).read_text()
                self.assert_no_rule(
                    text,
                    r"(?is)at most (?:one burst action|once per shot)|"
                    r"use at most one per shot|"
                    r"uses this pattern's single burst and holds",
                )
                self.assertIn("optional", text.lower())

    def test_stage_checks_allow_sustained_state_without_a_turn(self):
        for relative in [
            "seedance-prompt-25/SKILL.md",
            "seedance-prompt-25/references/scene-action.md",
            "prompt-review/references/review-checklists.md",
        ]:
            with self.subTest(path=relative):
                text = " ".join((SKILLS / relative).read_text().lower().split())
                self.assertTrue("sustained state" in text,
                                "Stage guidance must allow a sustained state")

    def test_dialogue_readability_does_not_ban_kinetic_energy(self):
        paths = [
            "seedance-shot-design/SKILL.md",
            "seedance-shot-design/references/coverage-patterns.md",
            "seedance-shot-design/references/worked-repairs.md",
            "seedance-prompt-25/references/shot-staging.md",
        ]
        forbidden = (
            r"only for shots without spoken lines|"
            r"keep their moves quiet|keep moves slow while a line|"
            r"keep them slow so lips|no large move is planned during a spoken line|"
            r"silhouette (?:is for|only on) shots without speech"
        )
        for relative in paths:
            with self.subTest(path=relative):
                text = (SKILLS / relative).read_text()
                self.assert_no_rule(text, forbidden)
                self.assertIn("readab", text.lower())

    def test_coverage_and_eval_expectations_have_no_unrequested_quotas(self):
        paths = list((SKILLS / "seedance-shot-design").rglob("*.md"))
        paths.append(SKILLS / "seedance-shot-design/evals/evals.json")
        forbidden = (
            r"adjacent shots (?:still )?differ in at least two|"
            r"at least one shot per scene is not plain eye level|"
            r"exactly one shot is flagged as the turn|"
            r"a hold with no preceding motion; it reads as inert|"
            r"does not run on clean singles alone"
        )
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assert_no_rule(path.read_text(), forbidden)

    def test_premise_and_sound_edit_handoff_are_inline(self):
        for relative in [
            "AGENTS.md",
            ".agents/contracts/performance-direction.md",
            ".agents/skills/brief-intake/SKILL.md",
        ]:
            with self.subTest(path=relative):
                text = self.text(relative).lower()
                for concept in [
                    "audience response", "attention", "ending",
                    "sound", "edit", "acceptance", "chat",
                ]:
                    self.assertIn(concept, text)
        intake = self.text(".agents/skills/brief-intake/SKILL.md").lower()
        self.assertIn("underspecified", intake)
        self.assertIn("unresolved", intake)

    def test_framing_does_not_require_invented_height_difference(self):
        text = self.text(".agents/skills/seedance-shot-design/references/framing.md")
        self.assertNotIn("stage the height difference", text)
        self.assertNotIn("the more a subject matters to the beat, the larger", text)
        self.assertIn("readable", text)

    def test_camera_framing_preserves_source_geometry_and_standalone_pov(self):
        text = self.text(".agents/skills/seedance-camera-presets/SKILL.md")
        self.assert_no_rule(
            text,
            r"use only when the two characters are at different heights|"
            r"cover it with a shot of the looker before it and the reaction after it",
        )
        for concept in ["source geometry", "standalone POV", "optional", "readab"]:
            self.assertIn(concept, text)

    def test_camera_and_pacing_move_counts_are_not_hard_caps(self):
        for skill in ["seedance-camera-presets", "seedance-pacing-presets"]:
            with self.subTest(skill=skill):
                text = self.text(f".agents/skills/{skill}/SKILL.md")
                self.assert_no_rule(
                    text,
                    r"at most (?:1-2|2) (?:per shot|moves per shot)|"
                    r"stack` is 2 or fewer|one-or-two-move limit|"
                    r"simultaneous moves to at most two|count it toward the move limit",
                )
                for concept in ["requested choreography", "optional", "readab"]:
                    self.assertIn(concept, text)

    def test_progressive_change_timing_is_source_led_not_mandatory_slowdown(self):
        text = self.text(".agents/skills/seedance-pacing-presets/SKILL.md")
        self.assert_no_rule(
            text,
            r"slow the movement so the crossing takes about 1\.5 s|"
            r"write the stages by timestamp and body part or region, about 0\.4 s apart",
        )
        for concept in ["source timing", "readability", "optional", "unverified"]:
            self.assertIn(concept, text)

    def test_camera_and_pacing_evals_do_not_reward_unrequested_repairs(self):
        cases = {
            "seedance-camera-presets": {2, 3, 4, 5, 6, 8, 10},
            "seedance-pacing-presets": {9},
        }
        for skill, identifiers in cases.items():
            data = json.loads(self.text(f".agents/skills/{skill}/evals/evals.json"))
            for case in data["evals"]:
                if case["id"] not in identifiers:
                    continue
                with self.subTest(skill=skill, identifier=case["id"]):
                    expectations = " ".join(
                        [case["expected_output"], *case["expectations"]]
                    )
                    self.assert_no_rule(
                        expectations,
                        r"at or below 2|at most (?:two moves|one secondary move)|"
                        r"with advice to cover the pov|"
                        r"should sit beside a shot of ana|"
                        r"with a slowed crossing of about 1\.5 s|"
                        r"is slowed so the crossing lasts about 1\.5 s",
                    )

    def test_sync_overlay_covers_camera_and_pacing_repairs(self):
        text = self.text(".agents/skills/sync-skills/SKILL.md")
        for concept in [
            "seedance-camera-presets", "seedance-pacing-presets",
            "standalone POV", "progressive-change",
        ]:
            self.assertIn(concept, text)

    def test_shot_references_do_not_restore_height_or_pov_requirements(self):
        for reference in ["framing.md", "coverage-patterns.md"]:
            with self.subTest(reference=reference):
                text = self.text(
                    f".agents/skills/seedance-shot-design/references/{reference}"
                )
                self.assert_no_rule(
                    text,
                    r"keep a pov shot adjacent to its looker and its reaction shot|"
                    r"over-the-hip shot between characters at the same height; "
                    r"use an over-the-shoulder instead|"
                    r"point-of-view shot with no looker beside it; the viewer cannot",
                )
                self.assertIn("standalone POV", text)

    def test_coverage_move_repairs_require_a_readability_failure(self):
        text = self.text(
            ".agents/skills/seedance-shot-design/references/coverage-patterns.md"
        )
        self.assert_no_rule(
            text, r"one primary move per shot and at most one secondary"
        )
        self.assertIn("requested choreography", text)
        self.assertIn("optional", text)

    def test_short_cut_guidance_is_provisional_not_a_provider_limit(self):
        for relative in [
            "seedance-pacing-presets/SKILL.md",
            "seedance-pacing-presets/references/assembly-cuts.md",
        ]:
            with self.subTest(path=relative):
                text = " ".join((SKILLS / relative).read_text().lower().split())
                self.assertNotIn("a shot under about 0.8 s is merged or dropped", text)
                self.assertIn("provisional", text)
                self.assertIn("not a provider limit", text)

    def test_manual_review_and_save_boundaries_survive(self):
        agents = self.text("AGENTS.md")
        self.assertIn("only when the user invokes `/prompt-review`", agents)
        self.assertIn("only when the user explicitly asks", agents)
        review = self.text(".agents/skills/prompt-review/SKILL.md")
        self.assertIn("disable-model-invocation: true", review)
        metadata = self.text(".agents/skills/prompt-review/agents/openai.yaml")
        self.assertIn("allow_implicit_invocation: false", metadata)
        for skill in SKILLS.iterdir():
            if skill.name in {"prompt-review", "sync-skills"}:
                continue
            for path in skill.rglob("SKILL.md"):
                with self.subTest(path=path):
                    self.assertNotIn("/prompt-review", path.read_text())

    def test_sync_preserves_local_forks_and_metadata(self):
        script = self.text(".agents/skills/sync-skills/scripts/sync.sh")
        allowlist = re.search(r'^ALLOWLIST="([^"]+)"', script, re.M).group(1).split()
        for protected in [
            "acting-direction", "seedance-acting-console",
            "seedance-fight-choreography", "scene-craft", "blocking-map",
            "seedance-shot-design", "template-factory", "seedance-music-video",
            "seed-audio-commercial", "filipino-micro-drama", "seedream-prop-asset",
            "seedream-storyboard", "seedream-character-sheet-cleanup",
            "seedance-motion-recast", "seedance-object-swap", "seedance-restyle",
            "seedance-frame-break", "seedance-graybox-world",
            "seedance-effects-studio", "seedream-handcrafted-3d",
            "seedream-woodblock-poster", "seedream-character-outfit",
            "seedance-ai-avatar",
        ]:
            self.assertNotIn(protected, allowlist)
        self.assertIn("--exclude='/agents'", script)

    def test_no_absent_evaluation_harness_is_required(self):
        text = self.text(
            ".agents/skills/prompt-review/references/creative-quality.md"
        )
        self.assertNotIn("evaluate_skill_quality.py", text)
        self.assertIn("chat", text)
        self.assertIn("neither", text)

    def test_ugc_constraints_do_not_impose_moderate_dynamics(self):
        text = self.text(
            ".agents/skills/ugc-motion-presets/references/execution-constraints.md"
        )
        self.assert_no_rule(text, r"jumps use described, moderate dynamics")
        self.assertIn("brief", text)
        self.assertIn("recovery", text)

    def test_evals_are_parseable_and_have_behavioral_expectations(self):
        for path in SKILLS.glob("*/evals/evals.json"):
            with self.subTest(path=path):
                data = json.loads(path.read_text())
                self.assertEqual(data["skill_name"], path.parents[1].name)
                identifiers = [case["id"] for case in data["evals"]]
                self.assertEqual(len(identifiers), len(set(identifiers)))
                for case in data["evals"]:
                    self.assertTrue(case["prompt"].strip())
                    self.assertTrue(case["expected_output"].strip())
                    expectations = case.get("expectations", case.get("assertions"))
                    if expectations is not None:
                        self.assertTrue(expectations)
                        self.assertTrue(all(isinstance(item, str) and item.strip()
                                            for item in expectations))

    def test_focused_evals_retain_paired_and_failure_cases(self):
        required_cases = {
            "brief-intake": {12, 13, 14, 15},
            "seedance-shot-design": {19, 20, 21, 22},
            "seedance-acting-console": {15, 16, 17},
            "seedance-prompt-25": {105, 106},
            "seedance-prompt-20": {6, 7},
            "prompt-review": {1, 2, 3, 4},
            "ugc-motion-presets": {7, 9},
            "seedance-camera-presets": {14, 15, 16, 17},
            "seedance-pacing-presets": {13, 14, 15},
        }
        for skill, identifiers in required_cases.items():
            with self.subTest(skill=skill):
                path = SKILLS / skill / "evals/evals.json"
                data = json.loads(path.read_text())
                by_id = {case["id"]: case for case in data["evals"]}
                self.assertTrue(identifiers <= by_id.keys())
                for identifier in identifiers:
                    case = by_id[identifier]
                    self.assertEqual(case["files"], [])
                    self.assertGreaterEqual(
                        len(case.get("expectations", case.get("assertions"))), 3
                    )


if __name__ == "__main__":
    unittest.main()
