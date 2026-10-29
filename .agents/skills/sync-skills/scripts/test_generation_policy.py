import json
import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[4]


def read(relative_path):
    return " ".join((ROOT / relative_path).read_text().split())


class GenerationPolicyTests(unittest.TestCase):
    def test_root_and_claude_share_nonfinancial_opt_in(self):
        policy = read("AGENTS.md")
        self.assertTrue((ROOT / "CLAUDE.md").is_symlink())
        self.assertEqual((ROOT / "CLAUDE.md").resolve(), ROOT / "AGENTS.md")
        self.assertIn("confirm each submit", policy)
        self.assertIn("not financial approval", policy)
        self.assertIn("Cost information is optional", policy)

    def test_transport_requires_each_exact_submit_not_a_budget(self):
        policy = read(".agents/contracts/generation-transport.md")
        for text in (
            "wait for an explicit yes",
            "Approval covers that submit only",
            "byte-identical",
            "Count every variation",
            "not financial approval",
            "Do not require a project or generation budget",
            "Missing pricing never blocks",
        ):
            with self.subTest(text=text):
                self.assertIn(text, policy)

    def test_native_draft_and_promotion_are_preserved(self):
        policy = read(".agents/contracts/generation-transport.md")
        for text in (
            'resolution: "480p"',
            "boolean `draft: true`",
            "edits, extensions and creative retries",
            "Confirm promotion separately",
            "`draft_task_id`",
            "creative change requires a new native draft",
            "Inspect the final output again",
            "do not silently drop the flag",
        ):
            with self.subTest(text=text):
                self.assertIn(text, policy)

    def test_unknown_submit_cannot_trigger_duplicate_or_failover(self):
        policy = read(".agents/contracts/generation-transport.md")
        for text in (
            "Use one transport per job",
            "Do not fail over mid-job",
            "Reconcile ambiguous responses before repeating a submit",
            "No usable selected transport",
            "Bulk or unattended generation loops",
            "confirm again before resubmitting",
        ):
            with self.subTest(text=text):
                self.assertIn(text, policy)

    def test_manual_review_and_rights_still_apply(self):
        root = read("AGENTS.md")
        policy = read(".agents/contracts/production-policy.md")
        self.assertIn("it never gates handoff or generation", root)
        self.assertIn("Unknown rights, identity, and consent facts stop the work", policy)
        self.assertIn("Under `ask_for_approval`, keep recommendations proposed", policy)
        self.assertIn("agent decision under `approve_for_me`", policy)
        self.assertIn("select an inspected candidate", policy)
        self.assertIn("Explicit user locks and requests to choose personally always win", policy)
        self.assertIn("not per-submit generation opt-in, rights or consent", policy)
        self.assertIn("When a review was requested", policy)
        self.assertNotIn("This workspace performs no provider submission", policy)

    def test_inherited_financial_prerequisites_are_absent(self):
        patterns = (
            r"\bbudget posture\b",
            r"\bcloud analysis is permitted within budget\b",
            r"\bretake budget used\b",
            r"\bprivacy, budget\b",
            r"\bprivacy, cost\b",
            r"\bcapability and cost are resolved\b",
            r"\bconfirm the model, references and cost\b",
            r"\bconfirm current billing rules\b",
            r"\b(?:budget_usd|spending_cap|unit_budget)\b",
            r"\b(?:authorize media spend|authorization to generate media or spend credits)\b",
        )
        paths = [ROOT / "AGENTS.md", ROOT / "README.md"]
        paths.extend((ROOT / ".agents").rglob("*.md"))
        paths.extend((ROOT / ".agents").rglob("*.json"))
        for path in paths:
            text = " ".join(path.read_text().split())
            for pattern in patterns:
                with self.subTest(path=str(path.relative_to(ROOT)), pattern=pattern):
                    self.assertIsNone(re.search(pattern, text, re.IGNORECASE))

    def test_optional_cost_card_and_historical_price_remain(self):
        skill = read(".agents/skills/omnihuman-prompt-20/SKILL.md")
        reference = read(".agents/skills/omnihuman-prompt-20/references/inputs-and-api.md")
        self.assertIn("Optional cost note", skill)
        self.assertNotIn("Estimated cost:", skill)
        self.assertIn("0.07 USD per second", reference)
        self.assertIn("not a prerequisite", reference)

    def test_capabilities_sampling_and_aliases_remain_valid(self):
        policy = read(".agents/contracts/production-policy.md")
        self.assertIn("Default mode uses one image sample", policy)
        self.assertIn("Strict mode proposes three stochastic samples", policy)
        self.assertIn("Explicit requested count wins", policy)
        self.assertIn("Additional generations require their own exact-package confirmation", policy)
        limits = read(".agents/skills/omnihuman-prompt-20/references/inputs-and-api.md")
        self.assertIn("4-300 s", limits)
        skills = ROOT / ".agents/skills"
        aliases = ROOT / ".claude/skills"
        self.assertEqual({path.name for path in skills.iterdir()},
                         {path.name for path in aliases.iterdir()})
        for alias in aliases.iterdir():
            with self.subTest(alias=alias.name):
                self.assertTrue(alias.is_symlink())
                self.assertEqual(alias.resolve(), skills / alias.name)
                self.assertTrue((alias / "SKILL.md").is_file())
        rules = json.loads((ROOT / ".agents/contracts/rules.json").read_text())["rules"]
        ids = [rule["id"] for rule in rules]
        self.assertEqual(len(ids), len(set(ids)))
        for rule in rules:
            with self.subTest(rule=rule["id"]):
                self.assertTrue((ROOT / rule["owner_path"]).is_file())

    def test_sync_preserves_local_policy_without_new_runtime(self):
        policy = read(".agents/skills/sync-skills/SKILL.md")
        self.assertIn("project/generation budget declarations", policy)
        self.assertIn("per-submit generation opt-in", policy)
        self.assertFalse((ROOT / ".agents/scripts/operation_store.py").exists())
        self.assertFalse((ROOT / ".agents/scripts/budget_report.py").exists())

    def test_policy_scenarios_have_unique_names_and_expected_results(self):
        path = ROOT / ".agents/contracts/generation-policy-evals.json"
        scenarios = json.loads(path.read_text())["cases"]
        names = [case["name"] for case in scenarios]
        self.assertEqual(len(names), len(set(names)))
        required = {
            "prompt_only_without_budget",
            "confirmed_generation_without_pricing",
            "submit_not_confirmed",
            "submit_declined",
            "empty_request",
            "native_draft_then_promotion",
            "changed_prompt_and_variation",
            "ambiguous_submit",
            "missing_rights",
            "unsupported_provider_limit",
            "missing_transport",
            "external_limit_rejection",
            "analysis_without_budget",
            "optional_cost_card",
        }
        self.assertTrue(required.issubset(names))
        for case in scenarios:
            with self.subTest(name=case["name"]):
                self.assertIsInstance(case["input"], str)
                self.assertTrue(case["expected"])
                self.assertTrue(all(isinstance(item, str) and item.strip()
                                    for item in case["expected"]))

    def test_all_json_and_skill_evaluation_ids_are_valid(self):
        for path in sorted((ROOT / ".agents").rglob("*.json")):
            with self.subTest(path=str(path.relative_to(ROOT))):
                data = json.loads(path.read_text())
                if path.name != "evals.json":
                    continue
                self.assertEqual(data["skill_name"], path.parent.parent.name)
                ids = [case["id"] for case in data["evals"]]
                self.assertEqual(len(ids), len(set(ids)))
                for case in data["evals"]:
                    self.assertTrue(case["prompt"].strip())
                    self.assertTrue(case["expected_output"].strip())
                    self.assertIsInstance(case["files"], list)
                    assertions = case.get("assertions", case.get("expectations"))
                    if assertions is not None:
                        self.assertIsInstance(assertions, list)
                        self.assertTrue(assertions)
                        self.assertTrue(all(isinstance(item, str) and item.strip()
                                            for item in assertions))


if __name__ == "__main__":
    unittest.main()
