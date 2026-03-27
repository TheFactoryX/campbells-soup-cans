"""
Campbell's Soup Can #2997
Produced: 2026-03-27 19:51:51
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import itertools

# ANSI color codes
RED    = '\033[31m'
YELLOW = '\033[33m'
GREEN  = '\033[32m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

COLORS = [RED, YELLOW, GREEN, BLUE, MAGENTA, CYAN]

# Woody Allen‑style philosophical quote
quote = "I am not afraid of death; I just don\u2019t want to be there when it happens."

def colored(s, color):
    """Wrap string s in the given ANSI color."""
    return f"{color}{s}{RESET}"

# Build a simple colored box
border = "+" + "-" * (len(quote) + 6) + "+"
top    = colored(border,    COLORS[0])
middle = colored(f"|  {quote}  |", COLORS[1])
bottom = colored(border,    COLORS[2])

# Print the colorful box
print(top)
print(middle)
print(bottom)