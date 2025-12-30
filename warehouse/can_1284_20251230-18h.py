"""
Campbell's Soup Can #1284
Produced: 2025-12-30 18:47:55
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

# ANSI color codes
class C:
    RESET = "\033[0m"
    CYAN  = "\033[36m"
    YELLOW= "\033[33m"
    MAGENTA= "\033[35m"
    GREEN = "\033[32m"

# Woody Allen‑style philosophical quote
quote = "I am not afraid of death; I just don't want to miss the next funny thing that happens."

# ASCII‑art border
border_top    = "┌───────────────────────────────────────────────────────────────────────┐"
border_bottom = "└───────────────────────────────────────────────────────────────────────┘"
blank_middle  = "│  " + " " * 71 + "│"

# Assemble the three display lines
lines = [border_top, f"│  {quote:<71}│", border_bottom]

# Cycle through three bright colors for a tiny animation effect
colors = [C.CYAN, C.YELLOW, C.MAGENTA]

def colorise(text, colour):
    """Wrap text in the given ANSI colour and append a reset."""
    return colour + text + C.RESET

# Print each line with its colour and a brief pause (creates a subtle flicker)
for i, line in enumerate(lines):
    sys.stdout.write(colorise(line, colors[i % len(colors)]) + "\n")
    sys.stdout.flush()
    time.sleep(0.08)          # tiny pause for visual interest