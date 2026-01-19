"""
Campbell's Soup Can #1715
Produced: 2026-01-19 17:39:03
Worker: Mistral: Devstral 2 2512 (free) (mistralai/devstral-2512:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_woody_quote():
    # Woody Allen style quote
    quote = "Eternity is a terrible thought. I mean, where would you spend it?"

    # ASCII art of Woody Allen's glasses
    glasses = r"""
        _______
      /         \
     |   O   O   |
     |     ∆     |
      \  ___  /
       \     /
        -----
    """

    # Print glasses in yellow
    print_colored(glasses, "93")

    # Print quote with animation
    print_colored("\nWoody Allen's Thought of the Day:\n", "96")
    for char in quote:
        print_colored(char, "95")
        sys.stdout.flush()
        time.sleep(0.05)

    # Print a neurotic follow-up
    follow_up = "\n\n(Though I suppose if you had a really good deli nearby...)"
    time.sleep(1)
    for char in follow_up:
        print_colored(char, "91")
        sys.stdout.flush()
        time.sleep(0.03)

    # Print a box around the whole thing
    print("\n" + "=" * 50)

if __name__ == "__main__":
    print_woody_quote()