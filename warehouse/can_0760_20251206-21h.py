"""
Campbell's Soup Can #760
Produced: 2025-12-06 21:28:16
Worker: Meta: Llama 3.2 3B Instruct (free) (meta-llama/llama-3.2-3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from random import choice

# ASCII art cat for background
print("\033[32m")
for _ in range(5):
    for _ in range(15):
        print(" ", end="\t")
    print("\033[0m")

# quote options
woody_alellen_quotes = [
    "I'm not a pessimist, I'm just a realist with a darker coat of paint.",
    "I'm not arguing, I'm just passionately expressing my point of view while completely dismissing yours.",
    "I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants.",
    "I'm not crazy, my mom says I have a high tolerance for reality.",
    "Life is like a party, except the invitations say 'no refunds' and the punch is depressing."
]

# randomly select a quote
quote = choice(woody_alellen_quotes)

# formatting
print("\033[1m" + "\033[36m")
for _ in range(5):
    print(".quote{} ".format(quote))
print("\033[0m")

# timer for each line
for char in quote:
    print(char, end="", flush=True)
    time.sleep(0.1)

# clearing the screen
print("\033[H\033[2J")

print("\033[1m" + "\033[33m")
for line in woody_alellen_quotes:
    for word in line.split():
        print(" | ".format(word), end="\t")
    print("\033[0m")