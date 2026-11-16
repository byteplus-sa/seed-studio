# Review mode

Review depth and decision authority are independent:

```yaml
review_mode: default
approval_mode: approve_for_me
```

`review_mode` accepts `default` or `strict`. `approval_mode` accepts
`approve_for_me` or `ask_for_approval`. Missing fields use the values above for
new actions only; never reinterpret old approvals. Invalid values need
correction, not an inferred fallback.

For chat-only work, "use strict review" or "use default review" sets the mode
for the current task without creating files.
Save a mode change only on explicit request in `project.md` frontmatter.
Read the current task choice first, then that brief, then the defaults.
Changing review depth never changes approval authority. A request to choose
personally overrides automatic selection for that choice.

## Default

- Compose and deliver the requested prompt without loading the full review
  pipeline, emitting checklist reports, or asking for routine stage approval.
- Perform one inline preflight: requested scope, preserved locks, required
  inputs, supported parameters and reference roles. Use already resolved
  capability evidence for the same tool/model/operation; refresh on change,
  uncertainty or an error, not for every unchanged prompt.
- Use one image sample unless a count or alternatives were requested.
  Previously covered exact standard Seedance 2.5 and access-confirmed Premium
  bindings use native `resolution: "480p"` and boolean `draft: true` for every
  new generation, regardless of review mode or delivery target. New exact
  model/operation bindings, including other 2.5 variants, use only a verified
  profile independently bound to provider, transport, tool schema revision and
  validity. New native operations use evidenced native controls; verified
  non-native operations use an ordinary preview at the evidenced resolution,
  even when 480p is also supported, clearly non-promotable. A final then needs
  separately confirmed fresh generation, not `draft_task_id`.
  Missing, malformed, expired, wrong-destination or unknown evidence leaves
  execution unresolved, not prompt-only creative writing. Do not infer Draft
  from a family substring. Promotion requires the exact selected successful
  native task, unchanged creative inputs and reference hashes, matching valid
  profile/transport and final inspection. Changed creative inputs require a
  new native draft; preserve historical task identity and selections.
- Under `approve_for_me`, select a suitable creative direction and inspect
  actual candidate output before selecting it. Keep a short reason, not a
  comprehensive scoring report. Do not invent user approval or claim an
  unseen candidate passed.
- Requested generation requires exact-package per-submit confirmation under
  [generation-transport.md](generation-transport.md), in either approval mode.
  Creative selection is not generation opt-in or real-person consent.
  Do not infer unbounded iterations, new private-file uses or new deliverables.
- Check the final prompt package once. For generated media, check that the
  result exists, decodes and has the expected streams, size and duration, and
  inspect the requested visible/audible result. Report unavailable inspection
  honestly. Do not attach all possible checklists to ordinary handoff.

## Strict

Choosing strict does not invoke `/prompt-review`, load its checklist, or make
review a handoff or generation gate. It requests more detailed explanations
of applicable validity checks and, when actual candidates are supplied,
detailed inspection evidence. Prompt QA runs only when the user invokes
`/prompt-review`; that manual review uses the applicable checklist and a
request-bound record in either mode. Do not spawn a reviewer unless the user
separately requests delegation.

Strict mode proposes three-image comparison sets when applicable.
Explicit requested count wins. A proposal never submits extra samples:
each needs per-submit confirmation. Native video drafts remain mandatory
under the model-specific policy in both modes.

Strict mode does not itself require user selection: `approve_for_me` still
lets the agent decide. `ask_for_approval` waits for the user's decision in
either review mode. A user-invoked `/prompt-review` runs even in default
mode; it does not permanently change the project mode.

## In both modes

Keep explicit user locks, exact approved dialogue, rights and real-person
consent, privacy, capability validity, source preservation, and single-job
transport/reconciliation safeguards. Do not manufacture facts, review
evidence, native-speaker sign-off or user quotes. Missing material inputs
remain questions. Publishing, destructive actions and work beyond the
authorized task remain separately authorized.

This contract governs review depth and repeated approval wording in older
skill recipes. It does not change the workspace's capability boundaries or
relax repository code tests and security checks.
