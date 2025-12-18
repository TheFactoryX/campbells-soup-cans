"""
Campbell's Soup Can #1010
Produced: 2025-12-18 07:33:49
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

# ANSI color codes
CYAN   = '\033[36m'
YELLOW = '\033[33m'
RESET  = '\033[0m'

# Woody Allen‑style quote
quote = "I am not terrified of death; I just don't want to miss my own funeral."

# Print the quote inside a colorful decorative box
def print_boxed(text):
    top    = f"{CYAN}╔{'─'*62}{RESET}"
    middle = f"{CYAN}║{YELLOW}  {text}  {RESET}{CYAN}║"
    bottom = f"{CYAN}╚{'─'*62}{RESET}"
    print(top)
    print(middle)
    print(bottom)

print_boxed(quote)