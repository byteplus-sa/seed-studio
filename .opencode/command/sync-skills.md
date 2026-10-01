---
description: Sync prompt-composition skills from the upstream source checkout
agent: build
---

# Sync skills from the upstream source

Follow the procedure in
[.agents/skills/sync-skills/SKILL.md](../../.agents/skills/sync-skills/SKILL.md)
exactly, working from this repo's root. It is shared with Claude Code
(`/sync-skills`) and Codex (`$sync-skills`).

Arguments: `$ARGUMENTS` — optional space-separated skill names, or `all`.
Pass them to both `sync.sh plan` and `sync.sh apply`. Never commit — leave
all changes for review.
