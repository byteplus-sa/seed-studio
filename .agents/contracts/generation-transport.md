# Generation transport (optional)

Load this contract only when the user explicitly asks to generate, submit, run,
or render a prompt. Every other request stays prompt-only: deliver the
block in chat.

## Modes

| Mode | When | Result |
| --- | --- | --- |
| Prompt-only (default) | No generation request, or no usable transport | Copy-paste block for Lumina |
| Prompt + generation | The user asks for generation and a transport is usable | Prompt shown to the user, then a confirmed submit and job status |

Composition is identical in both modes. Generation never changes how a prompt is
written; it only adds a submit step after the prompt is delivered.

## Detect the transport

Detect from the session; never assume, and never ask for or handle credentials.

1. **ark-mcp**: tools named `mcp__ark-mcp__*` exist in the session (they may be
   deferred; load them first). Call `ark_job_capabilities` for the supported
   models, operations, and parameters. It is the source of truth; do not
   hardcode payload fields here.
2. **arkcli**: `command -v arkcli` succeeds and the profile is authenticated.
   Use the `arkcli-auth` skill to check status and the `arkcli-gen` skill for
   `arkcli +gen`; do not hardcode flags here.
3. **Both available**: prefer ark-mcp (structured submit/get/cancel and durable
   artifacts). Use arkcli when the user names it or ark-mcp cannot do the job.
4. **Neither usable**: stay prompt-only, say generation was not attempted, and
   tell the user to connect one. Run auth or configuration flows only if asked.

Use one transport per job. Do not fail over mid-job: a failed or timed-out
submit may still have created a task, so check job status before any retry.

## Gates before every submit

1. The user has been shown the exact prompt and the ordered references.
2. The submitted prompt and reference order are byte-identical to what the
   user saw. Any change means showing it again.
3. Show a submit summary and wait for an explicit yes: transport, model,
   operation, duration/resolution/count, ordered references, and cost when
   known (`arkcli-pricing`, or capabilities output). Count every variation.
   Approval covers that submit only.

## In scope

- Seedance, Seedream, and Seed Audio generate, edit, and variation jobs.
- Job polling, cancel, and fetching a result reference for the user.
- Uploading reference files the user named in this request, after confirming
  each file.

## Still out of scope

- VOD enhance/transcode/subtitle/audio-separation, 3D generation, Blender, and
  any assembly, compositing, or muxing. Local `ffmpeg`/`ffprobe` stay
  analysis-only.
- Exact-copy, typography, logo, UI, and deterministic HTML/CSS/SVG work.
- Bulk or unattended generation loops. Submit what was confirmed, then report.

## Results and records

Report task id, status, and the result reference in chat. Save nothing by
default. On explicit request, write a provenance record to
`projects/<project>/generations/<asset-stem>.md` with transport, model, task
id, date, and the prompt file. Never store signed URLs,
keys, or account data. Download media only when asked.

A moderation rejection is evidence to diagnose. Revise, show the revised
prompt, and confirm again before resubmitting.
