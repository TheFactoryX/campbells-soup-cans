"""
Campbell's Soup Can #401
Produced: 2025-11-20 13:00:15
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
YELLOW = '\033[33m'
RESET = '\033[0m'

# Woody Allen quotes
quotes = [
    f"{GREEN}Life doesn't imitate art, it imitates bad television.{RESET}",
    f"{YELLOW}I'm not afraid of death; I just don't want to be there when it happens.{RESET}",
    f"{GREEN}I'm not a great cook, but I can open a can of soup.{RESET}",
    f"{YELLOW}I'm not neurotic, I have unique personal challenges.{RESET}",
    f"{GREEN}I don't want to achieve immortality through my work; I want to achieve it through not dying.{RESET}",
]

# ASCII art for the quote box
box = """
 ______
< Quote >
 ------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
"""

# Print the ASCII art and a random quote with a typing effect
print(box)
time.sleep(0.5)
for char in random.choice(quotes):
    print(char, end='', flush=True)
    time.sleep(0.05)