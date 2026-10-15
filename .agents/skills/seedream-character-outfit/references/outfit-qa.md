# Outfit QA

Inspect every result next to the parent sheet. Model-written descriptions of an
image are evidence to review, not the verdict.

## Checklist

| Check | Pass condition |
| --- | --- |
| Identity | Close-up face matches the parent: eyes, brows, nose, mouth, skin tone, mark placement |
| Hair | Same style, length and color; only a stated hat hides it |
| Build | Same height-to-head ratio and shoulders; clothing may change silhouette, not the body |
| Outfit | Every listed item present, correct colors and lengths |
| Residual original | No fragment of the old outfit: collar, strap, sleeve, shoe |
| Back/front agreement | Same layers, sleeve length and colors |
| Accessories | Glasses lenses clear with eyes visible; hat covers only what was stated; jewelry on the stated side |
| Layout | Three panels, parent order and spacing, plain gray background, neutral even light |
| Expression | Mouth closed, no smile, no emotion |
| Hands | Empty, five fingers each |
| Text | No lettering, labels or watermarks |
| Single face | Body panels show no second readable face when the requested reference policy needs one |

## Drift triage

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Face or hair changed | Outfit text overpowered the identity binding | Move the identity descriptor and `@Image 1` binding first; shorten the outfit text |
| Old garment still visible | Residual-original guard too weak | Name each old item under REMOVE and in the prompt; describe the new item's exact area |
| Back panel differs from front | Layers or sleeves not stated | State layers and sleeve lengths for both |
| Glasses reflect or hide the eyes | No clear-lens phrase | Add the clear non-reflective lens wording |
| Extra readable face in a body panel | Parent behavior or new pose | Use `seedream-character-sheet-cleanup` on the new version |
| Panels merged or reordered | Layout description too brief | Copy the parent Composition text verbatim |
| Skin tone shifted | Clothing color cast | Restate the skin tone from the descriptor; keep neutral white balance |

## Retry order

1. Tighten the prompt and rerun the three-sample set. Keep the parent as `@Image 1`.
2. Change the seed set only if the failure is random across samples.
3. For one small item on one panel, use a box edit on a copy; never overwrite
   the source sample.
4. If identity cannot be held, report it. Do not approve a drifted sheet.

Every retry is a new version. Preserve earlier samples and their prompts.
