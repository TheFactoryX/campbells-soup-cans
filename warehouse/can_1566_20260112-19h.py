"""
Campbell's Soup Can #1566
Produced: 2026-01-12 19:32:00
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

    # ASCII art of Woody Allen (simplified)
    ascii_art = r"""
       _____
     /       \
    |  O   O  |
    |    ∆    |
     \  ___  /
      \_____/
    """

    # Print ASCII art with color
    print_colored(ascii_art, "33")  # Yellow

    # Print quote with animation
    print("\n\033[31m" + "   Woody Allen's Thought of the Day:" + "\033[0m\n")
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")

    # Print a funny footer
    footer = "   (Ponder this while eating a pastrami sandwich...)"
    print_colored(footer, "32")  # Green

if __name__ == "__main__":
    print_woody_quote()