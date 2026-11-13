import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / ".agents/skills/sync-skills/scripts"
LOCATION = "seedream-location-asset"
PROMPT = "seedream-prompt"


class SyncOverlayPreservationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="sync-overlay-")
        self.addCleanup(self.temporary.cleanup)
        self.workspace = Path(self.temporary.name)
        self.source = self.workspace / "source"
        self.destination = self.workspace / "destination"
        self.environment = os.environ.copy()
        for name in tuple(self.environment):
            if name.startswith(("GIT_", "SYNC_")) or name == "SKILLS_SOURCE":
                del self.environment[name]
        self.environment.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_AUTHOR_NAME": "Sync Test",
            "GIT_AUTHOR_EMAIL": "sync-test@example.invalid",
            "GIT_COMMITTER_NAME": "Sync Test",
            "GIT_COMMITTER_EMAIL": "sync-test@example.invalid",
            "PYTHONDONTWRITEBYTECODE": "1",
            "SKILLS_SOURCE": str(self.source),
        })
        for repository in (self.source, self.destination):
            repository.mkdir()
            self.git(repository, "init", "--quiet")
            for skill in (LOCATION, PROMPT, "seedance-prompt-25"):
                self.write(repository, skill, "SKILL.md", f"# {skill}\n")
        for skill in (LOCATION, PROMPT, "seedance-prompt-25"):
            shutil.copy2(
                self.bundle(self.source, skill) / "SKILL.md",
                self.bundle(self.destination, skill) / "SKILL.md",
            )
        scripts = self.destination / ".agents/skills/sync-skills/scripts"
        scripts.mkdir(parents=True)
        for name in ("sync.sh", "leaks.py", "forbidden-refs.txt", "ownership.py"):
            shutil.copy2(SCRIPTS / name, scripts / name)
        self.script = scripts / "sync.sh"
        for repository in (self.source, self.destination):
            self.commit(repository)

    def git(self, repository, *arguments):
        return subprocess.run(
            ["git", "-C", str(repository), *arguments],
            env=self.environment, text=True, capture_output=True, check=True,
        ).stdout

    def bundle(self, repository, skill=LOCATION):
        return repository / ".agents/skills" / skill

    def write(self, repository, skill, relative, content):
        path = self.bundle(repository, skill) / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def commit(self, repository):
        self.git(repository, "add", ".agents")
        self.git(repository, "commit", "--quiet", "-m", "Prepare sync fixture")

    def sync(self, mode="apply", skills=(LOCATION,), **environment):
        return subprocess.run(
            ["bash", str(self.script), mode, *skills],
            cwd=self.destination,
            env={**self.environment, **environment},
            text=True, capture_output=True, timeout=20, check=False,
        )

    def snapshot(self, repository):
        result = {}
        for path in sorted((repository / ".agents").rglob("*")):
            relative = str(path.relative_to(repository))
            if path.is_symlink():
                result[relative] = ("symlink", os.readlink(path))
            elif path.is_file():
                result[relative] = ("file", path.read_bytes(), path.stat().st_mode)
            else:
                result[relative] = ("directory",)
        return result

    def assert_refused_without_writes(self, result, before, code=None):
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        if code is not None:
            self.assertEqual(result.returncode, code, output)
        self.assertEqual(self.snapshot(self.destination), before, output)

    def add_committed_overlay(self, relative="references/local lighting.md"):
        path = self.write(
            self.destination, LOCATION, relative, "Destination-owned lighting\n",
        )
        self.commit(self.destination)
        self.assertEqual(self.git(self.destination, "status", "--porcelain"), "")
        return path

    def test_clean_committed_overlay_blocks_apply_without_any_writes(self):
        overlay = self.add_committed_overlay()
        self.write(self.source, LOCATION, "SKILL.md", "# New upstream rules\n")
        self.commit(self.source)
        before = self.snapshot(self.destination)
        result = self.sync(SYNC_ALLOW_DIRTY="1")
        self.assert_refused_without_writes(result, before, 6)
        self.assertEqual(overlay.read_bytes(), b"Destination-owned lighting\n")
        self.assertIn("destination-only", result.stdout + result.stderr)
        self.assertIn(overlay.name, result.stdout)

    def test_plan_previews_committed_overlay_ownership_without_writes(self):
        overlay = self.add_committed_overlay()
        before = self.snapshot(self.destination)
        result = self.sync("plan")
        self.assertEqual(result.returncode, 6, result.stdout + result.stderr)
        self.assertEqual(self.snapshot(self.destination), before)
        self.assertIn("destination-only", result.stdout + result.stderr)
        self.assertIn(overlay.name, result.stdout)

    def test_overlay_in_later_bundle_blocks_updates_to_earlier_bundle(self):
        self.add_committed_overlay("evals/local.json")
        self.write(self.source, PROMPT, "SKILL.md", "# Upstream prompt update\n")
        self.commit(self.source)
        before = self.snapshot(self.destination)
        result = self.sync(skills=(PROMPT, LOCATION))
        self.assert_refused_without_writes(result, before, 6)

    def test_upstream_deletion_requires_an_explicit_ownership_decision(self):
        for repository in (self.source, self.destination):
            self.write(repository, LOCATION, "references/retired.md", "Old rules\n")
            self.commit(repository)
        (self.bundle(self.source) / "references/retired.md").unlink()
        self.commit(self.source)
        before = self.snapshot(self.destination)
        self.assert_refused_without_writes(self.sync(), before, 6)

    def test_dirty_destination_work_is_never_bypassed(self):
        for state in ("modified", "staged", "untracked", "ignored", "deleted"):
            with self.subTest(state=state):
                self.setUp()
                if state == "ignored":
                    self.write(self.destination, LOCATION, ".gitignore", "local.md\n")
                    self.commit(self.destination)
                    self.write(self.destination, LOCATION, "local.md", "Ignored work\n")
                elif state == "untracked":
                    self.write(self.destination, LOCATION, "local.md", "New work\n")
                elif state == "deleted":
                    (self.bundle(self.destination) / "SKILL.md").unlink()
                else:
                    self.write(self.destination, LOCATION, "SKILL.md", "Local edits\n")
                    if state == "staged":
                        self.git(self.destination, "add", ".agents")
                before = self.snapshot(self.destination)
                for mode in ("plan", "apply"):
                    result = self.sync(mode, SYNC_ALLOW_DIRTY="1")
                    self.assert_refused_without_writes(result, before, 5)

    def test_dirty_later_bundle_blocks_all_selected_updates(self):
        self.write(self.source, PROMPT, "SKILL.md", "Updated upstream prompt\n")
        self.commit(self.source)
        self.write(self.destination, LOCATION, "SKILL.md", "Unsaved local work\n")
        before = self.snapshot(self.destination)
        result = self.sync(skills=(PROMPT, LOCATION))
        self.assert_refused_without_writes(result, before, 5)

    def test_upstream_only_support_and_eval_files_are_copied(self):
        for relative in ("references/new rules.md", "evals/evals.json"):
            self.write(self.source, LOCATION, relative, "Reviewed upstream content\n")
        self.commit(self.source)
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for relative in ("references/new rules.md", "evals/evals.json"):
            self.assertEqual(
                (self.bundle(self.destination) / relative).read_bytes(),
                (self.bundle(self.source) / relative).read_bytes(),
            )
        self.assertTrue(self.git(self.destination, "status", "--porcelain"))

    def test_same_size_same_timestamp_upstream_content_is_updated(self):
        source = self.write(self.source, LOCATION, "SKILL.md", "New content\n")
        destination = self.write(
            self.destination, LOCATION, "SKILL.md", "Old content\n",
        )
        os.utime(source, (1700000000, 1700000000))
        os.utime(destination, (1700000000, 1700000000))
        self.commit(self.source)
        self.commit(self.destination)
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(destination.read_bytes(), source.read_bytes())

    def test_identical_bundle_does_not_change_destination(self):
        before = self.snapshot(self.destination)
        for mode in ("plan", "apply"):
            result = self.sync(mode)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(f"unchanged  {LOCATION}", result.stdout)
            self.assertEqual(self.snapshot(self.destination), before)
        self.assertEqual(self.git(self.destination, "status", "--porcelain"), "")

    def test_local_metadata_caches_aliases_and_unselected_forks_survive(self):
        self.write(self.destination, LOCATION, "agents/openai.yaml", "Local policy\n")
        self.write(self.source, LOCATION, "agents/openai.yaml", "Upstream policy\n")
        self.write(self.destination, "seedream-storyboard", "SKILL.md", "Local fork\n")
        self.commit(self.destination)
        self.commit(self.source)
        self.write(self.destination, LOCATION, "agents/openai.yaml", "Dirty local policy\n")
        self.write(self.destination, LOCATION, ".DS_Store", "Local cache\n")
        self.write(self.destination, LOCATION, "__pycache__/cache.pyc", "Local cache\n")
        aliases = self.destination / ".claude/skills"
        aliases.mkdir(parents=True)
        alias = aliases / LOCATION
        alias.symlink_to(f"../../.agents/skills/{LOCATION}")
        before = self.snapshot(self.destination)
        self.write(self.source, LOCATION, "references/new.md", "Upstream addition\n")
        self.commit(self.source)
        result = self.sync()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        after = self.snapshot(self.destination)
        for relative, contents in before.items():
            self.assertEqual(after[relative], contents)
        self.assertEqual(os.readlink(alias), f"../../.agents/skills/{LOCATION}")

    def test_dirty_source_requires_confirmation_but_plan_is_printed(self):
        self.write(self.source, LOCATION, "SKILL.md", "Uncommitted upstream\n")
        before = self.snapshot(self.destination)
        for mode in ("plan", "apply"):
            result = self.sync(mode)
            self.assert_refused_without_writes(result, before, 3)
        result = self.sync(SYNC_ALLOW_DIRTY="1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            (self.bundle(self.destination) / "SKILL.md").read_text(),
            "Uncommitted upstream\n",
        )

    def test_symlinks_in_source_or_destination_are_rejected_before_writes(self):
        for side in ("source", "destination"):
            for kind in ("file", "directory", "dangling", "bundle", "parent"):
                with self.subTest(side=side, kind=kind):
                    self.setUp()
                    self.write(self.source, PROMPT, "SKILL.md", "Upstream change\n")
                    self.commit(self.source)
                    repository = getattr(self, side)
                    outside = self.workspace / "outside"
                    outside.mkdir()
                    (outside / "notes.md").write_text("Outside content\n")
                    if kind == "bundle":
                        path = self.bundle(repository)
                        shutil.rmtree(path)
                        shutil.copytree(self.bundle(getattr(
                            self, "destination" if side == "source" else "source",
                        )), outside / "bundle")
                        path.symlink_to(outside / "bundle", target_is_directory=True)
                    elif kind == "parent":
                        path = repository / ".agents/skills"
                        path.rename(outside / "skills")
                        path.symlink_to(outside / "skills", target_is_directory=True)
                    else:
                        path = self.bundle(repository) / "linked"
                        target = {
                            "file": outside / "notes.md",
                            "directory": outside,
                            "dangling": outside / "missing.md",
                        }[kind]
                        path.symlink_to(target, target_is_directory=kind == "directory")
                    self.commit(repository)
                    before = self.snapshot(self.destination)
                    result = self.sync(skills=(PROMPT, LOCATION))
                    code = None if side == "destination" and kind == "parent" else 1
                    self.assert_refused_without_writes(result, before, code)
                    if code is not None:
                        self.assertIn("symlink", (result.stdout + result.stderr).lower())
                    self.assertEqual((outside / "notes.md").read_text(), "Outside content\n")

    def test_file_directory_type_conflict_is_rejected_before_any_copy(self):
        self.write(self.source, LOCATION, "references/rules.md", "New rules\n")
        self.write(self.destination, LOCATION, "references", "Local flat file\n")
        self.write(self.source, PROMPT, "SKILL.md", "New prompt rules\n")
        self.commit(self.source)
        self.commit(self.destination)
        before = self.snapshot(self.destination)
        self.assert_refused_without_writes(
            self.sync(skills=(PROMPT, LOCATION)), before,
        )

    def test_missing_later_bundle_prevents_earlier_copy(self):
        self.write(self.source, PROMPT, "SKILL.md", "Upstream change\n")
        shutil.rmtree(self.bundle(self.source))
        self.commit(self.source)
        before = self.snapshot(self.destination)
        self.assert_refused_without_writes(
            self.sync(skills=(PROMPT, LOCATION)), before, 1,
        )

    def test_rsync_preview_failure_does_not_modify_any_bundle(self):
        self.write(self.source, PROMPT, "SKILL.md", "Upstream change\n")
        self.commit(self.source)
        binaries = self.workspace / "bin"
        binaries.mkdir()
        rsync = binaries / "rsync"
        rsync.write_text("#!/bin/sh\nexit 23\n")
        rsync.chmod(0o755)
        before = self.snapshot(self.destination)
        result = self.sync(
            skills=(PROMPT, LOCATION),
            PATH=f"{binaries}{os.pathsep}{self.environment['PATH']}",
        )
        self.assert_refused_without_writes(result, before)

    def test_later_rsync_preview_failure_prevents_earlier_copy(self):
        self.write(self.source, PROMPT, "SKILL.md", "Upstream change\n")
        self.commit(self.source)
        binaries = self.workspace / "bin"
        binaries.mkdir()
        rsync = binaries / "rsync"
        real_rsync = shutil.which("rsync")
        self.assertIsNotNone(real_rsync)
        rsync.write_text(
            "#!/bin/sh\n"
            "case \"$*\" in\n"
            "  *seedream-location-asset*) exit 23 ;;\n"
            "esac\n"
            f"exec '{real_rsync}' \"$@\"\n"
        )
        rsync.chmod(0o755)
        before = self.snapshot(self.destination)
        result = self.sync(
            skills=(PROMPT, LOCATION),
            PATH=f"{binaries}{os.pathsep}{self.environment['PATH']}",
        )
        self.assert_refused_without_writes(result, before)

    def test_unsupported_source_file_type_blocks_all_selected_copies(self):
        self.write(self.source, PROMPT, "SKILL.md", "Upstream change\n")
        self.commit(self.source)
        os.mkfifo(self.bundle(self.source) / "unsupported-pipe")
        before = self.snapshot(self.destination)
        result = self.sync(skills=(PROMPT, LOCATION), SYNC_ALLOW_DIRTY="1")
        self.assert_refused_without_writes(result, before, 1)
        self.assertIn("unsupported file type", result.stderr)

    def test_source_revision_failure_stops_before_copying(self):
        self.write(self.source, LOCATION, "SKILL.md", "Upstream change\n")
        (self.source / ".git").rename(self.workspace / "detached-source-git")
        before = self.snapshot(self.destination)
        self.assert_refused_without_writes(self.sync(), before, 1)

    def test_empty_destination_only_directory_in_clean_checkout_is_preserved(self):
        (self.bundle(self.destination) / "local-empty").mkdir()
        self.assertEqual(self.git(self.destination, "status", "--porcelain"), "")
        before = self.snapshot(self.destination)
        self.assert_refused_without_writes(self.sync(), before, 6)

    def test_non_allowlisted_fork_is_rejected_without_writes(self):
        before = self.snapshot(self.destination)
        self.assert_refused_without_writes(
            self.sync(skills=("seedream-storyboard",)), before, 1,
        )

    def test_forbidden_upstream_references_still_require_scrubbing(self):
        self.write(self.source, LOCATION, "SKILL.md", "Calls `seed_understand`\n")
        self.commit(self.source)
        result = self.sync()
        self.assertEqual(result.returncode, 4, result.stdout + result.stderr)
        self.assertIn("SCRUB REQUIRED", result.stderr)


if __name__ == "__main__":
    unittest.main()
