# AGENTS.md — seed-prompt-studio

Prompt-first workspace for composing Lumina-paste-ready prompts for BytePlus
Seed-family models (Seedance, Seedream, Seed Audio). It writes prompts; review
is a manual `/prompt-review` the user runs. Generation and media production
are optional when requested or necessary to complete a user-authorized
deliverable with available tools.

## Scope and authority

This workspace produces copy-paste prompt blocks. By default the user pastes
them into Lumina or another Seed-model UI, where generation happens. When the
user requests generation or a deliverable requiring generated Seed media,
and a usable `ark-mcp` or `arkcli` is
connected, follow [Generation transport](.agents/contracts/generation-transport.md):
show the exact prompt, confirm each submit, use one transport per job. With neither
connected, stay prompt-only and say so. The workspace never assumes, configures,
or stores generation credentials.

Within the authorized task, agents may generate media, download references
and results, prepare audio/video inputs, trim, mux, concatenate, assemble,
transcode, and export deliverables using available tools, including local
`ffmpeg`/`ffprobe`. Save outputs to the user's requested destination, including
Desktop when requested. Preserve source assets and existing takes; do not
overwrite unrelated files. These permissions override prompt-only,
analysis-only, and destination-workflow-only restrictions in linked contracts
and skills for these operations. Other generation approval, reference,
security, and verification requirements still apply. Unrelated 3D, Blender,
and deterministic graphics workflows remain out of scope.

Deliver prompts in chat by default. Save a draft under
`projects/<name>/prompts/` only when the user explicitly asks.

Task scope does not expand into unrelated global configuration, external
publishing, or production edits. Keep project-specific instructions in
`.agents/`. Do not create a second competing `.agents/AGENTS.md`.

Before editing, inspect relevant files, plans and existing Git changes. Never
revert, overwrite or clean up work you did not create for this task. Ask for
missing information when it materially affects the intended result.

## Operational contracts

Load only the contract relevant to the current request:

| Need | Tracked source |
| --- | --- |
| Manual `/prompt-review` policy and stable rule IDs | [rules.json](.agents/contracts/rules.json) and [production policy](.agents/contracts/production-policy.md) |
| Requested camera, lens, lighting, grade, acting, pacing, blocking, medium axes | [Directorial axes](.agents/contracts/seedance-reference.md) |
| Canon, props, screens and reference roles | [Element identification](.agents/contracts/element-identification.md) |
| Dialogue synchronization and assembly | [Audio-video alignment](.agents/contracts/audio-video-alignment.md) |
| Source footage, Virtual Portrait identities, muted master and post audio for swap, recast and restyle | [Video-to-video inputs](.agents/contracts/video-to-video-inputs.md) |
| Explicit request to generate or submit a prompt | [Generation transport](.agents/contracts/generation-transport.md) |

## Routing

Compose only the axes the user requested. One grade, one dominant lighting
direction, and one or two camera moves per clip unless the explicitly
requested choreography needs more.

| Intent | Route |
| --- | --- |
| Brief shaping | `brief-intake` |
| Reference-video reverse engineering (breakdown → element, storyboard, Seedance prompts) | `template-factory` |
| Storyboard panel and grid prompts | `seedream-storyboard` |
| Motion recast of a source clip (new cast and world, same motion) | `seedance-motion-recast` |
| Object swap in existing footage (one character, outfit, product, prop or location) | `seedance-object-swap` |
| Restyle a whole clip into a new visual medium (same cast, place and motion) | `seedance-restyle` |
| Seedance 2.5 prompt grammar | `seedance-prompt-25` |
| Seedance 2.0 / 4K legacy grammar | `seedance-prompt-20` |
| Filipino/Tagalog dialogue direction | `seedance-prompt-25-filipino` |
| Filipino micro-drama stories and episode briefs | `filipino-micro-drama` |
| Acting direction and emotional intensity | `seedance-acting-console` |
| Camera / lens / lighting / pacing presets | `seedance-camera-presets`, `seedance-lens-presets`, `seedance-lighting-presets`, `seedance-pacing-presets` |
| Frame-break pop-out effect (subject bursts over black bars, 3D billboard look) | `seedance-frame-break` |
| Animation styles / Blender-video edit prompts | `seedance-animation-styles`, `seedance-graybox-world` |
| Motion design / music video / restoration / VFX edit prompts | `seedance-motion-design`, `seedance-music-video`, `seedance-restoration`, `seedance-vfx-prompt` |
| Seedream image prompts, character sheets, location plates, prop sheets | `seedream-prompt`, `seedream-character-sheet`, `seedream-location-asset`, `seedream-prop-asset` |
| Seedream edit prompt that leaves one readable face on a character sheet | `seedream-character-sheet-cleanup` |
| Seed Audio prompts | `seed-audio-prompt` |
| Audio commercial prompts (story arc, cast, tagline) | `seed-audio-commercial` |
| UGC ad modes / UGC motion presets | `ugc-ad-modes`, `ugc-motion-presets` |
| Color grade sentence | `color-grade-palettes` |
| Scene structure / staging references | `tig-scene-engine`, `tig-blocking-map` |
| Prompt QA (manual; only when the user runs `/prompt-review`) | `prompt-review` |

## Skills and orchestration

One skill provides one capability. Leaf skills remain independently usable;
composition hints are prose, not directives to load siblings. Load only the
specialists needed for the current request. `template-factory` is this
workspace's declared orchestrator for reference-video reverse engineering; it
sequences the prompt leaves.

This workspace ships prompt-composition skills only, plus the maintenance-only
`sync-skills` skill, which runs on explicit request. Generation is a transport
contract, not a skill: it uses the user's connected `ark-mcp` or `arkcli`.
Prompt leaves and `template-factory` produce prompts; the calling agent owns
authorized submission and media production. No installed media-processing
skill is required to use available tools for the operations permitted above.
Recipes such as muxing a song onto a video may be executed by the agent when
needed for the authorized deliverable; otherwise deliver them as instructions.
Do not assume unavailable tools or expand into unrelated production work.

Prompt QA is optional and user-triggered. `prompt-review` runs only when the
user invokes `/prompt-review`; no prompt-writing skill or workflow runs, loads,
or waits on it.

Keep skill metadata concise and valid YAML. Move substantial conditional
modes and examples into focused same-skill references.

## Prompt invariants

- Never run `prompt-review` or spawn a review sub-agent on your own. Review
  happens only when the user invokes `/prompt-review`; it never gates handoff
  or generation, and no skill or contract may require it or name it as a step.
- Freeze the exact prompt text before handoff. A generation submit must match
  the prompt the user saw byte for byte.
- Source video is inspected by an agent video pass when the client can watch
  it, or by local `ffmpeg`/`ffprobe` frame extraction read as images when it
  cannot; never claim to have watched footage you could not access.
- Preserve exact canonical descriptors where applicable. Prefer positive,
  observable direction; necessary edit-scope exclusions are allowed.
- Identify all visible props; only threshold-qualified props need locked
  references. Incidental generic props may be described.
- Do not bake captions, taglines, CTAs, end cards or other overlay text into
  prompts; on-screen text is added in post by the destination workflow.
- Static sheets use visible-design criteria; narrative shots need action and
  intent; audio uses its requested sound arc. Do not apply narrative tactics
  to every static sheet.
- Moderation rejection is evidence to diagnose, not proof of a false
  positive. Revisions remain legitimate and authorized.
- Exact-copy, typography, logo, UI, and deterministic HTML/CSS/SVG work is
  out of scope; say so rather than improvising a prompt.

## Local state and naming

`projects/<project-name>/` holds durable local drafts, never a default Git
staging target.

| Location | Contents |
| --- | --- |
| `projects/<project>/project.md` | Optional brief and confirmed choices |
| `projects/<project>/prompts/prompt_<asset-stem>.md` | Saved prompt drafts, immutable after handoff |
| `projects/<project>/elements/<element-id>/` | Optional element prompt records and acquired-asset provenance |
| `projects/<project>/generations/<asset-stem>.md` | Optional generation provenance record, saved on request; no signed URLs |
| `projects/<project>/frames/` | Analysis-only frame-extraction scratch; never a deliverable |

Folders and IDs use lowercase kebab-case. Prompt snapshots are saved only on
explicit request; chat-only is the default.

## Security and change boundaries

No credentials belong in this workspace; prompts and drafts contain no
secrets, signed URLs, or account data. Never output or commit credentials.

Never commit or push repository changes unless requested. When authorized,
stage only task-owned files. Clean up only your own temporary artifacts;
never revert or discard work you did not create.

## Verification

Prompt QA is optional: the user runs `/prompt-review` when they want it. For
repository changes run `git diff --check`; this workspace ships no code, so
unit, lint, type, and build checks are not applicable.

For produced media, verify output existence, audio/video streams, dimensions,
duration, and full decode integrity before delivery. When exact original audio
is required, preserve it without re-encoding where supported and verify audio
payload or decoded-sample equality. Technical checks do not establish visual
quality or lip sync; distinguish sampled-frame inspection from playback review.

Shared skills are maintained in an upstream source checkout and pulled in with
`/sync-skills` in Claude Code or opencode, or `$sync-skills` in Codex (see README
Maintenance). The command never overwrites the local `template-factory`,
`seed-audio-commercial`, `filipino-micro-drama`, `seedream-prop-asset`,
`seedream-storyboard`, `seedream-character-sheet-cleanup`,
`seedance-motion-recast`, `seedance-object-swap`, `seedance-restyle`,
`seedance-frame-break`, `seedance-graybox-world`, and `seedance-music-video`
forks and leaves its changes uncommitted for review.
