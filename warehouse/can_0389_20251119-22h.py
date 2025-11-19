"""
Campbell's Soup Can #389
Produced: 2025-11-19 22:33:19
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
    GREEN + "I'm not afraid of death; I just don't want to be there when it happens." + RESET,
    RED + "Life is full of misery, loneliness, and suffering - and it's all over much too soon." + RESET,
    GREEN + "I don't want to achieve immortality through my work; I want to achieve it through not dying." + RESET
]

# ASCII art for the quote
art = """
 ______   ______   __    __  ______   ______   ______
/\  ___\ /\  ___\ /\ \  /\ \/\  ___\ /\  ___\ /\  ___\
\ \ \____\ \ \____\ \ \ \/\ \ \ \  __\ \ \  __\ \ \  __\
 \ \_____\\ \_____\\ \ \_____\ \ \_\    \ \_\    \ \_\    \
  \/_____/ \/_____/ \/_____/  \/_/     \/_/     \/_/     \/
"""

# Print ASCII art
print(art)

# Print a random quote with a typing effect
for char in random.choice(quotes):
    print(char, end='', flush=True)
    time.sleep(0.05)