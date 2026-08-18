"""
Campbell's Soup Can #4684
Produced: 2026-08-18 22:41:36
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED   = "\033[91m"
GREEN = "\033[92m"
YELLOW= "\033[93m"
RESET = "\033[0m"

# Our Woody Allen‑style philosophical gem
quote = [
    "I’m not afraid of death; I just don’t want to be there when it happens.",
    "Life is like an egg‑roll: it rolls away before you can catch it.",
    "I want immortality the old‑fashioned way: by not dying."
]

# Build a colorful ASCII‑art box around the quote
WIDTH   = 78
TOP     = "┌" + "─" * (WIDTH - 2) + "┐"
BOTTOM  = "└" + "─" * (WIDTH - 2) + "┘"
BORDER  = "│"

def print_box(lines, color):
    """Print each line centered inside a box using the given color."""
    for line in lines:
        padded = line.center(WIDTH - 4)               # leave space for "│ "
        sys.stdout.write(color + BORDER + " " + padded + " " + RESET + BORDER)
        sys.stdout.write("\n")
    # top and bottom borders
    sys.stdout.write(color + TOP + RESET + "\n")
    sys.stdout.write(color + BOTTOM + RESET + "\n")

# Animate the box line‑by‑line (just a tiny pause for fun)
for line in quote:
    print_box([line], GREEN)
    time.sleep(0.4)

# Final splash of color
sys.stdout.write(YELLOW + "\nEnjoy the existential punchline!\n" + RESET)