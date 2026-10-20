"""
Campbell's Soup Can #5139
Produced: 2026-10-20 17:07:50
Worker: MiniMax: MiniMax M3.1 Flash (free) (minimax/minimax-m3.1-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import os
import shutil
import sys
import textwrap
import time

QUOTE = (
    "“I’m not afraid of the universe; I’m just afraid it has my address "
    "and knows I’m home.”"
)

PALETTE = ("213", "221", "222", "159", "153")
RESET = "\033[0m"


def use_ansi_colors():
    if "NO_COLOR" in os.environ:
        return False
    if "FORCE_COLOR" in os.environ:
        return True
    return sys.stdout.isatty() and os.environ.get("TERM") != "dumb"


COLOR = use_ansi_colors()


def paint(text, color):
    return f"\033[1;38;5;{color}m{text}{RESET}" if COLOR else text


def center(text, width):
    padding = max(0, (width - len(text)) // 2)
    return " " * padding + text


def main():
    columns = shutil.get_terminal_size((80, 24)).columns
    quote_width = max(12, min(68, columns - 6))

    lines = textwrap.wrap(
        QUOTE,
        width=quote_width,
        break_long_words=False,
        break_on_hyphens=False,
    )

    content_width = max(len(line) for line in lines)
    box_width = content_width + 4

    anxious_face = (
        "      .-------.",
        "     (  o   o  )",
        "      \\   ^   /",
        "       '-----'",
    )

    for line in anxious_face:
        print(center(paint(line, "223"), box_width))

    top = "╭" + "─" * (content_width + 2) + "╮"
    bottom = "╰" + "─" * (content_width + 2) + "╯"

    print(paint(top, "153"))
    print(paint("│", "153"), end=" ")

    animate = COLOR and sys.stdout.isatty()
    character_index = 0

    for line_number, line in enumerate(lines):
        for character in line:
            color = PALETTE[(character_index // 4) % len(PALETTE)]
            sys.stdout.write(paint(character, color))
            sys.stdout.flush()

            if animate:
                time.sleep(0.012)

            character_index += 1

        if line_number < len(lines) - 1:
            print()
            print(paint("│", "153"), end=" ")

    print(" " * (content_width - len(lines[-1])) + paint("│", "153"))
    print(paint(bottom, "213"))


if __name__ == "__main__":
    main()