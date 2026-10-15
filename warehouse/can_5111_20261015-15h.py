"""
Campbell's Soup Can #5111
Produced: 2026-10-15 15:01:19
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

def main():
    # Woody Allen‑style quote (original)
    quote = "I have a deep fear of success; what if I actually accomplish something and then have to deal with the responsibility?"

    # Simple ASCII art of a neurotic face
    ascii_face = r"""
      _____
     /     \
    |  o o  |
    |   ^   |
    |  '-'  |
     \_____/
    """
    # Colors
    CYAN   = "\033[36m"
    YELLOW = "\033[33m"
    GREEN  = "\033[32m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

    # Print face in green
    print(GREEN + ascii_face + RESET)

    # Prepare box dimensions
    padding = 2
    inner = " " + quote + " "
    width = len(inner) + 2  # space for left/right borders
    top_bottom = "+" + "-" * (width - 2) + "+"

    # Top border
    print(CYAN + top_bottom + RESET)
    # Left border
    sys.stdout.write(CYAN + "|" + RESET)
    # Typewriter effect for the quote
    for ch in inner:
        sys.stdout.write(BOLD + YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.07)
    # Right border and newline
    print(CYAN + "|" + RESET)
    # Bottom border
    print(CYAN + top_bottom + RESET)

if __name__ == "__main__":
    main()