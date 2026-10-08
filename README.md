# seed-prompt-studio

> A prompt-first workspace for composing **Lumina-paste-ready prompts** for BytePlus / Volcano Engine Seed models — **Seedance** (video), **Seedream** (images), and **Seed Audio** (audio).

This repository ships agent skills, not generation tooling. You describe what you
want, the agent composes a production-grade prompt from the skill libraries and
hands you a copy-paste block for the Lumina UI. Want a second opinion? Run
`/prompt-review` yourself; the agent never runs it on its own.

Generation is optional. If you have `ark-mcp` or `arkcli` connected and explicitly
ask the agent to generate, it submits the prompt you saw through that transport
after you confirm the model, references, and cost. Without either connected, or
without that request, it stays prompt-only. The agent never stores credentials or
writes production files. See
[`generation-transport.md`](.agents/contracts/generation-transport.md).

## What this is / is not

| This repo **is** | This repo **is not** |
|---|---|
| Prompt composition skills for Seed-family models | A generation pipeline — you paste prompts into the destination UI, or opt in to a confirmed submit through your own `ark-mcp` / `arkcli` |
| An optional, user-invoked review (`/prompt-review`) | A renderer — static and motion graphics are out of scope |
| Chat-first delivery of paste-ready prompt blocks | A 3D or assembly tool — 3D, compositing, and editing are out of scope |
| Optional local prompt drafts under `projects/` | A production canvas — no stage machinery, no task registry |

## How it works

```mermaid
flowchart LR
  A[Brief or directed request] --> B[Prompt skill composition]
  B --> D[Copy-paste block in chat]
  D --> E[Paste into Lumina]
  D -.->|you run it, optional| C[/prompt-review/]
  D -.->|on request| F[(projects/&lt;name&gt;/prompts/)]
  D -.->|on request, ark-mcp or arkcli connected| G[Confirm, then submit]
```

1. The agent routes your request to the relevant skill (grammar, presets,
   dialogue, acting, sheets, audio) and composes the prompt.
2. You receive one copy-paste block — prompt text, ordered reference bindings,
   and the parameter block. Paste it into Lumina.
3. Optionally, run `/prompt-review` to check a prompt against the workspace rule
   catalog. It is manual only and nothing else depends on it.
4. Drafts are saved locally only when you ask for them.

## Skills

| Skill | Summary |
| --- | --- |
| **brief-intake** | Shape intent-led briefs and treatments; preserve confirmed decisions. |
| **prompt-review** | Manual (`/prompt-review`) review and fix of prompts written for BytePlus generative models (Seedance, Seed Audio, Seedream) against the repo's skill best practices using a sub-agent review pipeline. |
| **template-factory** | Reverse-engineer a reference video into a prompt package: structured breakdown, Seedream element prompts (characters, locations, props), storyboard prompts, and Seedance 2.5 video prompts — paste-ready. |
| **seedance-prompt-25** | Write production-grade Seedance 2.5 video prompts with the six-part formula, 50-material multimodal referencing, variable-duration staging (4-30s), timestamp pacing, structured editing, extension, keyframes, storyboards, and blockouts. |
| **seedance-motion-recast** | Write Seedance 2.5 motion-transfer prompts that keep a source clip's motion, camera, cuts and timing while rebuilding cast, wardrobe, product, location and style from references; per-subject mapping, guards, Virtual Portrait identities, a muted source with audio in post, and style presets. |
| **seedance-object-swap** | Write Seedance 2.5 object-swap prompts that replace one character, outfit, product, prop or location in existing footage and keep the rest as filmed: five-part swap contract, contact windows, Virtual Portrait identities, and swap checks. |
| **seedance-restyle** | Write Seedance 2.5 restyle prompts that redraw a whole clip in a new medium (anime, watercolor, claymation, pixel art and more) while keeping its performance, camera and cuts; style catalog, same-place environment image, and restyle checks. |
| **seedance-prompt-25-filipino** | Write Filipino and Taglish dialogue direction while preserving exact words and register; evidence-based pronunciation hypotheses and opt-in lip-sync audio. |
| **filipino-micro-drama** | Write Filipino-market micro-drama episode briefs: proven Pinoy formulas, hook/reveal/cliffhanger beats, light cast, authentic settings, and English-dominant Taglish dialogue with subtitle translations. Story material only. |
| **seedance-prompt-20** | Legacy Seedance 2.0 prompt skill for 4K output (unsupported by 2.5), Fast/Mini speed variants, or lower cost per generation. |
| **seedance-acting-console** | Turn playable motives and tactics into observable acting cues appropriate to framing, visibility and intensity. |
| **seedance-animation-styles** | Write Seedance animation prompts for claymation, needle felt, wood puppets, toy miniatures, rubber hose, painterly 2D, cubist ink, stylized 3D, silicone creatures, and wax crayon. |
| **seedance-frame-break** | Write Seedance 2.5 frame-break pop-out prompts: two fixed black bars with the subject's limbs drawn over them, four timed break-out stages, product-hero variant, failure repairs, and a user-run acceptance check. |
| **seedance-camera-presets** | Turn a named camera move (dolly, pan, orbit, crane, tracking, handheld, FPV, aerial, bullet time, dolly zoom, whip pan, one-take, static) into a drop-in Camera block. |
| **seedance-graybox-world** | Write Seedance edit prompts for Blender-rendered videos (playblasts, graybox/previz, finished renders); change appearance while preserving Blender's motion, camera, and timing. |
| **seedance-lens-presets** | Translate a lens, focal length, aperture, or sensor request into a canonical visible-result phrase for Seedance prompts or Seedream style. |
| **seedance-lighting-presets** | Translate a named lighting setup into a canonical Seedream `Lighting:` recipe and a matching Seedance visual-style lighting phrase. |
| **seedance-pacing-presets** | Turn a named pacing preset (speed ramp, slow motion, bullet time, montage, cut rhythm, impact moment) into a timestamped motion, cut, and pacing block. |
| **seedance-motion-design** | Write Seedance 2.5 motion-design prompts for marketing deliverables; exact typography and UI are out of scope in this workspace. |
| **seedance-music-video** | Develop track-informed music-video treatments with intentional escalation, restraint, repetition or counterpoint and optional evidence-based synchronization. |
| **seedance-restoration** | Write Seedance video-to-video restoration prompts that remove grain, noise, scratch lines, dust, and flicker from aged footage while preserving the shot. |
| **seedance-vfx-prompt** | Write structured video-to-video VFX prompts with the `@Video N` / `@Image N` reference grammar, VFX taxonomy, relighting, layered space, and timing triggers. |
| **seedream-prompt** | Write Seedream prompts for synthesized or edited imagery; exact typography, pricing, CTA, product grids, and logos are out of scope in this workspace. |
| **seedream-character-sheet** | Write structured Seedream prompts for three-panel character sheets and identity references — the face anchors Seedance uses. |
| **seedream-character-sheet-cleanup** | Write a Seedream edit prompt that removes the head from the full-body panels so the close-up is the only readable face; non-destructive, with an acceptance checklist. |
| **seedream-location-asset** | Write structured Seedream prompts for cinematic location assets and reusable environment sheets. |
| **seedream-storyboard** | Write Seedream storyboard prompts from one hero panel to a multi-panel continuity board: sketch-default single-image grid or separate images, element binding, geometry and continuity contract, revision prompts. |
| **seedream-prop-asset** | Write structured Seedream prompts for prop and product identity sheets: prop threshold, acquisition-first order, hero or multi-view layout, neutral background, one canonical state. |
| **seed-audio-prompt** | Write structured Seed Audio 1.0 prompts for full-soundscape audio generation including dialogue, music, SFX, and ambience. |
| **seed-audio-commercial** | Compose dramatic, story-driven audio commercial prompts with a five-act arc, multi-character voice profiles, and commercial SFX/music patterns. |
| **ugc-ad-modes** | Write hooks, scripts and Seedance prompts for nine ad modes using supplied product facts, audience objections, supported claims and accurate CTAs. |
| **ugc-motion-presets** | Turn a named UGC motion preset (Atomic, Outfit Switch, Eating Zoom, Yacht, ...) into a canonical Seedance prompt block with reference bindings, duration, and constraint flags. |
| **color-grade-palettes** | Map a named color grade palette or film look into a canonical grade sentence for the Seedance Visual Style slot or the Seedream `Style:` section. |
| **tig-blocking-map** | Give Seedance characters DISPOSITION via a color-coded outline schematic — a staging reference for multi-character blocking. |
| **tig-scene-engine** | Write and audit screenplay scenes using a five-element dramatic engine — Goal, Obstacle, Tactic, Reversal, Value Shift. |

## Contracts

| Need | Source |
| --- | --- |
| Prompt review policy and stable rule IDs | [`.agents/contracts/rules.json`](.agents/contracts/rules.json), [`.agents/contracts/production-policy.md`](.agents/contracts/production-policy.md) |
| Camera, lens, lighting, grade, acting, pacing, blocking, medium axes | [`.agents/contracts/seedance-reference.md`](.agents/contracts/seedance-reference.md) |
| Canon, props, screens and reference roles | [`.agents/contracts/element-identification.md`](.agents/contracts/element-identification.md) |
| Dialogue synchronization and assembly | [`.agents/contracts/audio-video-alignment.md`](.agents/contracts/audio-video-alignment.md) |
| Source footage, Virtual Portrait identities, muted master and post audio for swap, recast and restyle | [`.agents/contracts/video-to-video-inputs.md`](.agents/contracts/video-to-video-inputs.md) |
| Optional generation via `ark-mcp` / `arkcli` | [`.agents/contracts/generation-transport.md`](.agents/contracts/generation-transport.md) |

## Repository structure

```
seed-prompt-studio/
├── AGENTS.md                       # workspace contract for agents
├── CLAUDE.md -> AGENTS.md          # symlink so Claude Code loads the same contract
├── .agents/
│   ├── contracts/                  # prompt-only policy, axes, descriptors, rule IDs
│   └── skills/                     # 35 prompt-composition skills + sync-skills (maintenance)
├── .claude/skills/<skill> -> ../../.agents/skills/<skill>   # per-skill symlinks for Claude Code
├── .opencode/command/
│   └── sync-skills.md              # opencode /sync-skills wrapper around the shared skill
└── projects/                       # local drafts (save-on-request; never a default Git staging target)
    └── <project-name>/
        ├── project.md              # optional brief
        └── prompts/                # saved prompt snapshots
```

## Maintenance

Shared skills are maintained in an upstream source checkout. Run the sync from
any supported agent to mirror the 23 allowlisted skill bundles into this repo:

| Agent | Command |
| --- | --- |
| Claude Code | `/sync-skills` |
| Codex | `$sync-skills` |
| opencode | `/sync-skills` |

All three run the same procedure in
[`.agents/skills/sync-skills/`](.agents/skills/sync-skills/SKILL.md), which only
runs when invoked explicitly. The local `template-factory`,
`seed-audio-commercial`, `filipino-micro-drama`, `seedream-prop-asset`,
`seedream-storyboard`, `seedream-character-sheet-cleanup`,
`seedance-motion-recast`, `seedance-object-swap`, `seedance-restyle`,
`seedance-frame-break`, `seedance-graybox-world`, and `seedance-music-video`
forks and all contracts are locally maintained and are never overwritten by a
sync. The command previews
changes, asks before copying unreviewed upstream work, and leaves the result
uncommitted for review. A scoped run — `/sync-skills seedance-prompt-25` — syncs
one skill only. A sync leaves each skill's `agents/` folder alone and scans the
result for references to tools and skills this workspace does not ship, stopping
until they are scrubbed. The sync source defaults to a sibling checkout at
`../ark-director` and can be relocated with `SKILLS_SOURCE`.
