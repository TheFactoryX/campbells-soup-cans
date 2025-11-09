"""
Campbell's Soup Can #151
Produced: 2025-11-09 02:18:48
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

# Function to print a colorful box
def print_box(text, color):
    lines = text.split('\n')
    width = max(len(line) for line in lines) + 4
    box = f"{color}╔{'═' * width}╗\n"
    for line in lines:
        box += f"║ {line.ljust(width - 4)} ║\n"
    box += f"╚{'═' * width}╝{RESET}"
    print(box)

# Function to print a blinking text
def print_blinking_text(text, color):
    for _ in range(3):
        print(f"{color}{text}{RESET}", end='\r')
        time.sleep(0.5)
        print(' ' * len(text), end='\r')
        time.sleep(0.5)
    print(f"{color}{text}{RESET}")

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function
def main():
    clear_screen()
    print_blinking_text("Woody Allen's Wisdom", MAGENTA)
    time.sleep(1)
    clear_screen()

    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The heart wants what it wants. Oh, the poor heart. Always wanting.",
        "More than any time in history, mankind faces a crossroads. One path leads to despair and utter hopelessness. The other, to total extinction. Let us pray we have the wisdom to choose correctly.",
        "I don't want to live on in the hearts of my countrymen; I want to live on in my apartment.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    ]

    quote = random.choice(quotes)
    print_box(quote, CYAN)

if __name__ == "__main__":
    main()