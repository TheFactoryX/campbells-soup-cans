"""
Campbell's Soup Can #3570
Produced: 2026-05-05 06:28:35
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Philosophical Wisdom™ - A Neurotic Journey
"""

import random
import time

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

# Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I used to think that I was the most interesting person in the world. Then I met myself.",
    "I'm such a deeply feeling person that I'm always sorry to hear about other people's troubles.",
    "I don't know half of you. I think I never met half of you.",
    "The heart is a muscle that never gets tired. That's why it's the only part of your body that really knows how to take a punch.",
    "I have a photon colliding with my head. It's a little too bright for me.",
]

def clear_screen():
    """Clear the terminal screen."""
    print('\033[2J\033[H', end='')

def print_typewriter(text, delay=0.03, color=''):
    """Print text with a typewriter effect."""
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(RESET)

def main():
    # Clear screen
    clear_screen()
    
    # Print header
    print()
    print(CYAN + BOLD + "  ╔══════════════════════════════════════════════════════════════════╗")
    print("  ║           WOODY ALLEN'S PHILOSOPHICAL WISDOM™                 ║")
    print("  ║           (A Neurotic Journey Through Existence)              ║")
    print("  ╚══════════════════════════════════════════════════════════════════╝" + RESET)
    print()
    
    # Select a random quote
    quote = random.choice(quotes)
    
    # Print with typewriter effect
    print("  ", end='')
    print_typewriter(quote, delay=0.04, color=MAGENTA)
    print()
    
    # Print a philosophical footer
    print(YELLOW + "  ──────────────────────────────────────────────────────────────" + RESET)
    print(CYAN + "  'Nuff said.' - Woody Allen" + RESET)
    print()

if __name__ == "__main__":
    main()