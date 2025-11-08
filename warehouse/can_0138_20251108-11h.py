"""
Campbell's Soup Can #138
Produced: 2025-11-08 11:25:49
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

quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I'm such a good lover because I practice a lot on my own.",
    "I'm not a great cook, but I can open a can of soup and make it look like I'm doing something complicated.",
    "I'm not afraid of growing old, I just don't want to be there when it happens.",
]

def print_quote(quote):
    print("\033[1;33m" + "--- Woody Allen ---" + "\033[0m")
    print("\033[1;35m" + quote + "\033[0m")
    print("\033[1;32m" + "--- Think about it! ---" + "\033[0m")
    time.sleep(1)
    print("\033[1;31m" + "--- But not too much! ---" + "\033[0m")
    time.sleep(1)

if __name__ == "__main__":
    while True:
        print("\033[1;36m" + "Loading... " + "\033[0m", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="")
        print("\n")
        print_quote(random.choice(quotes))
        time.sleep(2)
        print("\033[1;36m" + "Press Ctrl+C to quit or wait for another quote..." + "\033[0m")