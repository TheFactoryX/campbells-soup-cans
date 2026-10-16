"""
Campbell's Soup Can #5115
Produced: 2026-10-16 07:10:35
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
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow_print(text, delay=0.07):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Simple Woody Allen‑style ASCII art (just a goofy face)
    ascii_art = [
        r"   _____ ",
        r"  /     \ ",
        r" | () () |",
        r"  >   ^  <",
        r" /'------'\",
        r"  |~~~~~~| "
    ]

    quote = "I’m not scared of eternity; I just hope it comes with a good coffee refill."

    # Header
    print(CYAN + BOLD + "=" * 58 + RESET)
    for line in ascii_art:
        print(YELLOW + line + RESET)
    print(CYAN + BOLD + "=" * 58 + RESET)

    # Quote inside a colored box with typing effect
    box_width = len(quote) + 4
    print(GREEN + "+" + "-" * box_width + "+" + RESET)
    sys.stdout.write(GREEN + "| " + RESET)
    slow_print(quote)
    sys.stdout.write(" " + GREEN + "|" + RESET)
    print()
    print(GREEN + "+" + "-" * box_width + "+" + RESET)

    # Footer
    print(CYAN + BOLD + "=" * 58 + RESET)

if __name__ == "__main__":
    main()