"""
Campbell's Soup Can #1597
Produced: 2026-01-14 07:38:07
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
    print(f"\033[{color_code}m{text}\033[0m")

def print_woody_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "Woody Allen"

    # ASCII art of Woody Allen's glasses
    glasses = r"""
        _______
      /         \
     |   O   O   |
     |     ∆     |
      \  \___/  /
       \_______/
    """

    # Print glasses with color
    print_color(glasses, "33")  # Yellow

    # Print quote with animation
    print("\n\033[35m" + " " * 10 + "Philosophical Thought of the Day:" + "\033[0m\n")
    for char in quote:
        print(f"\033[36m{char}\033[0m", end='', flush=True)
        time.sleep(0.05)
    print("\n")

    # Print author with animation
    print("\033[35m" + " " * 15 + "- " + "\033[0m", end='')
    for char in author:
        print(f"\033[31m{char}\033[0m", end='', flush=True)
        time.sleep(0.1)
    print("\n")

    # Print a funny footer
    footer = "Remember: The universe is expanding, and so is your waistline."
    print("\n" + "\033[33m" + " " * 5 + footer + "\033[0m\n")

if __name__ == "__main__":
    print_woody_quote()