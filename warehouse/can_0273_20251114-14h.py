"""
Campbell's Soup Can #273
Produced: 2025-11-14 14:34:05
Worker: Mistral: Mistral Small 3.1 24B (free) (mistralai/mistral-small-3.1-24b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ASCII art for a thought bubble
thought_bubble = [
    "       _______________",
    "      /               \\",
    "     |                 |",
    "     |   Woody's       |",
    "     |   Wisdom        |",
    "     |                 |",
    "      \\_______________/"
]

# List of Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The heart wants what it wants, but the brain wants a break.",
    "I don't want to live on in the hearts of my countrymen; I want to live on in my apartment.",
    "I'm at two with nature. I don't get no respect from her."
]

# Function to print the thought bubble
def print_thought_bubble():
    for line in thought_bubble:
        print(f"{CYAN}{line}{RESET}")

# Function to print a quote with animation
def print_quote(quote):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for char in quote:
        color = random.choice(colors)
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(0.05)

# Main function
def main():
    print_thought_bubble()
    print()
    quote = random.choice(quotes)
    print_quote(quote)
    print()

if __name__ == "__main__":
    main()