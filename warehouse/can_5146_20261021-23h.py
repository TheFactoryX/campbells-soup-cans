"""
Campbell's Soup Can #5146
Produced: 2026-10-21 23:20:27
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
import random

# ANSI escape codes
BOLD = "\033[1m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J\033[H"
CURSOR_UP = "\033[1A"
CLEAR_LINE = "\033[2K"

COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]

QUOTE = (
    "I don't believe in an afterlife, but I'm packing a sweater just in case "
    "it's cold, existential, and requires a co-pay I can't afford."
)

ASCII_FACE = [
    "      ___      ",
    "   __(   )__   ",
    "  (__  ^  __)  ",
    "    \\  -  /    ",
    "   /     \\     ",
    "  |  o   o |   ",
    "   \\  \\_/  /   ",
    "    \\_____/    "
]

SYMPTOMS = [
    "Existential dread: LOADING...",
    "Therapist appointment: 3 weeks away",
    "Fear of commitment: CHRONIC",
    "Fear of death: ACUTE",
    "Fear of commitment to a fear of death: RECURSIVE",
    "Relationship status: it's complicated (with myself)",
]


def slow_type(text, delay=0.025, color="\033[93m"):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def main():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass

    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.flush()

    width = 58

    # Title box
    print(BOLD + "\033[95m" + "╔" + "═" * width + "╗" + RESET)
    title = " WOODY ALLEN'S NEUROTIC PHILOSOPHY GENERATOR "
    pad = max(0, (width - len(title)) // 2)
    print(
        BOLD
        + "\033[95m"
        + "║"
        + " " * pad
        + title
        + " " * (width - len(title) - pad)
        + "║"
        + RESET
    )
    print(BOLD + "\033[95m" + "╚" + "═" * width + "╝" + RESET)
    print()

    # Neurotic ASCII face
    for line in ASCII_FACE:
        print("\033[96m" + line + RESET)
    print()

    # Quote box top
    print("\033[94m" + "┌" + "─" * width + "┐" + RESET)

    # Typewriter quote
    slow_type(QUOTE, delay=0.03, color="\033[93m")

    # Quote box bottom
    print("\033[94m" + "└" + "─" * width + "┘" + RESET)
    print()

    # Flickering neurotic footer
    for _ in range(12):
        symptom = random.choice(SYMPTOMS)
        sys.stdout.write("\033[91m" + BOLD + "⚡ " + symptom + " ⚡" + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write(CURSOR_UP + CLEAR_LINE)
        sys.stdout.flush()

    final = random.choice(SYMPTOMS)
    print("\033[91m" + BOLD + "⚡ " + final + " ⚡" + RESET)
    print()
    print("\033[92m" + BOLD + "(Please direct all complaints to your analyst.)" + RESET)


if __name__ == "__main__":
    main()