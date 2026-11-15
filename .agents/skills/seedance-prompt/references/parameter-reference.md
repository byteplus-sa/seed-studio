# Parameter Reference

Focused reference for `seedance-prompt`. Read [the entrypoint](../SKILL.md) for
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

**Submission boundary:** this leaf does not generate, upload or submit. The
caller owns separately authorized execution; every parameter in this reference
is a submission value, never prompt text.

> The snapshot documents `dreamina-seedance-2-5-260628`; it is not a live
> availability check. Verify the selected ID against the
> [Model list](https://docs.byteplus.com/en/docs/ModelArk/1330310) without
> replacing an explicit model selection.

### Historical standard 2.5 reference limits

The following snapshot applies only to the documented standard 2.5 binding
above. It does not establish support for Premium, Flash, another operation or
another destination. Verify current limits and combinations before use.

| Material | Max | Recommended |
|---|---|---|
| Images | 30 (each ≤ 4K) | 1–8 subjects |
| Videos | 10 (combined ≤ 30s) | 1–5 subjects, 5–10s each |
| Audio | 10 (combined ≤ 30s) | Only what's directly relevant |
| **Total** | **50** | — |

### Audio syntax

These are 2.5 guide conventions, not universal parser tokens. Confirm the
selected destination accepts them; otherwise use plain language. Subtitle
notation is documented for context only: requested captions stay in post.

| Content | Syntax |
|---|---|
| Music | `()` |
| Sound Effects | `<>` |
| Dialogue | `{}` |
| Subtitles | `【】` |

### Historical standard 2.5 parameter auto-lock summary

| Task | Aspect Ratio | Duration |
|---|---|---|
| Video editing | Input-led; verify controls | Input-led; measure output drift |
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
- `return_last_frame`: use only with verified support for the selected exact
  model, operation and destination. A continuation also needs an eligible
  returned image and verified next-shot role compatibility.

### Historical output snapshot

The standard 2.5 documentation described 4-30s generation and 480p, 720p or
1080p output; multi-round extension up to 180s was beta. These are not a
creative default, a retiming rule or current evidence for another binding.
Preserve fractional source spans and audio tails. Any supported adaptation
uses a separate copy and requires agreement; never round or trim the original.

A locked 4K target or speed requirement does not select a different model.
Return missing exact-model support as unresolved. Any alternative stays
unselected until the caller obtains authorization and destination evidence.
Cost information is optional, not a prompt or submit prerequisite; consult
the [Pricing page](https://docs.byteplus.com/en/docs/ModelArk/1544106) when requested.

### Languages

Keep the requested language, register and exact approved dialogue. A language
list in an older guide does not verify native voice or lip-sync support for
the selected model, operation and destination. Unknown support is unresolved,
not a mandate for separate audio or model substitution.
For requested Tagalog/Filipino or Taglish guidance, the caller may compose the
`seedance-prompt-25-filipino` specialist; this leaf does not load it.

### Consistency rules
- Preserve selected references and canonical descriptors. Missing assets stay
  unresolved slots; asset creation is not a prerequisite for prompt-only text.
- Storyboarding is optional and planning-only. The caller owns any separately
  requested preparation; this leaf does not generate planning or production assets.
- Reuse stable reference authority across shots, binding only relevant assets.
- Keep locked decisions, requested delta and acceptance criteria in chat.
  Save a record only when requested; a revision does not authorize a retry.
- Change only one of {prompt wording, reference bundle, motion design} per retry when practical.

### Storyboard-to-video handoff

Storyboards are optional and planning-only. Storyboard grids, panels, crops and
animatics never become video conditioning inputs, including first/last-frame,
R2V and motion roles. Translate their staging and continuity into text.
Crop, cleanup, approval, selection, current hashes, mode support, style overrides,
promotion labels and board-derived regeneration do not change planning origin.
Character, location and prop sheets remain
the source of truth. An independent production still must be independently
authored, selected and text-free, not a cropped, cleaned or renamed board panel.
Independently authored, selected, text-free non-board production stills and
independent animated blockouts require verified exact model, operation,
transport and role support, rights, consent where applicable, current canonical
hashes, source lineage and artifact-specific QA. Independent blockouts are
animated geometry, not storyboard animatics; inspect motion separately from
appearance. A standalone image regenerated from a panel prompt remains
board-derived.

| Need | Mode | Reference rule |
|---|---|---|
| Use an approved opening still | First-frame | Submit only an independently authored, selected text-free production still with verified role support |
| Lock approved start and end states | First + last frame | Submit only two eligible independent production stills, one role per image, with matching ratios |
| Follow storyboard staging while preserving explicit references | R2V | Translate board staging into text; submit only eligible canonical assets and independent production stills |
| Inherit independently animated blocking | Verified motion-reference operation | Only an eligible independent animated blockout; appearance remains separate |
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
approval states in chat or a requested shot manifest before caller-confirmed submission.
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
