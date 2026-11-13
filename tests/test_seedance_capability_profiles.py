import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"


class SeedanceCapabilityProfilesTests(unittest.TestCase):
    def text(self, relative):
        return " ".join((SKILLS / relative).read_text().lower().split())

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
