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
for the current task without creating files. When a project brief exists,
persist an explicitly requested mode change in its `project.md` frontmatter.
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
- Use one image sample unless a count or alternatives were requested. Do not
  add a draft-first video pass automatically. Choose the requested supported
  delivery target; propose a cheaper probe only for a concrete uncertainty and
  within authorized scope and budget.
- Under `approve_for_me`, select a suitable creative direction and inspect
  actual candidate output before selecting it. Keep a short reason, not a
  comprehensive scoring report. Do not invent user approval or claim an
  unseen candidate passed.
- Requested generation authorizes its specified submissions and reference
  uploads without another yes for each step. It does not authorize unbounded
  iterations, extra spend, new uses of private files or different deliverables.
- Check the final prompt package once. For generated media, check that the
  result exists, decodes and has the expected streams, size and duration, and
  inspect the requested visible/audible result. Report unavailable inspection
  honestly. Do not attach all possible checklists to ordinary handoff.

## Strict

An explicit strict-mode choice requests detailed inline prompt review against
the applicable checklist and a request-bound findings record before handoff
or generation. Load only relevant checklist sections, resolve blocking
findings, and recheck changed inputs only. Do not spawn a reviewer unless the
user separately requests delegation.

Strict mode uses the existing detailed candidate checks and, when applicable,
three-image comparison sets and a supported draft-first video pass unless the
user's count or delivery request says otherwise. These additional submissions
still need appropriate generation scope and budget.

Strict mode does not itself require user selection: `approve_for_me` still
lets the agent decide. `ask_for_approval` waits for the user's decision in
either review mode. A specifically requested review runs even in default
mode; it does not permanently change the project mode.

## In both modes

Keep explicit user locks, exact approved dialogue, rights and real-person
consent, privacy, capability validity, source preservation, and single-job
transport/reconciliation safeguards. Do not manufacture facts, review
evidence, native-speaker sign-off or user quotes. Missing material inputs
remain questions. Publishing, destructive actions and spending beyond the
authorized task remain separately authorized.

This contract governs review depth and repeated approval wording in older
skill recipes. It does not change the workspace's capability boundaries or
relax repository code tests and security checks.
