"""
Campbell's Soup Can #4733
Produced: 2026-08-21 03:16:02
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys

# Optional screen clear for a cleaner look (works on most terminals)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# Woody Allen‑style philosophical quote, wrapped in a colorful ASCII box
quote = (
    "\033[92m+------------------------------+\033[0m\n"
    "\033[93m|   I’m not afraid of death;   |\033[0m\n"
    "\033[93m|   I just don’t want to be    |\033[0m\n"
    "\033[93m|   there when it happens—      |\033[0m\n"
    "\033[93m|   because I’ll miss my       |\033[0m\n"
    "\033[93m|   coffee before my crisis    |\033[0m\n"
    "\033[93m|   gets cold.                   |\033[0m\n"
    "\033[92m+------------------------------+\033[0m"
)

print(quote)