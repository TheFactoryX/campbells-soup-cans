"""
Campbell's Soup Can #1403
Produced: 2026-01-05 08:50:00
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from itertools import cycle

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]

RESET = "\033[0m"

def spinning_cursor():
    while True:
        for cursor in cycle(['|', '/', '-', '\\']):
            yield cursor

def print_woody_quote():
    # Randomly select a color
    color = random.choice(COLORS)

    # Woody Allen quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "But then again, who does? I mean, really, who actually wants to be there?\n"
        "It's like a bad dinner party that never ends. You're trapped in a room\n"
        "with people you don't like, and the food is terrible, and you can't leave.\n"
        "And the worst part is, you're the main course."
    )

    # Print with color and animation
    print(f"\n{color}=== WOODY ALLEN'S PHILOSOPHICAL THOUGHTS ==={RESET}\n")

    for line in quote.split('\n'):
        print(f"{color}{line}{RESET}")
        time.sleep(0.5)

    # ASCII art of Woody Allen
    woody_art = r"""
       _____
     /     \
    |       |
    |  >_<  |
    |   O   |
     \_____/
    """

    print(f"\n{color}{woody_art}{RESET}")

    # Spinning cursor animation
    spinner = spinning_cursor()
    print("\nThinking deeply about life...")
    for _ in range(10):
        print(next(spinner), end='\r')
        time.sleep(0.1)
    print(" " * 20, end='\r')

    # Final thought
    print(f"\n{color}But then again, what do I know? I'm just a neurotic comedian.{RESET}")

if __name__ == "__main__":
    print_woody_quote()