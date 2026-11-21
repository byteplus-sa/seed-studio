# Review Checklists

Consolidated, actionable validation checklists for every prompt-writing skill in the
repo. Use only when the user explicitly invokes `/prompt-review`; it never
gates prompt handoff or generation. Each section is self-contained for that
manual review.

## Model-first dispatch

Resolve model and operation first, then requested axes, genre and language.
An unknown model permits provisional creative findings, but capability review
stays incomplete. Missing or empty prompts stay incomplete, not passed.
Use only the selected version's base checklist; Filipino or music-video
guidance is additive and does not select 2.5. Reviews are findings-only unless
repair is separately authorized, including for unfrozen inputs.
Reference counts, duration and preview controls below are historical snapshots,
not family limits. Confirm exact model, provider, operation, transport, tool
schema revision and validity before calling them supported.

For all Seedance sections below, assess semantic completeness, not template
conformance. Section order, headings, `Define`, feature counts, grouping and
profile blocks are optional composition aids. Inline prose is valid when
subject identity, ordered reference roles, action, continuity, sound and
applicable preservation locks are unambiguous. Special syntax, including
indexed tokens and audio brackets, requires verified exact model, operation
and destination evidence when that syntax is used. Plain language needs no
bracket-syntax evidence. Missing required capability evidence still leaves
production review incomplete. Every applicable check remains required: assess
each one and report missing evidence, broken locks, unsupported controls and
exceeded verified limits. Do not mark real requirements optional merely because
their example headings or syntax are optional.

## Table of contents

- [Universal — all prompts](#universal--all-prompts)
- [Seedance 2.5](#seedance-25)
- [Seedance 2.0](#seedance-20)
- [Seedance VFX (video-to-video)](#seedance-vfx-video-to-video)
- [Seedance 2.5 edit (video-to-video)](#seedance-25-edit-video-to-video)
- [Seedance 2.5 recast (motion transfer)](#seedance-25-recast-motion-transfer)
- [Seedance 2.5 restyle](#seedance-25-restyle)
- [Seedance Filipino dialogue](#seedance-filipino-dialogue)
- [Seed Audio](#seed-audio)
- [Seedream image generation](#seedream-image-generation)
- [Seedream character sheet](#seedream-character-sheet)
- [Seedream location asset](#seedream-location-asset)
- [Seedream prop asset](#seedream-prop-asset)
- [Storyboard prompts](#storyboard-prompts)
- [Seedance music video](#seedance-music-video)

---

## Universal — all prompts

Applicability comes from explicit prompt type, model, operation, and change
contract. Workspace invariants are owned by `../../../contracts/rules.json`;
this section maps them into review guidance. Check applicability before each
item and record a reason for not_applicable. Specialized heuristics do not
change the production policy. Source metadata: `rule-provenance.json`.

1. **Visible consistency (`asset.visible_consistency`).** Required canonical
   inputs are named, versioned, and approved before dependent production
   generation. Draft breakdown may identify unresolved inputs. Branded,
   recurring, story-critical props and scene-variant wearables need separate
   references; incidental objects can be text-only. Copy locked descriptors
   exactly when they apply; a new element prompt is authoring canon, not
   consuming a pre-existing approved version of itself.

2. **Positive direction.** Prefer concrete desired behavior and appearance.
   Technical exclusions, precise edit boundaries, and preservation constraints
   are allowed when they reduce ambiguity; a negation alone is not a failure.

3. **Narrative event (`narrative.observable_event`).** Narrative shot prompts
   contain observable action and relevant intent. Static turnarounds, location
   plates, UI/product sheets, music beds, SFX, and ambience are not_applicable;
   evaluate their composition, consistency, or sonic event instead.

4. **Watermark.** Apply only where the selected tool supports the parameter.
   If the request specifies watermark behavior, it defaults to `false`
   unless the user explicitly requested the AIGC watermark.

5. **Duration right-sizing.** The prompt does not pad a scene to fill a maximum
   duration. Each scene is set to its natural length (4-30s for Seedance 2.5, up to
   15s for Seedance 2.0).

6. **Parameters in the API, not the prompt.** Generation parameters (duration,
   resolution, aspect ratio) are not embedded in the prompt text unless the skill's
   structure explicitly includes them. They belong in the submitted parameters,
   never in the prompt text.

7. **Prompt delivery.** Chat is the default. Save a snapshot only on explicit
   request, under the user's requested prompt location; no scene file or
   production registry is required for an inline prompt.

8. **No duplicate action descriptions.** The same action is not described twice in
   the same prompt. Each beat appears once.

9. **No generic adjectives.** The prompt avoids "beautiful," "stunning," "amazing,"
   "cinematic" as standalone descriptors. It uses concrete, specific, observable
   language instead.

10. **@tag references.** All project Elements (characters, locations, props) are
    referenced by their locked `@tag` and bound to the correct `@Image N` / `@Video N`
    / `@Audio N` index.

11. **Reference-derived talent is distinct.** When a template came from a
    competitor or category reference, character descriptors do not reproduce
    the reference performer's distinctive combination of face, hair, wardrobe
    and styling. Keep the role and staging; change the identity.

12. **Product descriptors match the packshot.** Every product cue in the prompt
    (pack type, size, colour, cap, label layout) agrees with the bound official
    product reference. A descriptor inherited from the reference ad's product
    fails.

13. **No invited copy or marks.** The prompt does not quote taglines, captions,
    slogans or source-brand names, and does not ask the model to render readable
    brand text or logos that a post-production overlay or a supplied official
    asset should provide. Words like "logo", "tagline" or "text reads" are
    deliberate only.

14. **Performance handoff (`acting.plan_bound`).** During this requested review,
    trace supplied intentions, triggers, registration, listener tasks and readable
    consequences into the prompt, regardless of the selected video model.
    Inline intent is valid; missing material input is incomplete, not permission
    to invent a scene file. Preserve quiet holds, masked framing, exact words,
    timing and deliberate non-response. Two to four cues is a heuristic, not a
    minimum. Critical omissions or contradicted locks are MAJOR. Static assets
    and preservation-only edits record not_applicable; inherited performance
    still needs its applicable preservation checks.

15. **Staged fights (`fight.readable_exchange`).** For authored fight action,
    trace participants, start/end states, apparent contact or avoidance,
    reactions and prop ownership through readable framing and timing.
    These criteria are model-independent; do not import another model's
    parameters. Do not certify hidden contact, impose a fighting style or
    change a locked outcome. Non-fight work and preservation-only edits record
    not_applicable with a concrete reason. These criteria do not make review
    automatic.

---

## Seedance 2.5

Source skill: `seedance-prompt`

### Native draft first

Previously covered exact standard Seedance 2.5 and access-confirmed Premium
bindings require explicit `resolution: "480p"` and boolean `draft: true` outside
prompt text for every new generation, edit, extension, probe and creative retry,
regardless of review depth or delivery target. Plain 480p is not native Draft.
A missing required native control is a capability mismatch, not a fallback.
New exact model/operation bindings, including other 2.5 variants, use only a
verified profile independently bound to provider, transport, tool schema revision
and validity. New native operations use evidenced native controls. Verified
non-native operations use an ordinary preview at the evidenced resolution,
even when 480p is also supported, clearly non-promotable; a final requires
separately confirmed fresh generation. Do not infer Draft from a family substring.
Missing, malformed, expired, wrong-destination or unknown evidence leaves
execution unresolved, not prompt-only creative writing.
Promotion by `draft_task_id` requires the exact selected successful native task,
unchanged creative inputs and reference hashes, matching valid profile/transport
and final inspection. Changed creative inputs require a new native draft.
Preserve historical task identity, hashes and selections; relabeling cannot make
an ordinary task native.
This check does not make manual `/prompt-review` mandatory.

### Formula check

1. **Subject + Action present.** The prompt contains at minimum a clear subject and a
   primary action or event. These are the only required parts.

2. **Flexible formula.** Subject, action/event, scene/environment, visual style,
   camera and audio may use any clear section order or inline prose. Include
   supplied, requested or necessary details; do not flag order alone.

3. **No double-description.** The same action is not described in multiple sections.

4. **Action granularity.** Describe critical action and perceptual outcomes,
   with body-part detail, range, speed, force, contact or recovery only where
   needed for readability and feasibility; leave incidental execution open.
   Speed, amplitude, interruptions and recovery follow the
   supplied intent. Do not penalize energetic action or dialogue merely for
   being fast; assess physical grounding and readable evidence.

### Reference materials

5. **Material mapping in prompt.** Every reference material is mapped directly in the
   prompt text — the model never has to guess which asset belongs to which
   person/prop/scene.

6. **Individual naming.** Each subject is named and bound individually. The prompt
   does not use lazy groupings like "@Images 1 through 4 define four characters."

7. **Optional grouping.** Type groups such as [Characters], [Props], [Scenes],
   [Motion and Audio] can clarify many references. Inline mappings are equally
   valid when each role and ownership are clear.

8. **Optional profiles.** Centralized profiles can clarify recurring subjects
   across scenes. Stable attributes, reference bindings and prop ownership
   remain consistent whether expressed inline or in profile blocks.

9. **Per-scene selection.** Each scene names only the references it uses — not all
   materials at once.

10. **Exclusion phrasing.** "Do not use..." exclusions appear only when leakage is
   genuinely possible. Not as a generic negative-prompt dump.

11. **Multiple views.** If multiple images define one subject, the prompt explicitly
    states "The output must contain only one [subject] throughout."

12. **Video reference inheritance.** If inheriting from a reference video, only the
    attributes to inherit are stated. The prompt does not restate every action from
    the reference (which can conflict).

13. **Control-only references (`references.control_only`).** Translate to text
    and omit by default. Storyboard grids, panels, crops and animatics remain
    planning-only in every conditioning role. Selection, current hashes, mode
    support, style overrides or promotion labels cannot change board origin.
    Independent production stills must be independently authored, selected and
    text-free, not cleaned or renamed planning imagery. Eligible non-board
    conditioning requires selection, current source hashes, supported tool/mode
    inputs, rights and QA; labels alone do not grant eligibility.

14. **Reference count limits.** Verify per-modality and total limits for the
    selected model/operation. The earlier 30-image, 10-video, 10-audio snapshot
    and recommended subject counts do not establish a family quota.

### Scene staging

15. **Stage structure.** Use consecutive stages when helpful. A shot or stage
    may carry readable ordered actions, reveals or a sustained state. Check
    causal order and perceptual outcomes, not a per-shot single-event quota.
    Waiting or listening may remain unchanged; do not demand a turn to fill a hold.

16. **Natural duration.** Each scene is generated at its natural duration (4-30s),
    not padded to 30s. 30s single-pass or extension is the exception, not the default.

17. **Timestamp ranges.** Time ranges are consecutive and non-overlapping. They are
    treated as a time budget, not precise edit points.

18. **Action feasibility.** Judge physical support, travel, contact and recovery
    against the available time and required readability. Action count alone
    does not establish impossibility. Cite a concrete conflict; without enough
    timing evidence, leave feasibility unresolved rather than inventing a limit.

### Audio syntax

**Audio ownership.** Check the chosen route against the brief: requested native
diegetic sound, including wordless action/ambience; an exact master or controlled
post soundtrack; or purposeful silence. Speech-free alone does not require
picture-only. Native sound specifies wanted effects/sync and unwanted voices or
music; negative wording is not proof of compliance. Explicitly post-owned sound
may use picture-only where supported; preserve exact masters and scope any
necessary assembly. A bed is not automatically frame-synced. Silence adds no bed and
requires verified removal if native audio cannot be disabled. Confirm supported
destination controls, reference roles, rights and approvals. Missing or conflicting
ownership stays unresolved. A contradicted route or reliance on wording alone to
guarantee silence is MAJOR. Require destination playback and listening for
unwanted audio, sync and master fidelity, again after promotion. Reject
noncompliant audio or propose an authorized repair, not automatic muting of
requested native sound. Mixed ownership names each layer's source. This manual
review does not authorize generation or post-production. Satisfactory native
audio can remain unchanged without a finishing pass. Finalization alone does
not authorize normalization, ducking, fades, word-level splicing or replacement.
Unavailable listening evidence stays unresolved; it does not justify a repair.

19. **Verified audio syntax only.** Bracket conventions for dialogue `{}`,
    music `()` and SFX `<>` apply only when verified for the exact model,
    operation and destination. Plain language is valid without that evidence;
    do not claim unsupported syntax or audio controls work. Subtitles and
    overlays belong in post, not generated footage.

20. **Dialogue intent.** Preserve requested language, regional variety/accent,
    delivery style, speaker attribution and approved words. A "Dialogue
    Language" prefix and a fixed field order are optional, not parser rules.

21. **Same dialogue in both prompts.** If audio-first pipeline is used, the exact
    dialogue text in the Seed Audio prompt matches the spoken text in the
    Seedance prompt. No paraphrasing, reordering, or omitted lines.

### Emotional direction

22. **Performance criteria.** Apply Universal items 14 and 15 with their
    applicability guards; they are shared with the other video models.

23. **No bare emotion words.** The prompt does not rely solely on emotion labels like
    "very sad" or "extremely angry" without physical externalization.

### Camera language

24. **Coherent camera direction.** Assess requested or delegated choreography by
    compatible paths and readable handoffs, with subject, beginning and endpoint
    stated. Move simplicity is a heuristic, not a count limit. Return genuine
    simultaneous conflicts; preserve a requested static camera and source locks.

24a. **Requested shot plan carried.** When the user requests or supplies a shot
    plan, each shot carries its duration, purpose, framing, camera move or
    static reason, visible lens intent and motivated light. Compare the prompt
    with that plan and confirmed axes; report dropped facts or broken locks.
    No separate plan is required for ordinary prompt requests.

24b. **Variety fits the requested energy.** For an explicitly requested dynamic
    sequence, compare neighboring shot sizes, angles, moves and key sides with
    the requested plan. Treat the shot-design thresholds as craft heuristics,
    not model guarantees. Preserve dialogue readability, fixed song timing,
    static formats and source-preserving edits. Actor energy, camera energy and
    edit rhythm are separate choices. Repeated framing, equal durations,
    clean singles and sustained holds need no exception count. There is no
    mandatory cadence, coverage mix, turn shot or "wow" image.

24c. **Motivated light and readable holds.** A planned source keeps its world
    position across cuts; a new source needs a visible motivating event. A
    light that goes off, dims or flickers inside a shot matches a cue recorded
    on a planned source, with its time and trigger. A static hold may
    emphasize performance or contrast with motion. Never add camera movement
    against a user lock merely to meet a variety target. Repeated
    `performance_hold` reasons and a whole held scene are valid when they
    sustain the intended attention.

24d. **Assembly precision and motion remedies.** Exact blink cuts, intercuts or
    vision flashes belong in assembly when prompted timing cannot meet the
    brief; 0.8 s is a provisional heuristic, not a universal minimum.
    A prompt that asks the model to skip an
    action it describes is a MAJOR finding. Requested focus loss is an
    unverified visible target, not a MINOR finding by itself; limited earlier
    T2V face-focus failures motivate an optional post alternative.
    A single burst with holds or slower motion is an optional
    remedy for a demonstrated failure, not a cap or MINOR finding by itself.
    Preserve repeated action and locked timing; assess readable support,
    momentum, contact and recovery rather than counting bursts.

25. **Uncommon cinematography terms.** If used, they follow the format:
    Term + Target Subject + Visual Change + Foreground/Background Relationship +
    Direction or Speed.

### Spatial continuity

26. **Spatial map present.** Movement-heavy scenes include: Start positions,
    Travel axis, Subject order, Boundary behavior, End state, Forbidden transitions.

27. **Physical locations.** Uses physical locations and ordered states, not relative
    verbs alone.

28. **Invariants repeated.** Critical spatial invariants are repeated in every
    shot/stage since every cut can reset relationships.

### Parameter auto-lock

29. **Editing task.** Aspect ratio and duration are not set (locked to input). Edit
    scope, target quantity, and content to preserve are defined.

30. **First/last-frame task.** Aspect ratio locks to first image. First and last
    frames share the same aspect ratio.

31. **Extension task.** Aspect ratio is not set (locked to input). Duration can be
    set. Boundary image, motion trend, and audio continuity are checked.

### Preflight review (15-point)

32. **Subject & action** clearly stated.
33. **Reference roles**: every reference states what to use and what not to use.
34. **Subject binding**: every required canonical character/product/prop named and bound to a
    reference.
35. **Scene selection**: references selected by scene, not forced to appear all at once.
36. **Stage structure**: critical ordered actions, reveals or a sustained state remain readable within each shot or stage, including purposeful unchanged attention.
37. **Consistency**: character count, clothing, prop ownership, spatial relationships
    stay consistent.
38. **Editing master**: for editing, sole editing master, edit scope, target quantity,
    content to preserve defined.
39. **Emotion & camera**: abstract emotions and cinematography terms paired with
    visible/audible cues.
40. **First/last frames**: one role per image; first and last share aspect ratio.
41. **Storyboards & blockouts**: board staging is translated into text and
    planning assets are absent from video inputs; eligible independent animated
    blockouts identify coarse vs fine and retain their motion authority.
42. **Auto-lock rules**: editing, first/last-frame, and extension follow locked
    aspect-ratio and duration rules.
43. **Extension boundary**: boundary image, motion trend, and audio continuity checked.
44. **One-click video**: material roles, image order, motion amount, editing style,
    and audio defined.
45. **Seamless transitions**: two videos' roles, trigger action, transition process,
    and arrival state defined.

46. **Speech fits duration.** Use measured delivery or a native-language-informed
    read with pauses. Spoken words / 2.2 is an English planning estimate in
    seconds, not a universal rejection rule; without delivery evidence, fit is
    provisional. If delivery leaves a substantial gap in the API `duration`,
    direct the gap (pauses, hesitations, action beats) or propose retiming.
    Budget onset separately (limited upstream observations: 0.5-1.5 s) and leave
    at least 0.4 s after the last word as an initial allowance. Actual delivery
    overrides estimates; flag an overfull line and propose retiming or splitting
    without automatically changing approved words.

**Prompt precision.** Check exact counts and stage positions for counted items,
anatomical side plus frame side for critical hand actions, and plain generic
surfaces where generated lettering would be a defect. These are authoring
heuristics, not guarantees of model control. Respect intentional occlusion,
entrances and exits; do not expose a hidden subject merely to count it.
Track total identity separately from visible count. Contradictory totals,
unexplained duplication or incompatible positions are MAJOR; a count stated
once with unambiguous continuity is not. Preserve locked reveal timing.

### Motion grammar (stylized animation & reverse-engineered takes)

47. **Selective motion grammar.** Require only the axes needed for critical
    action and readability. Amplitude, easing and rates are optional unless
    material to intent; loop periods apply only to intended repetition.
    Organic one-off motion and deliberate stillness need no invented loop or
    light change. Honor selected motion masters. Missing incidental axes
    alone are not a finding or evidence of a failed take.

48. **Camera motion distinguished.** Preserve a requested camera path or hold
    separately from subject motion; unrequested camera axes remain optional.

49. **Light/color motion stated when relevant.** Describe the intended visible
    effect and rate only when it matters; do not invent light motion for stillness.

### Storyboard grid reference

50. **Planning-only storyboard boundary.** Grids, panels, crops and animatics
    cannot be bound as first/last-frame, R2V, composition or motion inputs.
    Explicit selection, current hashes, compatible mode support, cleanup and
    style overrides do not change their origin. Translate approved shot order,
    staging and continuity into text; report a proposed board binding as a
    finding without repairing the prompt. An independently authored, selected
    text-free production still remains eligible with verified role support,
    rights and approval. Preserve historical board-linked records and hashes;
    review does not rewrite them or authorize new conditioning.

### Revision diff

51. **No approved per-shot detail lost.** When a prompt is revised to change one
    shot, every OTHER shot's previously-approved wording (descriptors, motion
    rates, glow pulses, gradient outlines, camera moves) is carried over
    verbatim. A revision that silently drops detail from untouched shots is a
    MAJOR finding — diff the new prompt against the prior snapshot and flag any
    removed descriptor or rate.

---

## Seedance 2.5 edit (video-to-video)

Source skills: `seedance-prompt` (editing) + `seedance-vfx-prompt` (2.5 section).

Apply "Universal — all prompts" first, then this section. Mark N/A any item
whose feature is absent (no references → skip material mapping).

### Editing task

The headings below are optional examples; inline prose carrying
the same editing contract is valid. Settings require exact destination evidence.

1. **Edit goal.** Identify the editing operation and source explicitly, e.g.
   `Edit @Video 1 …`. Use `omni_reference_task_type="edit"` only for a verified
   binding supporting that control; do not import a legacy `edit_video` value.
2. **Source video role.** Declare `@Video 1` as the sole editing master and
   list what it defines (subjects, scene, actions, camera, event order).
3. **Target material role.** When references are used, each `@Image N` is
   mapped to one target, and the image's unowned content is excluded
   ("Do not use its background/people").
   Exempt what the target class owns: a character reference owns its person, a
   location reference owns its background. Single-person sheets directed to
   use the close-up panel only.
4. **Edit scope.** State what changes and, for what must not change, a positive
   "exactly one <subject> — never a second or duplicated copy" guard.
5. **Content to preserve.** List identity/motion/timing/camera/lighting to keep.

### Preservation locks (only where MUST PRESERVE says so)

6. Quantity: "Exactly one <subject> in frame — never a second or duplicated copy."
7. Non-reaction (when the subject must not react): "…facial expression, gaze,
   and gestures remain exactly as in @Video 1; only <the changed thing>
   re-animates."
8. Grounding: "…naturally grounded — no cut-out edge, no halo; rim light
   matches the key direction."
9. Face protection (any preserved face): "real human skin with pores and
   catchlights — never waxy, smoothed, or warped."

### Audio / lip-sync

10. Preserve requested language, regional variety, delivery style and speaker;
    direct lips to the new approved words. Use bracket syntax only when
    verified for the exact model, operation and destination; plain language
    is valid otherwise. Do not alter approved punctuation to fit a template.
11. Same-content contract (language swap): target spoken line is the source line
    translated, no paraphrase/omission.
12. Preserve the brief's native or supplied sound unchanged unless an audio
    change is explicitly authorized. Use SFX/music brackets only under item
    10's verified syntax condition; do not suppress a requested score.

### Camera (only when the edit intentionally re-stages the camera)

13. One or two coherent camera moves when re-staging is intentionally requested;
    use semantic cues and add numeric timing only for requested or critical
    synchronization. Expand uncommon terms (orbit: direction + parallax).
    Apply the same camera-complexity guidance as general Seedance 2.5 item 24.
14. Camera-move items are N/A when the edit must preserve the source camera.

### Change contract

15. Flag only breakage of MUST PRESERVE or a quality defect in the change
    description — never an item the user explicitly asked to change.

### Object swap (only when one named element is replaced)

Source skill: `seedance-object-swap`. Apply audio items 10-12 only to the
selected sound intent and verified operation. An unchanged native soundtrack
is valid; silence and separate audio are not prerequisites (V1 below).

16. **Residual original (`swap.residual_original`).** The original object is
    identified by observable descriptors (position, colour, material, who holds
    or wears it) and a positive guard states that it is fully replaced in every
    frame and only the target appears. A missing guard or a vague original
    ("the product") is a MAJOR finding.

17. **Count and Timeline Inheritance (`swap.timeline_inheritance`).** The prompt
    states the target count for the entire video (and per cut when it changes)
    and a `[Timeline Inheritance]` clause: the target inherits every
    appearance, motion, occlusion and exit of the original, including timing,
    duration, path and speed changes. Missing either is MAJOR.

18. **Contact and preservation.** Each grip, mouth contact, occlusion and
    set-down window is listed with its approximate time; hands, faces,
    accessories and mouth movement stay under `[Content to Preserve]`. Swapping
    several people or the whole cast belongs to the recast section below.

19. **Video-to-video inputs.** Apply the shared items under
    [Video-to-video inputs](#video-to-video-inputs-swap-recast-restyle).

---

## Seedance 2.5 recast (motion transfer)

Source skill: `seedance-motion-recast`.

Apply "Universal — all prompts" and the general Seedance 2.5 reference items
first, then this section. A recast keeps the source clip's motion, camera path,
framing changes, cuts and timing, and rebuilds cast, wardrobe, product,
location and style from references. Mark N/A any item whose feature is absent
and record why.

### Motion authority

1. **Motion excludes appearance (`recast.motion_authority`).** The prompt limits
   `@Video 1` to motion, pose sequence, screen positions, camera path, framing,
   cuts and timing, and assigns faces, hair, wardrobe, products, location,
   palette and style to the references. A motion video with no appearance
   exclusion reproduces the source look; that is CRITICAL. The operation and
   task type match the mode the user chose and what the destination UI offers
   (`model.supported_mode`).

2. **Inherit, don't restate.** Only the inherited attributes are named; the
   prompt does not re-describe every source action, which conflicts with the
   motion video (general Seedance 2.5 item 12).

### Subjects and mapping

3. **Every subject has a disposition (`recast.subject_disposition`).** Each
   visible source subject is listed exactly once as mapped (to a reference),
   removed, or background extra, and the list agrees with the source
   inspection per cut. An unlisted subject, or an unresolved ambiguity carried
   into the prompt, is CRITICAL.

4. **Unambiguous mapping (`recast.mapping_unambiguous`).** Each mapped subject
   is identified by observable descriptors (screen position, clothing, action)
   and bound to one `@Image N`, e.g. "the person on the left in the red jacket
   → @Image 2". Blanket wording ("replace everyone", "the people", "@Images 1–4
   are the cast") or one reference serving two subjects is CRITICAL. Several
   views of one subject state that the output contains only one of them
   (`references.ordered_bindings`).

### Guards

5. **Accessory bleed and extra people (`recast.guards`).** Each target wears
   only the wardrobe and accessories in its reference; source glasses,
   jewellery, hats and bags are named where they must not carry over. The
   person count per cut is stated, background extras are given as a count or
   density, and no additional people appear. Missing either guard is MAJOR.

6. **Audio route (`recast.audio_route`).** Keep acceptable native or supplied
   audio unchanged. State sound intent and preserve exact-source locks;
   explicit silence or audio edits remain scoped choices. Verify the selected
   controls and reference roles independently. No native-audio exception,
   separate soundtrack or finishing pass is required. Unknown preservation
   support is incomplete, not permission to mute or regenerate a locked master.
   Lip-sync checks apply when someone speaks on screen; repairs need explicit
   authorization.

7. **No overlay text.** No captions, taglines, CTAs, end cards or readable brand
   copy are requested (Universal item 13). Source on-screen text has a stated
   disposition (removed or replaced by a plain surface); overlay copy is added
   in post.

### Limits and rights

8. **Reference counts.** Count each modality and total against current
   model/operation evidence. Exceeding a verified hard limit is CRITICAL;
   unknown limits are incomplete. Historical recommended counts alone are not
   MAJOR findings; optional splitting needs a readability reason and agreement.

9. **Video-to-video inputs.** Apply the shared items under
   [Video-to-video inputs](#video-to-video-inputs-swap-recast-restyle).

### Video-to-video inputs (swap, recast, restyle)

Shared by the object swap items, the recast section and the restyle section.
Policy source: the
[video-to-video inputs contract](../../../contracts/video-to-video-inputs.md).

V1. **Audio preservation (`v2v.audio_preservation`).** Keep acceptable native
    or supplied audio unchanged; a source with sound is not a defect by itself.
    No mute/extract/mux sequence is mandatory. Required source preparation needs
    independently verified exact model/operation/transport constraints and
    explicit authorization for a separate copy. Unknown support is incomplete.
    Check explicit silence, exact-source locks and any authorized edits against
    their scope; generation support does not prove exact passthrough. Preserve
    independent spans and audio tails, without automatic padding or truncation.
    Check source eligibility under V2 before binding.

V2. **Identity eligibility (`v2v.virtual_portrait_identity`).** For each source
    and target, check that an invented Virtual Portrait is eligible or that
    a real performer has consent and a verified real-person route. Leave
    unknown or rejected roles unresolved. Use binding positions in prompts.

V3. **Source rights.** The package notes the user's confirmed rights for the
    footage and the people in it. A missing confirmation is CRITICAL. Do not
    suggest wording that routes around a provider rejection.

V4. **Exact source timing (swap, recast and restyle).** Preserve the fractional source span,
    frame timestamps, cuts and playback speed. Do not require 8n+1 frames or
    whole-second rounding from a prior probe. Adapt only a separate copy for
    a verified destination requirement, with user agreement and the timing
    change recorded; retain original video and audio. Report output timing
    mismatches rather than accepting a blanket tolerance.

---

## Seedance 2.5 restyle

Source skill: `seedance-restyle`.

Apply "Universal — all prompts", the general Seedance 2.5 reference items and,
for the edit route, Seedance 2.5 edit items 1, 2, 4 and 5. Edit item 3 is
replaced by restyle item 3 (`[Style Reference Role]`, `[Identity Anchors]`);
edit item 9 is N/A because the photoreal face line contradicts drawn and
crafted styles (use it only for a capture look); edit items 10-12 apply only
to the selected sound intent, not an assumed silent output (V1).
A restyle keeps the source's subjects,
layout, actions, camera, cuts and timing and changes only the rendering
medium. Mark N/A any item whose feature is absent and record why.

1. **Content preserved (`restyle.content_preserved`).** The prompt pins the
   subject count, observable subject descriptors with identity cues, key props
   and set layout from the content inventory, and keeps poses, camera, cuts and
   timing with `@Video 1`. Introducing, removing or replacing a subject is
   CRITICAL; that request belongs to Object Swap or Motion Transfer.

2. **Medium lock.** One style applies to people, props, set, sky and effects,
   and nothing is left photographic unless the style is a capture look. A
   partial or conflicting style block is MAJOR.

3. **Style-only reference (`restyle.style_reference_only`).** Each style image
   supplies only medium, palette, line, texture and light quality and excludes
   its subjects, layout and characters. A style image without that exclusion
   is MAJOR. Studio, artist or franchise names, or frames from copyrighted
   productions, are CRITICAL.

4. **Identity anchors.** Eligible anchors, when used, are designed in
   the target medium and mapped to a source subject by observable descriptor.
   A photoreal anchor under a drawn or crafted style is MAJOR.

5. **Cadence and text.** Stepped styles state that beat poses still land.
   Source text surfaces become abstract shapes; no lettering is requested.

6. **Route and limits.** The operation matches the route the user chose and
   what the destination UI offers (`model.supported_mode`); an unverified route is
   labeled provisional. Apply the exact-binding preview policy under
   [Native draft first](#native-draft-first), not a family-wide 480p rule;
   missing required controls remain unresolved before execution.
   Draft settings are not a quality guarantee. Image counts,
   roles, ratio and duration follow verified destination limits; no default
   trim or rounding of exact source timing.

7. **Same place.** A restyle keeps the source place and layout. An environment
   image is optional, based on current inputs, user selection or observed
   incomplete medium coverage. Its absence alone is not a finding. When used,
   check approval, target-medium coverage, source geometry and stray objects;
   it does not override the source layout. Naming a different location is
   MAJOR unless requested. A no-image request stays valid without a guarantee
   of coverage; do not prescribe an image or a location change automatically.

8. **Video-to-video inputs.** Apply the shared items under
   [Video-to-video inputs](#video-to-video-inputs-swap-recast-restyle).

---

## Seedance 2.0

Source skill: `seedance-prompt`

### Structure

1. **Flexible structure.** Section order and headings are optional. Subject,
   action, reference roles and applicable constraints must remain clear,
   including when the action precedes the asset mapping.

2. **Ordered reference bindings.** Bind references directly in the prompt to
   their subjects and roles, with indices matching the ordered input bundle.
   Use the destination's verified notation; mapping may appear inline.

3. **Reference limits.** ≤ 9 images, ≤ 3 videos, ≤ 3 audio (15 total). Audio cannot
   be sent alone. Combined video duration ≤ 15s, combined audio duration ≤ 15s.

### Subject definitions

4. **Stable identity.** `Define` is optional; inline subject bindings are valid.
   Use distinctive static features where needed, not a feature quota.
   Identity uses no mutable attributes like expression or pose.

5. **Label reuse.** Keep each subject's reference binding consistent across
   shots; repeat it where needed to prevent ambiguity, not as a fixed quota.

6. **No Asset IDs.** Uses `@Image 1` / `@Video 1` format, not Asset IDs.

### Reference classification

7. **Classification.** Each reference is classified as: Visible identity, Visible
   environment, Motion/camera reference, or Control-only reference.

8. **Control-only handling.** Translate planning boards, panels, crops and
   animatics into text and omit them from every video input. Independently
   authored text-free production stills and eligible non-board controls require
   explicit selection, current hashes and exact role support; extraction
   instructions do not change planning origin.

9. **Face restriction.** No direct uploads of real human faces. Uses model outputs,
   preset digital characters, or authorized real-person assets.

### Task type declaration

10. **Task type declared.** One of: Multimodal Reference | Video Editing | Video
    Extension | Combined Tasks.

11. **Edit/extend phrasing.** For edit/extend: uses `@Video 1` directly ("Strictly
    edit @Video 1..."). Does NOT write "Reference @Video 1" (which triggers
    multimodal reference mode).

### Shots

12. **Readable sequence.** A continuous take need not use shot headings.
    Requested shots or stages carry ordered actions or a sustained state;
    check continuity rather than a fixed shot format.

13. **Per-shot authority.** Each shot's applicable references and roles stay
    unambiguous. Repeat critical bindings when a cut could reset relationships.

14. **Per-shot content.** Preserve requested camera, action, spatial changes,
    lighting, color and audio in any clear order; missing requested content,
    not its position in the text, is a finding.

15. **Coherent camera movement.** Use one or two clear requested movements per
    shot, with sequence and endpoints; avoid competing simultaneous directions.

16. **Complexity budget.** Assess whether action, speech and continuity fit
    15s. Three major beats or four related shots is a planning example, not a
    quota or provider limit. Cite an actual timing or readability conflict.

17. **Action detail.** Body-part level detail (hands, legs, head, shoulders, back)
    with range, speed, force.

18. **Intent-led motion.** Speed, amplitude, interruptions and recovery follow
    the brief, with physical support, momentum and contact. Energetic dialogue
    is valid when words, speaker and responses remain readable. Quiet acting,
    repeated framing and sustained holds are equally valid. Optional slower
    motion or burst-with-holds repairs require a relevant failure, not a quota.

19. **Emotion externalization.** Emotions are externalized as physical details,
    never bare labels.

20. **Dialogue attribution.** Preserve exact spoken words and identify each
    speaker. Bracket syntax requires verified exact model, operation and
    destination support; plain language with clear attribution is valid.

### Timing

21. **Duration via API.** Total video length set with API `duration` parameter, not
    timecodes in text.

22. **Natural pacing.** The model paces multi-shot generation naturally. Second-level
    timing only when user explicitly requests it.

23. **Timestamp format.** If used: concise ranges (`Shot 1 (0-4s):`), contiguous,
    non-overlapping, consistent with API duration.

### Spatial continuity

24. **Spatial map present.** Same 6-field format as Seedance 2.5 (Start, Travel axis,
    Subject order, Boundary behavior, End, Forbidden transitions).

25. **Physical locations.** Uses physical locations and ordered states, not relative
    verbs alone.

### Quality and constraints

26. **Inline constraints.** All constraints go inline in the text prompt (no separate
    negative_prompt field).

27. **Prioritized constraints.** Prioritizes constraints instead of accumulating a
    long blacklist.

28. **Positive phrasing.** States required physical behavior positively. Repeats only
    the few exclusions that prevent expensive failure.

### Preflight review (6-point)

29. **Parameter agreement.** Prompt and API resolution, duration, ratio, and audio
    setting agree.

30. **Reference indexing.** Every reference is indexed, classified, and bound only
    where intended.

31. **Spatial fields.** Start, travel axis, subject order, boundary behavior, and end
    state are explicit.

32. **No contradictions.** No contradictory instructions (e.g., "single continuous
    shot" plus several cuts; "no powers" plus an emitting aura reference).

33. **Focus.** Prompt is focused; repetition compressed before removing critical
    spatial state.

34. **Beats fit duration.** Requested beats fit the duration or the scene is split.

### Revision contract (if revising)

35. **Locked decisions carried.** Approved identity, action, camera, environment,
    audio, boundary behavior carried into revised prompt.

36. **One delta.** Only one of {prompt wording, reference bundle, motion design}
    changed per retry.

37. **Acceptance criteria.** Observable conditions for the next take to pass are
    stated.

38. **Known rejections.** Behaviors from earlier takes that must not return are listed.

---

## Seedance VFX (video-to-video)

Source skill: `seedance-vfx-prompt`

### Core principle

1. **Source clip is the lock.** The prompt preserves what to keep (subject identity,
   performance, camera motion) and describes only what should change. It does not
   re-describe the entire scene from scratch.

### Asset preparation

2. **@Video 1 is source.** Source clip is always `@Video 1`. Uses "Strictly edit
   @Video 1" (NOT "Reference @Video 1").

3. **Source described.** Subject, action, camera motion, and duration of source clip
   are described in asset preparation.

4. **Source inspected.** The source clip was inspected before writing (duration, fps,
   aspect ratio probed). Prompt is built from footage, not user's one-line summary.

5. **Texture references labeled.** Texture references say "texture only" — "appearance
   and fur/skin texture reference only; ignore the photo's background and lighting."

### Subject definitions

6. **Stable subject binding.** Bind the source identity using stable labels
   and relevant static features. `Define` and separate definitions are
   optional; inline bindings are valid without a feature quota.

### Locks (preservation)

7. **Locks declared.** Identity (face, body, costume, props), Performance (gait,
   gestures, expressions, timing), Camera (motion type, framing, lens, bob),
   Continuity are locked with `<Label>@Video 1`.

### Change

8. **Change named with timestamp.** The exact change and when it happens are stated
   (`At 0:NN` for localized changes). Global changes at `0:00`.

9. **Subject reaction.** Whether the subject reacts or does not react is stated.

### New world

10. **Full description.** Replacement/added environment/element is fully described.

### Lighting (embedded)

11. **Lighting lives in the world.** Light sources are physically present in the new
    world. Not described as a layer pasted on top.

12. **No generic lighting terms.** Does not say "cinematic lighting" or "dramatic
    lighting" alone — names the source.

13. **Light on subject.** Where light falls on subject (direction, color, intensity)
    is described.

14. **Light-environment interaction.** How light interacts with environment
    (volumetric mist, reflections, shadows) is described.

15. **Integration fork decided.** Either "preserve subject's lighting; grade only new
    elements" (default) OR "relight the whole frame under one look" is explicitly
    chosen.

16. **"Looks pasted in" recipe applied.** Light (direction, softness, shadow density),
    environmental bounce, optics & atmosphere (lens, micro-contrast, haze, DOF, grain),
    edges & grounding (no hard cut-out, no halos, matched rims) are addressed.

### Space

17. **Layered space.** Foreground (parallax elements), Midground (subject + primary
    environment), Background (atmosphere and scale) are described.

### Timing

18. **Sequential timestamps.** When each event triggers and how it progresses.

19. **Timed camera moves dual-anchored.** Semantic anchor ("At the line '<exact
    words>,' the camera <move>") AND numeric anchor ("At about <T> seconds...").

20. **Zoom type specified.** Crash zoom = fast hard punch-in. Smooth push-in = slow
    steady glide.

21. **Tail after trigger.** Enough tail (~2-3s) after trigger for payoff. If clip is
    short, zoom fires on first word.

22. **Reveal pull-back.** If used: opens tight on added element, moves outward to land
    on real plate, demands 100% match of source composition at landing.

23. **Lip-sync window checked.** If lip-sync preservation: line quoted verbatim,
    anchored twice (in change/action and in audio), all locked sound preserved,
    "lips matching the source exactly" in Locks, line fits surviving
    dialogue window.

### Audio

24. **Sound preservation.** Keep native or supplied sound unchanged within the
    source locks; a visual edit does not authorize removing soundtrack layers.

25. **Scoped changes.** New or changed background music, score or voiceover
    needs explicit scope and verified controls. No automatic post bed.

### Quality and constraints

26. **NON-IP.** No recognizable real persons, no copyrighted characters, no brand logos.

27. **Face protection.** Preserve the selected medium and the source identity.
    Use skin texture and catchlights for a photoreal target. For an approved
    stylized target, check the chosen material and facial design.

28. **Supported model/mode (`model.supported_mode`).** Resolve operation and
    model first. Follow the exact-binding preview policy under
    [Native draft first](#native-draft-first). Check the evidenced resolutions
    for ordinary creation, native Draft and promotion separately. A request for
    4K never selects a different model or waives a required Draft. Face/detail
    fidelity is an output-QA criterion, not a guaranteed property of resolution.

### Creature/element integration (if applicable)

29. **Photoreal demanded.** "Fully photoreal, real fur with depth and individual
    strands, true anatomy, never CG, plastic, or cartoonish."

30. **Tied into plate.** Same sun direction, real soft-edged contact shadow, same hazy
    atmosphere.

31. **Scale explicit.** Scale is explicit for giant creatures.

32. **Texture fallback.** If still reads CG: second input — reference photo of real
    animal as texture-only `@Image N`.

33. **Species behavior.** Behavior matches the species (sloth slow, chimp twitchy,
    snake coils and forked tongue, snakes don't blink).

34. **Living micro-movements.** For static creature holds: slow blink, jaw shift,
    steady breath.

### Duration discipline

35. **Source runtime default.** Defaults to source clip's exact runtime.

36. **Recomputed timing.** If runtime changed, numeric zoom timing is recomputed.

37. **Prepended-intro budget.** `total runtime − intro length = surviving window for
    source performance`. If source take longer than surviving window, one of three
    resolutions offered (extend total, start source earlier, accept truncation).

### Iteration discipline

38. **Only named change.** Only the named thing changes; rest of prompt stays stable.

39. **Refine via edit.** When refining a generated still/frame, edits the chosen result
    (passes it back as base) and fixes only what is off.

### Voice

40. **No generic adjectives.** No "beautiful," "stunning," "amazing," "cinematic."

41. **Concrete language.** Names exact materials, behaviors, scale, lenses, angles,
    moves. Uses texture words. Does not inflate, soften, or explain what things
    "represent."

---

## Seedance Filipino dialogue

Source skill: `seedance-prompt-25-filipino`

Use as an additional language checklist after the selected model and operation
when the scene contains Tagalog, Filipino, or Taglish dialogue. Never import
2.5-only parameters into a legacy or unknown-model request.

### Words, register and scope

1. **Exact words protected.** Locked dialogue, names and approved spelling are
   unchanged. A pronunciation request alone does not authorize simplification.
2. **Smallest relevant repair.** Separate wording, delivery, pronunciation and
   timing problems. Change vocabulary only when authorized and appropriate to
   the speaker, relationship, region and period; literary language is valid.
   A heard defect does not authorize word-level audio surgery. Offer a prompt
   cue or retake proposal; media edits need explicit audio-edit authorization
   and a new generation needs its own submit confirmation.
3. **Register grounded.** Do not impose modern Manila Taglish, contractions,
   honorifics or a fixed sentence length on every speaker. Preserve intentional
   code-switching and politeness.

### Pronunciation and delivery evidence

4. **Evidence distinguished.** Identify a supplied recording, pronunciation guide
   or competent speaker's correction. Without evidence, a predicted issue is a
   hypothesis, not a proven mispronunciation.
5. **No universal phonology recipe.** Do not force a default stress, flat contour,
   consonant substitution or one regional accent across Filipino speakers.
6. **Notes separate from speech.** Preserve exact spoken text, using braces
   only with verified destination syntax.
   Annotation or phonetic respelling inside dialogue requires explicit scope.
7. **Cues serve intent.** Use concise, observable delivery rather than a dictionary
   or a prescribed pitch sequence. Verify actual pronunciation by listening;
   ASR text alone does not establish stress, intonation or speaker identity.

### Separate audio, only when requested

8. **Native default retained.** Filipino language or an accuracy concern alone
   does not trigger a separate Seed Audio track.
9. **Same approved words.** When separate lip-sync audio is requested, both
   prompts preserve exact words; simplification is not a prerequisite.
10. **Actual evidence retained.** Audio path/hash, inspected duration and original
    timestamp evidence remain separate from proposed prompt timing. Align only
    the synchronization detail required by the request.
11. **Input binding checked.** The resolved tool supports the submitted audio
    role, and the caller records the exact ordered binding and review evidence.

---

## Seed Audio

Source skill: `seed-audio-prompt`

### Full-soundscape ingredients

1. **Environment.** Location, weather, context, acoustic space described.
2. **Background music and SFX.** Dramatic role, style, instruments, rhythm, mood,
   volume, opening intensity described.
3. **Character actions/appearance.** Included when they affect performance.
4. **Character voice profile.** Age, gender, accent, emotion, tone, speed, timbre for
   each character.
5. **Exact dialogue.** In double quotes, with delivery note before the quote.

### Arrangement order

6. **Input references** (only when reference audio included).
7. **Opening environment, ambience, music.**
8. **Dialogue, actions, SFX** in chronological order.
9. **Ending behavior.** Resolve, fade, sustain, or cut.
10. **Creative/quality constraints** (only when user supplies them).

### Input references

11. **Reference count.** ≤ 3 reference audio (TA2A) OR exactly 1 reference image
    (reference-image mode). Mutually exclusive.

12. **Per-clip limits.** ≤ 30s, ≤ 10 MB. Formats: WAV, MP3, PCM, OGG_OPUS.

13. **Single purpose per clip.** Each clip serves exactly one purpose: voice timbre
    cloning, emotion reference, or SFX reference.

14. **TA2A mapping.** `<<TGT_SPK1>>`, `<<TGT_SPK2>>`, `<<TGT_SPK3>>` mapped to ordered
    entries in `references[]`, labeled `@Audio1`, `@Audio2`, `@Audio3`.

15. **No references section.** When no references, the input references section is
    omitted entirely.

### Environment

16. **Acoustic quality specific.** "Hallway reverb," "stone corridor echo" — not just
    "echoey room."

17. **Layers described.** Foreground, midground, background.

18. **Evolution.** How environment evolves over time.

### Background music

19. **Dramatic role.** Underscore, tension bed, transition, reveal, celebration, outro.

20. **Style/genre/instruments.** Concrete musical language, not generic phrases.

21. **Dynamic arc.** How it begins, swells, thins, changes instrumentation, stops.

22. **Relationship to speech/effects.** When music ducks, effects dominate, ambience
    remains distant.

23. **Ending.** Clean stop, held unresolved note, crossfade, gradual fade.

### Ambience

24. **Persistent bed.** Separate from one-off effects.

25. **Distance/direction/room tone.** Echo, reverb, gradual evolution described.

26. **Subordinate to dialogue.** Unless scene requires otherwise.

### Sound effects

27. **Source/action/material/acoustic character.** Spatial position described.

28. **Positioned relative to actions/dialogue.**

29. **Evolution/decay.** Described when important.

30. **Onomatopoeia in quotes.** "ring-a-ling," "zzzip," "clack" — used to clarify
    texture, not as a substitute for describing the sound.

31. **Foreground/midground/background.** Identified when mix could be ambiguous.

### Character voice profiles

32. **T2A format.** `Name (age, gender, accent, voice timbre, emotional tone, delivery
    style) says: "dialogue text"`

33. **TA2A format.** `Name (voice description, voiced by <<TGT_SPKN>>) says [delivery
    note]: "dialogue text"`

34. **Voice contrast.** Each voice contrasts through pitch, timbre, accent, pacing,
    emotional baseline, or performance style.

### Dialogue

35. **Double quotes.** Spoken text in double quotes.

36. **Delivery note before quote.**

37. **Physical actions included.** When they affect delivery or generate sound.

38. **Multi-character chronological.** Alternates chronologically; actions/music/SFX
    between lines where listeners should hear them.

39. **Explicit attribution.** No unlabeled blocks of alternating quotes.

40. **Non-speech in brackets.** Ambient descriptions and non-speech sounds wrapped in
    square brackets.

41. **Prompt language = script language.** The prompt and the dialogue script are in
    the same language.

### Scene transitions

42. **Transition block format.** Audio state A → Transition trigger → Transition
    behavior → Audio state B → Forbidden carryover. All five fields present.

### Timestamp control

43. **Format.** `[start_time:end_time]` immediately before dialogue, in seconds with
    decimal precision.

44. **Used only when precision matters.** Omitted when event-relative cues suffice.

### Validation

45. **Character limit.** `text_prompt` ≤ 3000 characters.

46. **Duration limit.** Generated audio ≤ 120 seconds per call.

47. **No API concerns in prompt.** Does not insert "Max duration: 120 seconds" into the
    prompt — that is an API concern.

48. **Long requests split.** If requested generation > 120s, split before sending.

### Audio-video alignment (for explicitly selected separate lip-sync audio)

49. **Same dialogue text in both prompts.** Exact spoken lines match between
    Seed Audio `text_prompt` and Seedance, independent of optional brackets.

50. **Reference timing.** Check the selected role's evidenced duration limits
    without trimming source masters. Full delivery preserves independent picture
    and sound spans and tails; an input limit does not authorize conforming them.

51. **Shot timestamps align to audio.** Seedance shot time ranges match actual audio
    timing.

52. **Supported audio binding.** Use the ordered `reference_audio` binding
    (`@Audio 1`) only when that role is selected and verified for the destination.

### Brand-name pronunciation

53. **Respelling inside the dialogue line.** Any brand or domain name the
    voiceover must say correctly has its phonetic respelling written *inside*
    the dialogue line itself (not only in a note), using a real-word anchor
    rather than spaced or capitalized letters (e.g. `Echo-nos`, not `EH ko nos`).

---

## Seedream image generation

Source skill: `seedream-prompt`

Use this section only for user-invoked `/prompt-review`. Strict mode does not
invoke manual review or make it a handoff/generation gate. Findings do not
authorize generation or extra samples.

### Structure

1. **Task-first clarity.** Task > Subject and scene > Composition > Visual style >
   Constraints is a flexible writing aid, not a required template or measured
   weighting law. Omit irrelevant sections while preserving the requested result.

2. **Subject priority.** The primary subject and visual hierarchy are unambiguous.

3. **Reference labeling.** `@Image 1`, `@Image 2`, ... match actual input order.
   The `@` prefix is a repository convention, not a newly established 5.5 API rule.

4. **Reference precedence.** Each reference has a role, target, preserved features,
   excluded features and conflict priority, bound where it affects the output.
   A material or environment donor must not override the identity source's shape.

5. **Bindings stay consistent.** Reordering inputs requires rewriting every label
   and binding. Do not rely on an inventory alone or ambiguous image references.

### Reference limits

6. **Exact-model limits.** Preserve the selected model. Verify reference counts
   against its operation and current transport; Pro/Lite limits are not family limits.
7. **Batch versus variations.** Verify provider batch support separately from
   adapter `variations` (separate calls). The documented 5.5 and 5.0 Pro bindings
   do not support provider sequential batches; do not silently switch models.

### Task type

8. **Correct task type.** T2I, I2I, Image Editing, Sequential Generation, or
   Infographic/Information Visualization; extraction and channel adaptation
   state the requested change and protected features.

9. **Sampling follows review mode.** Default uses one image; strict proposes
   three when applicable. An explicit requested count or creative alternatives
   wins; each submit still needs confirmation. Comparison samples keep identical
   prompts, references and effective settings except supported seed variation.
   Seeds do not guarantee identical pixels.

### Subject

10. **Stable attributes.** Include enough supplied attributes to identify each
    subject; do not invent identity details to meet a quota.

11. **Multi-subject priority order.** Listed in order of visual priority.

### Photographic treatment, when requested

12. **Intent preserved.** Camera/film terminology is optional shorthand. Do not
    require it or a cinematic treatment for every photographic image.
13. **Lighting appropriate.** Soft, flat or shadowless light may be intentional.
    Preserve the approved lighting unless changing it is within scope.
14. **Identity protected.** Describe relevant existing texture; do not invent
    freckles, age, wrinkles or material damage as a generic realism cure.
15. **Readable hierarchy.** Lead with the requested result. Headings and ordering
    are clarity conventions, not proven positional weighting laws.
16. **Focused exclusions.** Use only necessary scope or demonstrated-leakage
    exclusions; do not demand aggressive boilerplate negatives.
17. **Diagnosis grounded.** Cite a visible symptom in a supplied output or label
    the example hypothetical. Do not promise a prompt will produce realism.
18. **Parameters verified.** Actual size and optimization settings belong in
    request metadata and must be supported by the resolved live model/tool.

### Text in image

19. **Routing boundary.** Model-rendered text is present only when the user
    expressly accepts it as expressive and non-exact. Delivery-critical copy,
    data, UI, pricing, CTA, logos, or pixel layout is a MAJOR routing defect;
    require a text-free generative layer plus deterministic finishing.

20. **Quoted prompt intent.** Accepted model text is in double quotes and its
    surface, line breaks, hierarchy, alignment, weight, spacing and safe margins
    are clear where relevant; quoting does not establish pixel-exact output.

21. **Proofread output.** Inspect every character, line break and spatial hierarchy
    in supplied results; OCR can assist but is not a substitute for inspection.
    Small text may remain unstable. A prompt-only check cannot pass unseen text.

### Constraints

22. **Creative constraints inline.** No separate `negative_prompt`. Supported
    settings such as `background`, `output_format`, size and structured edit fields
    stay in request metadata, not creative prose.

23. **Quality directives and negative constraints.** Only those that materially affect
    output.

### Prompt length

24. **Focused length.** Keep simple prompts concise; retain necessary bindings
    and preservation constraints in complex edits. The verified MCP adapter's
    4,000-character limit includes added coordinate markup, not just user prose;
    do not infer that limit for a different UI or transport.

### Coordinates and output acceptance

25. **Separate coordinate interfaces.** Guide prompt boxes
    `bbox=[xmin, ymin, xmax, ymax]` use 0-1000 as layout guidance, not exact pixels.
    MCP structured `bbox={x1,y1,x2,y2}` and `point={x,y}` use integers 0-999
    on the first image only. Put the edit target first and rewrite bindings after
    reordering. Let the adapter add markup; never duplicate it in the prompt.
    Reject missing source images, inverted, degenerate or out-of-range boxes.
    Explicitly map a valid guide endpoint 1000 to 999 at the adapter boundary;
    recompute after cropping or reframing, not by silently clamping invalid input.

26. **Transparency intent and alpha.** Distinguish transparent canvas, opaque
    cutout, translucent material and interior holes. Verify exact-model support
    for creation versus extraction and compatible `background`/`output_format`
    settings. Decode actual alpha; a PNG extension or painted checkerboard is
    insufficient. Inspect fine edges, holes, halos and composites on light and
    dark backgrounds. Partial alpha alone does not prove correct translucency.

27. **Marked edits.** Use unique region numbers, move source/destination,
    operation order and replacement size/orientation. Remove visible markers.
    Inspect edited and unmarked areas; coordinates do not guarantee strict
    boundary compliance.

28. **Accepted-output edit chain.** Use the last approved output as the next
    input, one major delta per round. Each prompt is self-contained with protected
    features, not assumed conversational memory. Retain accepted artifact/hash,
    prompt, reference order, exact model and settings in the chat handoff; save
    records only on request. Reject drift and roll back to the last accepted
    image; successful generation is not approval.

29. **Channel adaptation.** Distinguish deterministic resize/crop from generative
    recomposition and capability-verified canvas extension. State target ratio
    and safe areas; do not stretch subjects. Inspect identity, proportions,
    crop, hierarchy, text, logo clearance, actual dimensions and required alpha.
    Preserve approved reference identity. Exact-copy deterministic finishing is
    a destination-workflow handoff, not a new capability of this prompt workspace.

30. **Information and layers.** Conceptual dashboards and decorative charts are
    not factual data graphics. Exact labels, values and units need deterministic
    charting/design with editable copy outside this workspace. Provider layer
    decomposition/OCR is unavailable through the current MCP tool; do not invent
    controls or layers.

---

## Seedream character sheet

Source skill: `seedream-character-sheet`

### Layout

1. **Three-panel default.** Back full-body, front full-body, face close-up. Unless user
   explicitly asks for more panels.

2. **Neutral gray background.** Default studio background — neutral gray, never
   scene-specific. Deviates only if user explicitly wants stylized/filmic sheet
   background.

3. **Panel order.** Back full-body first, front full-body second, frontal close-up
   third.

### Subject

4. **Reference binding.** Each reference is bound inline.

5. **Required elements.** Age, ethnicity/cultural identity, 2-4 stable facial traits,
   hair and headwear, costume, key accessories.

6. **Same person statement.** Explicitly states it is the same person in all panels.

7. **No held props.** Nothing held, carried, aimed, or operated appears in the sheet;
   branded, recurring, or story-critical ones need separate `prop_` sheets,
   while incidental objects may be text-only in scenes. Scene-variant wearables (e.g.
   sunglasses worn only in some scenes) are also excluded and made props instead.
   Only always-worn outfit elements (hat, helmet, eyewear, jewelry) may appear.

### Setting

8. **Default background.** Neutral gray seamless, no props, no held objects, no
   furniture, no environmental clutter.

### Lighting

9. **Neutral, not scene-specific.** Soft, even studio light, flat fill, neutral
   white balance, no mood, no dramatic shadows, no hotspots, no blown highlights.
   Lighting never changes to match the character's scene or story mood.

10. **Consistent across panels.** Lighting is identical across all three panels.

### Composition

11. **Three panels only.** No extra panels.

12. **Same identity.** Same character identity across all panels.

13. **Readable silhouette.** Costume silhouette readable in body panels.

14. **Face authority.** Close-up panel is the face authority.

### Constraints

15. **Common negatives.** No extra panels, no profile panel, no 3/4 panel, no props in
    hands, no held objects/weapons, no background variation, no scene lighting or
    color cast, no distorted hands, no extra fingers, no watermark.

### Workflow

16. **Cleanup check.** When the requested downstream reference policy requires
    one readable face, inspect for extra faces and return the defect to the
    caller. Cleanup is conditional, non-destructive, and requires new selection;
    this reviewer does not invoke an editing skill.

17. **Element delivery.** Chat is the default; check a saved element record
    only when saving was explicitly requested.

18. **Selected variant.** An inspected, mode-authorized selection is recorded
    in chat or an explicitly requested file; it never replaces user locks,
    rights, consent or per-submit generation opt-in.

---

## Seedream location asset

Source skill: `seedream-location-asset`

### Location

1. **Place described.** Interior/exterior, function, scale, spatial mood, core
   architectural identity.

### Era and world rules

2. **Historical period.** Stated if relevant.

3. **Geography/climate.** Stated if relevant.

4. **Technology limitations.** Stated if relevant.

5. **Realism constraints.** Explicitly excludes modern intrusions if realism matters.

### Set dressing and objects

6. **1-3 hero set pieces.** Key defining objects.

7. **Practical objects.** Objects that imply use.

8. **Material realism and wear.** Surfaces show wear and use.

9. **Depth cues.** Foreground/midground/background.

10. **Lived in.** Not empty — feels inhabited.

### Style

11. **2-4 strong anchors.** From: photorealistic, cinematic, naturalistic editorial
    reference, grounded realism, film still, period-authentic.

### Lighting and atmosphere

12. **Practical key source.** Where the light comes from physically.

13. **Time of day / weather.**

14. **Shadow falloff.**

15. **Haze / dust / smoke / moisture.** Atmospheric particles.

16. **Brightness.** How bright or restrained the scene is.

### Composition and lens

17. **Establishing vs detail vs reference sheet.** Type stated.

18. **Camera angle.** Eye level / high angle / low angle.

19. **Lens length.**

20. **Aspect ratio.**

21. **Depth of field.**

### Ordering rules

22. **Place before mood.** What the place is comes before how it feels.

23. **Era/world rules before lens/style polish.**

### Constraints

24. **Common negatives.** No characters, no modern props, no plastic CGI surfaces,
    no bright white cyc background unless explicitly requested, no text overlays, no
    watermark.

### Three prompt patterns

25. **Pattern A — Reusable asset.** Stable architecture, clear material language,
    minimal action, readable space, reusable identity.

26. **Pattern B — Cinematic establishing still.** Emotional lighting, camera language,
    atmosphere, foreground/background layering.

27. **Pattern C — Reference-preserving iteration.** I2I for every reference-guided
    location prompt.

---

## Seedream prop asset

Source skill: `seedream-prop-asset`

### Gate

1. **Threshold met.** The prop is branded, story-critical, recurring across two
   or more shots, or a scene-variant wearable. A generic or briefly held object
   is text-only; a sheet prompt for it is a MAJOR scope defect unless the user
   explicitly asked for that sheet, which is then noted as below threshold.

2. **Acquisition first.** A real brand, logo, or labeled product the brief
   authorizes uses an asset the user supplies unless none is usable, a stylized
   substitute is requested, or acquisition is blocked. An unauthorized brand
   stays de-identified. Inventing a real logo is CRITICAL.

### Layout

3. **View plan declared.** Front and back by default; add side when requested
   or when the profile carries identity. Honor an explicit single-view request;
   existing hero references remain valid. State variants use only the faces
   where the change is visible. A detail close-up is separate, never a fourth
   view. Three views at most, in front/side/back row order for compact objects;
   front and back above a centered side profile for long objects.

4. **Background.** Pure white seamless with a faint contact shadow, or neutral
   light gray, with the same faint contact shadow, for white, silver, chrome,
   clear, or translucent objects, or when the project's approved props or
   character sheets already use gray. No colored, gradient, textured, or scene
   background.

5. **Neutral lighting.** Even, neutral white balance, identical across views.
   Shape-revealing highlights and gentle raking light are allowed; scene mood
   and color casts are not.

### Subject

6. **Reference binding.** Each reference is bound inline to the property it
   controls; an approved prop or authorized photo leads.

7. **Task type.** I2I whenever any reference guides a visible property,
   including every state variant of an approved prop.

8. **Count stated.** One object, or an exact matched-set count with one shared
   design.

9. **Identity description.** Silhouette and proportions, real-world size in
   words, materials and finish, colors, and the identity-critical details the
   video must reproduce. Wear and damage appear only as the story needs. Each planned face names its
   own details; opposite flanks use landmarks and frame terms, not left/right
   wording alone. Do not invent a missing branded face or its copy.

10. **One canonical state.** Open/closed, lit/unlit, folded/extended or similar
    is stated; emissive parts stay off unless the glow is canonical.

11. **Descriptor continuity.** A variant or revision reuses the approved
    descriptor word for word.

12. **No hands or wearers.** Held props appear without hands; wearables appear
    unworn, without a person, head, mannequin, or body part. A body continuity
    mark is the exception: it is an I2I close-up with laterality stated.

### Style

13. **Project style match.** Render style matches the approved characters and
    locations; 2–4 anchors.

### Composition

14. **Whole object.** Every full view fits the whole object with a requested 6%
    margin to canvas edges and neighboring views. A continuous seamless field
    separates views by empty space, without boxes, borders, labels or dividers.

15. **Consistent scale.** Views share one scale and design, compared by whole
    object height and an actual stable feature. Wheel diameter applies only
    to wheeled objects; roof fixtures only to vehicles that have them.
    Three-quarter front/back show opposite flanks and the profile shows the
    chosen near flank.

### Text in image

16. **Text route.** No readable text by default; a blank surface or an angle
    that hides the print is preferred, and pseudo-letters count as invented
    text. Identity-critical copy comes from a supplied authorized asset or is
    added in post; model text appears only when non-exact text is expressly
    accepted.

### Constraints

17. **Common negatives.** No hands or people, no other objects or duplicates, no
    unwanted background, no readable text or logos, no cropped edges, no extra
    views, boxes, borders, divider lines, labels or captions, no watermark —
    only those that apply.

---

## Storyboard prompts

Source skills: `seedream-storyboard`, plus `template-factory` (storyboard prompts)

### Core rules

1. **One frozen, decisive moment per panel.** Not a collage or multi-panel grid.

2. **Dynamic panel count.** When an upstream analysis (a video or frame pass,
   `scene-craft`, or a script/beat sheet) has identified
   N scenes/shots, the board defaults to one panel per identified scene/shot —
   not a fixed budget. A user-specified smaller count is honored only when
   explicit, with omitted shots recorded as motion notes.

3. **Storyboard handoff eligibility.** Storyboard grids, panels, crops and
   animatics stay planning-only, never video conditioning. Selection, hashes,
   cleanup, style overrides and promotion labels cannot change planning origin.
   Translate staging into text. An independently authored, selected text-free
   production still is a separate eligible asset subject to verified role
   support, rights and approval. Historical board-linked records remain unchanged.

4. **Explicit canon.** Recurring identities, locations, props, and style are in an
   explicit canon section.

5. **Canonical Element sheets attached.** When matching Element sheets exist, they are
   attached to the generation request — not substituted with text descriptions.

6. **Screen direction and geography.** Treated as sequence-level constraints.

7. **Natural language.** Coherent natural language, not comma-heavy keyword piles.

8. **References bound by role and target.** Every reference bound with exact `@Image N`
   tokens.

9. **Production notes outside image.** Arrows, labels, dialogue, timing, and production
   notes are outside the generated image unless visible story-world text is required.

### Panel prompt structure

10. **References.** Each reference labeled with role (character identity, location
    geometry, prop identity, composition control, approved style).

11. **Panel purpose.** The new story information or emotion this panel communicates.

12. **Subject and decisive moment.** One frozen moment. Every visible subject, pose,
    expression, action, and prop named. Identity and prop references bound inline.

13. **Setting and state.** Location, time, weather, persistent landmarks, visible
    object state. Location reference bound inline.

14. **Staging and continuity.** Screen-left/right positions, foreground/midground/
    background, eyelines, distances, overlaps, travel direction, entrances/exits, and
    what must match the previous panel.

15. **Style.** Medium, realism level, palette, stable treatment. Style reference bound
    inline when provided.

16. **Lighting.** Source, direction, quality, color, and atmosphere.

17. **Composition.** Aspect ratio, shot size, camera height/angle, lens intent,
    framing, depth, and focus priority. Composition guide bound inline when provided.

18. **Constraints.** Appropriate quality (draft or final), preservation (approved
    identity, geometry, pose, state, style), exclusion (only material faults — no text
    overlays, labels, storyboard borders, watermarks, unintended subjects, duplicated
    faces, control-guide marks).

### Sequential generation

19. **Sequence contract.** Cohesive ordered set of N separate images, one per panel.
    Recurring identity, wardrobe, location geometry, prop design, palette, and
    rendering style kept consistent.

20. **Each image is one moment.** Not a collage or multi-panel grid.

21. **Global visual canon.** Stable identity, location, prop, style, aspect ratio, and
    lighting rules stated before individual panels.

### Revisions

22. **Regeneration preferred.** After a composition is approved, prefer a revised
    prompt over re-authoring from scratch; tool-based pixel cleanup is out of
    scope in this workspace.

23. **Seeds for tracking.** Used for experiment tracking, not as the identity system.

### Status

24. **Review on generation.** Technically successful generation enters `review`.

25. **Explicit user choice.** Only explicit user choice sets `selected_variant` or
    `approved`.

---

## Seedance music video

Source skill: `seedance-music-video`

### Format and genre

1. **Format declared.** Performance, narrative, conceptual, lyric, visualizer,
   or hybrid — with address mode (direct / indirect / none).

2. **Treatment serves intent.** Preserve approved visual choices. Format and
   style are brief-derived, following the desired audience effect and available
   track evidence. Custom treatments and coherent hybrids are valid; genre
   recipes are optional examples, not compulsory locks or a ban on coherent hybrids.

### Song map

3. **Readable section intent.** A section may carry ordered events, reveals or
   sustained attention. Check causal order and perceptual outcomes without a
   single-event quota; preserve locked action, reveal timing and stillness.

4. **Repeated sections have an intentional relationship.** Escalation, restraint,
   repetition or counterpoint follows supplied audible changes or the requested
   effect. A quiet return need not become larger or faster.

5. **Structure is evidenced.** Do not invent a bridge or assume it requires a
   new location, wardrobe or angle. Label a plan provisional when no track or
   user section map supports exact structural claims.

### Audio contract

6. **Audio treatment explicit.** Distinguish native output audio from timing
   conditioning. Use supported direct `@Audio N` or an optional, selected
   black-sync `@Video N` only after verifying the destination's timing-input
   capability; otherwise mark support unresolved. Container acceptance alone
   does not prove audio conditioning. Existing-footage edits keep the source
   scene as `@Video 1`. Confirm current-song permissions, never infer them
   from a prior project or supplied file.

7. **Lip-sync lines verbatim.** Use `{...}` only with verified destination
   syntax; plain-language attribution is valid. Match the audio master exactly —
   no paraphrasing, no reordering, no omitted lines.

8. **Lyric timing follows audio evidence.** When coverage or synchronization
   requires per-line timing, use audio-measured slots (e.g. `[X-Ys] { line }`
   only with verified syntax), retaining
   raw measurements separately from proposed edits. With unavailable audio or
   unverified timings, use ordered cues and label timing provisional. Genre or
   fast delivery alone does not require timestamps or justify invented timings.

9. **"No line skipped" mandate present.** When the timestamped timeline is
   used, the prompt includes an explicit instruction that no line may be
   skipped, shortened, mumbled, or reordered.

10. **Native audio caveat acknowledged.** If native audio is requested, it may
    re-perform or alter the reference. Exact-song delivery retains the original
    master and checks audio equality separately from visible lip-sync playback;
    neither carrier choice nor restoring the master guarantees mouth accuracy.

### Beat contract

11. **Audio events named.** Which beats trigger cuts and camera moves —
    not just "cuts on the beat."

12. **Cuts follow intent and evidence.** Do not assume verses are quiet, choruses
    are loud, or every edit precedes a downbeat. Preserve continuous performance
    and unmetered pauses when requested; keep raw timing separate from simplification.

### Structure

13. **Right-sized (4–30s).** One song section per pass, or an explicit
    continuous one-take. Not padded to fill 30s.

14. **Treatment summary is optional.** When useful, summarize brief-derived
    continuity, coherent hybrid choices and deliberate section transitions.
    Preserve an approved single-style treatment; judge fidelity and readable
    transitions, not a mandatory genre lock or style-seal phrase.

### Rap-specific (when applicable)

15. **Timing is proportional.** Use source-grounded lyric timing when coverage
    or synchronization requires it; rap genre alone does not mandate timestamps.
    Do not invent beat timings or claim to have listened to unavailable audio.

16. **Delivery cue present.** The prompt includes a physical delivery cue
    (e.g., "jaw opening fully on vowels, lips stay in frame throughout").

---

## UGC hooks and scripts

1. **Product truth.** Trace numerical, comparison, performance and personal-use
   claims to supplied evidence. No invented trial duration, testimonial, saving
   or demonstrated result. Missing facts allow a truthful demonstration angle.
2. **Audience objection.** The hook addresses the supplied concern using a
   supported feature or proposed demonstration, not unrelated hype.
3. **Distinct angles.** Requested alternatives differ in persuasive mechanism
   or objection addressed; synonym swaps alone do not make distinct concepts.
4. **CTA fidelity.** Preserve the supplied offer and destination. Do not invent
   a discount, guarantee, scarcity claim or purchase experience.
5. **Mode respects scope.** Hooks/scripts can be completed without generating
   assets. Hypothetical actors are not evidence of real customer experiences.
