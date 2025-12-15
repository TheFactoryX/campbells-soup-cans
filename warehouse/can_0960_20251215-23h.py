"""
Campbell's Soup Can #960
Produced: 2025-12-15 23:32:01
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
    # Woody Allen style quote
    quote = "I'm not afraid of dying; I just don't want to be there when it happens."

    # ASCII art of Woody Allen's glasses
    glasses = r"""
       _______
     /         \
    |   O   O   |
    |     ∆     |
     \  ___  /
      \     /
    """

    # Print glasses with color
    print_color(glasses, "33")  # Yellow

    # Print quote with animation
    for char in quote:
        print_color(char, "36")  # Cyan
        sys.stdout.flush()
        time.sleep(0.05)

    print()  # New line

    # Print a witty follow-up
    follow_up = "After all, if it turns out there is a God, I don't want Him to think I wasn't listening."
    time.sleep(1)
    for char in follow_up:
        print_color(char, "35")  # Magenta
        sys.stdout.flush()
        time.sleep(0.03)

    print()  # New line

    # Print a final thought
    final_thought = "And if there isn't... well, then I've wasted a lot of time talking to myself."
    time.sleep(1)
    for char in final_thought:
        print_color(char, "32")  # Green
        sys.stdout.flush()
        time.sleep(0.02)

    print()  # New line

if __name__ == "__main__":
    print_woody_quote()