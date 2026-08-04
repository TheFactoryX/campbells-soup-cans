"""
Campbell's Soup Can #4436
Produced: 2026-08-04 23:18:07
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

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

def random_color():
    return random.choice(COLORS)

def print_with_effect(text, delay=0.04):
    for ch in text:
        sys.stdout.write(random_color() + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the quote

def main():
    quote = ("I'm not afraid of death; I just don't want to be there when it happens. "
             "But if I am, I hope there's Wi‑Fi in the afterlife.")
    
    # Simple decorative box
    width = len(quote) + 4
    top_bot = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    
    # Print top border with a flickering effect
    for _ in range(3):
        sys.stdout.write(random_color() + top_bot + RESET + "\r")
        sys.stdout.flush()
        time.sleep(0.1)
    print(random_color() + top_bot + RESET)
    
    # Print the quote with typing effect
    print_with_effect(quote)
    
    # Print bottom border with a flickering effect
    for _ in range(3):
        sys.stdout.write(random_color() + bottom + RESET + "\r")
        sys.stdout.flush()
        time.sleep(0.1)
    print(random_color() + bottom + RESET)

if __name__ == "__main__":
    main()