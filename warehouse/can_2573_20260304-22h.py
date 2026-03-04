"""
Campbell's Soup Can #2573
Produced: 2026-03-04 22:50:20
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen‑style philosophical joke, wrapped in a colorful ASCII box

quote = ("I don't want to achieve immortality through my work; I want to achieve it "
         "through not dying.")

# ANSI colour codes
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

# Build a dynamic box around the quote
inner  = "  " + quote + "  "          # generous padding on both sides
width  = len(inner)
top    = "╔" + "═" * width + "╗"
bottom = "╚" + "═" * width + "╝"
middle = "║" + inner + "║"

# Print the box with lively colours
print(MAGENTA + BOLD + top + RESET)
print(CYAN      + middle + RESET)
print(MAGENTA + BOLD + bottom + RESET)