"""
Campbell's Soup Can #4290
Produced: 2026-07-22 14:21:57
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen‑style philosophical quote with a splash of color and frame

import sys, time

# The quote
quote = "I’m not afraid of death; I just don’t want to miss the party when it happens."

# ANSI rainbow palette (91‑96 are bright foreground colors)
COLORS = ['\033[91m', '\033[93m', '\033[92m', '\033[94m', '\033[95m', '\033[96m']
RESET  = '\033[0m'

def rainbow_print(s: str) -> None:
    """Prints `s` character‑by‑character in cycling rainbow colors."""
    for i, ch in enumerate(s):
        sys.stdout.write(COLORS[i % len(COLORS)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.02)          # tiny pause for a rhythmic effect
    print()                         # newline after the full string

# Decorative frame
frame   = "════════════════════════════════════════════════════════════════"
top     = "┌" + frame + "┐"
bottom  = "└" + frame + "┘"
middle  = "│ " + quote.center(len(frame) - 2) + " │"

# Print the top border in cyan
sys.stdout.write('\033[96m' + top + '\033[0m')
sys.stdout.write('\n')

# Print the quote line with rainbow colors
rainbow_print(middle)

# Print the bottom border in cyan
sys.stdout.write('\033[96m' + bottom + '\033[0m')
sys.stdout.write('\n')