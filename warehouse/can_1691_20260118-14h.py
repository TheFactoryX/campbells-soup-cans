"""
Campbell's Soup Can #1691
Produced: 2026-01-18 14:33:14
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

# ---------- Helper functions ----------
def colour(text, code):
    """Wrap text in an ANSI colour code."""
    return f"\033[{code}m{text}\033[0m"

def typewriter(s, delay=0.03):
    """Print string character‑by‑character (typewriter effect)."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# ---------- The Woody Allen quote ----------
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Simple box drawing (Unicode box‑drawing characters)
box_top    = "┌───────────────────────────────────────────────┐"
box_middle = "│                                            │"
box_bottom = "└───────────────────────────────────────────────┘"

# Determine inner width (the space between the side bars)
inner_w = len(box_top) - 4   # 4 characters are the corners + sides

# Center the quote inside the box
centered = quote.center(inner_w)

# Build the lines that go inside the box
lines = [
    box_top,
    f"│{centered}│",
    box_bottom,
]

# ------- Fun visual treatment -------
# Colour cycling for each line (ANSI colour codes)
colours = [31, 33, 32, 36, 35]  # red, yellow, green, cyan, magenta
for idx, line in enumerate(lines):
    coloured_line = colour(line, colours[idx % len(colours)])
    typewriter(coloured_line, delay=0.025)

# Short pause before a tiny “author credit” (still part of the same output)
time.sleep(0.4)
credit = colour(" — Woody Allen (in spirit)", 35)
typewriter(credit, delay=0.04)