#!/usr/bin/env python3
"""Fail when numbered display equations drift from a shared PDF layout."""

import argparse
import re
import statistics
import sys
from pathlib import Path

import fitz


LABEL = re.compile(r"\((\d+)\)")
MATH_MARKERS = ("=", "∑", "√", "κ", "τ", "∙", "·", "−")


def numbered_equations(pdf_path):
    document = fitz.open(pdf_path)
    equations = []
    for page_number, page in enumerate(document, start=1):
        words = page.get_text("words")
        for label in words:
            if label[0] < page.rect.width * 0.75 or not LABEL.fullmatch(label[4]):
                continue
            y0, y1 = label[1], label[3]
            line = [
                word
                for word in words
                if word[0] < label[0] - 8
                and word[0] > page.rect.width * 0.2
                and not (word[3] < y0 - 7 or word[1] > y1 + 7)
            ]
            text = " ".join(word[4] for word in sorted(line, key=lambda item: item[0]))
            if not line or not any(marker in text for marker in MATH_MARKERS):
                continue
            x0 = min(word[0] for word in line)
            x1 = max(word[2] for word in line)
            equations.append(
                {
                    "page": page_number,
                    "label": label[4],
                    "number_x": label[0],
                    "formula_center": (x0 + x1) / 2,
                    "page_center": page.rect.width / 2,
                }
            )
    return equations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--number-tolerance", type=float, default=1.5)
    parser.add_argument("--center-tolerance", type=float, default=2.0)
    args = parser.parse_args()

    equations = numbered_equations(args.pdf)
    if not equations:
        print("ERROR: no numbered display equations detected", file=sys.stderr)
        return 2

    expected_number_x = statistics.median(item["number_x"] for item in equations)
    errors = []
    for item in equations:
        number_delta = abs(item["number_x"] - expected_number_x)
        center_delta = abs(item["formula_center"] - item["page_center"])
        print(
            f'p.{item["page"]} {item["label"]}: '
            f'number Δ={number_delta:.2f} pt, formula-center Δ={center_delta:.2f} pt'
        )
        if number_delta > args.number_tolerance:
            errors.append(f'{item["label"]} number shifted by {number_delta:.2f} pt')
        if center_delta > args.center_tolerance:
            errors.append(f'{item["label"]} formula shifted by {center_delta:.2f} pt')

    if errors:
        print("FAILED:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(equations)} numbered equations share one center and number column")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
