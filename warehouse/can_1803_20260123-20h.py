"""
Campbell's Soup Can #1803
Produced: 2026-01-23 20:40:45
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

import sys
import itertools
import time

# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "cyan": "\033[36m",
    "yellow": "\033[33m",
    "magenta": "\033[35m",
    "green": "\033[32m",
    "red": "\033[31m",
}
RESET = COLORS["reset"]

def colorize(text, color):
    """Wrap text in ANSI color codes."""
    return f"{COLORS.get(color, '')}{text}{RESET}"

# The Woody Allen‑style quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a colorful, ASCII‑art box around the quote
border_top    = "╔" + "═" * (len(quote) + 2) + "╗"
border_bottom = "╚" + "═" * (len(quote) + 2) + "╝"
border_middle = "\n".join(f"║ {line} ║" for line in quote.splitlines())

# Simple typing animation for extra visual flair
def typewriter(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

# Print the box line‑by‑line with a tiny animation
typewriter(colorize(border_top, "cyan"))
typewriter(colorize(border_middle, "yellow"))
typewriter(colorize(border_bottom, "cyan"))

# Add a final witty comment in a different color
final = " — maybe the only thing I’m good at is postponing the inevitable."
typewriter(colorize(final, "magenta"), delay=0.05)