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

- **Separate-images mode.** Write a narrow revision contract for the one failed
  panel's image.
- **Single-image grid mode.** Either revise the whole-grid prompt and ask the
  user to generate it again, or write a revision contract that targets one cell
  of the grid. Prefer the whole-grid revision when more than one cell is
  affected or a repeated defect suggests the prompt itself is at fault.
- After a composition is approved, change one failed dimension at a time and
  keep every approved property in the preserve list.

## Naming the region

Name the target by its position and content, in words the user can match on
screen, not by tool coordinates:

```text
the second panel in the top row (the confrontation at the church altar)
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
