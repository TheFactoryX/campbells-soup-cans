"""
Campbell's Soup Can #888
Produced: 2025-12-12 17:34:32
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
    print_colored(glasses, "33")  # Yellow

    # Print quote with animation
    print("\n\033[31m" + "  " + "\033[0m" * 10)  # Red dots for emphasis
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")

    # Print author with color
    print_colored(f"\n— {author}", "36")  # Cyan

    # Add some existential humor
    print("\n\033[35m" + "  (But seriously, who wants to be there for that?)", "\033[0m")

if __name__ == "__main__":
    print_woody_quote()