#!/usr/bin/env python3
"""Synchronize one final lab-report DOCX/PDF over older same-topic copies."""

from __future__ import annotations

import argparse
import shutil
import unicodedata
import stat
from pathlib import Path


DEFAULT_ROOTS = [
    Path("/Users/xiaocong/Desktop/Chemie/TC实验"),
    Path("/Users/xiaocong/Documents"),
    Path("/Users/xiaocong/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files"),
    Path("/Users/xiaocong/Library/Mobile Documents/iCloud~md~obsidian/Documents"),
]

INTERMEDIATE_MARKERS = (
    "backup",
    "audit",
    "render",
    "beispiel",
    "fix_current",
    "unit_fix",
    "layout_fix",
    "formula_audit",
    "missing_beispiel",
    "vorschlag",
)


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return text.lower()


def matches_topic(path: Path, topic: str) -> bool:
    haystack = norm(str(path))
    words = [w for w in norm(topic).replace("_", " ").split() if w]
    if not words:
        return False
    return all(word in haystack for word in words)


def is_intermediate(path: Path) -> bool:
    haystack = norm(str(path))
    return any(marker in haystack for marker in INTERMEDIATE_MARKERS)


def find_reports(roots: list[Path], topic: str) -> list[Path]:
    found: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".docx", ".pdf"} and matches_topic(path, topic):
                found.append(path)
    return sorted(set(found), key=lambda p: str(p))


def ensure_writable(path: Path) -> None:
    try:
        path.chmod(path.stat().st_mode | stat.S_IWUSR)
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", required=True, type=Path, help="Authoritative final DOCX")
    parser.add_argument("--pdf", required=True, type=Path, help="Authoritative final PDF")
    parser.add_argument("--topic", required=True, help="Normalized topic words, e.g. 'stoffuebergang chemischer reaktion'")
    parser.add_argument("--root", action="append", type=Path, help="Root folder to scan; repeatable")
    parser.add_argument("--commit", action="store_true", help="Apply changes; otherwise dry-run")
    args = parser.parse_args()

    source = {".docx": args.docx.resolve(), ".pdf": args.pdf.resolve()}
    for path in source.values():
        if not path.exists():
            raise FileNotFoundError(path)

    roots = args.root or DEFAULT_ROOTS
    targets = find_reports(roots, args.topic)
    actions: list[tuple[str, Path]] = []

    for target in targets:
        resolved = target.resolve()
        if resolved in set(source.values()):
            continue
        if is_intermediate(target):
            actions.append(("delete", target))
        else:
            actions.append(("overwrite", target))

    failures: list[tuple[str, Path, str]] = []

    for action, target in actions:
        print(f"{action:9s} {target}")
        if not args.commit:
            continue
        try:
            ensure_writable(target)
            if action == "delete":
                target.unlink(missing_ok=True)
            else:
                shutil.copy2(source[target.suffix.lower()], target)
        except OSError as exc:
            failures.append((action, target, str(exc)))

    print(f"\n{len(actions)} action(s) {'applied' if args.commit else 'planned'}")
    if failures:
        print("\nFailed actions:")
        for action, target, error in failures:
            print(f"{action:9s} {target}\n          {error}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
