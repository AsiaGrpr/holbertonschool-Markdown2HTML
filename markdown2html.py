#!/usr/bin/python3

import sys
import os


def main():
    """Converts a Markdown file to HTML.

    Expects two arguments:
      1. Input Markdown file name
      2. Output HTML file name
    """

    # Check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Check if markdown file exists
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)
    # Successful execution, no output message needed
    sys.exit(0)


if __name__ == "__main__":
    main()
