# Generation transport (optional)

Load this contract only when the user explicitly asks to generate, submit, run,
or render a prompt. Every other request stays prompt-only: deliver the
block in chat.

## Modes

| Mode | When | Result |
| --- | --- | --- |
| Prompt-only (default) | No generation request, or no usable transport | Copy-paste block for Lumina |
| Prompt + generation | The user asks for generation and a transport is usable | Prompt shown to the user, then an in-scope submit and job status under the approval mode |

Composition is identical in both modes. Generation never changes how a prompt is
written; it only adds a submit step after the prompt is delivered.

## Detect the transport

Detect from the session; never assume, and never ask for, read back, print or
store credentials. Authentication belongs to existing caller-managed runtime
configuration; this workspace never configures it.

1. **ark-mcp**: tools named `mcp__ark-mcp__*` exist in the session (they may be
   deferred; load them first). Call `ark_job_capabilities` for the supported
   models, operations, and parameters. It is the source of truth; do not
   hardcode payload fields here.
2. **arkcli**: `command -v arkcli` succeeds and the profile is authenticated.
   Use the `arkcli-auth` skill to check status and the `arkcli-gen` skill for
   `arkcli +gen`; do not hardcode flags here.
3. **Explicit direct HTTP/curl**: use this route only when the user explicitly
   requests direct HTTP or `curl` generation. Check that `curl` is available,
   and that an existing caller-managed runtime configuration provides the
   documented endpoint and authentication. Verify the current official API
   contract for the requested model and operation before constructing the
   payload; do not copy transport-specific fields from another client. Never
   put credential values in prompts, shell arguments, logs or repository files.
   If no secure runtime authentication mechanism is established, stay
   prompt-only and report the missing configuration; do not request secrets.
4. **Multiple available**: prefer ark-mcp for ordinary generation requests
   (structured submit/get/cancel and durable artifacts). Use arkcli when the
   user names it or ark-mcp cannot do the job. An explicit direct HTTP request
   selects `curl`; it is never an automatic fallback.
5. **No usable selected transport**: stay prompt-only, say generation was not
   attempted, and describe the missing transport or runtime configuration.
   Run auth or configuration flows only if separately asked.

Use one transport per job. Do not fail over mid-job: a failed or timed-out
submit may still have created a task, so check job status before any retry.
For an asynchronous direct HTTP operation, capture the provider task ID from
the response and poll that same ID using the documented status endpoint. For
a synchronous operation, use the returned result and request identifier when
available; never invent a task ID or polling endpoint. Reconcile ambiguous
responses before repeating a submit. A timeout does not prove the operation
failed or that no job was created.

## Preflight and authorization

Follow [review-mode.md](review-mode.md). Review depth and approval authority are
separate. Default needs a single inline request preflight, not a checklist
report. Strict adds detailed prompt review, not automatic human confirmation.

1. Present the exact prompt, ordered references and compact submit summary:
   transport, model, operation, duration/resolution/count and cost when known.
   Count every variation and preserve any stated spending limit.
2. Under `approve_for_me`, a generation request authorizes the specified
   submissions without another yes for each step. Under `ask_for_approval`,
   wait for the requested user choice; retain any existing batch authorization.
3. Submit the exact displayed package. A change must be shown, but needs fresh
   authorization only when it changes a user lock, exceeds the approved scope
   or budget, or the user asked to confirm submissions. Unknown material
   cost/scope is a question, never unlimited spending authority.

## In scope

- Seedance, Seedream, and Seed Audio generate, edit, and variation jobs.
- Job polling, cancel, and fetching a result reference for the user.
- Uploading reference files the user selected for this generation, without
  repeating authorization for each file. Respect offline/privacy constraints.

## Still out of scope

- Unrequested provider administration, 3D generation and Blender. Authorized
  local trimming, muxing, assembly and export use the existing permissions in
  the root workspace instructions; this contract does not retract them.
- Exact-copy, typography, logo, UI, and deterministic HTML/CSS/SVG work.
- Unbounded generation loops. Submit only the requested count or authorized
  batch; retries and new variations must remain within scope and budget.

## Results and records

Report task id, status, and the result reference in chat. Save nothing by
default. On explicit request, write a provenance record to
`projects/<project>/generations/<asset-stem>.md` with transport (`ark-mcp`,
`arkcli` or `curl`), model, provider task or request identifier when available,
date, and the prompt file. Never store signed URLs,
keys, or account data. Download media only when asked.

A moderation rejection is evidence to diagnose. Revise only legitimately,
show the changed prompt, and apply the current authorization boundary before
resubmitting. Never disguise restricted inputs or infer unlimited retry scope.
