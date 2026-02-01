"""
Campbell's Soup Can #1981
Produced: 2026-02-01 09:45:16
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
CYAN   = '\033[36m'
YELLOW = '\033[33m'
MAGENTA= '\033[35m'
RESET  = '\033[0m'

# The Woody Allen‑style philosophical gem
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Assemble a colorful ASCII box around the quote
interior = f'| {quote} |'
width    = len(interior)

top    = '+' + '-' * width + '+'
bottom = top

# Simple type‑writer effect for extra fun
def typewriter(s, speed=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write('\n')
    sys.stdout.flush()

# Print the box with alternating colors
typewriter(MAGENTA + top + RESET)
typewriter(YELLOW + interior + RESET)
typewriter(MAGENTA + bottom + RESET)