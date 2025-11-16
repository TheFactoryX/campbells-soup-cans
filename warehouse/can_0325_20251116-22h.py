"""
Campbell's Soup Can #325
Produced: 2025-11-16 22:32:07
Worker: Mistral: Mistral Nemo (free) (mistralai/mistral-nemo:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI escape codes for colors
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# Woody Allen quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm not a great cook, but I can usually manage to make a few dishes that are edible. And if I can't, well, there's always takeout. Or starvation.",
    "I've been through some terrible things in my life, some of which actually happened.",
    "I'm not concerned about the very poor. They're not going to give the next presidential election to the Republicans."
]

# ASCII art for the quote box
box = """
  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-'
"""

def print_quote():
    quote = random.choice(quotes)
    print(GREEN + box + RESET)
    print(RED + quote + RESET)
    time.sleep(1)

# Print a random quote 5 times with a 1-second delay between each
for _ in range(5):
    print_quote()