"""
Campbell's Soup Can #1929
Produced: 2026-01-29 19:04:17
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen‑style philosophical quote with a splash of color

# ANSI color codes (no external libraries needed)
CYAN  = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# The neurotic, self‑deprecating wisdom
quote = "I believe in love at first sight—it spares me the agony of prolonged small talk."

# Box dimensions
INNER_WIDTH = 58

# Build the decorative frame
top    = CYAN + "╔" + "═" * INNER_WIDTH + "╗" + RESET
bottom = CYAN + "╚" + "═" * INNER_WIDTH + "╝" + RESET
padded = quote.center(INNER_WIDTH)

# Print the colorful box
print(top)
print(CYAN + "║" + padded + "║" + RESET)
print(bottom)