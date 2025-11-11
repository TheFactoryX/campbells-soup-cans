"""
Campbell's Soup Can #199
Produced: 2025-11-11 06:46:17
Worker: Mistral: Mistral Nemo (free) (mistralai/mistral-nemo:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

from time import sleep
from random import choice

# Woody Allen quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm not that young anymore. I'm not that old either. I'm just that age that is in between.",
    "I'm not a great cook, but I can open a can of soup and make it taste horrible."
]

# ANSI escape codes for colors
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

def print_quote(quote):
    print(f"{GREEN}🎭 {quote}{RESET}")

def animate():
    for _ in range(3):
        print(f"{RED}💡{RESET}", end="")
        sleep(0.2)
        print("\033[1A\033[K", end="")  # Move cursor up and clear line

# Main
animate()
print_quote(choice(quotes))