"""
Campbell's Soup Can #3916
Produced: 2026-06-12 09:12:40
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/envpython3
# -*- coding: utf-8 -*-

# ANSI color codes (no external dependencies)
RED    = '\033[31m'
YELLOW = '\033[33m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

# Classic Woody Allen‑style philosophical quote
quote_lines = [
    "I'm not afraid of death;",
    "I just don't want to be there when it happens."
]

# Determine the maximum line length for a neat box
max_len = max(len(line) for line in quote_lines)
inner_width = max_len + 2          # padding: 1 space each side
border_len = inner_width           # length of the '-' line inside the box

# Build the top and bottom borders
top_border   = CYAN + '+' + '-' * border_len + '+' + RESET
bottom_border = top_border

# Build the middle lines with the quote inside the box
middle = []
for line in quote_lines:
    padded = ' ' + line.ljust(max_len) + ' '          # add side padding
    middle.append(YELLOW + '|' + padded + '|' + RESET)

# Assemble the full colorful ASCII art
output = '\n'.join([top_border, *middle, bottom_border])
print(output)