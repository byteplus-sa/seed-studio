# Worked repairs

Focused reference for `seedance-shot-design`. Read [the entrypoint](../SKILL.md)
for the procedure and the variety rules.

All cases are **hypothetical**. The failure descriptions are simulated editorial
judgments drawn from recurring prompt shapes, not measured generation outcomes.

## Equal-length size ladder with no move or light change

- **Brief:** A 12-second kitchen scene. A mother opens the door, her son peeks
  out from behind a visiting aunt and taps the door frame, and she smiles.
- **Initial prompt shape:** Shot 1 (0-3 s) wide shot of the room. Shot 2 (3-6 s)
  medium shot at the door. Shot 3 (6-9 s) medium two-shot. Shot 4 (9-12 s) wide
  shot. One lighting sentence at the top: "soft late-afternoon daylight".
- **Simulated failure:** The son's tap and the mother's registration are omitted;
  the cut returns wide before their interaction can be read.
- **Hypothesis:** The cut points were selected without the action's purpose.
  Equal lengths, eye level and stable light are not themselves defects.
- **Smallest repair:** Keep the four beats, equal durations and stable window
  light. In shot 3, place the boy's tap and the mother's registration in the
  two-shot before the cut returns wide. If their response cannot fit, propose
  borrowing time from the opening rather than silently changing locked timing.
- **Tradeoff:** The interaction relies on readable shared framing rather than
  a close-up. A more varied camera plan is an alternative only if requested.
- **Acceptance:** The tap and the mother's registration are readable in order;
  no shot invents a light source. A varied option is not required: a held
  setup or equal-length shots that reveal the same interaction are also valid.

## A recorded axis that never reaches the shots

- **Brief:** A seven-clip animated family piece. `project.md` records the camera
  axis as `user_confirmed`: "low, object-eye-level camera, gentle dolly and
  crane moves, one tracking move in the escape".
- **Initial prompt shape:** Each clip lists "overhead close-up", "medium shot",
  "medium close-up" and no move.
- **Simulated failure:** The stance is promised once and absent from every shot,
  so the footage has the sizes without the promised dolly, crane or tracking, and
  the overhead views contradict the low-camera axis.
- **Hypothesis:** The axis lived in the brief and nothing required the shot
  lines to carry it.
- **Smallest repair:** Add `axis_carry` to each scene plan. Assign the dolly,
  crane and tracking moves to named shots, and the tracking move to the escape
  clip only. Where a clip needs an overhead view the axis excludes, record a
  scene override with its reason.
- **Tradeoff:** Fewer free choices per shot; the stance becomes testable.
- **Acceptance:** Every move in the confirmed axis appears on a named shot, or
  the scene override says why it does not.

## Restrained brief that is still varied

- **Brief:** A naturalistic supermarket ad, 12 seconds. The client wants calm,
  unforced camera work and real-looking light. A shopper meets a neighbor in the
  freezer aisle. The shopper says {Hey, you finally came!} and the neighbor
  answers {Wouldn't miss it.}
- **Initial prompt shape:** "Hold a steady medium shot at eye level" for the whole
  clip, with "natural light".
- **Simulated failure:** The neighbor is obscured by a freezer door during the
  reply, hiding the shared greeting.
- **Hypothesis:** The framing misses the partner's response, not a variety quota.
- **Smallest repair:** Keep the held medium two-shot and calm performance.
  Shift the requested framing enough to keep the freezer-door edge clear of
  the neighbor's reply, with the actual aisle source named. Preserve both
  exact lines and the response time instead of adding a cut or a new turn.
- **Tradeoff:** A small framing shift may expose more aisle background; keep
  the supplied location and lighting consistent.
- **Acceptance:** Both greeting and reply remain readable, with the unforced
  camera requested by this calm brief. A held two-shot with an unobscured
  neighbor also passes. For this fictional English exchange only,
  words / 2.2 plus 1 s onset and 0.4 s tail is a provisional planning estimate,
  not a rejection threshold. Measured or native-language-informed delivery
  determines fit; retime or split if needed, without rewriting approved text.

## Dialogue scene whose moves hide the lips

- **Brief:** Two siblings argue across a dinner table, 14 seconds. The key line
  lands near the 9 second mark.
- **Initial prompt shape:** A whip pan between speakers on each line, and one
  global light sentence.
- **Simulated failure:** The whip pans land during speech, so the lips and the
  line are hard to read.
- **Hypothesis:** The pan crosses away from the speaker at the critical response.
- **Smallest repair:** Keep the argument's actor energy. Reposition the pan
  endpoint to frame the speaker before the key words, or use a tracking two-shot
  that retains both siblings. Quiet pushes are another option, not a requirement.
- **Tradeoff:** A tracking two-shot retains physical urgency but needs enough
  frame width and focus depth to reveal both responses.
- **Acceptance:** The key line, its speaker and the listener's registration
  remain readable at the planned speed, with consistent dinner-lamp geography.
  Energetic dialogue does not fail simply because movement continues.

## Energetic exchange and quiet counterpart

- **Brief:** Two couriers hurry side by side to deliver a parcel. One says exactly
  {This way!}; the other changes direction to follow. Keep their quick pace and
  use a tracking medium two-shot. No fall, collision or added dialogue.
- **Initial prompt:** Both slow to a gentle walk and stop for the line.
- **Simulated failure:** Speech protection removes the urgency of the delivery.
- **Hypothesis:** Actor energy was confused with camera stability.
- **Smallest repair:** Keep the brisk steps, weight transfer into the turn and
  the follower's response; track alongside at a distance that reveals both.
- **Tradeoff:** Framing and speech fit remain provisional without playback.
- **Acceptance:** Exact words and follower registration remain intelligible;
  no compulsory hold or extra cut interrupts the turn. For a counterpart brief
  asking for quiet couriers waiting in the same framing, preserve waiting
  instead. More movement is not the acceptance criterion.
