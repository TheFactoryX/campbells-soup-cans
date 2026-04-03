"""
Campbell's Soup Can #3106
Produced: 2026-04-03 11:03:43
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
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def type_text(text, delay=0.04, color=""):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def thinking_animation(dots=3, delay=0.5):
    """Show a simple 'thinking' animation."""
    sys.stdout.write("Thinking")
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Woody Allen‑style quote (original)
    quote_lines = [
        "I don't believe in an afterlife, although I am bringing",
        "a change of underwear just in case."
    ]

    # Determine box width based on longest line
    max_len = max(len(line) for line in quote_lines)
    width = max_len + 4  # padding for borders and spaces

    # Build top and bottom borders
    border = "+" + "-" * width + "+"

    # Choose random colors for each element
    border_color = random.choice([CYAN, BLUE, MAGENTA])
    quote_colors = [random.choice([RED, GREEN, YELLOW, WHITE]) for _ in quote_lines]

    # Show a little thinking animation first
    thinking_animation()

    # Print top border instantly
    sys.stdout.write(border_color + border + RESET + "\n")
    sys.stdout.flush()

    # Print each quote line with typewriter effect and colors
    for line, color in zip(quote_lines, quote_colors):
        # Center the line inside the box
        padded = line.ljust(width - 2)
        sys.stdout.write(border_color + "| " + RESET)
        type_text(padded, delay=0.05, color=color)
        sys.stdout.write(border_color + " |" + RESET + "\n")
        sys.stdout.flush()

    # Print bottom border instantly
    sys.stdout.write(border_color + border + RESET + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()