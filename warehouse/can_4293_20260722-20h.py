"""
Campbell's Soup Can #4293
Produced: 2026-07-22 20:32:14
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
COLORS = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bold": "\033[1m",
}


def typewriter(text, delay=0.05, color=COLORS["reset"]):
    """Print text character by character with optional color."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(COLORS["reset"] + "\n")


def main():
    quote = "\"I'm terrified of commitment... to life itself.\""
    # Box dimensions
    width = len(quote) + 4  # padding inside box
    top_border = "+" + "-" * (width - 2) + "+"
    empty_line = "|" + " " * (width - 2) + "|"

    # Choose random colors for each part
    border_color = random.choice([COLORS["cyan"], COLORS["blue"], COLORS["magenta"]])
    quote_color = random.choice([COLORS["yellow"], COLORS["green"], COLORS["white"]])
    face_color = COLORS["red"]

    # Print top border with typewriter effect
    typewriter(top_border, delay=0.02, color=border_color)
    typewriter(empty_line, delay=0.02, color=border_color)

    # Print the quote line
    quoted_line = f'|  {quote}  |'
    typewriter(quoted_line, delay=0.04, color=quote_color)

    typewriter(empty_line, delay=0.02, color=border_color)
    typewriter(top_border, delay=0.02, color=border_color)

    # Optional silly face underneath
    face = "( ಠ_ಠ )  ...I need therapy."
    typewriter(face, delay=0.05, color=face_color)


if __name__ == "__main__":
    main()