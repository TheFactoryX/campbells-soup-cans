"""
Campbell's Soup Can #4625
Produced: 2026-08-16 09:42:20
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
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

# Rainbow palette
COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]

# Woody Allen‑style philosophical quote
QUOTE = "I’m not scared of death; I just don’t want to be there when it happens."

def colorize(s):
    """Return a rainbow‑colored version of the string."""
    return ''.join(COLORS[i % len(COLORS)] + ch + RESET for i, ch in enumerate(s))

def box_border(char='*', length=70, color='\033[90m'):
    """Print a horizontal border line."""
    print(color + char * length + RESET)

def main():
    WIDTH = 70                     # total width of the ASCII box
    # Top border (dark gray)
    box_border('*', WIDTH)

    # Center the quote and fit it inside the box
    inner_width = WIDTH - 2        # space inside the '*' borders
    centered = QUOTE.center(inner_width)
    colored_centered = colorize(centered)

    # Print the centered, rainbow‑colored quote with side borders
    print('*' + colored_centered + '*')

    # Bottom border (matches the top)
    box_border('*', WIDTH)

if __name__ == '__main__':
    main()