"""
Campbell's Soup Can #3133
Produced: 2026-04-04 19:45:47
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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

def type_line(text, color=RESET, delay=0.05):
    """Print text character by character with a slight delay."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()

def main():
    # Woody Allen‑style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Simple neurotic face (ASCII art)
    face = [
        r"   (\_/)   ",
        r"   ('.')   ",
        r'   c(")(")   '
    ]

    # Print the face with a bit of flair
    for line in face:
        type_line(line, BRIGHT_MAGENTA, delay=0.07)
    time.sleep(0.3)

    # Build the quote box
    inner_width = len(quote) + 2          # spaces inside the box
    horiz_border = "+" + "-" * inner_width + "+"
    empty_line   = "|" + " " * inner_width + "|"
    quote_line   = f"| {quote} |"

    # Print the box with color
    type_line(horiz_border, BRIGHT_CYAN, delay=0.001)
    type_line(empty_line,   BRIGHT_CYAN, delay=0.001)
    type_line(quote_line,   BRIGHT_YELLOW + BOLD, delay=0.04)
    type_line(empty_line,   BRIGHT_CYAN, delay=0.001)
    type_line(horiz_border, BRIGHT_CYAN, delay=0.001)

if __name__ == "__main__":
    main()