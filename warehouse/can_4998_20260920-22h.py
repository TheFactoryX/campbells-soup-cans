"""
Campbell's Soup Can #4998
Produced: 2026-09-20 22:26:48
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=""):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def main():
    clear_screen()
    quote = "I'm not afraid of dying; I'm just afraid of being late to my own funeral."
    # Prepare lines with padding
    width = len(quote) + 4
    top_border = "╔" + "═" * width + "╗"
    bottom_border = "╚" + "═" * width + "╝"
    padded_quote = "║  " + quote + "  ║"

    # Choose a rotating color scheme for the box
    for i, line in enumerate([top_border, padded_quote, bottom_border]):
        color = COLORS[i % len(COLORS)] + BOLD
        typewriter(line, delay=0.005, color=color)
        time.sleep(0.2)  # pause between lines for effect

    # Final pause so the user can read it
    time.sleep(2)

if __name__ == "__main__":
    main()