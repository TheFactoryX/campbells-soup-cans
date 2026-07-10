"""
Campbell's Soup Can #4144
Produced: 2026-07-10 11:19:16
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

# ANSI color palette
COLS = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[94m",  # blue
    "\033[95m",  # magenta
    "\033[96m",  # cyan
]
RESET = "\033[0m"

# Woody Allen‑style philosophical quip
QUOTE = (
    "I am not afraid of death; I just hate "
    "being there when it happens."
)

# Print the quote one character at a time, cycling colors
for i, ch in enumerate(QUOTE):
    sys.stdout.write(COLS[i % len(COLS)] + ch)
    sys.stdout.flush()
    time.sleep(0.03)          # tiny pause for a type‑writer effect
sys.stdout.write(RESET + "\n")