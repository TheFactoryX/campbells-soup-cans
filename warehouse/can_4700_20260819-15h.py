"""
Campbell's Soup Can #4700
Produced: 2026-08-19 15:46:15
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

# ANSI color codes
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
CYAN  = "\033[36m"
MAGENTA= "\033[35m"
RESET = "\033[0m"

def typewriter(text, delay=0.03, color_code=RESET):
    """Print text character by character with optional color."""
    for ch in text:
        sys.stdout.write(color_code + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the string

def print_boxed_quote():
    quote = "I keep wondering if the universe is just a bad stand‑up routine and I forgot my punchline."
    # Prepare lines with padding
    width = len(quote) + 4
    top_border    = "┌" + "─" * (width - 2) + "┐"
    bottom_border = "└" + "─" * (width - 2) + "┘"
    empty_line    = "│" + " " * (width - 2) + "│"
    quote_line    = "│  " + quote + "  │"

    # Animate the box drawing
    for line in (top_border, empty_line, quote_line, empty_line, bottom_border):
        if line == quote_line:
            typewriter(line, delay=0.04, color_code=CYAN)
        elif line in (top_border, bottom_border):
            typewriter(line, delay=0.02, color_code=YELLOW)
        else:
            typewriter(line, delay=0.02, color_code=GREEN)
        time.sleep(0.1)

if __name__ == "__main__":
    print_boxed_quote()