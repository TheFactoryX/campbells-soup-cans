"""
Campbell's Soup Can #1507
Produced: 2026-01-10 02:24:01
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

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='')

def print_woody_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "Woody Allen"

    # ASCII art of Woody Allen's glasses
    glasses = r"""
        ______
       /      \
      |  O  O  |
      |   △   |
       \_____/
    """

    # Print glasses with color
    print_color(glasses, "33")  # Yellow

    # Print quote with animation
    for char in quote:
        print_color(char, "36")  # Cyan
        sys.stdout.flush()
        time.sleep(0.05)

    print("\n")

    # Print author with color
    print_color(author, "35")  # Magenta

    # Print a funny footer
    footer = "Remember: The universe is expanding, but your problems are not!"
    print("\n")
    for char in footer:
        print_color(char, "31")  # Red
        sys.stdout.flush()
        time.sleep(0.03)

if __name__ == "__main__":
    print_woody_quote()