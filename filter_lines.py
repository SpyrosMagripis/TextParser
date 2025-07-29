import argparse


def filter_lines(input_file: str, keywords: list[str], output_file: str) -> None:
    """Filter lines containing all keywords and write them to output with line numbers."""
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for i, line in enumerate(f_in, start=1):
            if all(keyword in line for keyword in keywords):
                f_out.write(f"{i}: {line}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Filter lines containing keywords and output line numbers")
    parser.add_argument('input_file', help='Path to the input text file')
    parser.add_argument('output_file', help='Path to the output text file')
    parser.add_argument('keywords', nargs='+', help='Keywords that must appear in each line')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filter_lines(args.input_file, args.keywords, args.output_file)
