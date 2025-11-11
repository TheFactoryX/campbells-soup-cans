"""
Campbell's Soup Can #207
Produced: 2025-11-11 14:36:03
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
    "I'm not that young anymore. I'm not that old either. I'm just... in between. Like a sandwich without the bread.",
    "I was thrown out of college for cheating on the metaphysics exam: I looked into the soul of the boy sitting next to me.",
    "I'm not neurotic. I have an inner life. It's just that my inner life is more interesting than most people's."
]

# ASCII art for Woody Allen
woody_art = """
 ______
< Woody Allen >
 ------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||
"""

def print_quote():
    quote = random.choice(quotes)
    print(f"{GREEN}{woody_art}{RESET}")
    time.sleep(1)
    print(f"{RED}{quote}{RESET}")

if __name__ == "__main__":
    print_quote()