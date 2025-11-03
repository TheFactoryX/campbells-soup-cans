"""
Campbell's Soup Can #34
Produced: 2025-11-03 18:40:38
Worker: Meta: Llama 4 Scout (free) (meta-llama/llama-4-scout:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes for colors
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"

def print_boxed_quote(quote, color):
    box_length = len(quote) + 4
    print(f"{color}+{'-' * box_length}+{RESET}")
    print(f"{color}|{' ' * 2}{quote}{' ' * 2}|{RESET}")
    print(f"{color}+{'-' * box_length}+{RESET}")

def animate_quote(quote, color):
    for _ in range(3):
        print_boxed_quote(quote, color)
        time.sleep(0.5)
        print("\033[2J")  # Clear screen
    print_boxed_quote(quote, color)

def main():
    quotes = [
        f"{RED}I'm not afraid of death; I just don't want to be there when it happens, because that would be awkward.{RESET}",
        f"{GREEN}Life is full of misery, loneliness, and suffering - and it's all over much too soon, but at least the coffee is good.{RESET}",
        f"{BLUE}I don't want to achieve immortality through my work; I want to achieve it through not dying, or at least not dying before my therapist session.{RESET}",
        f"{YELLOW}I'm addicted to placebos. I could quit, but it wouldn't make a difference, or would it?{RESET}",
    ]
    quote = random.choice(quotes)
    animate_quote(quote, "default")

if __name__ == "__main__":
    main()