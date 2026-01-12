"""
Campbell's Soup Can #1551
Produced: 2026-01-12 04:19:11
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
CYAN = '\033[36m'
MAGENTA = '\033[35m'
RESET = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "I’m not scared of death; I just don’t want to be there when it happens."

# Build a decorative, colored box around the quote
border = '*' * (len(quote) + 4)                # top/bottom border
top_line = '*' + ' ' + quote + ' ' + '*'      # middle line with quote

# Print the box (colors are applied only to the border and text)
print(CYAN + border + RESET)
print(MAGENTA + top_line + RESET)
print(CYAN + border + RESET)

# Slight pause to let the visual settle (purely aesthetic)
time.sleep(0.4)