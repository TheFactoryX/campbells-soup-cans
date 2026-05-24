"""
Campbell's Soup Can #3780
Produced: 2026-05-24 23:14:53
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
RESET = '\033[0m'
YELLOW = '\033[33m'
GREEN = '\033[32m'

def typewriter(text, delay=0.05):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Woody Allen‑style quote (original)
    quote = 'I ponder the void, but mostly I wonder if I left the stove on.'
    # Determine box width (quote + some padding)
    width = len(quote) + 10  # extra space for borders and breathing room

    # Animate top border
    sys.stdout.write(YELLOW + "+" + "-" * (width - 2) + "+" + RESET + "\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # Left border
    sys.stdout.write(YELLOW + "|" + RESET)
    sys.stdout.flush()
    time.sleep(0.1)

    # Type the quote inside the box
    typewriter(" " + quote, delay=0.04)

    # Fill remaining space to align right border
    remaining = width - 2 - len(quote)  # subtract left/right borders and quote
    sys.stdout.write(" " * remaining)
    sys.stdout.flush()
    time.sleep(0.1)

    # Right border and newline
    sys.stdout.write(YELLOW + "|" + RESET + "\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # Animate bottom border
    sys.stdout.write(YELLOW + "+" + "-" * (width - 2) + "+" + RESET + "\n")
    sys.stdout.flush()
    time.sleep(0.2)

if __name__ == "__main__":
    main()