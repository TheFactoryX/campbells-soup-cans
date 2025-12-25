"""
Campbell's Soup Can #1168
Produced: 2025-12-25 11:29:33
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
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # ASCII art of Woody Allen (simplified)
    ascii_art = r"""
        .-""""""-.
       /          \
      |            |
      |  O    O    |
      |    __      |
      |   /  \     |
      |  /    \    |
       \          /
        '-......-'
    """

    # Print ASCII art with color
    print_colored(ascii_art, "33")  # Yellow

    # Print quote with animation
    print("\n\033[31mWoody Allen's Thought of the Day:\033[0m\n")
    for char in quote:
        print_colored(char, "36")  # Cyan
        sys.stdout.flush()
        time.sleep(0.05)

    # Print a funny footer
    print("\n")
    print_colored("\n  (Now go eat a sandwich and ponder your existence.)", "35")  # Magenta

if __name__ == "__main__":
    print_woody_quote()