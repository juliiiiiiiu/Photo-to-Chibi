---
name: photo-to-chibi
description: Transform uploaded people photos into clean, highly super-deformed Japanese-anime-inspired chibi character art with sparse linework, flat cel colour, a solid white background, and automatic single-person, couple, family, or group composition. Use for cute isolated photo-to-chibi artwork, not realistic caricatures, painterly portraits, generic cartoons, or copies of named characters.
---

# Photo to Chibi

Create original, recognisable anime chibis through character redesign rather than a cartoon filter. Use extreme super-deformation, symbolic anime faces, sparse controlled lines, flat cel colour, one clear emotion, and clean subject isolation. The result must read immediately as cute anime chibi rather than a realistic caricature, watercolour portrait, children's-book cartoon, social-media sticker template, or standard-proportioned anime portrait.

## Inspect and route

Inspect every user-uploaded identity photo before generating. The published skill contains no bundled reference artwork. Never retrieve, reuse, copy, or package sample images from earlier conversations.

The default **Try it** experience needs no user-written prompt. Inspect the uploaded photo and route automatically:

1. One visible person: create one neutral-styled character unless the user requested another presentation.
2. Two visible people: create a balanced couple-style pair with a warm, non-sexual interaction such as standing close, holding hands, or a light side embrace. Do not add wedding, dating, or sexual cues.
3. Three to six visible people: preserve every recognisable person. Use the family route when the image itself clearly shows a mixed-age family; otherwise use the group route without asserting a relationship.
4. Seven or more visible people: create a compact, readable multi-row group composition and preserve everyone who is recognisable. Do not silently remove people.
5. An explicit user request for a single person, couple, family, group, feminine, masculine, or neutral treatment always overrides the automatic route.

Use neutral styling when presentation cues are mixed or unclear; do not claim anyone's gender or relationship in the response. Do not ask for a style or relationship prompt merely because several people are present. Ask for a clearer photo only when a face, hairstyle, distinctive accessory, or clothing is too obscured to preserve.

## Lock the visual target

Apply these invariants unless the user explicitly requests a different chibi direction:

- **Proportion:** use the route-specific target range in [references/chibi-recipe.md](references/chibi-recipe.md). Single people and couples default to 1.55–1.75 heads tall with the head occupying 58–65% of total height. Relax the ratio only as specified for larger groups.
- **Framing:** recompose the source rather than preserving its crop. Default to a square 1:1 canvas with complete compact figure(s); use a 4:5 canvas only when it is needed to keep a large family or group readable. Even for a vertical wallpaper, show the complete compact figure(s) unless the user asks for a close-up.
- **Composition:** establish one dominant diagonal or S-curve through the face, hands, hair, clothing, and hero prop. Use the pose and silhouette—not decorative surroundings—to create motion. Keep a comfortable plain-white margin around the complete figure and do not add a sticker border.
- **Line colour:** use `#A6A3A5` as the default visible character-contour colour. Keep internal construction lines at the same colour or lighter; do not use black or near-black for the outer silhouette. Eyes, lashes, brows, and filled hair masses may use deeper local colours when needed for readability, but they must not turn the complete figure outline dark again.
- **Skin:** use `#FAE8DD` as the default flat skin base. Keep skin highlights close to the base and use one restrained peach-rose or cool rose-beige cel-shadow derived from it. Do not shift the whole complexion toward yellow, orange, grey, or brown.
- **Palette:** use five to eight main colour families per character, predominantly low-to-medium saturation. Reserve the strongest chroma for the eyes and one small focal accent covering no more than about 10–15% of the figure. Keep skin light and neutral-warm without a yellow-orange cast.
- **Rendering:** use clean flat fills and one hard-edged cel-shadow step per material. A small second shadow is allowed only in deep hair or clothing overlaps. Confine highlights to the eyes and one or two simple hair or fabric shapes. Do not use watercolour wash, paper grain, painterly blending, realistic bounce light, pearl effects, plastic gloss, or 3D rendering.
- **Background:** default to a fully opaque, perfectly uniform pure-white canvas (`#FFFFFF`). Do not request or simulate transparency. Never draw a grey-and-white checkerboard, transparency grid, tiled pattern, or cutout-preview pattern. Do not add scenery, colour fields, gradients, panels, halos, circles, stars, sparkles, ribbons, petals, icons, floor planes, cast shadows, borders, or foreground elements. If the user explicitly requests a transparent PNG, use a real alpha channel only; never render a checkerboard pattern into the pixels.

Preserve identity through a few high-signal cues: hairstyle silhouette and colour, skin tone, glasses, a facial mark, key accessories, and recognisable clothing colours. Freely simplify face geometry, anatomy, fingers, fabric folds, and the original framing to achieve the mascot proportions. Identity preservation must not pull the result back toward realistic adult anatomy.

When the source shows only the upper body, preserve the visible top and design a plausible lower-body outfit rather than copying the top colour downward. The lower garment must use a clearly different but coordinated primary colour, separated from the top by hue or by a noticeable lightness difference. Avoid a one-colour jumpsuit effect unless the visible source clearly shows one. When footwear is not visible, canvas sneakers are a preferred default. Use at least two visibly distinct colours across the shoe body, toe cap, laces, and sole; never invent featureless single-colour shoes.

## Apply the original style specification

Read [references/chibi-recipe.md](references/chibi-recipe.md) first and apply only the route-specific parameters. Then read [references/style-spec.md](references/style-spec.md) for the shared visual language. Both references are generic and are not tied to any existing character or artwork.

If the user voluntarily supplies a style reference for the current request, use it only as transient guidance for high-level visual qualities. Do not reproduce its character, outfit, accessories, text, logo, or exact composition. Do not copy it into the skill, save it as an asset, or make future runs depend on it.

## Generate

Use the built-in image generation tool by default. This is a photo-to-illustration transformation, so use the `style-transfer` use case while explicitly preserving the subject's identity features.

- Use only the current user's identity source or sources, plus an optional style reference supplied in that same request.
- If an identity source is already visible in the current conversation, do not reopen it merely to inspect it again. If it exists only as a local file, inspect it once before generation.
- Label each input image's role in the prompt. For couples, families, and groups, make clear which features belong to each visible person. Never pull images from the skill directory or a previous task.
- Read [references/prompt-templates.md](references/prompt-templates.md) for the matching route and adapt only the fields supplied by the user.
- When generating multiple examples or variants, keep every output on the same perfectly uniform pure-white background. Vary the pose, expression, crop, clothing treatment, or finish only when variation was requested; never manufacture variation through backdrops or decorations.

Reinterpret any key action or prop in refined chibi form. Keep exactly one meaningful item such as a flower, camera, or strawberry when it is central to the source or request. Do not duplicate it or echo it with surrounding motifs. Use an original design and do not add extra people, unrequested animal ears, pets, branded items, text, signatures, or watermarks.

For couples, families, and groups, keep every face separately recognisable and retain individual hair, clothing, and accessories. Use natural, non-sexual interactions. Do not alter a person's apparent age, create romantic interactions in family or group compositions, merge bodies, or make one person a decorative secondary character.

## Publication and rights guardrails

- Keep the published package limited to original text, code, and assets that the publisher owns or has an explicit redistribution licence for. Do not include user photos, generated samples, screenshots, third-party art, logos, fonts, or model outputs with uncertain rights.
- Treat uploaded photos and current-request style references as transient inputs only. Do not save, package, publish, train on, or reuse them in another user's request.
- Do not reproduce named characters, franchises, logos, copyrighted artwork, or a particular artist's signature visual expression. Offer an original generic chibi treatment instead.
- The user is responsible for having permission to upload and transform every person and source image. This skill does not grant rights to photos or third-party material.

## Review and iterate

Read [references/qa-checklist.md](references/qa-checklist.md) after every generation. If there is a material error, make at most one targeted retry that names only the failed invariant, such as fixing a swapped hairstyle or removing extra fingers. Do not repeatedly regenerate without user direction.

For preview-only requests, show the selected result inline. If the user asks for a project asset or gives a destination, place the final selected image there without overwriting an existing file unless replacement was explicitly requested.
