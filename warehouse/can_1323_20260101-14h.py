"""
Campbell's Soup Can #1323
Produced: 2026-01-01 14:35:16
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

# ANSI color codes
RED    = '\033[31m'
YELLOW = '\033[33m'
CYAN   = '\033[36m'
GREEN  = '\033[32m'
RESET  = '\033[0m'

# Woody Allen‑style existential joke
QUOTE = (
    "I’m not afraid of death; I just keep forgetting to bring my existential "
    "crisis to the party."
)

def color_wrap(text, color):
    """Wrap text in the given ANSI color."""
    return f"{color}{text}{RESET}"

def print_centered(text, width=60, fill='='):
    """Print `text` centered inside a decorative line of `fill`."""
    line_len = width - len(text)
    left = line_len // 2
    right = line_len - left
    print(color_wrap(f"{fill*left}{text}{fill*right}", YELLOW))

def animate(text, delay=0.02, color=CYAN):
    """Print text character‑by‑character for a typewriter effect."""
    for ch in text:
        sys.stdout.write(color_wrap(ch, color))
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after animation

def main():
    # A playful header
    animate("☣ A Moment of Existential Humor ☣", delay=0.02, color=CYAN)
    print()
    time.sleep(0.5)

    # Decorative border
    border = color_wrap("╔" + "═"*40 + "╗", YELLOW)
    top    = color_wrap("║" + " "*38 + "║", YELLOW)
    bottom = color_wrap("╚" + "═"*40 + "╝", YELLOW)

    # Center the quote inside the box
    padded = f" {QUOTE} "
    middle = color_wrap(f"║ {padded.center(38)} ║", YELLOW)

    # Print the box
    print(border)
    print(top)
    print(middle)
    print(bottom)
    print()

    # A concluding line
    print_centered("May it make you ponder the absurdity of being... and also laugh.", width=70)

if __name__ == '__main__':
    main()