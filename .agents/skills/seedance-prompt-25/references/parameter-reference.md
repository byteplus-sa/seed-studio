# Parameter Reference

Focused reference for `seedance-prompt-25`. Read [the entrypoint](../SKILL.md) for
mode selection and caller responsibilities.

- [Quick reference card](#quick-reference-card)
- [Native draft first](#native-draft-first)
- [Guide disclaimer](#guide-disclaimer)

## Quick reference card

These tables are a versioned snapshot, not live capability evidence. Verify
the exact model, provider, operation, transport, tool schema revision and
explicit validity interval independently against the intended destination.
Evidence includes supported roles, per-modality and total reference limits,
self-contained parameter schemas and conditional constraints. Unknown support
is unresolved, not false or a default copied from a related model.
Studio defines no runtime profile adapter or production catalog.

### Model IDs

| Variant | Model ID |
|---|---|
| Seedance 2.5 | `dreamina-seedance-2-5-260628` |
| Seedance 2.0 Standard (legacy) | `dreamina-seedance-2-0-260128` |
| Seedance 2.0 Fast (legacy) | `dreamina-seedance-2-0-fast-260128` |
| Seedance 2.0 Mini (legacy) | `dreamina-seedance-2-0-mini-260615` |

**Submission boundary:** this workspace writes prompts only — the user pastes the prompt and the parameter block into the destination UI. Every parameter in this reference is a submission value, never prompt text.

> The model ID `dreamina-seedance-2-5-260628` is live on BytePlus ModelArk. Confirm the current ID on the [Model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) before finalizing the parameter block.

### Reference limits

| Material | Max | Recommended |
|---|---|---|
| Images | 30 (each ≤ 4K) | 1–8 subjects |
| Videos | 10 (combined ≤ 30s) | 1–5 subjects, 5–10s each |
| Audio | 10 (combined ≤ 30s) | Only what's directly relevant |
| **Total** | **50** | — |

### Audio syntax

| Content | Syntax |
|---|---|
| Music | `()` |
| Sound Effects | `<>` |
| Dialogue | `{}` |
| Subtitles | `【】` |

### Parameter auto-lock summary

| Task | Aspect Ratio | Duration |
|---|---|---|
| Video editing | Locked to input | Locked to ~input (±0.3s) |
| First/last-frame | Locked to first image | Settable |
| Video extension | Locked to input | Settable |

### Camera techniques

| Technique | What to Specify |
|---|---|
| One-take shot | Subjects, spaces, events in order |
| Dolly zoom | Subject size; bg closer or farther |
| Aerial view | Height, direction, area to reveal |
| FPV | Flight path, speed, turns |
| Bullet time | Action to freeze; orbit direction |
| Handheld camera | Subject; amount of shake |
| Bounce speed ramp | Acceleration/deceleration points; final state |

### Reproducibility
- `seed`: use only if the destination exposes it. The upstream 2.5 client checked on 2026-10-06 did not; reuse the approved prompt and references without promising identical output.
- `camera_fixed`: do not assume the destination exposes it. The upstream 2.5 client checked on 2026-10-06 did not; state the locked camera in the prompt.
- `return_last_frame`: set to `true` to chain multi-shot continuity.

### Output duration
- 4–30s per generation (up from 4–15s in 2.0).
- Output resolution: 480p, 720p, or 1080p. For 4K output, use legacy Seedance 2.0 via `seedance-prompt-20`, or whitelist-only 2.5 Premium only when the caller confirms access and support in the destination.
- Multi-round extensions up to 180s (beta).

### Cost ladder
- For previously covered exact standard 2.5 and access-confirmed Premium
  bindings, start with `resolution: "480p"` and boolean `draft: true`, then
  promote the selected native draft. New bindings follow the verified profile
  under [Native draft first](#native-draft-first), not this historical ladder.
- Video generation is billed per successful task completion.
- Cost information is optional; consult the [Pricing page](https://docs.byteplus.com/en/docs/ModelArk/1544106)
  when reporting current billing, not as a prerequisite for prompt delivery or
  a confirmed submit.

### When to use Seedance 2.0 instead of 2.5

Offer `seedance-prompt-20` and the 2.0 model as unselected alternatives when:

- You need **4K output resolution** — standard 2.5 caps at 1080p; whitelist-only 2.5 Premium is a separate access-dependent option.
- You need **Fast or Mini speed variants** — 2.5 has no Fast/Mini; 2.0 Fast/Mini are cheaper and faster for prototyping.
- You need the lowest possible cost per generation for quick iteration.

### Languages
- 10+ languages supported natively: Chinese, English, Spanish, Indonesian, Malay, Thai, Arabic, Portuguese, Vietnamese, Japanese, Korean.
- For non-Chinese dialogue, use the dialogue language reinforcement formula.
- For **Tagalog/Filipino or Taglish** (not in the supported list), compose with the partner skill `seedance-prompt-25-filipino` for pronunciation, intonation, and audio-first pipeline guidance.

### Consistency rules
- Lock character sheets, prop sheets, and scene sheets with Seedream before spending video credits.
- Storyboarding is optional. Generate storyboard panels from approved assets when composition must be reviewed before motion; otherwise generate video directly from canonical Element references (R2V) or text-to-video.
- Reuse the same reference bundle across every shot in a scene.
- Preserve a written locked-decisions and requested-delta record for every retry.
- Change only one of {prompt wording, reference bundle, motion design} per retry when practical.

### Storyboard-to-video handoff

Storyboards are optional and planning-only. Storyboard grids, panels, crops and
animatics never become video conditioning inputs, including first/last-frame,
R2V and motion roles. Translate their staging and continuity into text.
Selection, current hashes, mode support, style overrides and promotion labels
do not change planning origin. Character, location and prop sheets remain
the source of truth. An independent production still must be independently
authored, selected and text-free, not a cropped, cleaned or renamed board panel.

| Need | Mode | Reference rule |
|---|---|---|
| Use an approved opening still | First-frame | Submit only an independently authored, selected text-free production still with verified role support |
| Lock approved start and end states | First + last frame | Submit only two eligible independent production stills, one role per image, with matching ratios |
| Follow storyboard staging while preserving explicit references | R2V | Translate board staging into text; submit only eligible canonical assets and independent production stills |
| Generate video without a storyboard | R2V or T2V | Submit canonical Element references only (R2V) or text-only prompt (T2V) |

For supported R2V, index eligible independent stills and canonical assets separately:

```text
@Image 1: independently authored production still — selected composition and visible state
@Image 2: approved character sheet — identity and wardrobe only
@Image 3: approved location sheet — geometry and production design only
@Image 4: approved prop sheet — shape, materials, and markings only
```

These modes are mutually exclusive. Do not combine first/last-frame roles with
an R2V bundle unless the live model explicitly confirms that combination. Record
the chosen mode, ordered reference roles, paths, hashes, selected variants, and
approval states in the shot manifest before submission.
Preserve historical board-linked task identities, hashes and selection records;
they are history, not eligibility for a new request.

## Native draft first

For the previously covered exact standard 2.5 and access-confirmed Premium bindings,
every new generation, including edits, extensions and creative
retries, starts with explicit `resolution: "480p"` and boolean `draft: true`.
Keep these controls in the destination parameter block, not prompt text.
Review depth does not change this rule. A requested 720p or 1080p final is a
delivery target, not permission to skip the native draft.

The caller inspects and selects the successful draft, retains its provider
task ID, then requests promotion with `draft_task_id` and supported output
settings. The final is separately paid and inspected. Do not resend or change
prompt text, references, duration, ratio or audio parameters in promotion.
Changing any creative input requires a new native draft first.

Promotion also requires the exact selected successful native task, unchanged
reference hashes and creative inputs, matching exact model, operation, transport
and profile, evidence still within expiry, and final inspection. Do not turn a
historical ordinary task into native Draft by changing metadata or a profile.
Failed, unselected, expired or mismatched tasks are not promotable.

A plain 480p output is not a native draft and cannot be promoted by naming its
task ID. If a previously covered exact binding's UI/tool does not expose native draft mode,
resolve the capability mismatch before submission rather than dropping
`draft: true`. Do not invent a control the interface cannot accept.
For a new exact model, including a 2.5 variant outside the previously covered set,
use its verified operation profile only, independently bound to provider,
transport, tool schema revision and validity. New native operations use their
evidenced native controls. A verified non-native operation uses an ordinary
preview at the evidenced resolution, even when 480p is also supported,
clearly non-promotable, and a separately confirmed fresh generation for the final. Do not force
480p or infer native Draft from a model-name substring. Unknown preview or
promotion support blocks execution, not prompt-only creative writing.
Missing, malformed, expired or wrong-destination evidence remains unresolved;
do not invent parameters or silently drop `draft` to resolve a conflict.

## Guide disclaimer

The examples in this skill illustrate prompt-writing techniques only. Actual
generation results may vary depending on the input materials, task complexity,
and generation parameters.
