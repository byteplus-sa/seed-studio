# Measured Edit Ledger

Use this optional analysis record when the user wants the reference's edit
structure rebuilt with new content, or a correction must preserve cut timing.
It supplements the normal breakdown; it does not replace the schema or add a
required stage. Return it in chat and save only on request. Keep it outside
`analysis.json`, whose schema has no ledger fields.

Adapted from the planning ideas in upstream [PR #38](https://github.com/byteplus-sa/ark-director/pull/38),
including its generic cleanup in [PR #42](https://github.com/byteplus-sa/ark-director/pull/42)
and [PR #46](https://github.com/byteplus-sa/ark-director/pull/46), at revision
`0539a2e3`. The timing relationships below are authoring evidence, not claims
that a generator will reproduce frame-accurate cuts.

## Record the source before interpreting it

Use picture-stream duration and confirmed cut candidates from
[frame extraction](frame-extraction.md). A still or detector event is not
proof of a cut. Keep estimated boundaries explicitly estimated when the
source cannot be measured. For long references, analyze windows at confirmed
boundaries and carry subject positions, held props and unresolved timing
across them before merging the full timeline.

| Field | Record |
| --- | --- |
| Shot key | Match `shots[].index`; never associate revisions by row position |
| Interval | Start inclusive, end exclusive, duration and source time origin |
| Entry | Hard cut, dissolve, whip, continuous, or unresolved; cite the observed evidence |
| Cut driver | Beat, speech, action, none or unknown; distinguish observation from inference |
| Timing anchor | Measured beat/word/action time and cut offset, or unknown |
| Visible motion | Subject/camera movement and entry/exit state; retain sampled-motion uncertainty |
| Text event | Source title/caption/CTA timing, kept separate from generated picture |
| Dependencies | Referenced identity, prop, location, audio cue or neighboring cut |

Audio stream presence proves no beat, word or music rights. Without an audible
pass or supplied timing evidence, use `unknown` for an audio-driven cut and its
anchor. A supplied untimed transcript gives words, not word timings. Use
`none` only when the available evidence supports no cut driver. Do not infer
music from fast cuts or silence from frames.

Keep beat offsets or frame tolerances only when the source supports that
precision. A generator's timestamp directions remain time budgets. Exact
cutting, typography, logos and motion-graphics execution belong to the
destination workflow; flag those segments and continue the in-scope prompt
package without inventing a graphics prompt.

## Apply a bounded revision

| Requested change | Recheck |
| --- | --- |
| Replace one identity, product or location | Every prompt binding that element, not unrelated shots |
| Change a cut boundary | Both neighboring shot durations, action continuity and any sound crossing it |
| Change dialogue | Speech timing and dependent cuts; the old rhythm cannot be assumed to fit new words |
| Change caption copy only | The separate post-copy note and its timing; preserve unaffected picture prompts |
| Split or merge shots | Assign new shot keys, update dependent element shot lists and motion records, then revalidate the breakdown |

Record the locked decisions, delta, affected shot keys and acceptance criteria.
Re-present changed approved timing before dependent prompts use it. Unaffected
prompts and selections remain unchanged. Never silently remap a motion record
to a new shot just because the array index moved.

## Hypothetical ledger example

| Shot key | Interval | Driver and evidence | Revision dependency |
| --- | --- | --- | --- |
| 1 | 0.00–2.00 s | Action: the hand reaches the plain cup immediately before the confirmed cut | Cup reference; cut at 2.00 s |
| 2 | 2.00–5.00 s | Unknown: picture measured, soundtrack not available | Same cup; preceding cut |

Moving the boundary to 2.20 s changes both durations (2.20 s and 2.80 s).
The 5.00 s ending stays locked. The action and any audio crossing 2.00 s must
be checked again; unavailable audio remains unresolved rather than assumed
continuous.
