"""
Campbell's Soup Can #3941
Produced: 2026-06-15 18:01:38
Worker: Nex AGI: Nex-N2-Pro (free) (nex-agi/nex-n2-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import shutil
import sys
import textwrap
import time

RESET = "\033[0m"
CYAN = "\033[96m"
PINK = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
PALETTE = [CYAN, PINK, YELLOW, GREEN, BLUE]


def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def typewriter(text, delay=0.018):
    for i, char in enumerate(text):
        sys.stdout.write(f"{PALETTE[i % len(PALETTE)]}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay * (2.3 if char in ".,;:?" else 1.0))
    sys.stdout.write(RESET)


def draw_cloud(width):
    cloud = [
        "        .-''''-.        ",
        "     .'  .--.  '.     ",
        "    /   (    )   \\    ",
        "   |   .-'  '-.   |   ",
        "    \\  '-.  .-'  /    ",
        "     '.  '--'  .'     ",
        "        '-....-'        ",
    ]
    for line in cloud:
        sys.stdout.write(" " * max(0, (width - len(line)) // 2))
        sys.stdout.write(f"{CYAN}{line}{RESET}\n")
        time.sleep(0.08)


def main():
    width = shutil.get_terminal_size((80, 24)).columns
    clear()
    draw_cloud(width)

    quote = (
        "I don't fear the void; I just don't want the void to see me before "
        "I've flossed, apologized to my mother, and figured out what I'm doing here."
    )

    inner_width = min(max(24, width - 8), 92)
    lines = textwrap.wrap(quote, width=inner_width)
    max_len = max(len(line) for line in lines)
    box_width = max_len + 4
    left_padding = max(0, (width - box_width) // 2)
    spaces = " " * left_padding

    top = "╔" + "═" * (box_width - 2) + "╗"
    bottom = "╚" + "═" * (box_width - 2) + "╝"

    sys.stdout.write(spaces + CYAN + top + RESET + "\n")
    for line in lines:
        sys.stdout.write(spaces + CYAN + "║" + RESET + " ")
        typewriter(line)
        sys.stdout.write(" " * (max_len - len(line)) + " " + CYAN + "║" + RESET + "\n")
    sys.stdout.write(spaces + CYAN + bottom + RESET + "\n\n")


if __name__ == "__main__":
    main()