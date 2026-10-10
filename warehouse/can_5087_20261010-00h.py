"""
Campbell's Soup Can #5087
Produced: 2026-10-10 00:52:16
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote — colorful, neurotic, existential."""

import time
import sys

# ANSI escape sequences for colors and formatting
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"

# One Woody Allen style philosophical quote
QUOTE = (
    "I don't fear death. I just don't want to be there when it happens. "
    "Mostly because I'm usually in the middle of a thought, "
    "and I hate being interrupted—even by the end of existence."
)

# Tiny ASCII "neurotic brain"
BRAIN = (
    "     .--.\n"
    "    / o o \\\n"
    "    (   v   )\n"
    "     \\  ^  /\n"
    "      | | |\n"
    "     /'-'-'/"
)

def main():
    # Box width based on quote length (minimum 44 chars)
    width = max(len(QUOTE), 40) + 4

    # Colored top border
    print(CYAN + BOLD + "┌" + "─" * width + "┐" + RESET)
    # Title line
    print(CYAN + BOLD + f"│ {YELLOW}WOODY ALLEN PHILOSOPHY {CYAN}│" + RESET)
    # Quote line — cyan borders, green text
    print(
        CYAN + BOLD + "│" + RESET
        + GREEN + QUOTE + RESET
        + CYAN + BOLD + "│" + RESET
    )
    # Colored bottom border
    print(CYAN + BOLD + "└" + "─" * width + "┘" + RESET)

    # Slight "thinking" pause (animation flare)
    time.sleep(0.5)
    print(RED + "   (thinking...)" + RESET)
    time.sleep(0.5)

    # Neurotic ASCII art below the box
    print()
    print(GREEN + BOLD + BRAIN + RESET)
    print()
    print(RED + BOLD + "       The universe shrugged and upped the rent." + RESET)

if __name__ == "__main__":
    main()