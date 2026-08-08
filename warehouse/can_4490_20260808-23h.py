"""
Campbell's Soup Can #4490
Produced: 2026-08-08 23:44:38
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # Woody Allen‑style philosophical quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    width = len(quote) + 4                     # account for "| " and " |"
    border = "+" + "-" * width + "+"

    # ANSI colour codes
    magenta = "\033[35m"
    yellow  = "\033[33m"
    reset   = "\033[0m"

    # Print a colorful framed quote
    print(magenta + border + reset)
    print(yellow + "| " + quote + " |" + reset)
    print(magenta + border + reset)

if __name__ == "__main__":
    main()