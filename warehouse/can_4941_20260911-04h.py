"""
Campbell's Soup Can #4941
Produced: 2026-09-11 04:41:46
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
    # ANSI color codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Width of the box (including the side '+' characters)
    WIDTH = 120

    # Top and bottom border
    top_bottom = CYAN + "+" + "-" * (WIDTH - 2) + "+" + RESET

    # Middle line template (just spaces between the '|')
    middle_template = CYAN + "|" + " " * (WIDTH - 2) + "|" + RESET

    # The Woody Allen‑style quote (yellow)
    quote = YELLOW + "\"I spend my whole life trying to find a purpose, only to realize it's just another excuse for a nap.\"" + RESET

    # Print the box
    print(top_bottom)
    # Center the quote within the middle line
    padding = (WIDTH - 2 - len(quote)) // 2
    left = " " * padding
    right = " " * (WIDTH - 2 - len(quote) - padding)
    print(middle_template.replace(" " * (WIDTH - 2), left + quote + right))
    print(top_bottom)

if __name__ == "__main__":
    main()