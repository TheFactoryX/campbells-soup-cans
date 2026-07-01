"""
Campbell's Soup Can #4061
Produced: 2026-07-01 10:48:23
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time

# ----------------------------------------------------------------------
# ANSI color codes (no external dependencies)
# ----------------------------------------------------------------------
RED   = "\033[91m"
YELLOW = "\033[93m"
CYAN  = "\033[96m"
RESET = "\033[0m"

# ----------------------------------------------------------------------
# Woody Allen‑style philosophical quote
# ----------------------------------------------------------------------
quote = (
    "I'm not afraid of death; I just don't want to be there when it happens - "
    "and even then I'd probably be late to the afterlife."
)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored_box(text):
    """Print the given text inside a colorful ASCII box."""
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    width = max_len + 4  # padding on each side

    top_bottom = YELLOW + "+" + "-" * (width - 2) + "+" + RESET
    print(top_bottom)

    for line in lines:
        padded = line.ljust(max_len)
        print("| " + CYAN + padded + RESET + " |")

    print(top_bottom)

if __name__ == "__main__":
    # Small pause for dramatic effect
    time.sleep(0.5)
    clear_screen()
    print_colored_box(quote)
    # Keep the result visible for a few seconds
    time.sleep(5)