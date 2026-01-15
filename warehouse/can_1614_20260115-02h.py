"""
Campbell's Soup Can #1614
Produced: 2026-01-15 02:27:41
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

    # ASCII art of Woody Allen's glasses
    glasses = r"""
       ______
     /        \
    |  O   O   |
    |    ∆     |
     \________/
    """

    # Print glasses with color
    print_colored(glasses, "33")  # Yellow

    # Print quote with animation
    print("\n\033[35mWoody Allen's Thought of the Day:\033[0m\n")
    for char in quote:
        print_colored(char, "36")  # Cyan
        sys.stdout.flush()
        time.sleep(0.05)

    # Print a neurotic follow-up
    follow_up = "\n\n(But seriously, what if I'm there and I don't know it?)"
    print_colored(follow_up, "31")  # Red

    # Print a box around the quote
    box_width = len(quote) + 4
    print("\n" + "\033[32m" + "╔" + "═" * box_width + "╗" + "\033[0m")
    print("\033[32m" + "║" + "\033[0m" + " " * (box_width) + "\033[32m" + "║" + "\033[0m")
    print("\033[32m" + "║" + "\033[0m" + " " + quote + " " + "\033[32m" + "║" + "\033[0m")
    print("\033[32m" + "║" + "\033[0m" + " " * (box_width) + "\033[32m" + "║" + "\033[0m")
    print("\033[32m" + "╚" + "═" * box_width + "╝" + "\033[0m")

if __name__ == "__main__":
    print_woody_quote()