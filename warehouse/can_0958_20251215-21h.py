"""
Campbell's Soup Can #958
Produced: 2025-12-15 21:32:55
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys
from itertools import cycle

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m",  # Bright Cyan
    "\033[0m"    # Reset
]

# Woody Allen style quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

def spinning_cursor():
    """Generate a spinning cursor animation."""
    while True:
        for cursor in '|/-\\':
            yield cursor

def print_quote_with_animation():
    """Print the quote with a spinning cursor and color animation."""
    spinner = spinning_cursor()
    color_cycle = cycle(COLORS)

    print("\n" + " " * 20 + "Woody Allen's Wisdom" + "\n" + "=" * 40)
    print("\n" + " " * 10 + "Loading existential dread..." + "\n")

    for char in QUOTE:
        color = next(color_cycle)
        sys.stdout.write(color + next(spinner) + " " + char + " " + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b\b\b" + "   \b\b\b")
        sys.stdout.flush()

    print("\n\n" + " " * 10 + "Enjoy your existential crisis!" + "\n")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    print_quote_with_animation()