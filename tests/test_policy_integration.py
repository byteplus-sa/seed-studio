import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def text(path):
    return " ".join((ROOT / path).read_text().split())


class PolicyIntegrationTests(unittest.TestCase):
    def test_review_mode_never_invokes_manual_review(self):
        mode = text(".agents/contracts/review-mode.md")
        self.assertIn("strict does not invoke", mode)
        self.assertIn("only when the user invokes `/prompt-review`", text("AGENTS.md"))
        self.assertIn("it never gates handoff or generation", text("AGENTS.md"))
        review = text(".agents/skills/prompt-review/SKILL.md")
        self.assertIn("Only when the user invokes `/prompt-review`", review)
        self.assertNotIn("or selects strict review", review)

    def test_generation_confirmation_is_independent_of_creative_selection(self):
        transport = text(".agents/contracts/generation-transport.md")
        for requirement in [
            "wait for an explicit yes", "Approval covers that submit only",
            "byte-identical", "Neither approval mode authorizes submission",
            "confirm again before resubmitting",
        ]:
            self.assertIn(requirement, transport)
        self.assertIn("confirm each submit", text("AGENTS.md"))

    def test_modes_cannot_disable_native_drafts(self):
        mode = text(".agents/contracts/review-mode.md")
        self.assertIn('resolution: "480p"', mode)
        self.assertIn("draft: true", mode)
        for path in [
            ".agents/contracts/review-mode.md",
            ".agents/contracts/production-policy.md", "README.md",
        ]:
            content = text(path)
            self.assertNotIn("no compulsory draft-first", content)
            self.assertNotIn("or mandatory draft-first", content)
        transport = text(".agents/contracts/generation-transport.md")
        self.assertIn("Confirm promotion separately", transport)
        self.assertIn("creative change requires a new native draft", transport)

    def test_mode_changes_do_not_imply_saving(self):
        mode = text(".agents/contracts/review-mode.md")
        self.assertIn("Save a mode change only on explicit request", mode)
        self.assertIn("never reinterpret old approvals", mode)
        self.assertIn("Invalid values need correction", mode)

    def test_sampling_is_not_generation_permission(self):
        mode = text(".agents/contracts/review-mode.md")
        self.assertIn("Explicit requested count wins", mode)
        self.assertIn("proposes", mode)
        self.assertIn("per-submit confirmation", mode)

    def test_review_records_are_not_handoff_prerequisites(self):
        policy = text(".agents/contracts/production-policy.md")
        self.assertIn("Neither mode requires a review record for handoff", policy)
        self.assertIn("When a review was requested", policy)

    def test_rule_catalog_keeps_selection_separate_from_submission(self):
        rules = json.loads((ROOT / ".agents/contracts/rules.json").read_text())
        rule = next(rule for rule in rules["rules"]
                    if rule["id"] == "approval.explicit_choice")
        self.assertIn("per-submit", rule["summary"])
        self.assertIn("user locks", rule["summary"])

    def test_review_scenarios_do_not_authorize_implicit_pipeline(self):
        cases = json.loads(
            (ROOT / ".agents/contracts/review-mode-evals.json").read_text()
        )["cases"]
        self.assertEqual(len(cases), len({case["name"] for case in cases}))
        strict = next(case for case in cases
                      if case["name"] == "strict_with_agent_selection")
        self.assertIn("does not invoke", " ".join(strict["expected"]))
        generation = next(case for case in cases
                          if case["name"] == "requested_generation")
        self.assertIn("explicit yes", " ".join(generation["expected"]))

    def test_no_conflict_markers(self):
        for path in [ROOT / "AGENTS.md", ROOT / "README.md",
                     *ROOT.glob(".agents/**/*.md"), *ROOT.glob(".agents/**/*.json")]:
            self.assertIsNone(re.search(r"(?m)^(<<<<<<<|=======|>>>>>>>)",
                                        path.read_text()), str(path))


if __name__ == "__main__":
    unittest.main()
