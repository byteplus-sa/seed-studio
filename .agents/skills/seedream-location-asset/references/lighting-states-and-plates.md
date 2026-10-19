# Lighting States and Same-Place Plates

Adapted from ark-director's location-lock guidance through [PR #46](https://github.com/byteplus-sa/ark-director/pull/46), source revision `0539a2e335a81b7366fc293f33527848bf51f699`. These are authoring and candidate-comparison techniques, not guarantees about model behavior.

## Separate place, state and medium

Keep three decisions distinct: persistent architecture and dressing; lighting, weather and practical-light state; rendering medium. Change only the requested decision. A clay version of a daytime street remains that street at that time; a night version changes illumination without moving its doors or replacing its furniture.

Use an available approved location image as `@Image 1`, explicitly bound to geometry and retained dressing. List any lighting or medium reference separately and bind it only to that role. Do not claim to have inspected an absent image. Missing geometry evidence leaves the result an unlocked proposal rather than a verified same-place plate.

## One prompt per requested lighting state

When several shots need different states, write a distinct prompt for each requested state from the same location canon. Reuse the matching selected state image downstream; conflicting daylight visible in a reference can persist despite a night instruction. Describe the target positively, then compare the actual result. A state label alone proves nothing.

Keep the doors, windows, furniture and practical fixtures in their original physical positions. Distinguish a wall or compass direction from frame-left/right: a new viewpoint can change screen positions without moving a source. Keep the original camera for a lighting-only revision. Do not invent a lens, grade, weather change or camera move to fill a section.

For each requested state, record:

| Field | Direction |
| --- | --- |
| Exterior and time | The sky and exterior brightness actually requested; an interior may have no visible sky |
| Dominant source | Named emitter and physical position, direction, quality, reach and shadow falloff |
| Practicals | Which existing fixtures or windows are lit, which are off, and where their pools fall |
| Atmosphere | Retain the approved weather and haze unless a change is requested |
| Preserved layout | Doors, windows, landmarks, counts, dressing and camera position |

Night does not require a black sky, a moon or low-key treatment in every brief. Follow the supplied weather, moon visibility and exposure intent. For a moonless street, describe a dark overcast sky and the requested existing lamp pools without adding a moon. For a brightly lit night market, preserve its light density. Name a wanted light shape positively, such as a soft pool on the pavement, rather than relying on a negation to suppress a beam.

## Same-place environment plates

For a restyle or background plate, describe the observed source's own room or street: layout, landmarks, fixed objects, plants, camera side and time of day. Apply only the requested medium. A more attractive different city, room or culture is a place change, not a medium change.

Use I2I when a supplied source frame or location image guides the plate. With only a verified written description, a T2I concept can be drafted, but same-place fidelity stays unresolved until compared with source evidence. Do not invent reference bindings. People may be omitted for an empty environment plate when requested or inherent in that deliverable; preserve the scene's required furniture and props.

Count recurring set pieces and name their locations. For plain crates, jars, sacks or shop fronts, describe blank unprinted surfaces before adding a short text exclusion. Preserve real source markings only when supplied and authorized; exact copy belongs to the destination's deterministic finishing step.

## Architecture and comparison checks

When stairs, landings or galleries matter, state the observed ascent direction, turns, landing position, connection and supported base. Do not prescribe a universal rail count or invent tread counts. Keep landmarks identified by the same wall or physical relation across prompts. From a changed view, account for occlusion rather than relocating them.

When candidates are supplied, compare architecture, perspective, landmark positions, fixed-object counts, practical-light positions and state, shadow direction and exterior brightness. For a medium-only plate, confirm time of day and lighting geography remain stable. For a lighting-only iteration, confirm material, medium and camera remain stable. Check the whole image for added objects or pseudo-text. If images cannot be inspected, report those checks as unverified; a prompt and provider success do not establish fidelity or approval.
