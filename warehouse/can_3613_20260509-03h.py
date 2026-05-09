"""
Campbell's Soup Can #3613
Produced: 2026-05-09 03:56:17
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

python#!/usr/bin/env python3
import sys, time

# ANSI colour codes
RESET        = '\033[0m'
CYAN         = '\033[36m'
BRIGHT_YELLOW = '\033[93m'  # for the box border

def animate_print(lines, delay=0.02):
    """Print each line with a tiny pause for a typing‑like effect."""
    for line in lines:
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(delay)

# The Woody Allen‑style philosophical quote (multi‑line)
quote = [
    "Life is like an onion: You peel it off, and then you start crying,",
    "but the worst part is, you still can't make it taste any better.",
    "— a neurotic philosopher who never learned to budget his existential dread."
]

# Build a simple coloured box around the quote
width = 70
border = BRIGHT_YELLOW + "+" + "-" * (width - 2) + "+" + RESET
box_lines = [border]

for line in quote:
    # Center each line inside the box (account for the surrounding "| " and " |")
    padded = line.center(width - 4)
    interior = CYAN + "| " + padded + " |" + RESET
    box_lines.append(interior)

box_lines.append(border)   # close the box

# Print the coloured box with a tiny animation delay
animate_print(box_lines)