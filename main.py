#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes the one-line joke to /output/entry.txt and prints it.

The joke: everyone agrees the meeting should have been an email, then
spends an hour drafting that email. The turn lands in the last words,
and the loop -- a meeting about the email the meeting should have been --
is the part nobody expects.
"""

import os

LINE = "We all agreed this meeting should have been an email, then spent an hour drafting the email."


def output_path() -> str:
    """Where the entry goes: /output/entry.txt, unless OUTPUT_PATH says otherwise.

    The grader runs with the default. The override exists only so a local
    check can aim at a throwaway file instead of the real output path.
    """
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate(line: str) -> str:
    """The sealed scorer gates on 1-200 UTF-8 characters, not only whitespace.

    Fail loudly here rather than shipping an entry the gate would refuse.
    """
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry line fails the 1-200 char gate")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = validate(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
