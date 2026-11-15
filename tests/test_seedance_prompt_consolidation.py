import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
RETIRED = ("seedance-prompt-20", "seedance-prompt-25")
RETIRED_REFERENCE = re.compile(r"\bseedance-prompt-(?:20|25)(?![\w-])")
REFERENCES = (
    "audio-performance-camera", "keyframes-storyboards-blockouts",
    "parameter-reference", "reference-inputs", "repair-examples",
    "scene-action", "shot-staging", "transitions-and-one-click",
    "video-editing", "video-extension", "worked-examples",
)


class SeedancePromptConsolidationTests(unittest.TestCase):
    def test_only_consolidated_entrypoint_and_alias_remain(self):
        for name in RETIRED:
            with self.subTest(name=name):
                self.assertFalse((SKILLS / name).exists())
                self.assertFalse((ROOT / ".claude/skills" / name).exists())
                self.assertFalse((ROOT / ".claude/skills" / name).is_symlink())
        alias = ROOT / ".claude/skills/seedance-prompt"
        self.assertTrue(alias.is_symlink())
        self.assertEqual(alias.resolve(), SKILLS / "seedance-prompt")
        self.assertTrue((SKILLS / "seedance-prompt-25-filipino/SKILL.md").is_file())

    def test_mode_references_are_local_and_reachable(self):
        entrypoint = (SKILLS / "seedance-prompt/SKILL.md").read_text()
        for name in REFERENCES:
            relative = f"references/{name}.md"
            with self.subTest(reference=name):
                self.assertTrue((SKILLS / "seedance-prompt" / relative).is_file())
                self.assertIn(relative, entrypoint)

    def test_all_skill_aliases_resolve_to_their_owned_bundle(self):
        aliases = ROOT / ".claude/skills"
        expected = {path.parent.name for path in SKILLS.glob("*/SKILL.md")}
        self.assertEqual({path.name for path in aliases.iterdir()}, expected)
        for name in expected:
            with self.subTest(skill=name):
                self.assertTrue((aliases / name).is_symlink())
                self.assertEqual((aliases / name).resolve(), SKILLS / name)

    def test_reference_links_and_anchors_resolve_within_the_bundle(self):
        bundle = SKILLS / "seedance-prompt"
        for path in bundle.rglob("*.md"):
            text = path.read_text()
            self.assertEqual(sum(line.startswith("```") for line in text.splitlines()) % 2, 0, path)
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in target:
                    continue
                relative, _, anchor = target.partition("#")
                destination = (path.parent / relative).resolve() if relative else path
                with self.subTest(path=path.name, target=target):
                    self.assertTrue(destination.is_file())
                    if not anchor or not destination.is_file():
                        continue
                    headings = re.findall(r"(?m)^#{1,6} (.+)$", destination.read_text())
                    anchors = {
                        re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
                        for heading in headings
                    }
                    self.assertIn(anchor, anchors)

    def test_active_callers_do_not_route_to_retired_skills(self):
        paths = [ROOT / "AGENTS.md", ROOT / "README.md"]
        paths.extend((ROOT / ".agents/contracts").glob("*"))
        paths.extend(
            path for path in SKILLS.rglob("*")
            if "sync-skills" not in path.parts
            and not set(RETIRED).intersection(path.parts)
        )
        for path in paths:
            if path.is_file() and path.suffix in {".md", ".json", ".yaml"}:
                with self.subTest(path=str(path.relative_to(ROOT))):
                    self.assertIsNone(RETIRED_REFERENCE.search(path.read_text()))

    def test_all_historical_eval_cases_have_unique_consolidated_ids(self):
        data = json.loads((SKILLS / "seedance-prompt/evals/evals.json").read_text())
        self.assertEqual(data["skill_name"], "seedance-prompt")
        cases = {case["id"]: case for case in data["evals"]}
        expected = set(range(1, 13))
        expected.update(2000 + case_id for case_id in (*range(1, 8), *range(101, 109)))
        expected.update(2500 + case_id for case_id in (
            *range(1, 13), *range(101, 107), *range(301, 310),
        ))
        self.assertTrue(expected.issubset(cases))
        self.assertEqual(len(cases), len(data["evals"]))
        for case in cases.values():
            self.assertTrue(case["expected_output"].strip())
            self.assertEqual(case["files"], [])
            self.assertGreaterEqual(len(case["expectations"]), 3)

    def test_sync_allowlist_excludes_retired_and_local_generic_skill(self):
        text = (SKILLS / "sync-skills/scripts/sync.sh").read_text()
        allowlist = re.search(r'^ALLOWLIST="([^"]+)"', text, re.MULTILINE).group(1).split()
        self.assertEqual(len(allowlist), len(set(allowlist)))
        self.assertEqual(len(allowlist), 19)
        for name in (*RETIRED, "seedance-prompt"):
            self.assertNotIn(name, allowlist)
        self.assertIn("seedance-prompt-25-filipino", allowlist)

    def test_sync_leak_patterns_reject_only_retired_exact_names(self):
        text = (SKILLS / "sync-skills/scripts/forbidden-refs.txt").read_text()
        patterns = [
            re.compile(line) for line in text.splitlines()
            if line and not line.startswith("#")
        ]
        for name in RETIRED:
            self.assertTrue(any(pattern.search(name) for pattern in patterns))
        for name in ("seedance-prompt", "seedance-prompt-25-filipino"):
            self.assertFalse(any(pattern.search(name) for pattern in patterns))

    def test_shared_bundle_contains_no_private_source_links(self):
        for path in (SKILLS / "seedance-prompt").rglob("*.md"):
            with self.subTest(path=path.name):
                self.assertNotRegex(path.read_text(), r"larkoffice\.com|/Users/|file://")

    def test_edit_and_extension_preserve_sources_without_automatic_adaptation(self):
        for name in ("video-editing", "video-extension"):
            text = (SKILLS / f"seedance-prompt/references/{name}.md").read_text().lower()
            with self.subTest(reference=name):
                for concept in ("fractional", "audio tail", "playback speed",
                                "separate", "probes", "exact model",
                                "operation", "destination"):
                    self.assertIn(concept, text)
                self.assertRegex(text, r"\bagree(?:d|ment)\b")
                self.assertNotIn("±0.3s", text)

    def test_reference_guidance_has_no_automatic_model_ladder_or_hard_quotas(self):
        for name in REFERENCES:
            text = (SKILLS / f"seedance-prompt/references/{name}.md").read_text().lower()
            with self.subTest(reference=name):
                self.assertNotIn("prototype on mini", text)
                self.assertNotIn("### cost ladder", text)
                self.assertNotIn("one per shot only", text)
                self.assertNotIn("seedance 2.5 natively supports these languages", text)
                self.assertNotIn("generate a 30s base take", text)

    def test_parameter_guidance_does_not_require_assets_or_unverified_controls(self):
        text = " ".join(
            (SKILLS / "seedance-prompt/references/parameter-reference.md")
            .read_text().lower().split()
        )
        self.assertNotIn("lock character sheets, prop sheets, and scene sheets", text)
        self.assertNotIn("before spending video credits", text)
        self.assertNotIn("preserve a written", text)
        for concept in ("selected references", "unresolved slots", "chat",
                        "only when requested", "does not generate"):
            self.assertIn(concept, text)
        control = next(line for line in text.split("- ") if line.startswith("`return_last_frame`"))
        self.assertIn("verified", control)
        self.assertIn("selected", control)

    def test_repair_guidance_does_not_add_a_manual_review_gate(self):
        text = " ".join(
            (SKILLS / "seedance-prompt/references/repair-examples.md")
            .read_text().lower().split()
        )
        self.assertNotIn("needs current bindings and renewed review", text)
        for concept in ("locked decisions", "requested delta", "acceptance criteria",
                        "known rejections", "chat", "manual review", "only",
                        "requested", "does not authorize"):
            self.assertIn(concept, text)

    def test_vfx_handoffs_keep_model_alternatives_unselected(self):
        for name in ("compact-legacy", "fidelity-and-continuity"):
            text = " ".join(
                (SKILLS / f"seedance-vfx-prompt/references/{name}.md")
                .read_text().lower().split()
            )
            handoff = text.split("> **seedance 2.5 ", 1)[1]
            handoff = handoff.split("### ", 1)[0]
            with self.subTest(reference=name):
                for concept in ("selected model", "unselected", "exact", "operation",
                                "destination", "seedance-prompt"):
                    self.assertIn(concept, handoff)
                self.assertNotIn("and use the 2.5 model", handoff)

    def test_frame_break_syntax_depends_on_destination_evidence(self):
        for relative in ("SKILL.md", "references/prompt-template.md"):
            text = " ".join(
                (SKILLS / "seedance-frame-break" / relative).read_text().lower().split()
            )
            with self.subTest(path=relative):
                for concept in ("bracket", "verified", "exact model", "destination",
                                "plain language", "listening"):
                    self.assertIn(concept, text)

    def test_conditional_references_do_not_restore_mandatory_prompt_formatting(self):
        shot = " ".join(
            (SKILLS / "seedance-prompt/references/shot-staging.md")
            .read_text().lower().split()
        )
        audio = " ".join(
            (SKILLS / "seedance-prompt/references/audio-performance-camera.md")
            .read_text().lower().split()
        )
        self.assertNotIn("with its reason recorded", shot)
        self.assertIn("no separate justification", shot)
        self.assertNotIn("using the `dialogue language` prefix", audio)
        self.assertIn("optional", audio.split("## scripted dialogue", 1)[1])
        self.assertIn("exact approved", audio)

    def test_control_only_planning_images_are_omitted_without_banning_independent_inputs(self):
        text = " ".join(
            (SKILLS / "seedance-prompt/references/reference-inputs.md")
            .read_text().lower().split()
        )
        self.assertNotIn("for a control-only image, prefer", text)
        for concept in ("omit the planning image", "independently authored",
                        "production stills", "animated blockouts", "rights",
                        "consent", "lineage", "current hashes", "qa"):
            self.assertIn(concept, text)

    def test_readme_catalog_matches_consolidated_scope_and_skill_count(self):
        text = (ROOT / "README.md").read_text()
        rows = re.findall(r"(?m)^\| \*\*seedance-prompt\*\* \| (.+) \|$", text)
        self.assertEqual(len(rows), 1)
        for concept in ("2.5-based", "composition", "references", "edits", "extensions"):
            self.assertIn(concept, rows[0])
        count = len(list(SKILLS.glob("*/SKILL.md"))) - 1
        self.assertIn(f"{count} prompt-composition skills + sync-skills", text)

    def test_ui_metadata_and_eval_accept_source_edits_without_execution(self):
        text = (SKILLS / "seedance-prompt/agents/openai.yaml").read_text()
        self.assertIn('display_name: "Seedance Prompt"', text)
        for concept in ("2.5-based", "composition", "references", "edits",
                        "extensions", "$seedance-prompt", "selected exact model"):
            self.assertIn(concept, text)
        self.assertNotRegex(text, RETIRED_REFERENCE)
        self.assertNotIn("source-video edits or", text)
        data = json.loads((SKILLS / "seedance-prompt/evals/evals.json").read_text())
        case = next(case for case in data["evals"] if case["id"] == 11)
        self.assertIn("source-preserving edit prompt", case["expected_output"].lower())
        self.assertNotIn("out-of-scope", case["expected_output"].lower())
        self.assertTrue(any("no rounding" in value.lower() for value in case["expectations"]))

    def test_extension_boundary_uncertainty_does_not_relax_exact_locks(self):
        for reference in ("scene-action", "video-extension"):
            text = " ".join(
                (SKILLS / f"seedance-prompt/references/{reference}.md")
                .read_text().lower().replace("**", "").split()
            )
            with self.subTest(reference=reference):
                self.assertNotRegex(text, r"(?:are not|will not be) pixel-identical")
                for concept in ("not guaranteed pixel-identical", "exact-boundary",
                                "locks", "unresolved", "verified"):
                    self.assertIn(concept, text)

    def review_section(self, heading):
        text = (SKILLS / "prompt-review/references/review-checklists.md").read_text()
        section = text.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0]
        return " ".join(section.lower().replace("**", "").split())

    def test_review_accepts_action_before_assets_and_audio_before_camera(self):
        for heading in ("Seedance 2.0", "Seedance 2.5"):
            section = self.review_section(heading)
            with self.subTest(heading=heading):
                self.assertIn("flexible", section)
                self.assertIn("section order", section)
                for obsolete in ("parts are in this order", "prompt assembles in this order",
                                 "before any prompt body", "per-shot description order"):
                    self.assertNotIn(obsolete, section)
        legacy = self.review_section("Seedance 2.0")
        self.assertNotIn("uses `shot 1 / shot 2 / shot 3` format", legacy)
        self.assertIn("continuous take", legacy)
        self.assertIn("ordered actions", legacy)

    def test_review_accepts_inline_identity_without_define_or_feature_quota(self):
        for heading in ("Seedance 2.0", "Seedance VFX (video-to-video)"):
            section = self.review_section(heading)
            with self.subTest(heading=heading):
                for concept in ("stable", "identity", "inline", "optional", "quota"):
                    self.assertIn(concept, section)
                self.assertNotRegex(section, r"uses `define`(?: keyword)? with 2-3")
        self.assertIn("no mutable attributes", self.review_section("Seedance 2.0"))

    def test_review_accepts_multi_scene_bindings_without_group_or_profile_headings(self):
        section = self.review_section("Seedance 2.5")
        grouping = section.split("7. ", 1)[1].split("9. ", 1)[0]
        for concept in ("optional", "group", "profile", "inline",
                        "stable attributes", "ownership"):
            self.assertIn(concept, grouping)
        self.assertNotIn("references are organized as", grouping)
        self.assertNotIn("subjects have a centralized profile block", grouping)
        self.assertIn("each scene names only the references it uses", section)

    def test_review_audio_syntax_requires_evidence_not_model_family(self):
        dispatch = self.review_section("Model-first dispatch")
        self.assertIn("when that syntax is used", dispatch)
        self.assertIn("plain language needs no bracket-syntax evidence", dispatch)
        for heading in ("Seedance 2.0", "Seedance 2.5",
                        "Seedance 2.5 edit (video-to-video)"):
            section = self.review_section(heading)
            with self.subTest(heading=heading):
                for concept in ("plain language", "verified", "syntax", "speaker"):
                    self.assertIn(concept, section)
                self.assertNotIn("all audio content uses the correct bracket type", section)
        audio = self.review_section("Seedance 2.5").split("### audio syntax", 1)[1]
        audio = audio.split("### emotional direction", 1)[0]
        for concept in ("exact model", "operation", "destination", "optional",
                        "exact dialogue", "no paraphrasing", "listening", "rights"):
            self.assertIn(concept, audio)
        self.assertNotIn("non-chinese dialogue includes:", audio)

    def test_review_accepts_edit_semantics_without_template_headings(self):
        section = self.review_section("Seedance 2.5 edit (video-to-video)")
        task = section.split("### editing task", 1)[1].split("### preservation", 1)[0]
        for concept in ("optional", "headings", "sole editing master",
                        "scope", "content to preserve", "each", "target"):
            self.assertIn(concept, task)
        self.assertNotIn("present and one-sentence", task)
        self.assertNotIn("present iff", task)

    def test_review_still_rejects_ambiguous_identity_and_planning_conditioning(self):
        section = self.review_section("Seedance 2.5")
        for concept in ("every reference material is mapped directly",
                        "each subject is named and bound individually",
                        "never has to guess", "planning-only in every conditioning role",
                        "contradictory totals", "unexplained duplication",
                        "current source hashes"):
            self.assertIn(concept, section)
        recast = self.review_section("Seedance 2.5 recast (motion transfer)")
        for concept in ("one reference serving two subjects is critical",
                        "unlisted subject", "is critical", "motion excludes appearance"):
            self.assertIn(concept, recast)

    def test_review_still_rejects_source_changes_outside_authorized_scope(self):
        edit = self.review_section("Seedance 2.5 edit (video-to-video)")
        for concept in ("breakage of must preserve", "never an item the user explicitly",
                        "every appearance, motion, occlusion and exit"):
            self.assertIn(concept, edit)
        recast = self.review_section("Seedance 2.5 recast (motion transfer)")
        for concept in ("fractional source span", "frame timestamps", "playback speed",
                        "adapt only a separate copy", "verified destination requirement",
                        "user agreement", "retain original video and audio"):
            self.assertIn(concept, recast)

    def test_review_still_rejects_unsupported_controls_and_incomplete_evidence(self):
        dispatch = self.review_section("Model-first dispatch")
        for concept in ("unknown model", "capability review stays incomplete",
                        "missing or empty prompts stay incomplete",
                        "exact model, provider, operation, transport",
                        "tool schema revision and validity", "every applicable check"):
            self.assertIn(concept, dispatch)
        recast = self.review_section("Seedance 2.5 recast (motion transfer)")
        for concept in ("exceeding a verified hard limit is critical",
                        "unknown limits are incomplete"):
            self.assertIn(concept, recast)
        native = self.review_section("Seedance 2.5").split("### formula check", 1)[0]
        for concept in ("missing required native control", "capability mismatch",
                        "expired", "wrong-destination", "new native draft"):
            self.assertIn(concept, native)

    def test_review_remains_manual_findings_only_with_required_checks(self):
        checklist = (SKILLS / "prompt-review/references/review-checklists.md").read_text()
        entrypoint = " ".join((SKILLS / "prompt-review/SKILL.md").read_text().split())
        for concept in ("only when the user explicitly invokes `/prompt-review`",
                        "gates prompt handoff or generation",
                        "repair is separately authorized"):
            self.assertIn(concept, " ".join(checklist.split()))
        for concept in ("Check every item in the checklist. Do not skip items.",
                        "Missing inputs, unchecked required rules",
                        "Re-review of a frozen input is findings-only",
                        "request_sha256"):
            self.assertIn(concept, entrypoint)


if __name__ == "__main__":
    unittest.main()
