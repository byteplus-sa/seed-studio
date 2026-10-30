# Seedance pre-check

Part of a manual `/prompt-review` run only. Before dispatching the review
sub-agent, check each Seedance prompt against this list. Each item was a
repeated MINOR or MAJOR finding in production reviews. Fixing it first usually
saves a second review round. This list does not replace the checklist review,
and no prompt-writing skill runs it on its own.

| # | Check | Typical failure → fix |
|---|---|---|
| 1 | **Canonical descriptor is copied, not paraphrased.** Product, character, and prop descriptors match the element manifest's `Canonical descriptor` word for word, and the manifest matches the approved image. | "cupped pepperoni" when the image shows flat slices → fix the manifest first, then copy it. Missing visible components (onion slivers) are findings too. |
| 2 | **The reference role claims only what the image shows.** `Use @Image N only for …` lists attributes visible in that image. States the image cannot show (cut into slices, raw, stretched cheese) are written as text. | "use @Image 1 for the cut" on an uncut packshot → "use @Image 1 for toppings and crust … cut into eight wedges". |
| 3 | **State is explicit when it changes.** Raw vs baked, empty vs filled, and before vs after each have a stated state per stage or clip. A reference showing the final state does not silently define earlier stages. | Build shots drift to the baked look → "The pizza is raw throughout this clip: pale dough rim, unmelted cheese." |
| 4 | **Camera moves have clear endpoints.** Use event-relative timing or supplied time locks; second-level timestamps are not mandatory. | A following tilt must settle before the slice exits: state that endpoint without inventing timing precision. |
| 5 | **Motion has a cause and hands are accounted for.** An object that moves on its own states how. Hand count, grip, and entry edge are stated in every shot that has hands. | A slice rising with no cause invites an invented hand → "rises as if drawn from above out of frame; only the pizza, board and steam are in frame". |
| 6 | **Shot count fits readable action.** About 0.8 s per shot and 6-7 shots per clip are provisional feasibility aids, not quotas. Preserve equal timing and repeated holds; timestamps apply only where needed. | Five piping actions bundled as "four quick shots" need an accurate action sequence and time to read it; propose splitting only if that sequence cannot fit. |
| 7 | **Transitions and fades land before the trim point.** When the edit trims a clip, any whip or fade that must survive peaks before the trim. Final fades to black are done in post. | Fade at 11.6–12 s, trim at 11.3 s → hold to the end and fade in post. |
| 8 | **Audio uses bracket syntax end to end.** Music descriptions sit inside `( … )` including arrangement cues. Discrete effects use `< … >`. Words the model must not voice are excluded explicitly. | Drop-outs and the dead stop written outside the brackets → move the whole arrangement inside `( … )`. |
| 9 | **The timeline covers the full requested duration.** The last stage ends at the `duration` parameter, not before it. | Stages end at 16.8 s for a 17 s request → extend the last stage to 17 s. |
| 10 | **Nothing in the frame needs exact text.** No on-screen copy, logos, or captions. Overlay copy is composited later, and the prompt keeps clean space where overlays will sit. | — |
| 11 | **Counts preserve reveals.** Track total identity separately from visible count; account for hidden, entering and occluded subjects without exposing them early. | Three people total, two visible until the door opens: the reveal does not add a fourth identity. |
| 12 | **Audio follows ownership.** Preserve requested native diegetic sound in wordless scenes, exact master/post ownership or purposeful silence. Verify supported destination controls and require listening for unwanted audio; negative wording is not proof. | Native latch clicks stay native; an exact master stays unchanged in post; silence gets no bed. Reject unwanted score or propose an authorized repair in the destination workflow. |
