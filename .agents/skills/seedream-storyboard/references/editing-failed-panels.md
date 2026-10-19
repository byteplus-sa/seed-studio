# Editing Failed Panels

Focused reference for `seedream-storyboard`. Read [the entrypoint](../SKILL.md) for
mode selection and the prompt-only boundary.

- [Choosing a revision path](#choosing-a-revision-path)
- [Naming the region](#naming-the-region)
- [Revision contract](#revision-contract)

This workspace writes the revision prompt only. The user attaches the board
image in the destination UI and runs the edit; no image is uploaded, edited or
processed here.

## Choosing a revision path

**Use the smallest repair scope: panel, then shot, then scene.** Preserve correct panels when a failure is isolated.

| Finding | Revision path |
| --- | --- |
| Local defect in an otherwise correct panel, such as an extra prop, hand detail or expression | Write a narrow edit prompt for that panel or grid cell |
| Wrong beat, reversed axis or incorrect geography | Correct the full prompt and regenerate that panel |
| Shared cause across a shot's panels | Fix the source reference or prompt, then revise only that shot's affected panels |
| Shared cause across most grid cells or the whole scene | Revise the grid or scene with a stated reason |

After two edits fail the same acceptance criterion, stop repeating the local edit and propose regenerating the affected panel from a corrected prompt. Structural errors can take that path immediately. More than one failed cell alone is not a reason to regenerate every cell.

Change one failed dimension at a time and keep every approved property in the preserve list. Keep the original candidate and prompt when presenting a new version. A revision grants no approval and does not invalidate unaffected siblings.

## Naming the region

Name the target by its position and content, in words the user can match on
screen, not by tool coordinates:

```text
the second panel in the top row (the confrontation beside the lighthouse stairs)
```

Add a distinguishing detail when two cells look alike, such as the object or
character in the cell. If the destination UI offers a point or box selection,
tell the user which cell to mark; this workspace does not compute coordinates.

## Revision contract

```text
References:
@Image 1: base storyboard panel to edit
@Image 2: approved character identity

Task:
Image Editing — local storyboard correction

Edit instructions:
In @Image 1, [single requested change at the named panel or marked region].
Use the identity from @Image 2 for [character]. Preserve the camera, composition,
pose, screen direction, background geometry, lighting, palette, and all
unmarked subjects and props.

Acceptance criteria:
- [observable result]
- [continuity property that must remain unchanged]

Constraints:
No new subjects, no wardrobe change, no background redesign, no text, no
watermark, and no changes outside the target region.
```

Change one failed dimension at a time. The user treats the corrected result as
a continuity anchor only after it passes the acceptance checks in
[review and selection](review-and-selection.md).

## Check the full result

When a revised candidate is supplied, compare the entire image with its parent, including areas outside the target region. Check pose, anatomy, count, scale, camera, geography, eyelines, light and unchanged grid cells as well as the requested correction. A corrected prop with a changed character pose fails preservation even if the local correction passes. If the image cannot be inspected, leave preservation unverified.

Local removals may suit an edit. Additions at the frame edge and broad geometry changes can redraw neighboring objects or change the depicted beat. Treat these as risks to verify, not measured success rates or guarantees. Prefer regeneration for structural geometry errors.
