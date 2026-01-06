"""
Campbell's Soup Can #1423
Produced: 2026-01-06 06:52:14
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
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m",  # Bright Cyan
    "\033[0m"   # Reset
]

def spinning_cursor():
    while True:
        for cursor in cycle(['|', '/', '-', '\\']):
            yield cursor

def print_woody_quote():
    quote = "I'm not afraid of death. I just don't want to be there when it happens. But then, I don't want to be there when it doesn't happen either."

    # Create a spinning cursor animation
    spinner = spinning_cursor()

    # Print the quote with color cycling
    for i, char in enumerate(quote):
        color = next(cycle(COLORS))
        print(f"{color}{char}\033[0m", end='', flush=True)
        time.sleep(0.05)

    print("\n\n")

    # Print a little ASCII art
    art = r"""
       _____
      /     \
     |       |
     |  O   O |
     |   -   |
     |  \___/
     \_______/
    """
    print(art)

    # Print a box around the quote
    box = f"""
+{'='*len(quote)+'='}+
| {quote} |
+{'='*len(quote)+'='}+
"""
    print(box)

if __name__ == "__main__":
    print("\033[93mWelcome to Woody Allen's Existential Thought Generator!\033[0m")
    time.sleep(1)
    print("\033[94mThinking deeply about life...\033[0m")
    time.sleep(2)
    print_woody_quote()