# Effect recipes - Art and style

Prompt-composition recipes. Start-frame descriptions are required inputs, not instructions to generate. Parameters are suggestions for destination settings; `Post` is a destination handoff. Status records are upstream observations from 2026-10-08, not current local verification.

## Menu rows

| id | label | route | duration | start photo |
| --- | --- | --- | --- | --- |
| `comic` | Comic | `v2v-restyle` | source length (typ. 5 s) | user's clip, one central subject |
| `canvas` | Canvas | `v2v-restyle` | source length (typ. 5 s) | user's clip, one separable moving subject |
| `palette` | Palette | `v2v-restyle` | source length (typ. 5 s) | any clip, wide-angle or fast motion |
| `lsd` | LSD | `v2v-restyle` | source length (typ. 5 s) | clip, people close to camera |
| `scrapbook-collage` | Scrapbook collage | `composite` | 6 s | full-body standing, plain background |
| `cutout` | Cutout | `i2v-first-and-last` | 8 s | person small in structured environment |
| `pearl-earring` | Pearl earring | `composite` | 7 s | head-and-shoulders face, plain background |
| `cyclope` | Cyclope | `composite` | 7 s | one person, full body, outdoor |
| `fallen-angel` | Fallen angel | `composite` | 7 s | clear upper-body portrait, one person |

### `comic` - Comic

**Look:** the live clip redrawn as an inked, cel-shaded comic page whose sky, clouds and pattern overlays change look every third of a second while the subject's geometry stays locked.
**Route:** `v2v-restyle`. Muted source `@Video 1` supplies subjects, props, motion, camera and timing. An empty environment image `@Image 1` defines the same place in the requested medium. The style block below supplies the effect; input preparation follows the local video-to-video contract. This is a composition hint for `seedance-restyle`, not delegation.
**Parameters:** duration and ratio match the source; audio off with original sound restored in destination post. Source-frame compatibility follows the local video-to-video inputs contract. Resolution follows destination support and the user request. Stepped cadence may need post retiming.
**Start photo:** source clip requirements: user-owned footage with a recorded rights decision; 4-8 s single take; one clear central subject against sky or a simple backdrop; no cuts; no readable signage in frame (source text becomes abstract shapes). Poor input: crowds, many small subjects, busy text-heavy scenes, handheld footage with heavy blur.
**Beats (from the originals):**
- 0-1s: cel-shaded ink rendering; sky and background re-skin about every 0.3 s (bright blue, navy with orange flat clouds, pale hazy blue with halftone-dot clouds); pattern overlays on hard surfaces; outfit tones shift.
- 1-2.5s: bold outline around the subject; radial manga speed-line burst behind the subject; swirl-cloud sky.
- 2.5-5s: pose and camera follow the source; sunset gradients, teal rim tint, hard black shadows and sunburst rays alternate at the same rhythm.
- No hard cuts; one continuous take.
**Prompt template:**
```text
Edit @Video 1. Replace the scene with the inked comic version of {place} from @Image 1, and redraw {subject_inventory} as a comic illustration. Keep every subject, action, prop, camera move and timing from @Video 1.
@Video 1 is the sole editing master. It defines {subject_inventory}, {key_props}, {camera_path}, and the event order: {source_beats}.
@Image 1 defines only how the empty place looks in comic ink: {place_features}. Use no person from it.
Style: the entire video is redrawn as a printed comic with heavy black ink contours, flat cel shading, halftone dot shading and a bold white-and-black outline around {main_subject}. {outfit_policy} The sky and background change look every 0.3 s, cycling through {background_variants}; the subject's pose, silhouette and position never change between steps. From {burst_start}s to {burst_end}s a radial manga speed-line burst surrounds {main_subject}.
Stepped cadence: the picture redraws about 10 times per second, each step held still.
Exactly {people_count} {people_noun} appear. {text_surfaces} show abstract coloured shapes only. No letters, digits or words anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{place}`, `{place_features}`: read from the source (for example "a stack of rusty shipping containers under open sky"); the required environment image uses the same description, empty of people and props the shot lacks.
- `{subject_inventory}`, `{main_subject}`, `{people_count}`, `{people_noun}`: observable descriptors and the exact count from the source inspection.
- `{key_props}`, `{camera_path}`, `{source_beats}`: from the source inventory with times (default camera: "the source camera path unchanged").
- `{outfit_policy}`: default "Outfit colours stay as in @Video 1." Use "Outfit colours shift with each step" only when the user wants the original's recolouring.
- `{background_variants}`: default "bright blue sky with flat white clouds, navy sky with flat orange clouds, pale hazy blue sky with halftone-dot clouds, sunset gradient with a teal rim tint".
- `{burst_start}`, `{burst_end}`: default 1 and 2.5 for a 5 s clip, scaled proportionally for other lengths.
- `{text_surfaces}`: source signage, container sides, shirts, for example "Container sides". When the source has none, delete the sentence that begins with this slot and keep "no letters, digits or words anywhere".
**Post:** retime to the stepped look and restore audio. `ffmpeg -i out.mp4 -vf "fps=10,fps=30" -an stepped.mp4` (30 fps delivery gives an even three-frame hold per step), then mux the saved source audio. Captions or titles only via the destination workflow or FFmpeg overlay.
**QA:**
- Subject count, silhouette and screen positions match the source at the start, middle and end frames.
- Background look changes at least 12 times over 5 s, with no steady single grade.
- A speed-line burst is visible in the 1-2.5 s window and absent after it.
- No letters, digits or words on any surface.
- After post, frame holds are an even three frames at 30 fps.
**Risks:** Seedance smooths the flicker into one steady grade, so the cadence is also enforced in post; outfit colour drift is intended only if `{outfit_policy}` allows it; invented container lettering; speed lines can render static; a Seedream environment image gives one look, so the background variants rely on text. The page for this effect had no copy beyond a title, so the look is read from frames only.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-28, video edit with an environment image, 480p, no draft mode, sound on, person-free source clip at 9:16): usable with defects; the background changes about every second, not every 0.3 s; no stepped look until retimed in post. Not verified on other clips or at a higher resolution.

### `canvas` - Canvas

**Look:** real footage where the one main subject carries a thick white spray-painted sticker outline and the whole scene is scribbled over with bright marker doodles that redraw differently at every step.
**Route:** `v2v-restyle`. Muted source `@Video 1` supplies subjects, props, motion, camera and timing. An empty environment image `@Image 1` defines the same place in the requested medium. The style block below supplies the effect; input preparation follows the local video-to-video contract. This is a composition hint for `seedance-restyle`, not delegation.
**Parameters:** duration and ratio match the source; audio off with original sound restored in destination post. Source-frame compatibility follows the local video-to-video inputs contract. Resolution follows destination support and the user request. Stepped cadence may need post retiming.
**Start photo:** source clip requirements: user-owned footage with a recorded rights decision; 4-8 s; one clearly separable moving subject (skater, cyclist, walker) who stays inside frame; bystanders allowed but few. Poor input: several equal-sized subjects (the outline lands on the wrong one), a subject that touches frame edges, very dark footage.
**Beats (from the originals):**
- 0-0.3s: first frame is a torn-edge sticker subject on crumpled kraft paper covered in doodles (optional post step, not requested of Seedance).
- 0.3-4.5s: the real street plate returns; the subject keeps a white spray outline; fresh random doodles (stars, hearts, arrows, spirals, stick figures) are redrawn over walls and floor every step; falling small objects get white outlines.
- 4.5-5s: bystanders enter without an outline; doodle layer continues.
- No hard cuts.
**Prompt template:**
```text
Edit @Video 1. Keep the footage photographic, with every subject, action, camera move and timing unchanged, and add a hand-made sticker outline and a marker doodle layer.
@Video 1 is the sole editing master. It defines {subject_inventory}, the scene {place}, {camera_path}, and the event order: {source_beats}.
Edit scope: exactly one subject, {main_subject}, gets a thick white hand-sprayed outline about {outline_width} wide, like a die-cut sticker, following the silhouette including {outline_extras}. No outline is drawn on {bystanders}.
Over the {surfaces} of the scene, saturated marker and wax-crayon doodles are drawn in {doodle_palette}: stars, spirals, hearts, arrows, small smiley faces and stick figures with visible hand wobble. The doodle layer redraws in new random positions about 12 times per second, each step held still. No doodle touches {main_subject}'s face or either hand.
Style: real photographic footage with flat opaque marker strokes drawn on top.
Doodles are shapes only: every mark is an abstract stroke, star, spiral, heart, arrow or face outline, and no letters, digits or words appear anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject_inventory}`, `{main_subject}`, `{camera_path}`, `{source_beats}`, `{place}`: from the source inspection.
- `{outline_width}`: default "5 percent of the subject's height".
- `{outline_extras}`: what travels with the subject, for example "the bouquet and the falling petals"; default "worn clothing and carried objects".
- `{bystanders}`: for example "the three runners in the background"; default "every other person in frame".
- `{surfaces}`: walls, ground, sky actually in frame.
- `{doodle_palette}`: default "red, yellow, blue, green, pink and orange".
**Post:** `ffmpeg -i out.mp4 -vf "fps=12,fps=24" -an stepped.mp4`, then mux the saved source audio. Optional opening kraft-paper frame (first 0.3 s): static plate via the destination workflow, concatenated with FFmpeg.
**QA:**
- Exactly one subject carries the white outline, with no doubled or drifting edge.
- Doodles appear on walls and ground and change between steps; none cover the subject's face.
- Footage remains photographic and the subject path matches the source.
- No scribble reads as a letter or word.
**Risks:** outline drift or doubling; outline applied to bystanders; doodles smoothed into one static drawing; text-like scribbles; sticker edge flicker; doodles dimming the footage. Page copy was thin, so the rule that no environment image is needed is an assumption to verify at the probe.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-29, video edit, 480p, no draft mode, sound on, person-free source clip at 9:16): not achieved; take 1 doodled only the sky between 1.5 and 4 s; take 2 put doodles on the car body, which the prompt forbade. Not verified on other clips or at a higher resolution.

### `palette` - Palette

**Look:** the clip rendered as one continuous thick-impasto oil painting, with visible knife ridges and brush-streak smears on fast-moving objects.
**Route:** `v2v-restyle`. Muted source `@Video 1` supplies subjects, props, motion, camera and timing. An empty environment image `@Image 1` defines the same place in the requested medium. The style block below supplies the effect; input preparation follows the local video-to-video contract. This is a composition hint for `seedance-restyle`, not delegation.
**Parameters:** duration and ratio match the source; audio off with original sound restored in destination post. Source-frame compatibility follows the local video-to-video inputs contract. Resolution follows destination support and the user request. Stepped cadence may need post retiming.
**Start photo:** source clip requirements: user-owned footage with a recorded rights decision; 4-8 s; wide-angle or dynamic motion (low fisheye walk-over, subject leaning from a moving car) gains most; faces large enough to hold likeness under strokes. Poor input: static talking head, tiny faces, dark or low-contrast footage.
**Beats (from the originals):**
- 0-5s: the whole clip is thick oil paint, with strokes visible on sky, fabric, metal and glass; fast objects (taxis, grass, pedestrians) smear into directional streaks; strokes shimmer at 12 fps; the look never changes.
- No hard cuts; the camera is the source camera.
**Prompt template:**
```text
Edit @Video 1. Replace the scene with the thick oil-painted version of {place} from @Image 1, and repaint {subject_inventory} in the same oil painting. Keep every subject, action, prop, camera move, lens distortion and timing from @Video 1.
@Video 1 is the sole editing master. It defines {subject_inventory}, {key_props}, {camera_path}, and the event order: {source_beats}.
@Image 1 defines only how the empty place looks in oil paint: {place_features}. Use no person from it.
Style: the entire video is redrawn as thick oil impasto painting with coarse visible brush strokes and palette-knife ridges in the sky, fabric, metal and glass, rich layered colour and canvas weave. {fast_movers} smear into long brush streaks along their direction of travel. Faces keep clear eye, nose and mouth shapes in finer strokes.
Stepped cadence: the strokes repaint about 12 times per second, shimmering slightly while every contour stays locked to @Video 1.
Exactly {people_count} {people_noun} appear in the foreground; {background_extras}. {text_surfaces} show abstract paint shapes only. No letters, digits or words anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{place}`, `{place_features}`, `{subject_inventory}`, `{key_props}`, `{camera_path}`, `{source_beats}`, `{people_count}`, `{people_noun}`: from the source inventory; the required environment image depicts `{place_features}`.
- `{fast_movers}`: the fastest-moving items in the source, for example "Taxis and passing pedestrians".
- `{background_extras}`: default "every other figure stays a small painted shape in the background".
- `{text_surfaces}`: signs, number plates, shopfronts in frame. When the source has none, delete the sentence that begins with this slot and keep "no letters, digits or words anywhere".
**Post:** `ffmpeg -i out.mp4 -vf "fps=12,fps=24" -an stepped.mp4`, then mux the saved source audio. No overlays.
**QA:**
- Coarse strokes are visible at full resolution on sky, fabric and metal, not a smooth digital filter.
- Moving objects show directional smear; static areas shimmer between steps.
- Camera distortion and move match the source; subject count unchanged.
- Faces remain recognisable as the same person.
**Risks:** drift to a smooth painting filter instead of coarse strokes; strokes frozen instead of shimmering; face likeness lost under heavy texture; fisheye straightened; the environment image for a wide-angle street gives the model a flatter perspective than the source. Confidence in the original look is high.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-30, video edit, then reference-to-video retake, 480p, no draft mode, sound on, person-free source clip at 9:16): not achieved; the edit route painted only the sky; the retake paints sky and buildings but the car and road stay lightly painterly (review fail). Not verified on other clips or at a higher resolution.

### `lsd` - LSD

**Look:** a strobing alternation between a scratched high-contrast black-and-white photocopy and oil-slick rainbow swirl floods, with people turned to cracked white silhouettes.
**Route:** `v2v-restyle`. Muted source `@Video 1` supplies subjects, props, motion, camera and timing. An empty environment image `@Image 1` defines the same place in the requested medium. The style block below supplies the effect; input preparation follows the local video-to-video contract. This is a composition hint for `seedance-restyle`, not delegation.
**Parameters:** duration and ratio match the source; audio off with original sound restored in destination post. Source-frame compatibility follows the local video-to-video inputs contract. Resolution follows destination support and the user request. Stepped cadence may need post retiming.
**Start photo:** source clip requirements: user-owned footage with a recorded rights decision; 4-8 s; people close to camera or strong wide shapes (shelves, tables) that can warp; no flashing lights already in the footage. Poor input: footage that already strobes, very dark or very bright scenes.
**Beats (from the originals):**
- 0-5s: every 0.2-0.3 s the frame alternates between Look A (photocopy black-and-white, scratches, dust, cracked white silhouettes, blown highlights) and Look B (original colours or oil-slick rainbow swirls with chromatic fringing).
- 1-2s: full neon magenta, cyan and green swirl wash; subjects stay cracked white silhouettes.
- 3-4s: warp peak; shelves bend into waves; halftone dots; subjects stretch with the distortion.
- 4.5-5s: overexposed blowout, then back to grainy black-and-white (the safe default stops at a pale peak, not full white).
- No hard cuts; strobing is a filter effect.
**Prompt template:**
```text
Edit @Video 1. Keep every subject, action, camera move, lens distortion and timing from @Video 1, and restyle the whole picture as two alternating looks.
@Video 1 is the sole editing master. It defines {subject_inventory}, the scene {place}, {camera_path}, and the event order: {source_beats}.
Look A: a hard high-contrast black-and-white photocopy with dust, fine scratches, blown highlights, and {people_noun} shown as cracked white silhouettes with dark outlines.
Look B: the original colours flooded by saturated oil-slick swirls of magenta, cyan and green across {swirl_surfaces}, with chromatic fringing at light sources.
Stepped cadence: the picture steps 10 times per second and the two looks alternate, each holding {hold_s} s. At {warp_start}s the swirls bend {swirl_surfaces} into waves with halftone dots, peaking at {warp_peak}s; at {peak_end}s a pale pastel peak resolves back to Look A. The frame never turns fully white.
Exactly {people_count} {people_noun} appear; faces stay one readable shape each. Signs and labels show abstract grey shapes only. No letters, digits or words anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject_inventory}`, `{place}`, `{camera_path}`, `{source_beats}`, `{people_count}`, `{people_noun}`: from the source inspection.
- `{swirl_surfaces}`: the walls, shelves and tables in frame.
- `{hold_s}`: default 0.4; faithful mode 0.25 with the warning.
- `{warp_start}`, `{warp_peak}`, `{peak_end}`: default 3, 4, 4.7 for a 5 s clip, scaled for other lengths.
**Post:** `ffmpeg -i out.mp4 -vf "fps=10,fps=30" -an stepped.mp4`, then mux the saved source audio. Run a luminance check on the final file before delivery (no more than three large-area flashes per second, no sustained saturated red) and add a photosensitivity warning card via the destination workflow when faithful mode is used.
**QA:**
- Both looks are visible and alternate on the stated hold, not one steady grade.
- No frame is fully white and no flash rate exceeds three per second in default mode.
- Warp peaks in the 3-4 s window and the clip returns to Look A at the end.
- People remain countable and readable; subject count matches the source.
**Risks:** Seedance settles into one steady style; photosensitivity from strobing and blowouts (cap by default, disclose otherwise); faces melt and identity drifts under warp; crackle reads as lens dirt; the pastel peak replaces the original blowout and is a deliberate deviation. Page confidence is medium.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-31, video edit; the first submission was rejected for its output audio, 480p, no draft mode, sound on, person-free source clip at 9:16): not achieved; no wave warp or halftone dots, a slow look hold, and the car turns dark grey (review fail). Not verified on other clips or at a higher resolution.

### `scrapbook-collage` - Scrapbook collage

**Look:** a crumpled-paper scrapbook page with a white-bordered full-body cut-out above two torn-edge inset photos (shoes and face) that move in sync with the main figure.
**Route:** `composite`. One first-frame image supplies the full-body subject on a plain backdrop. Compose only the person clip. The destination builds the paper page, white cut-out border and exactly two synchronized inset crops from that same clip; a single generated layout is unreliable.
**Parameters:** duration 6; ratio follows the photo (9:16 or 3:4 portrait preferred); `generate_audio: false`. Layout canvas 720x1280 (9:16) by default.
**Start photo:** whole body head to shoes, standing, face readable, a plain one-colour studio backdrop, clear detail zones (shoes, hem, trouser cuffs). Poor input: busy backdrops (matting fails), cropped feet, long skirts that hide the legs, crossed arms, backdrop the same colour as the clothing.
**Beats (from the originals):**
- 0-0.8s: locked flat frame; subject in horse stance, fists raised; left inset trousers and heels, right inset face close-up.
- 0.8-2s: knee lift, head turns to profile; right inset shows the profile, hair starting to lift.
- 2-4s: high kick held, hair and jacket blown back; left inset swaps to foot lift and a heel side view; burst marks near foot and mouth.
- 4-6s: kick retracts, subject returns to the opening stance, insets return to the opening crops (loop).
- No hard cuts; camera locked; motion stepped like swapped paper pieces.
**Prompt template:**
```text
@Image 1 is the first frame. It defines {subject}'s face, hair, outfit, full-body framing and the flat {backdrop_color} studio backdrop; keep them unchanged.
Exactly one person with two arms and two legs, centred, filling about {fill_pct} percent of the frame height, head to shoes always fully in frame.
At 0s {subject} stands in a wide horse stance with both fists raised near the chin, holding until 0.8s. From 0.8s to 2s the {leg_side} knee lifts to waist height and the head turns to the left profile. From 2s to 4s the {leg_side} leg extends into a straight high kick to head height and holds, hair and {flare_item} blown back. From 4s to 5.5s the leg retracts and {subject} lands back in the opening stance, matching the first frame until 6s.
The motion is stepped like stop-motion paper pieces: 12 frames per second, each pose held for one step.
Locked-off camera, no zoom or pan, a fixed full-body frame. The backdrop stays one flat uniform {backdrop_color} with no props, floor line or cast shadow. Clothing and backdrop are plain surfaces with no lettering or logos.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject}`: what the photo shows, for example "a woman with long blonde hair, round glasses and a dark oversized suit".
- `{backdrop_color}`, `{fill_pct}`: read from the photo (default fill 70).
- `{leg_side}`: "right" or "left" as seen in the frame, chosen so the kick leaves the torso uncrossed.
- `{flare_item}`: the loose garment, for example "jacket"; default "clothing".
- Alternative action for skirts or dresses: replace the kick sentences with "a slow full turn in place with arms swinging out", keeping the same timings.
- Layout defaults (post): cut-out box x 40-680, y 40-830; left inset 300x360 at (45, 870); right inset 300x360 at (375, 870); paper gradient from the outfit's complementary warm hues, with crop windows keyframed per beat from the generated clip (left window follows the shoe, right window follows the head).
**Post:** Required destination layout: paper background, white cut-out border, exactly two deckle-edged inset crops from the same clip, synchronized poses, blue burst marks around the kick beat, 12 fps stepped cadence. This leaf does not render the layout.
**QA:**
- Exactly two insets, left shoes or legs, right face; both show the same pose moment as the main figure.
- One white border around the cut-out, no flicker between steps.
- Kick holds between 2 s and 4 s; last frame matches the first.
- Matte has no backdrop halo, and no text in any panel.
**Risks:** leg, shoe and heel anatomy during the kick; hair flyaways break the matte; crop-derived insets cannot show a profile unless the head actually turns (accepted trade for sync); backdrop shadow or colour matching the garment ruins the key; count errors if insets are generated rather than cropped.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-32, first-frame plus deterministic layout, 480p draft, sound on, one invented subject at 9:16): clean; the kick goes to frame-left; the cadence reads stepped. Not verified on other photos or at a higher resolution.

### `cutout` - Cutout

**Look:** the surroundings erode to a pure white void and separate into floating paper-flat cut-out layers around an untouched person, then snap back to the exact original photo.
**Route:** `i2v-first-and-last`: `@Image 1` is the first frame, `@Image 2` is the last frame, both the same file (copy it to a second role so the two bindings are separate inputs). Ratio locked to the photo; both match by construction. No reference images (Seedance 2.5 cannot mix first_frame with reference_image).
**Parameters:** duration 8; ratio follows the photo (4:3, 3:4, 16:9, 1:1 seen); `generate_audio: false` (optional light paper-rustle bed via Seed Audio in post). The same image as first and last frame was accepted by the provider and the 2026-10-08 draft ended on the photo (scene-33), so the route works; the fallback below is only for a draft that does not end on the photo: `i2v-first-frame` with `@Image 1` only, drop every `@Image 2` sentence, and end the prompt with "By 8s the scene is back to the original photo: every piece in its original position and size, no white remaining, the camera at the start framing."
**Start photo:** a person standing in a recognisable structured scene (stair block, cafe counter, street, bookshop) with separable objects (lamps, counter, floor tiles, balconies, laundry line); the whole person visible and fairly small in frame. Poor input: close-up portraits, plain walls, cluttered scenes with dozens of tiny items, subject touching frame edges.
**Beats (from the originals):**
- 0-1s: the original scene, subject still, camera locked.
- 1-3s: sky and far background fade to pure white from one corner, distant and upper structures erase, remaining pieces separate as flat cut-out layers.
- 3-5s: layers float and tilt in the white void with soft ground shadows; subject braces on a small floor fragment; camera tilts down.
- 5-7s: floating arrangement holds; small particles fall.
- 7-8s: the white void fades and everything snaps back to the original positions; the last frame equals the first. No hard cuts.
**Prompt template:**
```text
@Image 1 is the first frame and @Image 2 is the last frame; both are the same photo, so the video ends exactly where it began.
The scene contains {subject_description} {subject_position}, and exactly {piece_counts_total} separate pieces: {piece_list_with_counts}.
At 0s the camera is locked and nothing moves. From 1s to 3s the sky and distant background fade to pure white #FFFFFF starting at the {corner} corner, then {erased_pieces} erase completely into the white. The {kept_count} pieces {kept_pieces} stay and each lifts away as a flat paper cut-out layer with a thin white paper edge and a soft drop shadow on the floor.
From 3s to 5s the {kept_count} cut-out layers float and tilt slowly in a clean white void while {subject} stays photographic and unchanged, standing on {fragment}, {subject_reaction}; the camera tilts down about 10 degrees.
From 5s to 7s the arrangement of {kept_count} floating pieces holds, with {particles} falling slowly past.
At 7s the white void fades out in under one second, every erased and every floating piece returns to its original position and size, and the camera tilts back to the start framing, matching @Image 2.
Counts: exactly one person; {piece_counts_total} pieces at 0s and again from 7s; between 3s and 7s exactly {kept_count} pieces float and {erased_count} stay erased.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject_description}`, `{subject}`, `{subject_position}`: from the photo, for example "a woman in a yellow jacket and blue jeans standing on a concrete stair landing".
- `{piece_list_with_counts}`, `{piece_counts_total}`: inventory read from the photo with exact counts, for example "two hanging lamps, one counter, one laundry line" with a total of "four".
- `{kept_pieces}`, `{kept_count}`: the 3-6 most separable pieces that float in the middle section, named with their counts, and their total (for example "the two hanging lamps and the counter", "three").
- `{erased_pieces}`, `{erased_count}`: the remaining pieces that stay erased between 3s and 7s, named with their counts, and their total (for example "the laundry line", "one"). When every piece is kept, delete the clause "then {erased_pieces} erase completely into the white" and write "zero" for the erased count.
- `{corner}`: the sky corner of the photo, for example "top-left".
- `{fragment}`: for example "a small fragment of stair".
- `{subject_reaction}`: default "gripping the nearest rail with a small startled shift of weight"; for open scenes "shifting weight and looking up".
- `{particles}`: scene-matched, for example "coffee beans", "paper scraps"; default "small paper scraps".
**Post:** none required. Optional paper-rustle and soft whoosh bed via Seed Audio.
**QA:**
- The void is pure white by about 3 s and the subject is unchanged in identity and outfit.
- Pieces read as flat cut-outs with soft shadows, not melted geometry.
- At 0 s and 8 s all `{piece_counts_total}` pieces are present in their original places.
- At 4 s exactly `{kept_count}` pieces float and `{erased_count}` are erased, with no added or extra piece.
- Last frame matches the first frame; no residual white.
**Risks:** background kept instead of white; layers melt instead of cut flat; subject drifts or is carried away with debris; pieces fail to return to original positions; item counts change; first-and-last with identical images is unproven.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-33, first and last frames with the same image, 480p draft, sound on, one invented subject at 9:16): usable with defects; a quiet orchestral underscore leaked; the floating pieces read as crumpled paper, not clearly the lamps and counter. Not verified on other photos or at a higher resolution.

### `pearl-earring` - Pearl earring

**Look:** the user, costumed in a blue-and-yellow turban and ochre jacket, turns over the shoulder to the camera in the pose of a famous Dutch portrait, shown above the real painting.
**Route:** `composite`. Required 1:1 opening still: same face, hair colour and skin tone in left profile wearing a blue silk turban with yellow tail, ochre jacket, white collar and pearl drop earring, dark plain backdrop. `@Image 1` is that still. The destination stacks the clip above an authorized painting crop; the painting is not a generation reference.
**Parameters:** duration 7; ratio 1:1 (clip), final stack 1:2; `generate_audio: false`.
**Start photo:** clear head-and-shoulders face photo, front, three-quarter or profile, plain background, soft even light, hair mostly visible. Poor input: sunglasses, heavy hats, face partly covered, extreme angles, tiny faces. Likeness: use only the user's own photo or a photo they have consent for; a real face goes through the repo's real-person handling with separate likeness-consent evidence, not Virtual Portrait, which is for invented characters.
**Beats (from the originals):**
- 0-1s: top half in left profile, turns head over shoulder to a three-quarter pose looking into the lens; bottom half is the static painting.
- 1-4.5s: pose held, almost still; a soft light shaft from upper left crosses the dark backdrop.
- 4.5-5.5s: one slow blink, tiny head and breath motion.
- 5.5-7s: hold. No hard cuts; camera locked.
**Prompt template:**
```text
@Image 1 is the first frame. It defines {subject}'s own face, hair colour and skin tone, the costume, the dark backdrop and the left-profile pose; keep them unchanged.
{subject} wears a blue silk turban with a yellow cloth tail hanging behind the shoulder, an ochre jacket with a small white collar, and exactly one pearl drop earring on the ear nearest the camera.
At 0s {subject} is in left profile, looking off-screen to the left. From 0s to 1s the head turns smoothly over the shoulder until the face is three-quarter toward the lens and the eyes meet the camera, then stops there. From 1s to 4.5s the pose holds with only slight breathing. At 4.5s one slow blink. From 5.5s to 7s the pose holds still.
A single soft light shaft from the upper left crosses the dark backdrop and lights the near cheek and the turban.
Locked-off medium close-up of head and shoulders in a square frame, no camera movement. The turban, jacket and backdrop are plain fabric and paint with no lettering. No text anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject}`: what the photo shows, for example "a young woman with dark hair" (the identity comes from the still).
- Pre-step a separate image prompt text: "@Image 1 is used only for the person's face, hair colour and skin tone; ignore its pose, clothing, background and light. Generate a square head-and-shoulders portrait of this person in left profile wearing a blue silk turban with a yellow tail, an ochre jacket with a white collar and one pearl drop earring, on a dark plain backdrop"; the prepared still needs the user's likeness check before use.
- Fallback when the still fails identity: skip the still, bind the photo as `reference_image` (route `reference-images`, ratio 1:1 set explicitly; it cannot be combined with a first frame), replace the first line of the template with "@Image 1 is an identity reference for the person only: use {subject}'s face, hair colour and skin tone and ignore its pose, clothing, background and light. The scene is a dark plain backdrop with {subject} in the costume below.", and keep the rest of the timeline.
**Post:** Required destination split-screen: clip above an authorized square painting crop, both panels the same width, two square panels stacked into 1:2, no gap or readable labels. The painting crop shows head and shoulders without frame edges or museum labels. Verify the painting source rights separately.
**QA:**
- Top half shows exactly one earring on the near ear and a turban with a yellow tail.
- Head reaches three-quarter toward the lens by 1 s and stays there; one slow blink near 4.5 s.
- The two halves are 1:1 each, stacked 1:2, with no text and no gap.
- Top half does not reproduce the painting's face; it is the user's face.
**Risks:** identity drift when re-costuming a casual portrait; earring count or ear side; turban fold geometry; head turning past three-quarter; lighting not matching; speech or music baked into native audio (generate_audio stays false). Gallery clips were matched to presets by thumbnail inspection, so the beats are read with medium certainty.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-34, first-frame plus FFmpeg stack, 480p draft, sound on, one invented subject at 9:16): clean; the fabric rustle is not audible; the turban top sits close to the crop edge. Not verified on other photos or at a higher resolution.

### `cyclope` - Cyclope

**Look:** a photoreal one-eyed giant slowly lifts over a boulder to peer down at a small human on the grass, shown above the painting that inspired the pose.
**Route:** `composite`, footage route `i2v-first-and-last`. Required first 1:1 still: person prone on seaside grass at dusk beside a lichen-covered grey boulder, one seagull on top and one sword nearby, no giant. Last still keeps the same scene and identity, adding the giant head and hand over the boulder and the person cowering. The destination stacks footage over an authorized painting crop, not bound as a generation reference.
**Parameters:** duration 7; ratio 1:1 (clip), final stack 1:2; `generate_audio: false` (optional wind, distant surf and low rumble bed via Seed Audio in post).
**Start photo:** one person, full or upper body, any outdoor pose; face visibility matters less because the person is low in frame, seen from the side or back. Poor input: groups, indoor scenes, tight face crops with no body to put on the grass. Likeness: use only the user's own photo or a photo they have consent for; a real face goes through the repo's real-person handling with separate likeness-consent evidence, not Virtual Portrait, which is for invented characters.
**Beats (from the originals):**
- 0-1s: person prone on grass, propped on forearms, looking at the boulder; seagull perched; bottom half static painting.
- 1-2.5s: a huge grey hand rises behind the boulder and grips its top; the seagull flaps away.
- 2.5-4.5s: the bald head rises beside the hand, one central eye in the same peeking pose as the painting; the person rolls and backs against the rock, sword raised.
- 4.5-7s: the giant lifts its shoulders and looks down; the person cowers, forehead on the grass. No hard cuts; camera locked.
**Prompt template:**
```text
@Image 1 is the first frame and @Image 2 is the last frame. @Image 1 defines {subject}, {wardrobe}, the grass meadow, the grey lichen-covered boulder, the seagull on its top and the dusk sea behind. @Image 2 defines the giant's final pose over the boulder and {subject} cowering; keep both scenes' framing.
Exactly one person and one giant appear.
At 0s {subject} lies prone, propped on both forearms, watching the boulder; the seagull stays perched. At 1s a huge grey hand with five fingers, on the {hand_side} of the frame, rises from behind the boulder and grips its top edge; the seagull flaps away to the right. At 2.5s a bald head the size of the boulder rises beside the hand, with grey stone-textured skin and exactly one large round eye centred in the forehead; the giant peeks over the boulder looking down, while {subject} rolls onto one side and backs against the foot of the rock, holding {held_prop} upright. From 4.5s the giant raises its shoulders into view and looks down at {subject}, who curls up with the forehead on the grass, ending as in @Image 2.
Locked-off wide shot in a square frame, no camera movement. Photoreal, soft dusk light, wind in the grass. The sword and boulder carry no markings, only plain steel and grey lichen. No text anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject}`, `{wardrobe}`: read from the photo; the prep still dresses the person in simple period clothing only if the photo shows none.
- `{held_prop}`: default "a plain steel sword with a leather-wrapped hilt".
- `{hand_side}`: the side of the frame where the giant's gripping hand rises, default "left"; the seagull then flaps away to the right, and the flap direction is swapped when the hand side is "right".
- Pre-step texts: first still "@Image 1 is used only for the person's face, hair and skin tone. Generate a square wide shot of this person prone on a dusk seaside meadow beside a large lichen-covered grey boulder with one seagull on top and a sword in the grass"; last still "@Image 1 is the scene: keep its framing, meadow, boulder and sword, with no seagull remaining in the last still. @Image 2 is used only for the person's face, hair and skin tone. Add a photoreal grey giant peering over the boulder with exactly one large eye centred in the forehead and a five-fingered hand gripping the top, and show the person curled with the forehead on the grass".
- Fallback without the last still: use `i2v-first-frame`, drop the opening "and @Image 2 is the last frame" clause, every `@Image 2` sentence and the closing "ending as in @Image 2" phrase.
**Post:** destination stack with the same square-panel layout as `pearl-earring` (crop to the upper hill, head and eye of the painting, without frame or labels). No overlays.
**QA:**
- Exactly one person and one giant; the giant has exactly one eye and five fingers on the gripping hand.
- Hand appears by about 1 s, head by about 2.5 s, the giant towers over the person.
- Last frame matches `@Image 2`; seagull leaves; person count never changes.
- Stack is 1:2 with no text.
**Risks:** two eyes or extra fingers; scale (the giant must tower); the hand not gripping the rock convincingly; person identity from a prone pose; the seagull multiplying; the painting must not be reproduced in the top half. The first/last stills double the prep cost and need scene continuity between them. Gallery matching by thumbnail inspection, medium certainty.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-35, first and last frames plus FFmpeg stack, 480p draft, sound on, one invented subject at 9:16): usable with defects; a rising orchestral score leaked; the giant head arrives about 1 s late; her face is small and turned away. Not verified on other photos or at a higher resolution.

### `fallen-angel` - Fallen angel

**Look:** a white-winged person seated on seaside rocks lifts an arm across the face in a grief gesture, shown above the painting that inspired the pose.
**Route:** `composite`. Required 1:1 opening still: same person seated on dark coastal rocks, two white feathered wings behind shoulders, draped off-white tunic, calm sea, peach golden-hour sky, gazing left, hands in lap. `@Image 1` is that still. The destination stacks the clip above an authorized painting crop; the painting is not a generation reference.
**Parameters:** duration 7; ratio 1:1 (clip), final stack 1:2; `generate_audio: false` (optional soft sea ambience via Seed Audio in post).
**Start photo:** clear portrait or upper body of one person, any skin tone, face unobstructed, plain or soft background. Poor input: sunglasses, hands already near the face, hats, tiny faces. Likeness: use only the user's own photo or a photo they have consent for; a real face goes through the repo's real-person handling with separate likeness-consent evidence, not Virtual Portrait, which is for invented characters.
**Beats (from the originals):**
- 0-1s: winged person seated on rocks, gazing left, hands in lap.
- 1-2.5s: one arm rises, the hand pressing to the face or eye.
- 2.5-4.5s: the arm lifts across the face in the painting's gesture; head turns slightly to camera.
- 4.5-7s: the arm lowers, a sigh, the person looks back to the sea and holds. No hard cuts; camera locked.
**Prompt template:**
```text
@Image 1 is the first frame. It defines {subject}'s own face, hair and skin tone, the seated pose on dark coastal rocks, the two white feathered wings attached behind the shoulders, the off-white draped tunic, and the calm sea under a peach golden-hour sky; keep them unchanged.
Exactly one person with exactly two wings.
At 0s {subject} sits gazing out to the left, both hands resting in the lap. From 1s to 2.5s the arm on the {arm_side} of the frame rises, the forearm bending until that hand presses against the brow and eye, the elbow lifting out to the side. From 2.5s to 4.5s the forearm crosses and covers the eyes, the elbow pointing to the {elbow_side}, and the head turns slightly toward the camera behind the arm; the wings stay folded and attached, moving only with the shoulders. From 4.5s the arm lowers back to the lap, the shoulders rise and fall once slowly, and {subject} looks back out to sea and holds still until 7s.
Locked-off medium shot in a square frame, no camera movement. Golden-hour side light and soft sea reflections. The tunic and rocks are plain, with no lettering. No text anywhere.
Silent output. Sound is added in post.
```
**Slots:**
- `{subject}`: what the photo shows, for example "a young man with short curly brown hair".
- `{arm_side}`: the side of the frame on which the lifted arm appears, "left" or "right", chosen so the arm does not cross the wings; default "left".
- `{elbow_side}`: where the elbow points, default "left of the frame".
- Pre-step a separate image prompt text: "@Image 1 is used only for the person's face, hair and skin tone; ignore its pose, clothing, background and light. Generate a square portrait of this person seated on dark coastal rocks by a calm sea at golden hour, exactly two white feathered wings attached behind the shoulders, a draped off-white tunic, gazing left, both hands in the lap"; check for two wings and for likeness.
**Post:** destination stack with the square-panel layout described under `pearl-earring`. The painting depicts a nude figure: crop to head, hair and raised arms and exclude the torso so the delivered panel is suitable for shared use, and record the crop. No overlays.
**QA:**
- Exactly two wings, attached at the shoulder blades, through the whole arm lift.
- The hand covers the eyes by about 3 s and is lowered by about 5 s.
- Face identity and skin tone match the still before and after the arm lift.
- Stack is 1:2, clean crop, no text.
**Risks:** wings fusing with the back or doubling during the arm lift; fingers and eye contact artifacts when the hand covers the face; identity drift while the face is covered; skin-tone drift; the nude source painting (crop it, do not generate nudity). Gallery matching by thumbnail inspection, medium certainty.
**Status:** tested once in the 2026-10-08 showcase run (project `effects-showcase`, scene-36, first-frame plus FFmpeg stack, 480p draft, sound on, one invented subject at 9:16): clean; the lift is about 0.5 s early; one quiet sigh in the sound. Not verified on other photos or at a higher resolution.
