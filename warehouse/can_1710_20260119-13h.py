"""
Campbell's Soup Can #1710
Produced: 2026-01-19 13:12:16
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
        ______
       /      \
      |  O O  |
      |   ∆   |
       \_____/
    """

    # Print glasses in yellow
    print_colored(glasses, "33")

    # Print quote with animation
    print("\n")
    for char in quote:
        print_colored(char, "36")  # Cyan color
        sys.stdout.flush()
        time.sleep(0.05)

    print("\n")
    print_colored(f" — {author}", "35")  # Magenta color

    # Print a neurotic thought bubble
    print("\n")
    thought_bubble = r"""
        (  .-")
         .( (  )
        (__(__)
    """
    print_colored(thought_bubble, "31")  # Red color

    # Print a funny existential question
    existential_question = "Why is the universe expanding? It's probably just trying to get away from me."
    print("\n")
    for char in existential_question:
        print_colored(char, "32")  # Green color
        sys.stdout.flush()
        time.sleep(0.03)

if __name__ == "__main__":
    print_woody_quote()