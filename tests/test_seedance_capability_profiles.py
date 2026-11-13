import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"


class SeedanceCapabilityProfilesTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

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
