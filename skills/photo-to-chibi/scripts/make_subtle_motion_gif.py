#!/usr/bin/env python3
"""Create a small, seamless live-style GIF loop from one opaque still image."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image


STYLE_SETTINGS = {
    "natural": (0.006, 18, 8.0),
    "cute": (0.012, 16, 8.0),
    "funny": (0.009, 14, 9.0),
    "cool": (0.004, 20, 8.0),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Turn one opaque still image into a subtle multi-frame looping GIF."
    )
    parser.add_argument("source", type=Path, help="Still master PNG or JPEG")
    parser.add_argument("--output", required=True, type=Path, help="Output .gif path")
    parser.add_argument(
        "--style", choices=STYLE_SETTINGS, default="natural", help="Motion curve"
    )
    parser.add_argument("--frames", type=int, help="Override the style's frame count")
    parser.add_argument("--fps", type=float, help="Override the style's frame rate")
    parser.add_argument("--colors", type=int, default=256, help="Palette size (2-256)")
    return parser.parse_args()


def motion_scale(style: str, phase: float, amplitude: float) -> float:
    if style == "cute":
        # A rounded little bounce with a slow settle at the neutral size.
        return 1.0 + amplitude * max(0.0, math.sin(phase)) ** 2
    if style == "funny":
        # Two short pulses per loop, still restrained enough to avoid warping.
        return 1.0 + amplitude * (0.5 + 0.5 * math.sin(2 * phase))
    if style == "cool":
        # A nearly imperceptible slow push-in and release.
        return 1.0 + amplitude * (0.5 + 0.5 * math.sin(phase - math.pi / 2))
    # Natural: a gentle breathing arc.
    return 1.0 + amplitude * (0.5 + 0.5 * math.sin(phase - math.pi / 2))


def crop_position(style: str, phase: float) -> tuple[float, float]:
    if style == "cute":
        return (0.5, 0.5 + 0.5 * math.sin(phase))
    if style == "funny":
        return (0.5 + 0.5 * math.sin(2 * phase), 0.5)
    if style == "cool":
        return (0.5 + 0.25 * math.sin(phase), 0.5 + 0.25 * math.cos(phase))
    return (0.5, 0.5 + 0.3 * math.sin(phase))


def scaled_frame(
    source: Image.Image, scale: float, horizontal_position: float, vertical_position: float
) -> Image.Image:
    width, height = source.size
    enlarged = source.resize(
        (max(width + 2, round(width * scale)), max(height + 2, round(height * scale))),
        Image.Resampling.LANCZOS,
    )
    left = round((enlarged.width - width) * horizontal_position)
    top = round((enlarged.height - height) * vertical_position)
    return enlarged.crop((left, top, left + width, top + height))


def main() -> None:
    args = parse_args()
    if not args.source.is_file():
        raise SystemExit(f"source does not exist: {args.source}")
    if args.output.suffix.lower() != ".gif":
        raise SystemExit("--output must end in .gif")
    if not 2 <= args.colors <= 256:
        raise SystemExit("--colors must be between 2 and 256")

    amplitude, default_frames, default_fps = STYLE_SETTINGS[args.style]
    frames_count = args.frames or default_frames
    fps = args.fps or default_fps
    if frames_count < 3:
        raise SystemExit("--frames must be at least 3")
    if fps <= 0:
        raise SystemExit("--fps must be greater than zero")

    with Image.open(args.source) as input_image:
        master = input_image.convert("RGB")

    frames = []
    for index in range(frames_count):
        phase = 2 * math.pi * index / frames_count
        horizontal_position, vertical_position = crop_position(args.style, phase)
        frames.append(
            scaled_frame(
                master,
                motion_scale(args.style, phase, amplitude),
                horizontal_position,
                vertical_position,
            )
        )
    palette = frames[0].quantize(
        colors=args.colors,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.FLOYDSTEINBERG,
    )
    paletted = [palette]
    paletted.extend(
        frame.quantize(palette=palette, dither=Image.Dither.FLOYDSTEINBERG)
        for frame in frames[1:]
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    paletted[0].save(
        args.output,
        save_all=True,
        append_images=paletted[1:],
        duration=max(20, round(1000 / fps)),
        loop=0,
        optimize=False,
        disposal=2,
    )


if __name__ == "__main__":
    main()
