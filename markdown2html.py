#!/usr/bin/python3
"""Converts a Markdown file to HTML.

Expects two arguments:
    1. Input Markdown file name
    2. Output HTML file name"""


import sys
import os


if __name__ == "__main__":

    # Check for correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    # Check if files exist
    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)

    exit(0)
