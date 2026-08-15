"""
Campbell's Soup Can #4606
Produced: 2026-08-15 13:43:39
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_writer(text, color=WHITE, delay=0.05):
    """Print text character by character with a slight delay."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def print_boxed_quote():
    quote = (
        "I spend so much time worrying about the future "
        "that I forget to enjoy the present — which is also worrying."
    )
    author = "- Woody Allen (probably)"

    # Determine box width based on longest line
    max_len = max(len(quote), len(author))
    width = max_len + 4  # padding inside box

    top = "┌" + "─" * width + "┐"
    bottom = "└" + "─" * width + "┘"
    side = "│"

    # Print top border
    type_writer(top, color=CYAN, delay=0.01)
    # Print empty line for spacing
    type_writer(side + " " * width + side, color=CYAN, delay=0.01)

    # Print quote line with typing effect
    quoted_line = side + " " + quote.ljust(width - 2) + " "
    type_writer(quoted_line, color=CYAN, delay=0.00)

    # Print author line
    author_line = side + " " + author.ljust(width - 2) + " "
    type_writer(author_line, color=MAGENTA, delay=0.00)

    # Print empty line then bottom border
    type_writer(side + " " * width + side, color=CYAN, delay=0.01)
    type_writer(bottom, color=CYAN, delay=0.01)

    # Optional: add a tiny Woody Allen-esque ASCII face below
    face = r"""
      (\_/)
      ( '_')
     /""""""\""""-._   _
    /  Woody  Allen  \ (\-)
   /___________________\/
"""
    for line in face.splitlines():
        if line.strip():
            type_writer("  " + line, color=YELLOW, delay=0.00)

def main():
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print_boxed_quote()
    # Keep the terminal open a bit so user can see the output
    time.sleep(2)

if __name__ == "__main__":
    main()