"""
Campbell's Soup Can #5142
Produced: 2026-10-21 04:49:30
Worker: Nex AGI: Nex-N2.5-Pro (nex-agi/nex-n2.5-pro)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

... Wait final answer must code. Let's ensure no markdown.
#!/usr/bin/env python3
import shutil
import sys
import time
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
BLUE = "\033[36m"
PURPLE = "\033[35m"
AMBER = "\033[33m"
GREEN = "\033[32m"

QUOTE = (
    "Death doesn't frighten me; eternity does—mostly because I have no idea "
    "what one wears to it, and I suspect the seating will be awful."
)


def paint(text, color):
    return f"{color}{text}{RESET}"


def centered(text, color, width):
    padding = max(0, (width - len(text)) // 2)
    return " " * padding + paint(text, color)


def typewrite(text, color, delay=0.025):
    for char in text:
        sys.stdout.write(paint(char, color))
        sys.stdout.flush()
        if char != " ":
            time.sleep(delay)


def main():
    width = max(52, min(shutil.get_terminal_size((80, 20)).columns, 110))
    inner = width - 4
    border = "+" + "-" * (inner + 2) + "+"

    print()
    print(centered(".      *        .        *      .", BLUE, width))
    time.sleep(0.12)
    print(centered("*    a tiny existential inconvenience    *", BOLD + PURPLE, width))
    time.sleep(0.12)
    print(centered(".      .        *        .       .", DIM + BLUE, width))
    print()

    print(paint("  " + border, BLUE))
    print(paint("  |" + " " * (inner + 2) + "|", BLUE))

    for line in textwrap.fill(
        QUOTE,
        width=inner,
        break_long_words=False,
        break_on_hyphens=False,
    ).splitlines():
        sys.stdout.write(paint("  | ", BLUE))
        typewrite(line.ljust(inner), AMBER)
        sys.stdout.write(paint(" |", BLUE))
        sys.stdout.write("\n")

    print(paint("  |" + " " * (inner + 2) + "|", BLUE))
    print(paint("  " + border, BLUE))
    print()
    print(centered(paint("✦", GREEN), GREEN, width))
    print()


if __name__ == "__main__":
    main()