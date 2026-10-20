"""
Campbell's Soup Can #5138
Produced: 2026-10-20 11:38:16
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
    YELLOW = "\033[93m"
    RED = "\033[31m"
    RESET = "\033[0m"

    # The Woody Allen style philosophical quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens – it's the ultimate inconvenience."

    # Box dimensions (total width including '|' characters)
    width = 70
    inner_width = width - 2  # space between the '|' characters

    # Build the ASCII box
    border = YELLOW + "+" + "-" * inner_width + "+" + RESET
    top_bottom = YELLOW + "|" + " " * inner_width + "|" + RESET

    # Center the quote inside the box
    padded_quote = quote.center(inner_width)
    quote_line = RED + "|" + padded_quote + "|" + RESET

    # Print the formatted box
    print(border)
    print(top_bottom)
    print(quote_line)
    print(top_bottom)
    print(border)
    print(RESET)  # reset colors to normal

if __name__ == "__main__":
    main()