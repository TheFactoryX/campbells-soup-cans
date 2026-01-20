"""
Campbell's Soup Can #1739
Produced: 2026-01-20 20:28:59
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
    quote = "I'm not afraid of dying; I just don't want to be there when it happens."
    author = "— Woody Allen (probably)"

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
    print_colored(glasses, "33")  # Yellow

    # Print quote with animation
    print("\n")
    for char in quote:
        print_colored(char, "36"),  # Cyan
        sys.stdout.flush()
        time.sleep(0.05)

    print("\n")
    for char in author:
        print_colored(char, "35"),  # Magenta
        sys.stdout.flush()
        time.sleep(0.03)

    print("\n\n")

    # Bonus: A neurotic thought
    neurotic_thought = "P.S. What if the universe is just a big joke and we're the punchline?"
    print_colored("   ", "0")
    for char in neurotic_thought:
        print_colored(char, "31"),  # Red
        sys.stdout.flush()
        time.sleep(0.04)

    print("\n")

if __name__ == "__main__":
    print_woody_quote()