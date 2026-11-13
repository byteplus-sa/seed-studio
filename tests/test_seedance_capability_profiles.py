import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
PREVIEW_OWNERS = (
    "template-factory/SKILL.md",
    "seedance-effects-studio/SKILL.md",
    "seedance-restyle/SKILL.md",
    "seedance-object-swap/SKILL.md",
    "ugc-motion-presets/references/execution-constraints.md",
    "seedance-fight-choreography/SKILL.md",
)
PREVIEW_CASES = (
    (
        "covered-legacy",
        ("Use the previously covered exact standard 2.5 or access-confirmed "
         "Premium binding for an edit, extension or retry in default or strict mode."),
        ("previously covered exact standard", "access-confirmed premium",
         'resolution: "480p"', "boolean `draft: true`", "default and strict",
         "edits", "extensions", "creative retries"),
    ),
    (
        "ordinary-720p-with-480p",
        ("Keep my selected new exact 2.5 variant. Its valid destination-bound "
         "operation profile prescribes ordinary 720p and also supports 480p."),
        ("ordinary 720p", "even when 480p is also supported", "non-promotable",
         "never infer support from a family substring", "preserve the selected"),
    ),
    (
        "nonlegacy-native",
        ("My new exact binding verifies native preview controls other than "
         "boolean Draft/480p. Promotion support must be checked separately."),
        ("evidenced native controls", "native preview", "promotion support",
         "do not inherit 480p"),
    ),
    (
        "ordinary-fresh-final",
        ("I selected a successful ordinary preview. Prepare a fresh final, "
         "not task-ID promotion, and keep my creative inputs unchanged."),
        ("ordinary task ids cannot be promoted", "separately confirmed fresh final",
         "supported output settings", "final inspection"),
    ),
    (
        "unknown-or-invalid-evidence",
        ("The profile is missing, malformed, expired, wrong-destination or "
         "unknown. Still write creative text, but do not execute or choose a model."),
        ("provider", "transport", "tool schema revision", "validity",
         "missing", "malformed", "expired", "wrong-destination", "unknown",
         "execution unresolved", "prompt-only"),
    ),
    (
        "missing-native-control",
        ("The covered legacy binding's UI omits Draft. Do not silently drop "
         "Draft, invent a parameter or substitute ordinary 480p."),
        ("missing legacy draft controls", "capability mismatch",
         "not permission to drop `draft` or substitute ordinary 480p"),
    ),
    (
        "native-selection-and-history",
        ("An unselected, failed or historical ordinary task is offered for "
         "native promotion. A changed reference hash must also fail."),
        ("exact selected successful native task", "unchanged creative inputs",
         "reference hashes", "matching valid model/operation/profile/transport",
         "failed, unselected or mismatched", "historical task identity"),
    ),
    (
        "prompt-only-and-denied-probe",
        ("No prompt or references yet; write a draft in chat. No probe or "
         "generation is authorized, and strict mode does not invoke manual review."),
        ("opt-in probes", "prompt-only", "per-submit confirmation",
         "no automatic review", "does not authorize generation"),
    ),
)


class SeedanceCapabilityProfilesTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

    def test_remaining_preview_owners_cover_scoped_narrative_cases(self):
        for path in PREVIEW_OWNERS:
            content = (SKILLS / path).read_text()
            section = re.search(
                r"^#{2,3} Preview evidence\n(.*?)(?=^#{1,3} |\Z)",
                content, re.MULTILINE | re.DOTALL,
            )
            with self.subTest(path=path):
                self.assertIsNotNone(section, "Missing owner-scoped preview policy")
            if section is None:
                continue
            text = " ".join(section.group(1).lower().split())
            for case_id, prompt, expectations in PREVIEW_CASES:
                with self.subTest(path=path, case=case_id):
                    self.assertTrue(prompt.strip())
                    for expectation in expectations:
                        self.assertIn(expectation, text)

    def test_remaining_preview_owners_remove_unqualified_native_directives(self):
        stale_directives = (
            "every new seedance 2.5 generation uses explicit",
            "every new seedance 2.5 generation, including video edits, starts",
            "every new seedance 2.5 test uses",
            "for new seedance 2.5 requests, the caller must use native draft",
            "for every new seedance 2.5 generation",
            ("other video models without native draft mode use a clearly "
             "labeled ordinary 480p test"),
            "a native probe uses explicit",
            ("use explicit `resolution: \"480p\"` and boolean `draft: true` "
             "for a new native probe"),
            ('`generate_audio: false`, `watermark: false`, `resolution: "480p"`, '
             "`draft: true` for each new test"),
        )
        for path in PREVIEW_OWNERS:
            with self.subTest(path=path):
                text = self.text(path)
                for directive in stale_directives:
                    self.assertNotIn(directive, text)

    def test_ordinary_finals_have_successful_selection_and_separate_inspection(self):
        for path in PREVIEW_OWNERS:
            text = self.text(path)
            with self.subTest(path=path):
                self.assertIn("ordinary task ids cannot be promoted", text)
                final = text.split("ordinary task ids cannot be promoted", 1)[1]
                final = final.split("missing, malformed", 1)[0]
                for concept in (
                    "inspected", "selected successful ordinary preview",
                    "separately confirmed fresh final", "unchanged creative inputs",
                    "supported output settings", "final inspection",
                ):
                    self.assertIn(concept, final)

    def policy_surfaces(self):
        paths = (
            "AGENTS.md",
            ".agents/contracts/production-policy.md",
            ".agents/contracts/review-mode.md",
            ".agents/contracts/generation-transport.md",
            ".agents/skills/seedance-prompt-25/SKILL.md",
            ".agents/skills/seedance-prompt-25/references/parameter-reference.md",
            ".agents/skills/prompt-review/references/review-checklists.md",
        )
        surfaces = {
            path: " ".join((ROOT / path).read_text().lower().split())
            for path in paths
        }
        catalog = json.loads((ROOT / ".agents/contracts/rules.json").read_text())
        rule = next(rule for rule in catalog["rules"]
                    if rule["id"] == "seedance.draft_promotion")
        self.assertEqual(rule["owner_path"], ".agents/contracts/production-policy.md")
        self.assertEqual(rule["severity"], "error")
        surfaces["seedance.draft_promotion"] = " ".join(
            (rule["summary"] + " " + " ".join(rule["exceptions"])).lower().split()
        )
        return surfaces

    def test_studio_01_every_owner_scopes_native_policy_to_exact_covered_bindings(self):
        for path, text in self.policy_surfaces().items():
            with self.subTest(path=path):
                for concept in ("previously covered", "exact", "standard",
                                "premium", "480p", "draft", "true"):
                    self.assertIn(concept, text)
                if path == ".agents/contracts/generation-transport.md":
                    self.assertIn("edits, extensions and creative retries", text)
                for stale in ("every new seedance 2.5 generation",
                              "every new seedance 2.5 request",
                              "every proposed 2.5 probe",
                              "a new 2.5 face-containing edit starts"):
                    self.assertNotIn(stale, text)

    def test_studio_01_ordinary_720p_is_evidence_led_even_when_480p_is_supported(self):
        for path, text in self.policy_surfaces().items():
            with self.subTest(path=path):
                for concept in ("new", "verified", "model", "operation", "provider",
                                "transport", "schema revision", "validity",
                                "ordinary", "evidenced", "non-promotable",
                                "fresh", "substring"):
                    self.assertIn(concept, text)
                self.assertRegex(text, r"even when 480p is (?:also )?supported")
                self.assertIn("native controls", text)
                self.assertNotIn("use an ordinary 480p", text)
                self.assertNotIn("non-promotable 480p test", text)

    def test_studio_01_invalid_evidence_never_authorizes_execution_or_promotion(self):
        for path, text in self.policy_surfaces().items():
            with self.subTest(path=path):
                for concept in ("missing", "malformed", "expired",
                                "wrong-destination", "unknown", "unresolved",
                                "prompt-only", "native", "selected", "successful",
                                "reference hashes", "final inspection", "historical"):
                    self.assertIn(concept, text)

    def test_unknown_profile_blocks_execution_not_creative_writing(self):
        text = self.text("seedance-prompt-25/references/parameter-reference.md")
        for concept in ("exact model", "provider", "operation", "transport",
                        "tool schema revision", "validity", "unknown",
                        "prompt-only", "non-promotable"):
            self.assertIn(concept, text)
        self.assertNotIn("for other video models without native draft mode, "
                         "use an ordinary 480p", text)

    def test_promotion_requires_matching_selected_native_task(self):
        text = self.text("seedance-prompt-25/references/parameter-reference.md")
        for concept in ("successful", "selected", "reference hashes",
                        "expiry", "profile", "final", "inspect"):
            self.assertIn(concept, text)
        self.assertIn("plain 480p output is not a native draft", text)

    def test_limits_are_bound_to_evidence_not_family_name(self):
        text = self.text("seedance-prompt-25/references/parameter-reference.md")
        self.assertIn("per-modality", text)
        self.assertIn("conditional", text)
        self.assertIn("snapshot", text)
        self.assertIn("not live capability evidence", text)

    def test_manual_checklist_unknown_model_stays_incomplete(self):
        text = self.text("prompt-review/references/review-checklists.md")
        self.assertIn("unknown model", text)
        self.assertIn("incomplete", text)
        self.assertIn("model and operation first", text)
        self.assertNotIn("use as an additional checklist alongside seedance 2.5", text)


if __name__ == "__main__":
    unittest.main()
