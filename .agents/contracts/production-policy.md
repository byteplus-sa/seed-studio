# Production policy

## Review depth

Follow [review-mode.md](review-mode.md): `default` uses a compact inline
preflight; `strict` adds detail without invoking manual prompt review.
This is independent of `approval_mode`, whose default is `approve_for_me`.
Neither mode requires a review record for handoff. Detailed prompt review
runs only when the user invokes `/prompt-review`; never manufacture a report.

## Stage evidence and authorization

Draft brief and scene breakdown can identify assets before canon exists. Before dependent prompt authoring, require the appropriate approved recurring/critical element descriptors and declared reference roles. Canon may be defined by prompt-only element sheets (Seedream prompts) or by acquiring and approving real brand/product/logo descriptors; prompt-only authoring may deliver a draft without generating or downloading assets. When the brief borrows visual or motion grammar from a cited brand ad or other footage, obtain a watchable copy first (the user's file, or a link the user can open) and analyze it by agent video pass or local frame extraction; do not treat scripts or article text as the reference.

The normal flow is brief → draft breakdown → required canon → optional storyboard prompts → optional requested lip-sync audio notes → video prompts → handoff. Handoff of the prompt package marks completion; do not infer completion from filenames.

## Prompt-package memory

Keep one record per authored prompt: the exact prompt text, its ordered reference list, and the parameter block. Save drafts under `projects/<project>/prompts/` only on explicit request; otherwise deliver in chat. Retain earlier revisions, rejected wording, and decisions while adding the current package.

Update the record after every material change to a brief, breakdown, element prompt, storyboard prompt, audio prompt, or video prompt. A handed-off prompt is frozen; changed inputs need a new prompt version.

Under `approve_for_me`, choose coherent in-scope defaults against the brief and
label them `agent_confirmed`; user choices remain `user_confirmed`. Under
`ask_for_approval`, keep recommendations proposed until the user chooses.
Approval persists within its stated scope. Authoring a prompt does not approve
an unseen result.

Either a genuine user choice or an agent decision under `approve_for_me` can
select an inspected candidate or approve a package. Under `ask_for_approval`,
automated advice uses `recommended_variant`. Preserve earlier selections and
user-written metadata when updating a bounded field.
These are creative decisions, not per-submit generation opt-in, rights or
consent. Explicit user locks and requests to choose personally always win.

## Directing guidance

Identify assets using [element-identification.md](element-identification.md). Copy locked identity descriptors faithfully into prompts where needed. Use positive, observable direction. Necessary technical exclusions may define a limited edit scope; negative-only prompt lists are discouraged rather than universally forbidden.

Narrative shots need events, intent, blocking and observable end states. Static character/prop sheets need clear composition and visible design; music/SFX/ambience need a sound arc appropriate to the requested artifact. Do not force story tactics into a static-image or sound-bed prompt.

Exact copy, typography, logos, screen/UI layouts, title cards, posters, product lineups, and price/CTA treatments are out of scope in this workspace: say so rather than improvising a prompt. Use Seedream prompts for invented photographic or illustrative imagery, expressive texture, and image synthesis.

Never ask the model to render overlay text such as captions, taglines, CTAs or end cards; keep generated footage text-free — on-screen text is added in post by the destination workflow, which is out of scope here. A transparent delivery graphic and a solid-background model reference are separate assets; never use a white matte as fake transparency.

Single-person references should preserve the intended identity and avoid cloning. Preserve approved visual descriptors and the face anchor; do not infer gender identity from appearance. Tool-based post-generation pixel cleanup is out of scope here — regenerate from a revised prompt instead. Image-editing prompts (I2I edit instructions) remain prompt deliverables.

Real people and source footage need confirmed rights before a prompt depends on them. A real, identifiable person used as a target (a likeness reference, a voice) needs the user's confirmed consent and, for photoreal likeness generation, a confirmed approval for that use. Source footage needs confirmed rights, and identifiable real performers in it need confirmed consent for reuse of their performance. Note each confirmation in the prompt package. Unknown rights, identity, and consent facts stop the work; a creative choice never supplies them, and calling a job a test does not either. Offer an invented cast or a consenting performer instead. A privacy or sensitive-content rejection the user reports is evidence to diagnose: never crop, blur, stylize, recompose, or swap inputs to get a real likeness or real footage past a check.

An explicitly selected supported conditioning input is a promoted composition or motion reference, not a control-only asset. Record the selected source, its current hash when it is a local file, and the intended reference role. Changing a flag alone does not grant approval.

## Request preflight and optional review

Before handing off a **generation-bound** prompt, freeze its exact text in the
chat package or requested file, list ordered reference roles and check required
inputs and supported parameters once. Record current hashes for local reference
files in the chat package or requested record. Reuse valid capability evidence for
unchanged inputs; refresh on uncertainty or changed model/operation.
Neither mode starts manual review or waits for a review record.

Acquired brand, logo, or packshot descriptors require inspection and a selection
under the approval mode before dependent use. Rights are separate from that
creative decision. See [element-identification.md](element-identification.md).

When the user runs `/prompt-review`, use explicit prompt type, model, operation, language, requested axes, may_change and must_preserve to route the review. A completed review is bound to the request hash and lists applicable rule outcomes and evidence. Missing/empty reviewer output is incomplete. Static image, audio, editing and narrative checks are applied to their relevant artifact types.

The request hash covers exact prompt bytes, model/operation/effective parameters and ordered reference roles/bindings. Credentials and timestamps are excluded. Changed request content makes an earlier review result stale.

## Handoff and optional generation

Without a generation request, deliver prompts for the destination UI and stop.
When generation is requested,
follow [generation-transport.md](generation-transport.md) for exact-package,
per-submit opt-in, not financial approval. No project budget, spending cap,
cost estimate or spending authorization is required. Cost information is
optional; this workspace has no task registry or spending ledger.
Do not introduce a production stage ledger or review-report requirement for
prompt delivery in either mode.

Provider-side outcomes are diagnostic evidence for revision: rejection is
evidence to diagnose, not a false positive by default, and reported success
does not approve an output. Legitimate creative revisions stay within
authorization and record the exact delta.

## Generation and review defaults

Every new Seedance 2.5 generation starts with explicit `resolution: "480p"`
and boolean `draft: true`, including edits, extensions and creative retries.
Plain 480p is not native draft mode. This first-test policy is independent of
review depth and final delivery resolution. Parameter notes follow it even
when the output is prompt-only; authoring does not authorize submission.

The caller inspects and selects a successful native draft before a separately
authorized promotion using `draft_task_id` and supported output settings.
Changed prompt text, references, duration, ratio or audio settings require a
new native draft, not a modified promotion. Re-check the final output.
Resolve a missing draft control in a Seedance 2.5 tool/UI instead of silently
submitting non-draft 480p. Other video models without native draft mode use
an ordinary, non-promotable 480p test; a final is a fresh generation.

Prefer per-shot prompts at natural duration over compressed timelines. Continuous single-take extension is exceptional; flag every seam. Separate lip-sync audio remains opt-in; follow [audio-video-alignment.md](audio-video-alignment.md).

Use the requested suitable image resolution and the native-video policy above.
Default mode uses one image sample. Strict mode proposes three stochastic
samples when applicable. Explicit requested count wins. Additional generations
require their own exact-package confirmation; review depth never authorizes them.
Sampling sets keep identical prompt, references and effective parameters except
supported seed variation. Creative alternatives change only requested variables.
Watermark handling follows the supported destination parameters.

Verify the package once before handoff: ordered references match the bindings
and the parameter block is complete and within documented limits. When a review
was requested, its record must match the final request; otherwise no review
record is required.

## Reserved upstream rules

`canvas.stage_current` and `canvas.snapshot_current` are reserved for production workspaces with a canvas; this workspace intentionally omits one.
