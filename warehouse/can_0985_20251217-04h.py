"""
Campbell's Soup Can #985
Produced: 2025-12-17 04:46:17
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
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # ASCII art of Woody Allen's glasses
    glasses = r"""
       _______
     /       \\
    |  O   O  |
    |    ∆    |
     \_______/
    """

    # Print glasses in yellow
    print_color(glasses, "93")

    # Print quote with animation
    for char in quote:
        print_color(char, "96")  # Cyan color
        sys.stdout.flush()
        time.sleep(0.05)

    # Print a funny footer
    footer = "\n-- Woody Allen (probably)"
    print_color(footer, "91")  # Red color

if __name__ == "__main__":
    print_woody_quote()