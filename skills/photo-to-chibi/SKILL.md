---
name: photo-to-chibi
description: Transform uploaded people photos into clean, highly super-deformed Japanese-anime-inspired chibi character art with sparse linework, flat cel colour, an optional solid-white or scenic background, and automatic single-person, couple, family, or group composition. Use for cute chibi character art, not realistic caricatures, painterly portraits, generic cartoons, or copies of named characters.
---

# Photo to Chibi

Create original, recognisable anime chibis through character redesign rather than a cartoon filter. Use super-deformation, symbolic anime faces, sparse controlled lines, flat cel colour, one clear emotion, and clean subject isolation. The result must read immediately as cute anime chibi rather than a realistic caricature, watercolour portrait, children's-book cartoon, social-media sticker template, or standard-proportioned anime portrait.

## Inspect and route

Inspect every user-uploaded identity photo before generating. The published skill contains no bundled reference artwork. Never retrieve, reuse, copy, or package sample images from earlier conversations.

The default **Try it** experience needs no user-written prompt. Based on the number of recognisable people, automatically choose a single-person, couple-style pair, or group composition; use a family composition only when the image clearly shows a mixed-age family. Preserve every recognisable person and do not infer relationships beyond what the image establishes. An explicit user request for a single person, couple, family, group, feminine, masculine, or neutral treatment always overrides the automatic route.

## Try it prompts

Use the default entry point with an uploaded photo, or copy one of these English prompts:

- `$photo-to-chibi`
- `/photo-to-chibi Keep the original background.`
- `/photo-to-chibi Add a scenic mountain and lake background.`
- `/photo-to-chibi Add a charming town-view background.`
- `/photo-to-chibi Place the character in a warm, sunlit flower garden.`
- `/photo-to-chibi Create a cozy nighttime city background with glowing streetlights.`
- `/photo-to-chibi Use a dreamy pastel sky with soft clouds and floating sparkles.`

Use neutral styling when presentation cues are mixed or unclear; do not claim anyone's gender or relationship in the response. Do not ask for a style or relationship prompt merely because several people are present. Ask for a clearer photo only when a face, hairstyle, distinctive accessory, or clothing is too obscured to preserve.

## Lock the visual target

Apply these invariants unless the user explicitly requests a different chibi direction:

- **Proportion:** use the route-specific target range in [references/chibi-recipe.md](references/chibi-recipe.md), except that single people and couples default to 2.4–2.9 heads tall. Relax the ratio only as specified for larger groups.
- **Framing:** preserve the source's visible framing by default; do not independently extend a partial or upper-body source into a full-body figure. Extend it only when the user explicitly asks for a full-body composition or when retaining the original framing would make the user's requested description unattainable. When a full figure is warranted, default to a square 1:1 canvas with compact figure(s); use a 4:5 canvas only when it is needed to keep a large family or group readable.
- **Composition:** establish one dominant diagonal or S-curve through the face, hands, hair, clothing, and hero prop. Use the pose and silhouette—not decorative surroundings—to create motion. For the default white background, keep a comfortable plain-white margin around the complete figure and do not add a sticker border.
- **Line colour:** use the light cool grey `#B8B7BA` as the default visible character-contour colour. Draw exactly one thin continuous outer contour, with no second offset stroke. Keep internal construction lines at the same colour or lighter; do not use black or near-black for the outer silhouette. Never add a white outer stroke, white rim, halo, sticker border, glow, or any pale fringe between the character and the background. Eyes, lashes, brows, and filled hair masses may use deeper local colours when needed for readability, but they must not turn the complete figure outline dark again.
- **Skin:** use `#FAE8DD` as the default flat skin base. Keep skin highlights close to the base and use one restrained peach-rose or cool rose-beige cel-shadow derived from it. Do not shift the whole complexion toward yellow, orange, grey, or brown.
- **Palette:** use five to eight main colour families per character. Keep most colours low-to-medium saturation but make clothing and footwear cheerful and visually varied rather than uniformly grey, beige, or muted. Reserve the strongest chroma for the eyes and one small focal accent covering no more than about 10–15% of the figure. Keep skin light and neutral without a yellow-orange cast.
- **Rendering:** use clean flat fills and one hard-edged cel-shadow step per material. A small second shadow is allowed only in deep hair or clothing overlaps. Confine highlights to the eyes and one or two simple hair or fabric shapes. Do not use watercolour wash, paper grain, painterly blending, pearl effects, plastic gloss, or 3D rendering.
- **Background:** default to a pure-white canvas (`#FFFFFF`). Do not request or simulate transparency. Never draw a grey-and-white checkerboard, transparency grid, tiled pattern, or cutout-preview pattern. Do not add scenery, colour fields, gradients, panels, halos, circles, stars, sparkles, ribbons, petals, icons, floor planes, cast shadows, borders, or foreground elements. This default is overridden only when the user explicitly requests a scenic or other non-white background. If the user explicitly requests a transparent PNG, use a real alpha channel only; never render a checkerboard pattern into the pixels.

## Scenic background adaptation

When the user explicitly requests a non-white background, preserve the specified location, time, weather, season, and essential objects. Before writing the generation prompt, follow this routing process:

1. Identify one primary background type from the requested setting or the clearly visible source setting.
2. Read **only** its matching reference file:
   - Mountains, forests, fields, shores, or Japanese mountain lakes: [landscape.md](references/scenic-environments/landscape.md)
   - Streets, stations, shopfronts, residential areas, or city views: [town.md](references/scenic-environments/town.md)
   - School gates, classrooms, corridors, courtyards, or playgrounds: [school.md](references/scenic-environments/school.md)
   - Living rooms, bedrooms, kitchens, dining rooms, or home entrances: [home.md](references/scenic-environments/home.md)
   - Cafés, libraries, studios, galleries, or other public interiors: [interior.md](references/scenic-environments/interior.md)
   - A lake, river, sea, pool, or water surface that is the main scene anchor: [water.md](references/scenic-environments/water.md)
   - A night, dusk, or illuminated evening scene: [night.md](references/scenic-environments/night.md)
3. When the scene contains several types, select the one that supplies the principal visual anchor. A Japanese mountain lake is `landscape`; use `water` only when the water surface itself is the primary subject.
4. Do not read unrelated scene references. Apply time, weather, and season within the selected primary-scene file.

Render the characters and environment at deliberately different detail levels: preserve clean, flat, highly super-deformed chibi rendering for the people, while rendering the environment as a high-fidelity, cinematic Japanese-anime background with near-photographic natural material detail. Keep the atmosphere lucid, cool, crisp, and cleanly colour-graded, using believable scale, aerial perspective, and controlled hard-edged clarity. This is not a flat cel-shaded or children's-cartoon backdrop; it should remain distinctly anime rather than literal photography, muddy haze, or over-bloomed imagery.

**Source sunlight:** when the original photo visibly contains natural sunlight or sunbeams, carry that lighting into the output with a restrained, natural sunlit haze or soft lens-flare halo. Integrate it with the scene's apparent light direction, keep it away from the character outline and face, and preserve a clear, readable subject. This conditional lighting treatment may be used even when the normal background is white; it does not permit a sticker-like halo, decorative circle, or indiscriminate bloom.

Keep characters as the primary focal point. Reduce detail, contrast, and saturation behind faces, hands, and the hero prop. Do not add unrequested text, logos, watermarks, vehicles, people, animals, tents, or landmark objects. User-specified scene content has highest priority; character identity and readability always remain highest.

Preserve identity through a few high-signal cues: hairstyle silhouette and colour, skin tone, glasses, a facial mark, key accessories, and recognisable clothing colours. Freely simplify face geometry, anatomy, fingers, fabric folds, and the original framing to achieve the mascot proportions. Identity preservation must not pull the result back toward realistic adult anatomy.

**Beards and moustaches:** remove subtle, sparse, short, or stubble-like beards and moustaches by default. Preserve them only when they are a strong, clearly recognisable identity feature—for example, a dense full beard, a long beard, or a prominent thick moustache. When retained, simplify them into one or two clean flat chibi shapes; never render individual hairs or realistic stubble.

When a full-body extension of an upper-body source is warranted under the framing rule, preserve the visible top and design a plausible lower-body outfit rather than copying the top colour downward. The lower garment must use a clearly different but coordinated primary colour, separated from the top by hue or by a noticeable lightness difference. Avoid a one-colour jumpsuit effect unless the visible source clearly shows one. Default to straight-leg or gently tapered trousers, an A-line skirt, or shorts as appropriate; for feminine styling, default trousers to a visibly slim jeans, or gently tapered leg similar to the reference's trouser width. Do not invent flared, bell-bottom, or excessively wide-leg trousers unless clearly shown in the source. When footwear is not visible, canvas sneakers are a preferred default. Use at least two visibly distinct colours across the shoe body, toe cap, laces, and sole; never invent featureless single-colour shoes.

## Apply the original style specification

Read [references/chibi-recipe.md](references/chibi-recipe.md) first and apply only the route-specific parameters. Then read [references/style-spec.md](references/style-spec.md) for the shared visual language. Both references are generic and are not tied to any existing character or artwork.

If the user voluntarily supplies a style reference for the current request, use it only as transient guidance for high-level visual qualities. Do not reproduce its character, outfit, accessories, text, logo, or exact composition. Do not copy it into the skill, save it as an asset, or make future runs depend on it.

## Generate

Use the host's available image-generation or image-editing capability. Prefer an image-to-image portrait transformation that can receive the current identity photo directly; if the host exposes named modes, choose its closest image-editing or style-transfer mode. Do not assume a particular vendor, model, command, or tool name. If the host cannot generate or edit images, return one production-ready prompt that preserves all applicable constraints and clearly state that no image was generated.

- Use only the current user's identity source or sources, plus an optional style reference supplied in that same request.
- If an identity source is already visible in the current conversation, do not reopen it merely to inspect it again. If it exists only as a local file, inspect it once before generation.
- Label each input image's role in the prompt. For couples, families, and groups, make clear which features belong to each visible person. Never pull images from the skill directory or a previous task.
- Read [references/prompt-templates.md](references/prompt-templates.md) for the matching route and adapt only the fields supplied by the user.
- When generating multiple examples or variants, keep the selected background treatment consistent across every output: a perfectly uniform pure-white background by default, or the requested scenic background when applicable. Vary the pose, expression, crop, clothing treatment, or finish only when variation was requested; never manufacture variation through unrelated backdrops or decorations.

Reinterpret any key action or prop in refined chibi form. Keep exactly one meaningful item such as a flower, camera, or strawberry when it is central to the source or request. Do not duplicate it or echo it with surrounding motifs. Use an original design and do not add extra people, unrequested animal ears, pets, branded items, text, signatures, or watermarks.

For couples, families, and groups, keep every face separately recognisable and retain individual hair, clothing, and accessories. Use natural, non-sexual interactions. Do not alter a person's apparent age, create romantic interactions in family or group compositions, merge bodies, or make one person a decorative secondary character.

## Publication and rights guardrails

- Keep the published package limited to original text, code, and assets that the publisher owns or has an explicit redistribution licence for. Do not include user photos, generated samples, screenshots, third-party art, logos, fonts, or model outputs with uncertain rights.
- Treat uploaded photos and current-request style references as transient inputs only. Do not save, package, publish, train on, or reuse them in another user's request.
- Do not reproduce named characters, franchises, logos, copyrighted artwork, or a particular artist's signature visual expression. Offer an original generic chibi treatment instead.
- The user is responsible for having permission to upload and transform every person and source image. This skill does not grant rights to photos or third-party material.
