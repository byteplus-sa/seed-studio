---
name: brief-intake
description: >
  Shape a creative brief around the intended audience reaction, central visual
  idea, and practical constraints. Derive applicable directing choices with
  reasons; offer two distinct treatments during exploration or a compact
  proposal when direction is settled. Confirm only decisions that need a lock.
  When the brief cites real brand video ads or other footage for visual or motion
  inspiration, record that reference and hand off to template-factory for
  analysis (agent video pass, or local frame extraction when the video cannot be
  watched) — do not treat scripts or article text as the reference. Use for a
  new project or a scoped brief revision. Never generates media.
---

# Brief Intake

Translate intent into a usable creative direction. Genre is context, not a
lookup key that selects a look. Preserve the user's existing creative choices
and authorization; distinguish recommendations from confirmed decisions.

## When to use

Use during project development, when a brief needs sharpening, or when the user
requests recommended directing choices. This leaf capability writes a brief or
proposal; it does not invoke other skills or generate media.

## 1. Read intent and constraints

Read the supplied brief and existing confirmed decisions first. Extract:

| Input | Question it answers |
| --- | --- |
| Audience and context | Who sees it, and where or under what viewing conditions? |
| Intended reaction | What should the viewer feel, understand, remember, or do? |
| Central visual idea | What specific event, contrast, image, or recurring action carries that reaction? |
| Story/product truth | Which supplied facts, characters, relationships, and claims must remain accurate? |
| Constraints | Runtime, format, available references, budget posture, delivery needs, forbidden changes |
| Tone/genre references | What useful quality is being borrowed, and which convention should be avoided? |
| Confirmed decisions | Which axes and identities are already accepted? |
| Where the feeling lives | Which channel carries the inner state (performance, sound, light, framing, edit) rather than literal effects? |
| Source bible | Is there a source text, script, brand book or prior canon whose lines and details must survive every stage? |
| Quality bar | Whose reaction is the bar: a named person, the user's own taste, or a past version of the user? |
| Sound plan | Is the deliverable silent, on-camera dialogue, ambience or score, and is a separate sound bed acceptable? |
| Look | Is a grade or capture-format look requested, or should the original model colours remain? |
| On-screen copy | Which captions, title, CTA or end card should be listed separately for post? |

When a tone or genre reference is a **concrete brand video ad or other footage**
(URL, campaign name, or user-supplied file) meant for visual or motion
inspiration, record it under constraints or creative intent and **hand off** —
this skill does not fetch or analyze media. Downstream work needs media the
reviewer can actually inspect, preferably a decodable local copy. Prefer an
**agent video pass** when the client can watch it, or **local frame extraction**
(`ffmpeg`/`ffprobe`) read as images, with measured timing and timestamped
evidence. Route full reverse-engineering through `template-factory`; a lighter
visual pass uses the same evidence requirements.

When native perception is insufficient, the caller may use an available
capable analysis tool under the user's privacy, cost and offline constraints.
Do not require uploads or tool setup for analysis the host can already perform.
A local CLI does not prove on-device inference; explicit offline work requires
verified on-device perception or human evidence. Audio needs actual auditory
perception or documented human listening. Transcripts, scripts and article
write-ups can support words or claims, but cannot replace visual inspection or
establish soundscape. These are handoff requirements, not tool calls by this leaf.

An absent genre is not a blocker. If intent is clear, derive a proposal from it.
Ask a focused question only when missing information materially changes the
result. With no usable brief, ask what is being made, for whom, and the intended
reaction; develop reversible suggestions while runtime or format is pending.
Label assumptions instead of inventing audience research or product facts.

Three questions sharpen a dramatic brief without adding a questionnaire.
Answer them from the brief when you can and ask only when the answer changes
the result:

- **Where does the feeling live?** Prefer suggestion over spectacle. Pain,
  power or fear carried by the performance, a sound and the light usually
  lands harder than a literal effect; keep one brief stylized image when the
  idea needs a picture (a burned-texture hand instead of fire).
- **Is there a counterpoint?** A location, prop or sound that plays against
  the genre can state the world's rules without dialogue (a science-fiction
  test held in a library says this world has no computers). Propose one only
  when it serves the reaction.
- **What is the bible?** When a source exists, list the lines, images and
  details that must survive, and recheck them at script, generation, edit and
  music. Fidelity to the source is a confirmed decision, not a style.

State the creative spine in one sentence: **For [audience/context], show
[specific idea] so the viewer [intended reaction].** This is an aid to reasoning,
not mandatory output syntax. A static asset can use a visual contrast rather
than a narrative event; a sound-only brief can use a sonic idea.

For a moving-image brief, flag sound-route decisions that affect the result.
Native dialogue, picture-only with a separate ambience/score bed, separate
lip-sync audio and silence serve different needs. Native audio can add unwanted
music or voices despite exclusions, so propose picture-only when strict control
matters and the destination supports it. Preserve any accepted audio choice;
separate lip-sync audio remains opt-in. Leave a grade or film look out unless
requested. These are scoped proposals, not new mandatory axes or approvals.

## 2. Choose the appropriate depth

- **Fast proposal (default):** give one compact treatment tied to the creative
  spine and only the axes needed to execute it. When camera/light planning or
  energy direction is requested, tie their stance and energy level (restrained,
  standard or kinetic) to the intended reaction. Do not produce alternatives or
  a questionnaire merely because a project is new.
- **Exploration:** when the user asks for directions, alternatives, or help
  choosing a concept, offer two materially different treatments. Distinguish
  them by central idea, viewpoint, or emotional strategy, not a lens or palette
  swap. Each names its idea, key visible/sonic moment, rationale, and tradeoff.
  Do not generate either or treat a recommendation as selection.
- **Full Q&A (opt-in):** walk applicable axes with rationale and alternatives
  when the user requests it. Do not revisit already accepted choices unless
  their prerequisites changed or the user wants a revision.

For example, an invitation to feel welcome might use a subjective doorway view
with people making room, or a still overhead table accumulating personal objects.
The alternatives change the storytelling mechanism; warmer versus cooler grading
of the same shot does not constitute two treatments.

## 3. Derive applicable axes from the idea

Every recommended choice needs a concrete visible or audible purpose and a
tradeoff where it affects feasibility. Choose fewer coherent instructions over
an exhaustive preset stack. For a requested shot plan, carry the accepted
camera/light stance through the shots; a static camera is a valid choice when
the format or intended reaction calls for it.

| Axis | Derivation | Composition hint for a calling agent |
| --- | --- | --- |
| Structure | Narrative development needs an event and progression; one-off static assets do not | `scene-craft` |
| Acting | Specify an observable reaction/tactic only if a performer matters; match detail to framing | `seedance-acting-console` |
| Camera | Choose viewpoint, framing, and necessary movement to reveal the central idea | `seedance-camera-presets` |
| Lens | Describe perspective, separation, and context; add optical terms only when useful | `seedance-lens-presets` |
| Lighting | Motivate a source and guide attention to the story/product truth | `seedance-lighting-presets` |
| Grade | Support tone and reference fidelity; retain accepted palette | `color-grade-palettes` |
| Pacing | Give the action enough time; stillness, repetition, contrast, and escalation are choices | `seedance-pacing-presets` |
| Staging | Define geography only when action or relationships depend on it | `blocking-map` |
| Medium | Preserve requested medium; propose only when the idea benefits from that choice | `seedance-animation-styles` |
| Audio | Honor silent/native/soundtrack requests; separate lip-sync audio remains opt-in | `seed-audio-prompt` / `seed-audio-commercial` |

These hints do not require loading sibling skills. Never require acting for a
product-only still, a camera move for an audio brief, or a speed ramp because a
genre is energetic. Genre examples such as noir concealment or comic reaction
holds are optional creative heuristics, not model requirements or performance
claims. A bright noir comedy can use information withholding in cheerful light;
it need not inherit a neon palette or fear performance.

For hybrid briefs, combine compatible intent, not the first matching genre row.
When signals truly conflict, preserve explicit choices and identify the smallest
remaining decision. Explain what each interpretation would make the viewer feel.

## 4. Confirm and persist the right scope

Present the proposed direction with reasons, then identify decisions actually
requiring acceptance: a new concept, a changed lock, or an impactful assumption.
Do not demand a fixed checklist of confirmations for prompt-only drafts. Silence,
an undisplayed default, and acceptance of one axis never approve an entire set.
An explicit acceptance of a displayed set confirms that set. Existing task
instructions can already establish an accepted choice; do not request it again.

When project-file updates are in scope, record in `project.md`:

```yaml
creative_intent:
  audience: first-time visitors
  reaction: feel welcome
  central_idea: a crowded table makes room for one more place setting
  feeling_lives_in: the space the family makes, not anyone's words
  quality_bar: the user's memory of their grandmother's table
  source: user_confirmed
directorial_axes:
  camera:
    value: static overhead framing keeps the new place setting visible
    rationale: the change in shared space carries the welcome
    source: proposed
  audio_mode:
    value: native
    source: user_confirmed
    approval_evidence: "User requested native table ambience."
locked:
  audio_mode: native
```

`proposed` means recommendation; `defaulted` means a disclosed working assumption;
only `user_confirmed` choices enter `locked`. Preserve prior evidence for unchanged
choices. Scene overrides carry their own value/source/evidence and do not overwrite
project-wide locks. For a one-axis revision, change that axis and identify any
actual downstream dependency; do not reopen the whole brief. In prompt-only or
chat-only work, return the proposal without creating project files.

## Worked repairs and checks

Read [worked repairs](references/worked-repairs.md) when a proposal feels generic,
a hybrid brief produces competing defaults, or alternatives differ only in style.
These are hypothetical teaching cases, not measured generation outcomes.

Before returning, check that the proposal serves the stated reaction, names a
specific idea, says where the feeling lives, respects constraints, accepted
choices and any source bible, and omits irrelevant axes. Two treatments appear only when exploration is wanted, and differ in
mechanism. Unknowns remain labeled; recommendations remain unapproved until the
user chooses them. Evaluate the reasoning and usefulness, not exact headings.
