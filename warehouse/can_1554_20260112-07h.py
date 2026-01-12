"""
Campbell's Soup Can #1554
Produced: 2026-01-12 07:41:17
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from itertools import cycle

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m",  # Bright Cyan
    "\033[0m"   # Reset
]

# Woody Allen-style quotes
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The heart's memory eliminates the bad and magnifies the good, and thanks to this artifice we're able to endure the burdens of the past.",
    "I don't want to live in a world where I'm the smartest person in the room. I want to live in a world where I'm the dumbest person in the room.",
    "I'm at two with nature. I don't trust it.",
    "I'm not a paranoid deranged millionaire. God knows I'm not a millionaire.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist. I'm not a pessimist, I'm a realist. I'm not a pessimist, I'm a realist."
]

def print_woody_quote():
    quote = random.choice(QUOTES)
    color_cycle = cycle(COLORS)

    # Create a colorful box around the quote
    print("\033[1m" + "=" * (len(quote) + 4) + "\033[0m")
    for char in quote:
        print(next(color_cycle) + char + "\033[0m", end="", flush=True)
        time.sleep(0.1)
    print("\n" + "\033[1m" + "=" * (len(quote) + 4) + "\033[0m")

    # Add a little animation
    print("\nThinking deeply about this...")
    for _ in range(3):
        for frame in ["-", "\\", "|", "/"]:
            print(f"\r{frame} \033[33mWoody Allen\033[0m", end="", flush=True)
            time.sleep(0.1)
    print("\n\n")

if __name__ == "__main__":
    print("\033[1m\033[35m" + "WOODY ALLEN'S PHILOSOPHICAL QUOTE GENERATOR" + "\033[0m")
    print("\033[36m" + "=" * 40 + "\033[0m\n")

    while True:
        print_woody_quote()
        again = input("\033[32mWant another one? (y/n)\033[0m ").lower()
        if again != 'y':
            print("\033[31mOkay, I'll stop overthinking my existence now.\033[0m")
            break