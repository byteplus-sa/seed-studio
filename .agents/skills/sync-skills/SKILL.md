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
- `filipino-micro-drama`, `seedream-prop-asset`, `seedream-storyboard`,
  `seedream-character-sheet-cleanup`, `seedance-motion-recast`, and
  `seedance-frame-break` — prompt-only local forks of upstream skills, with
  generation and orchestrator references removed.
- `sync-skills` — this maintenance skill is local.
- Everything under `.agents/contracts/` — locally maintained variants.
- Every skill not on the allowlist.

## What a sync keeps and what it brings back

A sync copies upstream wording verbatim, and upstream is not prompt-only.

- **Kept automatically:** each skill's `agents/` folder is never copied or
  deleted, so local-only `agents/` folders and local policy edits such as
  `policy: allow_implicit_invocation: false` in `prompt-review/agents/openai.yaml`
  survive.
- **Caught automatically:** references to tools and skills this workspace does
  not ship (`ark-mcp`, `showcase-html`, MCP tool names, `seed_understand`,
  deleted-skill names, upstream scripts), and code files inside a skill. The
  names live in [scripts/forbidden-refs.txt](scripts/forbidden-refs.txt);
  `plan` previews the count per skill, `apply` exits 4 until they are scrubbed,
  and `verify.py` fails on any that remain. Add a line to that file when
  upstream gains a skill or tool that should stay out.
- **Restore by hand:** local edits the scan cannot see, listed below.

## Local edits to re-apply after a sync

Prompt review is manual and isolated in this workspace, so a sync can
reintroduce review wording that was removed locally. After applying, check
the diff and restore these:

- `prompt-review`: `disable-model-invocation: true` in `SKILL.md` and the
  "Manual review (/prompt-review)" description and "When to trigger" section.
  Also remove upstream's `scripts/` folder and its references: this workspace
  ships no code in skills.
- `seedance-prompt-25`, `seedance-vfx-prompt`, `seedance-music-video`,
  `seedream-prompt`, `seed-audio-prompt`: the "Submission boundary" paragraph
  must not mention a "hash-bound prompt review" or a review stage, and the
  `seedance-music-video` description must not say the caller "owns review".
- `seedance-prompt-25-filipino`: the caller-ownership sentence must not say
  "complete prompt review".
- Any other synced skill that gains a `prompt-review` reference: remove it.
  Only the `prompt-review` skill itself may name `prompt-review`.

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
- A "would bring in N reference(s)" line under a skill means upstream's copy
  of it mentions tools or skills this workspace does not ship. Tell the user
  how many skills are affected, and expect to scrub them after applying.
- If this repo has uncommitted changes, warn that the sync diff will mix with
  them and recommend committing or stashing first.

The sync copies the source **working tree**, not its committed revision.

### 2. Apply

```bash
bash .agents/skills/sync-skills/scripts/sync.sh apply <names or all>
```

After the user confirmed a dirty scope, prefix `SYNC_ALLOW_DIRTY=1`.
`rsync --delete` mirrors each changed bundle, so renamed or removed reference
files disappear here too, except each skill's `agents/` folder, which is left
alone. The script never creates a skill directory and never touches
`.agents/contracts/`.

After copying, `apply` scans the synced skills and lists every forbidden
reference as `file:line`. **Exit 4** means the sync is not finished: the copy is
in place but upstream wording leaked in. Do not report success.

### 2b. Scrub

For every `file:line` the scan listed, edit the skill so it is prompt-only
again: delete the reference, or reword the sentence so it describes the user's
paste-and-generate step instead of a tool call. Keep upstream's real content
changes (new rules, examples, grammar). Then restore the local edits listed
above. Delete any code file the scan flags rather than editing it.

### 3. Verify

```bash
python3 .agents/skills/sync-skills/scripts/verify.py
```

It checks that frontmatter names match their directories, that relative
Markdown links resolve, that no `.DS_Store` or `__pycache__` sits under
`.agents/`, and that no skill mentions a tool or skill this workspace does not
ship. It must report `forbidden references: 0` before the sync is done. Report
every problem it lists, and repeat step 2b until it is clean.

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
- How many forbidden references the scan found and that the scrub removed them
  (`verify.py` clean), and which local edits were restored.
- State that nothing was committed. If nothing changed, say so plainly.
