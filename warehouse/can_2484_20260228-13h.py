"""
Campbell's Soup Can #2484
Produced: 2026-02-28 13:47:58
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
C_Y = '\033[33m'  # yellow
C_G = '\033[32m'  # green
C_C = '\033[36m'  # cyan
C_Reset = '\033[0m'

def slow_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Woody Allen‑style philosophical quote
quote = "I don't want immortality through my code—I just want to avoid an infinite recursion in my life."

# Build a simple colored box
pad = 2
width = len(quote) + pad * 2
border = C_Y + '+' + '-' * width + '+' + C_Reset
inside = '|' + ' ' + quote + ' ' + '|'

# Print the box with a typewriter effect
slow_print(border, 0)
slow_print(C_G + inside + C_Reset, 0)
slow_print(border, 0)

# Add a quick flash of cyan stars for extra flair
stars = C_C + '*' * width + C_Reset
for _ in range(2):
    slow_print(stars, 0.01)