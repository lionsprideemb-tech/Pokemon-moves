#!/usr/bin/env python3
"""Capture the selected hg-engine preview tests as small MP4 clips."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import signal
import subprocess
import sys
import time

from desmume.emulator import DeSmuME, DeSmuME_Memory

COMM_HOLE = 0x02FFF81C
TEST_CASE_PASS = -1
TEST_CASE_FAIL = -2
TEST_CASE_KNOWN_FAILING = -3


class FfmpegWriter:
    def __init__(self, path: pathlib.Path, fps: int):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self.proc = subprocess.Popen(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-f",
                "rawvideo",
                "-pix_fmt",
                "rgb24",
                "-s",
                "256x192",
                "-r",
                str(fps),
                "-i",
                "-",
                "-an",
                "-c:v",
                "libx264",
                "-preset",
                "veryfast",
                "-crf",
                "24",
                "-pix_fmt",
                "yuv420p",
                "-movflags",
                "+faststart",
                str(path),
            ],
            stdin=subprocess.PIPE,
        )
        self.frames = 0

    def write(self, image):
        if self.proc.stdin is None:
            return
        # py-desmume returns both DS screens stacked vertically.
        top = image.crop((0, 0, 256, 192)).convert("RGB")
        self.proc.stdin.write(top.tobytes())
        self.frames += 1

    def close(self):
        if self.proc.stdin is not None:
            self.proc.stdin.close()
        rc = self.proc.wait()
        if rc != 0:
            raise RuntimeError(f"ffmpeg failed for {self.path} with exit code {rc}")


def load_test_names() -> list[str]:
    p = pathlib.Path("build/battle_tests/test_manifest.json")
    data = json.loads(p.read_text(encoding="utf-8"))
    return [x["name"] for x in data["selected_tests"]]


def preview_id_from_test_name(name: str) -> str:
    m = re.search(r"\bPreview\s+(anim_[0-9]+)\b", name)
    if not m:
        raise ValueError(f"Test is not a preview test: {name}")
    return m.group(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--sample-every", type=int, default=2)
    parser.add_argument("--idle-timeout", type=int, default=180)
    parser.add_argument("--max-frames-per-test", type=int, default=1200)
    args = parser.parse_args()

    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    test_names = load_test_names()
    preview_ids = [preview_id_from_test_name(x) for x in test_names]
    total = len(test_names)
    if total == 0:
        raise SystemExit("No preview tests were generated.")

    emu = DeSmuME()
    emu_memory = emu.memory
    memory = DeSmuME_Memory(emu)

    current = 0
    writer = None
    last_activity = time.monotonic()
    cycle_count = 0
    failures: list[str] = []

    def close_writer():
        nonlocal writer
        if writer is not None:
            writer.close()
            writer = None

    def callback(_address, _size):
        nonlocal current, last_activity
        value = emu_memory.signed[COMM_HOLE]
        if value not in (TEST_CASE_PASS, TEST_CASE_FAIL, TEST_CASE_KNOWN_FAILING):
            return
        close_writer()
        if current < total:
            pid = preview_ids[current]
            state = "pass" if value == TEST_CASE_PASS else "fail"
            print(f"[{state}] {pid}", flush=True)
            if value != TEST_CASE_PASS:
                failures.append(pid)
        current += 1
        last_activity = time.monotonic()

    memory.register_write(COMM_HOLE, callback)

    def shutdown(_signum=None, _frame=None):
        try:
            close_writer()
        finally:
            emu.destroy()
        raise SystemExit(1)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    emu.open("test.nds")
    emu.backup.import_file("test.sav")

    # Match hg-engine's own runner boot warm-up.
    for _ in range(120):
        emu.cycle(False)

    emu_memory.write_long(COMM_HOLE, 0 + (total << 16))

    while current < total:
        if time.monotonic() - last_activity > args.idle_timeout:
            raise RuntimeError(
                f"Preview capture timed out on {preview_ids[current]} after {args.idle_timeout}s"
            )

        if writer is None:
            writer = FfmpegWriter(out_dir / f"{preview_ids[current]}.mp4", args.fps)

        emu.cycle(False)
        cycle_count += 1

        if cycle_count % max(1, args.sample_every) == 0 and current < total and writer is not None:
            writer.write(emu.screenshot())
            if writer.frames >= args.max_frames_per_test:
                raise RuntimeError(
                    f"Preview {preview_ids[current]} exceeded {args.max_frames_per_test} captured frames"
                )

    close_writer()
    emu.destroy()

    result = {
        "captured": preview_ids,
        "failures": failures,
        "count": len(preview_ids),
    }
    (out_dir / "capture_result.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )

    # A failed mechanics expectation does not necessarily invalidate the visual,
    # but surface it in the workflow so it can be inspected.
    if failures:
        print("Preview mechanics failures: " + ", ".join(failures), file=sys.stderr)


if __name__ == "__main__":
    main()
