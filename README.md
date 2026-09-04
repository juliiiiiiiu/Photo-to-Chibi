# Photo to Chibi

Turn an uploaded photo of one or more people into clean, highly super-deformed anime-inspired chibi artwork on a uniform white background.

The single source of truth is the visible `skills/photo-to-chibi/` directory. The core `SKILL.md` and its references are vendor-neutral. `agents/openai.yaml` is optional OpenAI/Codex UI metadata; Grok and other hosts can ignore it.

## Try it

Upload a photo, then use one of these prompts:

```text
$photo-to-chibi
```

```text
/photo-to-chibi Keep the original background.
```

```text
/photo-to-chibi Add a scenic mountain and lake background.
```

```text
/photo-to-chibi Add a charming town-view background.
```

```text
/photo-to-chibi Place the character in a warm, sunlit flower garden.
```

```text
/photo-to-chibi Create a cozy nighttime city background with glowing streetlights.
```

```text
/photo-to-chibi Use a dreamy pastel sky with soft clouds and floating sparkles.
```

## Requirements

The host needs to be able to inspect the supplied identity image and generate or edit a raster image. When image generation is unavailable, the skill returns a production-ready prompt instead of claiming that it generated an image.

## Use with Codex

Open this repository as the Codex project and invoke:

```text
$photo-to-chibi
```

Codex discovers the repository skill through `.agents/skills/photo-to-chibi`, which is only a symbolic link to the visible source directory. There is no duplicate skill content to maintain.

## Use with Grok Build

Grok Build discovers project skills from `.grok/skills`, user skills from `~/.grok/skills`, and additional directories configured under `[skills] paths`. Point Grok Build at the visible source directory instead of copying the skill.

Add the following to `~/.grok/config.toml`, replacing the example with the absolute path of your clone:

```toml
[skills]
paths = ["/absolute/path/to/Q-animme/skills"]
```

Verify discovery and start Grok Build:

```bash
cd /absolute/path/to/Q-animme
grok inspect
grok
```

Then upload or provide the portrait and invoke:

```text
/photo-to-chibi
```

For a one-off run without changing Grok configuration, open Grok Build in the repository and ask:

```text
Read @skills/photo-to-chibi/SKILL.md and follow it with my supplied portrait. Read every reference that SKILL.md routes to for this request.
```

If the current Grok Build environment does not expose an image-generation or image-editing capability, it will return the final production prompt for use with an image generator.

## Use with Grok Bot

Grok Bot uses saved or packaged skills. After this repository is available to the Bot through a public link, attached files, or a connected GitHub account, ask it:

```text
Read skills/photo-to-chibi/SKILL.md and every referenced file in that folder. Save the complete workflow as a private skill named "Photo to Chibi" without changing its identity, composition, rendering, safety, or quality constraints.
```

Open **Settings → Plugins → Yours**, enable the private skill for the selected Bot, attach a portrait, and invoke the skill from the `/` menu.

Grok Bot currently stores the saved private skill in the Bot account; its documented workflow does not promise automatic synchronization with this Git repository. Treat this repository as canonical and re-import the skill after publishing an update. Packaged cross-platform distribution can be added later without changing the core instructions.

## Compatibility notes

- `SKILL.md` provides the portable workflow and required `name` and `description` frontmatter.
- `references/` contains the visual recipe, prompt templates, and quality checks used by every host.
- `agents/openai.yaml` improves the Codex interface only and does not lock the skill to OpenAI.
- Host-specific tool names are intentionally absent from the core workflow.
