"""
Campbell's Soup Can #42
Produced: 2025-11-04 04:35:46
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
    "I'm not a great cook, but I can usually manage to boil an egg without breaking it... or the house.",
    "I'm not saying I'm Wonder Woman, but I do have a certain... je ne sais quit.",
    "I'm not afraid of heights; I'm afraid of widths."
]

# ASCII art
ascii_art = """
 ______     __  __     __     ______     ______     __  __
/\  ___\   /\ \/\ \   /\ \   /\  ___\   /\  ___\   /\ \/\ \
\ \  \_\ \  \ \ \ \ \  \ \ \  \ \ \____  \ \  \_\ \  \ \ \ \ \
 \ \  \/\ \  \ \ \ \ \  \ \ \  \ \ \___|  \ \  \/\ \  \ \ \ \ \
  \ \_____\  \ \_\ \_\  \ \_\  \ \ \__\   \ \_____\  \ \_\ \_\ \
   \/_____/   \/_/\/_/   \/_/   \/____/    \/_____/   \/_/\/_/
"""

def print_quote():
    print(GREEN + ascii_art + RESET)
    time.sleep(1)
    print(RED + random.choice(quotes) + RESET)

if __name__ == "__main__":
    print_quote()