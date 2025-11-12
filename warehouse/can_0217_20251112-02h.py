"""
Campbell's Soup Can #217
Produced: 2025-11-12 02:15:27
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
    "I'm not a great cook, but I can usually manage to boil an egg without breaking it. Which is more than I can say for my relationships.",
    "I'm not afraid of growing old, I just don't want to be there when it happens.",
    "I'm not looking for a handout, just a hand up. And maybe a little foot rub while I'm at it."
]

# ASCII art for Woody Allen
woody_art = """
  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-'
"""

def print_quote(quote):
    print(GREEN + woody_art + RESET)
    print(RED + "Woody Allen says:" + RESET)
    print(quote)
    time.sleep(1)
    print(RESET)

if __name__ == "__main__":
    random_quote = random.choice(quotes)
    print_quote(random_quote)