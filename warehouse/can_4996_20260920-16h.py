"""
Campbell's Soup Can #4996
Produced: 2026-09-20 16:47:59
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
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def type_print(text, delay=0.04):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the whole line

def main():
    quote = "I’m not afraid of death; I just don’t want to be there when it happens."
    # Build a simple box
    width = len(quote) + 4  # padding inside the box
    top_bottom = "╔" + "═" * width + "╗"
    sides = lambda: "║" + " " * width + "║"
    empty_line = "║" + " " * ((width - len(quote)) // 2) + quote + " " * (width - len(quote) - ((width - len(quote)) // 2)) + "║"

    # Print with color and typewriter effect
    type_print(YELLOW + top_bottom + RESET, delay=0.001)
    type_print(YELLOW + sides() + RESET, delay=0.001)
    type_print(CYAN + empty_line + RESET, delay=0.03)
    type_print(YELLOW + sides() + RESET, delay=0.001)
    type_print(YELLOW + top_bottom + RESET, delay=0.001)

if __name__ == "__main__":
    main()