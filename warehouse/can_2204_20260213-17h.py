"""
Campbell's Soup Can #2204
Produced: 2026-02-13 17:56:44
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
COL = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

# Woody Allen philosophical one‑liner
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Determine a box width that comfortably fits the quote
width = len(quote) + 4                     # at least 4 extra chars for margins
top    = "╔" + "═" * (width-2) + "╗"
bottom = "╚" + "═" * (width-2) + "╝"

# Center the quote inside the middle line
pad_left  = (width-2 - len(quote)) // 2
pad_right = (width-2 - len(quote)) - pad_left
inner = " " * pad_left + quote + " " * pad_right

# Assemble the three lines of the box
lines = [
    top,
    "║" + inner + "║",
    bottom
]

# Print each line with a splash of colour and a tiny pause (animation)
for i, line in enumerate(lines):
    colour_name = list(COL.keys())[i % len(COL)]   # cycle through colours
    coloured_line = f"{COL[colour_name]}{line}{COL['reset']}"
    sys.stdout.write(coloured_line + "\n")
    time.sleep(0.12)    # slight delay for a playful flicker effect