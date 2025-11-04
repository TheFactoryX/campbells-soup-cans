"""
Campbell's Soup Can #44
Produced: 2025-11-04 06:45:56
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
    "I'm not saying I'm Wonder Woman's equal, but I am saying... no one has ever seen me and Wonder Woman in the same room.",
    "I'm so depressed, I can't even get a good night's sleep. I wake up in the middle of the night and think, 'Oh, no! I'm not getting any younger!'",
    "I'm not that young anymore. I'm not that old either. I'm... in between. I'm... in betweenish."
]

def print_quote():
    quote = random.choice(quotes)
    print(f"{GREEN}🎭 {quote}{RESET}")
    time.sleep(1)
    print(f"{RED}💭 {quote}{RESET}")
    time.sleep(1)
    print(f"{GREEN}🎭 {quote}{RESET}")
    time.sleep(1)
    print(f"{RED}💭 {quote}{RESET}")
    time.sleep(1)

print_quote()