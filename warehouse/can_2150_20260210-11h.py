"""
Campbell's Soup Can #2150
Produced: 2026-02-10 11:13:10
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A Woody Allen‑style philosophical joke, served with ANSI colors and a tiny ASCII box

# ANSI color codes
RED   = '\033[31m'
CYAN  = '\033[36m'
YELLOW= '\033[33m'
RESET = '\033[0m'

# The quote (two short lines for maximum neurotic impact)
_lines = [
    "I’m not afraid of death; I just don’t want to be there when it happens,",
    "especially if there’s a worse alternative waiting at the door."
]

# Build a fixed‑width box (68 dashes wide)
WIDTH = 68
border_top    = "┌" + "─" * WIDTH + "┐"
border_bottom = "└" + "─" * WIDTH + "┘"

def colored(line, color):
    return f"{color}{line}{RESET}"

print(colored(border_top, RED))
for i, txt in enumerate(_lines):
    interior = txt.center(WIDTH)                # Pad to exactly WIDTH characters
    line     = f"│{interior}│"                    # Add the side borders
    # Cycle colors for visual fun
    palette = [CYAN, YELLOW]
    color   = palette[i % len(palette)]
    print(colored(line, color))
print(colored(border_bottom, RED))
print(RESET, end="")  # Ensure terminal is left clean