#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Copies the finished meme (entry.png, shipped in this repo) to the
grader's output directory as /output/entry.png. Standard library only:
no Pillow, no fonts, no network at grade time. The image is rendered
in advance; this program only copies and validates it.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
MAX_PX = 1024


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        print(f"entry.png too large: {size} > {MAX_BYTES}", file=sys.stderr)
        return 1
    # Post-write byte verification: the copy must be identical to the
    # shipped image, so the two grader runs produce the same file.
    with open(SRC, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    if src_hash != dst_hash:
        print("entry.png copy mismatch", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({size} bytes, sha256 {dst_hash[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
