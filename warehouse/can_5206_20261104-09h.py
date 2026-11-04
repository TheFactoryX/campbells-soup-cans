"""
Campbell's Soup Can #5206
Produced: 2026-11-04 09:13:51
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes
BOLD = "\033[1m"
RESET = "\033[0m"
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def type_write(text, delay=0.04, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_boxed_quote(lines, width=58):
    top = "╭" + "─" * (width - 2) + "╮"
    bottom = "╰" + "─" * (width - 2) + "╯"

    type_write(random.choice(COLORS) + top + RESET, delay=0.01)
    for line in lines:
        padded = line.ljust(width - 2)
        type_write(random.choice(COLORS) + "│ " + padded + " │" + RESET, delay=0.03)
        time.sleep(0.05)
    type_write(random.choice(COLORS) + bottom + RESET, delay=0.01)


def main():
    clear_screen()

    print(BOLD + "\033[95m" + "=" * 60 + RESET)
    type_write("  A WOODY ALLEN-STYLE PHILOSOPHICAL MUSING  ", delay=0.02, color="\033[96m")
    print(BOLD + "\033[95m" + "=" * 60 + RESET)
    print()

    time.sleep(0.3)

    neurotic_face = [
        "      ___      ",
        "     /   \\     ",
        "    | o o |    ",
        "    |  >  |    ",
        "     \\___/     ",
        "   /       \\   ",
        "  |  NEURO   | ",
    ]

    for line in neurotic_face:
        print(random.choice(COLORS) + line + RESET)
        time.sleep(0.05)

    print()

    quote_lines = [
        "I'm not afraid of death.",
        "I'm just deeply concerned about the logistics.",
        "",
        "Who will water my plants?",
        "Will the afterlife have Wi-Fi?",
        "And most importantly,",
        "will I have to make small talk?",
    ]

    print_boxed_quote(quote_lines, width=58)

    print()
    type_write("- Woody Allen (probably, mid-panic on a couch)", delay=0.03, color="\033[93m")
    print()
    print(BOLD + "\033[95m" + "=" * 60 + RESET)


if __name__ == "__main__":
    main()