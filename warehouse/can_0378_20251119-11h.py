"""
Campbell's Soup Can #378
Produced: 2025-11-19 11:29:07
Worker: Mistral: Mistral Small 3.1 24B (free) (mistralai/mistral-small-3.1-24b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys
import os

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print a colorful box
def print_box(text, color):
    box_lines = [
        f"{color}+{'-' * (len(text) + 2)}+{RESET}",
        f"{color}|{RESET} {text} {color}|{RESET}",
        f"{color}+{'-' * (len(text) + 2)}+{RESET}"
    ]
    for line in box_lines:
        print(line)
        time.sleep(0.5)

# Print a typing effect
def print_typing_effect(text, color):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.05, 0.1))
    print(f"{color}{text}{RESET}")

# Main function
def main():
    clear_screen()
    print_box("Woody Allen's Wisdom", MAGENTA)
    time.sleep(1)
    clear_screen()

    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The heart wants what it wants. Oh, the poor heart. So much disappointment.",
        "To you, I'm an atheist; to God, I'm the Loyal Opposition.",
        "I don't want to live in a world that is linear. I want to live in a world that is eternal. Unfortunately, this doesn't seem to be the world we are living in.",
        "I don't want to achieve immortality through my work... I want to achieve it through not dying."
    ]

    quote = random.choice(quotes)
    print_typing_effect(quote, YELLOW)

    time.sleep(1)
    print("\n" + "-" * len(quote))
    print(f"{CYAN}Enjoy the existential crisis!{RESET}")

if __name__ == "__main__":
    main()