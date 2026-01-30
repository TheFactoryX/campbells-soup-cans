"""
Campbell's Soup Can #1944
Produced: 2026-01-30 13:30:01
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import itertools, sys

# ANSI color codes
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

# Palette for a playful, rainbow effect
PALETTE = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

# Woody Allen‑style philosophical quip
QUOTE = "I’m not afraid of death; I just don’t want to be there when it happens."
AUTHOR = "– Woody Allen (as imagined by Python)"

# Create a tidy ASCII‑art box
WIDTH = 60
top    = "┌" + "─" * (WIDTH - 2) + "┐"
quote_line   = f"│ {QUOTE} │"
author_line  = f"│ {AUTHOR} │"
bottom = "└" + "─" * (WIDTH - 2) + "┘"

# Print each line of the box with a different color (cycle through the palette)
for i, line in enumerate([top, quote_line, author_line, bottom]):
    sys.stdout.write(PALETTE[i % len(PALETTE)] + line + RESET + "\n")