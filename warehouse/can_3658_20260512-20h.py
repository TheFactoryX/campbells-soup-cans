"""
Campbell's Soup Can #3658
Produced: 2026-05-12 20:50:06
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
]
RESET = "\033[0m"

def type_line(text, color_func=None, char_delay=0.03):
    """Print a line character by character, optionally coloring each char."""
    if color_func is None:
        color_func = lambda: random.choice(COLORS)
    for ch in text:
        sys.stdout.write(color_func() + ch + RESET)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def print_boxed_quote():
    width = 60
    horiz = "+" + "-" * width + "+"
    empty = "|" + " " * width + "|"

    # Top border
    print("\033[96m" + horiz + RESET)  # Cyan top
    time.sleep(0.1)

    # Empty line
    print("\033[95m" + empty + RESET)  # Magenta side
    time.sleep(0.1)

    # Quote lines (Woody Allen style)
    quote = [
        "I don't believe in an afterlife,",
        "but I am bringing a change of underwear just in case."
    ]
    for line in quote:
        print("\033[95m|" + RESET, end="")  # left border
        type_line(line, char_delay=0.04)
        print("\033[95m|" + RESET, end="")  # right border after line
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(0.2)

    # Empty line
    print("\033[95m" + empty + RESET)
    time.sleep(0.1)

    # Bottom border
    print("\033[96m" + horiz + RESET)  # Cyan bottom
    time.sleep(0.1)

    # Footer message
    footer = "Ponder that... or don't."
    print("\n\033[2m" + footer.center(width + 2) + "\033[0m")  # Dim centered

if __name__ == "__main__":
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print_boxed_quote()