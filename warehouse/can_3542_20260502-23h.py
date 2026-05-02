"""
Campbell's Soup Can #3542
Produced: 2026-05-02 23:03:07
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
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

# Woody Allen‑style quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

# ANSI color codes
COLORS = {
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}
RESET = "\033[0m"


def color_text(text, code):
    return f"\033[{code}m{text}{RESET}"


def typewriter(text, code, delay=0.05):
    for ch in text:
        sys.stdout.write(color_text(ch, code))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def thinking_animation(duration=1.0):
    frames = ["|", "/", "-", "\\"]
    end = time.time() + duration
    idx = 0
    while time.time() < end:
        sys.stdout.write("\r" + color_text(frames[idx], COLORS["cyan"]) + " thinking...")
        sys.stdout.flush()
        time.sleep(0.1)
        idx = (idx + 1) % len(frames)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()


def draw_box():
    padding = 2
    width = len(QUOTE) + 2 * padding
    horiz = "+" + "-" * width + "+"
    empty = "|" + " " * width + "|"
    quote_line = "|" + " " * padding + QUOTE + " " * padding + "|"

    # top border
    print(color_text(horiz, COLORS["yellow"]))
    time.sleep(0.2)
    # empty line
    print(color_text(empty, COLORS["yellow"]))
    time.sleep(0.1)
    # quote line with typewriter effect
    typewriter(quote_line, COLORS["green"], delay=0.04)
    time.sleep(0.1)
    # bottom border
    print(color_text(horiz, COLORS["yellow"]))


def main():
    # Optional tiny neurotic face
    face = color_text("  ( ಠ_ಠ)  ", COLORS["magenta"])
    print(face)
    thinking_animation(1.2)
    draw_box()


if __name__ == "__main__":
    main()