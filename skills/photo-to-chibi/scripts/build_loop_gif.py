#!/usr/bin/env python3
"""Assemble ordered still frames into a stable looping GIF."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a looping GIF from ordered PNG/JPEG frames."
    )
    parser.add_argument("frames", nargs="+", type=Path, help="Frames in playback order")
    parser.add_argument("--output", required=True, type=Path, help="Output .gif path")
    parser.add_argument("--fps", type=float, default=10.0, help="Playback rate (default: 10)")
    parser.add_argument(
        "--ping-pong",
        action="store_true",
        help="Append reversed interior frames for a seamless return",
    )
    parser.add_argument(
        "--hold-first-ms", type=int, default=0, help="Extra hold on the first frame"
    )
    parser.add_argument(
        "--hold-last-ms", type=int, default=0, help="Extra hold on the last frame"
    )
    parser.add_argument(
        "--colors", type=int, default=256, help="Shared GIF palette size (2-256)"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.fps <= 0:
        raise SystemExit("--fps must be greater than zero")
    if not 2 <= args.colors <= 256:
        raise SystemExit("--colors must be between 2 and 256")
    if args.output.suffix.lower() != ".gif":
        raise SystemExit("--output must end in .gif")
    if args.hold_first_ms < 0 or args.hold_last_ms < 0:
        raise SystemExit("hold durations cannot be negative")

    frames: list[Image.Image] = []
    for path in args.frames:
        if not path.is_file():
            raise SystemExit(f"frame does not exist: {path}")
        with Image.open(path) as source:
            frames.append(source.convert("RGB"))

    expected_size = frames[0].size
    mismatched = [
        str(path)
        for path, frame in zip(args.frames, frames)
        if frame.size != expected_size
    ]
    if mismatched:
        raise SystemExit("all frames must have the same dimensions: " + ", ".join(mismatched))

    if args.ping_pong and len(frames) > 2:
        frames.extend(frame.copy() for frame in reversed(frames[1:-1]))

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

    frame_ms = max(20, round(1000 / args.fps))
    durations = [frame_ms] * len(paletted)
    durations[0] += args.hold_first_ms
    durations[-1] += args.hold_last_ms

    args.output.parent.mkdir(parents=True, exist_ok=True)
    paletted[0].save(
        args.output,
        save_all=True,
        append_images=paletted[1:],
        duration=durations,
        loop=0,
        optimize=False,
        disposal=2,
    )


if __name__ == "__main__":
    main()
