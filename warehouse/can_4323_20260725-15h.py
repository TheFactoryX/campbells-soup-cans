"""
Campbell's Soup Can #4323
Produced: 2026-07-25 15:19:24
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

RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"

def spinner():
    for _ in range(3):
        for ch in "|/-\\":
            sys.stdout.write(f"\r{YELLOW}Thinking {ch}{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()

def main():
    spinner()
    quote = "I spend my life worrying about the afterlife, meanwhile I can't even decide what to have for lunch."
    width = len(quote) + 4  # padding for borders
    top_bottom = CYAN + "+" + "-" * (width - 2) + "+" + RESET
    line = (
        CYAN
        + "|"
        + RESET
        + YELLOW
        + quote.center(width - 2)
        + RESET
        + CYAN
        + "|"
        + RESET
    )
    print(top_bottom)
    print(line)
    print(top_bottom)

if __name__ == "__main__":
    main()