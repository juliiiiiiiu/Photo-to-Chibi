# Live-style animation recipe

Use this reference only when the requested output includes motion. The goal is a tiny, believable loop that feels like a living illustration, not a talking avatar or a camera effect.

## Motion priorities

Preserve, in order:

1. Person count, identity, hairstyle silhouette, accessories, clothing, and facial proportions.
2. A locked crop, camera, background, and character placement.
3. One readable style-specific facial action.
4. Subtle secondary motion such as breathing, hair tips, or clothing edges.
5. A clean first-to-last-frame loop.

The primary action must be visibly expressed in the face. A GIF that merely moves, scales, crops, or shakes the full image has failed this skill, even if it contains several frames.

Do not introduce speech, lip-sync, teeth changes, face turns beyond a few degrees, hand gestures that alter anatomy, camera pans, zooms, tilts, global scale changes, parallax drift, flashing effects, new props, or new decorations unless explicitly requested. Keep the camera, crop, background, and every non-animated facial feature in the same position across frames.

## Style map

| Style | Primary action | Secondary motion | Timing and feel |
|---|---|---|---|
| `自然` | One soft two-eye blink | Barely visible breathing; optional 1–2 px-equivalent hair-tip drift | 2.8–3.6 s, calm, asymmetrical timing |
| `可爱` | Soft blink followed by a tiny smile or 2–4° head tilt | Small buoyant settle; slight blush change | 2.4–3.2 s, light and springy, never babyish distortion |
| `搞怪` | One wink, cheek puff, eyebrow pop, or brief tongue peek; choose exactly one gag | Tiny head bob timed to the gag | 2.0–2.8 s, readable but controlled; no face warping |
| `酷酷` | Slow half-lid blink or brief sideways eye glance | Very slight chin lift and restrained hair or coat-edge sway | 2.6–3.4 s, composed, low-amplitude, no dramatic spin |

Choose one primary action only. Add no more than two secondary motions. For a custom style, infer the closest motion grammar while preserving these amplitude and continuity limits.

The action listed in the **Primary action** column is mandatory. It must reach a clearly distinct peak frame: fully or noticeably closed eyelids for a blink/wink, a visibly different eye direction for a glance, or a distinct eyebrow/cheek/mouth state for the selected playful action. A tiny overall scale change, hair drift, or body bob cannot count as the primary action.

For couples and groups, avoid synchronized blinking. Animate no more than two faces prominently at the same instant, stagger blinks by roughly 0.3–0.8 seconds, and keep the rest of the group nearly still. Never omit, merge, or hide a person during motion.

## Image-to-video prompt scaffold

Use the still chibi master as the sole visual source:

```text
Create a short seamless looping animation from this exact chibi master image. Keep the camera, crop, background, body pose, person count, identity cues, hairstyle, accessories, clothing shapes, colours, linework, and facial proportions locked. Motion style: [自然 / 可爱 / 搞怪 / 酷酷]. Primary action: [one action from the style map]. Secondary motion: [zero to two subtle motions]. Duration: [2–4 seconds]. The first and last frame must match naturally. No talking, lip-sync, camera movement, zoom, scene parallax, face morphing, anatomy changes, new objects, disappearing details, flicker, outline wobble, or background swimming.
```

If the generator supports first/last-frame conditioning, use the same neutral master for both ends. If it supports motion strength, start low. Prefer a fixed seed or reference-lock setting when exposed, but do not assume those controls exist.

## Frame-based fallback

Use this only when a consistent image-editing capability can preserve the same master across edits. Create the fewest frames needed for the chosen action. Do not include a final frame identical to the first; the GIF loop supplies that return and a duplicated endpoint creates an accidental pause:

- Blink: neutral → half-closed → closed → half-closed.
- Wink: neutral → one eye half-closed → one eye closed → half-closed.
- Smile or eyebrow change: neutral → subtle transition → peak; assemble with `--ping-pong`.
- Head tilt or bob: neutral → small offset → peak offset; assemble with `--ping-pong`.

Edit only the named facial or secondary-motion regions. Keep canvas size and subject placement pixel-aligned. Reuse the neutral master as both the first and last state. Do not redraw the whole scene independently for each frame.

Save ordered frames as PNGs, then run:

```bash
python3 scripts/build_loop_gif.py --output result.gif --fps 10 --hold-first-ms 400 frame-01.png frame-02.png frame-03.png frame-04.png
```

Use 8–12 fps. Extend the neutral frame duration rather than duplicating many identical frames. For a one-way motion sequence that does not already return to neutral, add `--ping-pong`.

## Guaranteed-GIF raster fallback

When the host generated only one static master and cannot make stable edited keyframes, do not use a non-facial loop to satisfy a facial-animation request. The conservative local fallback below is permitted only when the user explicitly asks for a camera-like micro-motion loop without a changing expression:

```bash
python3 scripts/make_subtle_motion_gif.py --style natural --output result.gif master.png
```

Map the selected style to the script value: `自然` → `natural`, `可爱` → `cute`, `搞怪` → `funny`, `酷酷` → `cool`. The fallback uses only a very small scale pulse or bounce. It cannot create a true blink, wink, facial gag, or eye glance from a single static raster, and must never be selected automatically for any of those requested actions.

Treat the master PNG as an intermediate artifact. Confirm that the output path ends in `.gif` and that the result has three or more frames before presenting it to the user.

## Quality gate

Inspect the rendered GIF, not only its source frames. Confirm:

- the face and silhouette remain recognisable and stable;
- the neutral and peak frames show the required visible facial change;
- eyes close along the existing eyelid direction without changing eye size or spacing;
- the background is stationary and does not shimmer;
- no zoom, pan, tilt, overall-image breathing, or other camera movement occurs;
- the loop has no visible jump, flash, or pause caused by duplicate endpoint frames;
- the motion remains legible at normal chat-preview size;
- the GIF is fully opaque unless the user explicitly requested true transparency.

Use one corrective retry for a material failure. Prefer less motion when stability and expressiveness conflict.
