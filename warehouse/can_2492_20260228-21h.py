"""
Campbell's Soup Can #2492
Produced: 2026-02-28 21:34:09
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time

# ---------- ANSI colour helpers ----------
ANSI = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

def color(text, name):
    """Wrap *text* in the given ANSI colour."""
    return ANSI.get(name, "") + str(text) + ANSI["reset"]

# ---------- The Woody Allen quote ----------
quote = (
    "I don't want to achieve immortality through my work; "
    "I want to achieve it through simply staying alive just a little longer."
)

# ---------- Fancy bordered box ----------
WIDTH = 70
BORDER_TOP = "+" + "-" * (WIDTH - 2) + "+"
BORDER_BOTTOM = BORDER_TOP
SIDE = "|"

def build_box():
    lines = []
    lines.append(color(BORDER_TOP, "yellow"))
    lines.append(
        SIDE
        + color(" " * (WIDTH - 2), "magenta")
        + SIDE
    )
    # Center the quote and colour it cyan
    centered = quote.center(WIDTH - 2)
    lines.append(
        SIDE
        + color(centered, "cyan")
        + SIDE
    )
    lines.append(
        SIDE
        + color(" " * (WIDTH - 2), "magenta")
        + SIDE
    )
    lines.append(color(BORDER_BOTTOM, "yellow"))
    return lines

box_lines = build_box()

# ---------- Print with a little typewriter animation ----------
def typewriter(lines, delay=0.03):
    for line in lines:
        for ch in line:
            sys.stdout.write(color(ch, "white"))
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
        sys.stdout.flush()

print()  # blank line before the art
typewriter(box_lines)

# ---------- End with a playful outro ----------
time.sleep(1)
print(color("\nPress ENTER for an extra existential punchline...", "green"), end="", flush=True)
input()
print(color("Punchline: The universe is absurd, but at least the coffee is good.", "green"))