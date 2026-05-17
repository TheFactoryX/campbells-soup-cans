"""
Campbell's Soup Can #3708
Produced: 2026-05-17 11:33:23
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

# ANSI color codes
RED   = "\033[31m"
YELLOW= "\033[33m"
CYAN  = "\033[36m"
RESET = "\033[0m"

# The Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Create a simple bordered box
top    = "+" + "-" * 45 + "+"
middle = "|" + " " * 45 + "|"
bottom = "+" + "-" * 45 + "+"

def main():
    # Print the box with colors
    print("\n")
    print(RED + top + RESET)
    print(RED + middle + RESET)
    print(YELLOW + "   " + quote + "   " + RESET)
    print(RED + middle + RESET)
    print(bottom + RESET)
    print("\n")

if __name__ == "__main__":
    main()