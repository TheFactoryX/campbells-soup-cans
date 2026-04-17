"""
Campbell's Soup Can #3329
Produced: 2026-04-17 19:31:48
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
BOLD = "\033[1m"

def colorize(text, color):
    return f"{color}{text}{RESET}"

def print_with_delay(lines, delay=0.05):
    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # newline after each line

def main():
    quote = (
        "I’m convinced that the meaning of life is to find a good parking spot, "
        "and even that’s usually taken."
    )
    # Create a simple box
    width = len(quote) + 4
    top_bottom = "╔" + "═" * (width - 2) + "╗"
    middle = f"║  {quote}  ║"
    bottom = "╔" + "═" * (width - 2) + "╝"

    # Choose random colors for each part
    top_color = random.choice(COLORS)
    mid_color = random.choice(COLORS)
    bot_color = random.choice(COLORS)

    box_lines = [
        colorize(top_bottom, top_color + BOLD),
        colorize(middle, mid_color + BOLD),
        colorize(bottom, bot_color + BOLD),
    ]

    # Print with a slight typing effect
    print_with_delay(box_lines, delay=0.03)

if __name__ == "__main__":
    main()