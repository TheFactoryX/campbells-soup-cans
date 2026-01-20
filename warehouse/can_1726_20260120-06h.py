"""
Campbell's Soup Can #1726
Produced: 2026-01-20 06:55:57
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

# Typewriter effect
def typewriter(text, color=RESET, delay=0.05):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Blinking text effect
def blink_text(text, color=RESET, delay=0.5, times=3):
    for _ in range(times):
        sys.stdout.write(color + text + RESET + '\n')
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(delay)

# Main function
def main():
    clear_screen()

    quotes = [
        "I'm not afraid of dying; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The heart wants what it wants, but the brain wants a refund.",
        "I don't want to live on in the hearts of my countrymen; I want to live on in my apartment.",
        "I'm at two with nature."
    ]

    quote = random.choice(quotes)

    # Box around the quote
    box = f"""
{BLUE}+{'-'*50}+{RESET}
|{CYAN} {quote.center(48)} {CYAN}|{RESET}
{BLUE}+{'-'*50}+{RESET}
    """

    # Typewriter effect for the box
    for line in box.splitlines():
        typewriter(line, delay=0.02)

    # Blinking text effect
    blink_text("Woody Allen", MAGENTA, delay=0.3, times=5)

    # Final message
    typewriter("Life is like a game of chess...", YELLOW)
    typewriter("...except the chess pieces are always moving and you're not sure of the rules.", YELLOW)

if __name__ == "__main__":
    main()