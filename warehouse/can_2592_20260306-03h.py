"""
Campbell's Soup Can #2592
Produced: 2026-03-06 03:08:04
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I worry that I might be a character in someone else's play, and the director keeps cutting my scenes before I can even deliver the punchline."
border = '*' * (len(quote) + 4)

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def colored(txt, code):
    return f"{code}{txt}{RESET}"

print(colored(border, RED))
print(colored(f" *** {quote} *** ", GREEN))
print(colored(border, YELLOW))