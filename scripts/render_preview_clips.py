#!/usr/bin/env python3
"""Render hg-engine PREVIEW_CAPTURE tests to small MP4 clips with py-desmume.

Each clip keeps a rolling window immediately preceding the test-complete signal,
which removes most battle startup time while retaining the move animation.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import signal
import subprocess
import sys
import time
from collections import deque

from desmume.emulator import DeSmuME, DeSmuME_Memory


COMM_HOLE = 0x02FFF81C
TEST_CASE_PASS = -1
TEST_CASE_FAIL = -2
TEST_CASE_KNOWN_FAILING = -3


def crop_battle_screen(image):
    image = image.convert("RGB")
    width, height = image.size
    if width >= 256 and height >= 384:
        return image.crop((0, 0, 256, 192))
    if width >= 256 and height >= 192:
        return image.crop((0, 0, 256, 192))
    return image.resize((256, 192))


def write_mp4(frames, output: pathlib.Path, fps: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if not frames:
        raise RuntimeError(f"No frames captured for {output.name}")

    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", "256x192", "-r", str(fps), "-i", "-",
        "-an", "-c:v", "libx264", "-preset", "veryfast",
        "-crf", "27", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(output),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    try:
        for frame in frames:
            proc.stdin.write(frame.tobytes())
    finally:
        proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"ffmpeg failed for {output} with exit code {rc}")


def load_preview_test_ids(manifest_path: pathlib.Path) -> list[str]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    ids = []
    pattern = re.compile(r"PREVIEW_CAPTURE\s+(anim_[A-Za-z0-9_-]+)")
    for entry in data.get("selected_tests", []):
        name = entry.get("name", "")
        match = pattern.search(name)
        if not match:
            raise RuntimeError(f"Unexpected non-preview test in manifest: {name}")
        ids.append(match.group(1))
    return ids


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", default="test.nds", type=pathlib.Path)
    parser.add_argument("--save", default="test.sav", type=pathlib.Path)
    parser.add_argument("--test-manifest", default="build/battle_tests/test_manifest.json", type=pathlib.Path)
    parser.add_argument("--output-dir", required=True, type=pathlib.Path)
    parser.add_argument("--fps", type=int, default=15)
    parser.add_argument("--sample-every", type=int, default=4, help="Capture one frame every N emulator cycles")
    parser.add_argument("--seconds", type=int, default=10, help="Rolling seconds retained before test completion")
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--end-index", type=int, default=-1)
    args = parser.parse_args()

    preview_ids = load_preview_test_ids(args.test_manifest)
    end_index = len(preview_ids) if args.end_index < 0 else min(args.end_index, len(preview_ids))
    start_index = max(0, args.start_index)
    if start_index >= end_index:
        raise RuntimeError(f"Empty capture range {start_index}:{end_index}")

    selected_ids = preview_ids[start_index:end_index]
    max_frames = max(1, args.fps * args.seconds)
    ring = deque(maxlen=max_frames)
    completed = []
    failures = []
    current_local = 0
    cycle_count = 0
    last_activity = time.monotonic()

    emu = DeSmuME()
    emu_memory = emu.memory
    memory = DeSmuME_Memory(emu)

    def current_preview():
        if 0 <= current_local < len(selected_ids):
            return selected_ids[current_local]
        return None

    def on_result(address, size):
        nonlocal current_local, last_activity
        del address, size
        value = emu_memory.signed[COMM_HOLE]
        if value not in (TEST_CASE_PASS, TEST_CASE_FAIL, TEST_CASE_KNOWN_FAILING):
            return

        preview_id = current_preview()
        if preview_id is None:
            return

        last_activity = time.monotonic()
        output = args.output_dir / f"{preview_id}.mp4"
        write_mp4(list(ring), output, args.fps)
        completed.append(preview_id)
        if value != TEST_CASE_PASS:
            failures.append({"preview_id": preview_id, "result": int(value)})
        print(f"[rendered] {preview_id} -> {output}", flush=True)
        ring.clear()
        current_local += 1

    memory.register_write(COMM_HOLE, on_result)

    def stop(signum, frame):
        del frame
        try:
            emu.destroy()
        finally:
            raise SystemExit(signum)

    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)

    emu.open(str(args.rom))
    emu.backup.import_file(str(args.save))

    for _ in range(120):
        emu.cycle(False)

    emu_memory.write_long(COMM_HOLE, start_index + (end_index << 16))

    while current_local < len(selected_ids):
        if time.monotonic() - last_activity > 180:
            raise RuntimeError(f"Timed out while rendering {current_preview()}")

        emu.cycle(False)
        cycle_count += 1
        if cycle_count % args.sample_every == 0:
            ring.append(crop_battle_screen(emu.screenshot()))

    emu.destroy()

    summary = {
        "start_index": start_index,
        "end_index": end_index,
        "requested": len(selected_ids),
        "rendered": len(completed),
        "failures": failures,
        "preview_ids": completed,
    }
    (args.output_dir / "render_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
