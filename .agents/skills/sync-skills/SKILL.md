---
name: sync-skills
description: >-
  Maintenance only: sync this repo's allowlisted prompt-composition skills
  from the upstream source checkout and leave the changes uncommitted for
  review. Run only on explicit request (/sync-skills in Claude Code and
  opencode, $sync-skills in Codex).
argument-hint: "[all | skill-name ...]"
disable-model-invocation: true
---

# Sync skills from the upstream source

Mirror the allowlisted skill bundles from the upstream checkout into this
repo. Never commit — leave all changes for review. This is the single source
for the procedure; Claude Code, Codex and opencode all run it.

## Scope

The allowlist lives in [scripts/sync.sh](scripts/sync.sh) — 25 skills. Never
sync:

- `template-factory` and `seed-audio-commercial` — deliberate local forks
  whose content diverges upstream.
- `filipino-micro-drama` and `seedream-prop-asset` — prompt-only local forks
  of upstream skills, with generation and orchestrator references removed.
- `sync-skills` — this maintenance skill is local.
- Everything under `.agents/contracts/` — locally maintained variants.
- Every skill not on the allowlist.

## Arguments

The skill names given with the invocation, space-separated, or `all`. Names
must be on the allowlist. None or `all` syncs the full allowlist.

## Procedure

Run the scripts from the repo root. Each script is self-contained, so no
shell state has to carry between commands.

### 1. Plan

```bash
bash .agents/skills/sync-skills/scripts/sync.sh plan <names or all>
```

It checks the source (default `../ark-director`, overridden by
`SKILLS_SOURCE`), prints the source revision and this repo's working-tree
changes, validates the names, checks the source scope, and lists which skills
would change. It copies nothing.

- **Exit 1** — stop and report the error. Never sync from another path
  unless the user sets `SKILLS_SOURCE`.
- **Exit 3** — dirty source paths intersect the sync scope; the sync would
  copy unreviewed upstream work. The plan is still printed. List those paths
  and ask the user to confirm before applying.
- If this repo has uncommitted changes, warn that the sync diff will mix with
  them and recommend committing or stashing first.

The sync copies the source **working tree**, not its committed revision.

### 2. Apply

```bash
bash .agents/skills/sync-skills/scripts/sync.sh apply <names or all>
```

After the user confirmed a dirty scope, prefix `SYNC_ALLOW_DIRTY=1`.
`rsync --delete` mirrors each changed bundle, so renamed or removed reference
files disappear here too. The script never creates a skill directory and
never touches `.agents/contracts/`.

### 3. Verify

```bash
python3 .agents/skills/sync-skills/scripts/verify.py
```

It checks that frontmatter names match their directories, that relative
Markdown links resolve, and that no `.DS_Store` or `__pycache__` sits under
`.agents/`. Report every problem it lists.

### 4. Report

Summarize as a table: skill | unchanged / updated | files that changed. Then
include:

- The source revision hash from the plan.
- `git status --short` and `git diff --stat` so the user can review the sync
  diff directly.
- If any synced `SKILL.md` changed its frontmatter description, list those
  skills and ask whether the README skill-table row should be updated. Do not
  rewrite README rows automatically — several rows are deliberately reworded
  for this prompt-only workspace.
- State that nothing was committed. If nothing changed, say so plainly.
