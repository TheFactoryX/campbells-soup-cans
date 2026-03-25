"""
Campbell's Soup Can #2957
Produced: 2026-03-25 10:09:25
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Woody Allen‑style quote (split into lines for typing effect)
QUOTE_LINES = [
    "I’m terrified of commitment, which is why my relationships",
    "last about as long as a New York minute — if that minute were",
    "stuck in traffic, wondering if it left the stove on."
]

def typewriter(text: str, delay: float = 0.06) -> None:
    """Print text character by column with a small pause."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def print_cyan(text: str, end: str = "\n") -> None:
    sys.stdout.write(CYAN + text + RESET + end)
    sys.stdout.flush()

def print_yellow(text: str, end: str = "") -> None:
    sys.stdout.write(YELLOW + text + RESET + end)
    sys.stdout.flush()

def main() -> None:
    # A tiny neurotic face just for fun    face = MAGENTA + " (•̀ᴗ•́)و " + RESET
    print(face)
    print()  # spacing

    # Determine box width based on the longest quote line
    max_len = max(len(line) for line in QUOTE_LINES)
    box_width = max_len + 4  # space for borders and padding

    # Top border
    print_cyan("+" + "-" * box_width + "+")
    print_cyan("")  # blank line inside box for breathing room

    # Quote lines with typing effect
    for line in QUOTE_LINES:
        print_cyan("| ", end="")
        typewriter(line, delay=0.07)
        # Pad remaining spaces to align the right border
        padding = " " * (max_len - len(line))
        print_cyan(padding + " |")
    print_cyan("")  # blank line after quote

    # Bottom border
    print_cyan("+" + "-" * box_width + "+")
    print()  # final newline

if __name__ == "__main__":
    main()