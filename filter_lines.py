"""Utilities for filtering lines in text content."""

import argparse
from typing import Iterable, List


def filter_lines_from_lines(lines: Iterable[str], keywords: List[str]) -> List[str]:
    """Return lines containing all keywords prefixed with their line numbers."""
    return [
        f"{i}: {line}"
        for i, line in enumerate(lines, start=1)
        if all(keyword in line for keyword in keywords)
    ]


def filter_lines(input_file: str, keywords: List[str], output_file: str) -> None:
    """Filter lines in a file and write matching ones to output with line numbers."""
    with open(input_file, "r", encoding="utf-8") as f_in, open(
        output_file, "w", encoding="utf-8"
    ) as f_out:
        for result in filter_lines_from_lines(f_in, keywords):
            f_out.write(result)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Filter lines containing keywords and output line numbers")
    parser.add_argument('input_file', help='Path to the input text file')
    parser.add_argument('output_file', help='Path to the output text file')
    parser.add_argument('keywords', nargs='+', help='Keywords that must appear in each line')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filter_lines(args.input_file, args.keywords, args.output_file)
