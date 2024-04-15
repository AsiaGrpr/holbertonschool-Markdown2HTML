#!/usr/bin/python3

import sys
import os


def main(markdown_file, output_file):
    """Converts a Markdown file to HTML.

    Expects two arguments:
      1. Input Markdown file name
      2. Output HTML file name
    """

    # Check if markdown file exists
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    # Check for correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Extract name file
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    main(markdown_file, output_file)

    # Successful execution, no output message needed
    sys.exit(0)


if __name__ == "__main__":
    main()
