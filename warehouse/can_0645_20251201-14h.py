"""
Campbell's Soup Can #645
Produced: 2025-12-01 14:40:53
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
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

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}

def typewriter_effect(text, color='white', delay=0.05):
    """Print text with a typewriter effect and color."""
    for char in text:
        print(f"{COLORS[color]}{char}{COLORS['reset']}", end='', flush=True)
        time.sleep(delay)
    print()

def print_boxed(text, color='cyan', border_color='yellow'):
    """Print text in a colorful box."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)

    # Top border
    print(f"{COLORS[border_color]}╔{'═' * (max_len + 4)}╗{COLORS['reset']}")

    # Content
    for line in lines:
        print(f"{COLORS[border_color]}║ {COLORS[color]}{line.ljust(max_len)}{COLORS[border_color]} ║{COLORS['reset']}")

    # Bottom border
    print(f"{COLORS[border_color]}╚{'═' * (max_len + 4)}╝{COLORS['reset']}")

def main():
    # Clear screen
    print("\033c", end="")

    # ASCII art of Woody Allen
    woody_art = r"""
    {red}   _____
   /     \
  | () () |
  \  ^  /
   |||||
   |||||{reset}
    """
    print(woody_art.format(**COLORS))

    # Typewriter effect for introduction
    typewriter_effect("Woody Allen's Existential Thought Generator", 'magenta')
    print()

    # Randomly select a quote
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The heart wants what it wants, but the brain knows better.",
        "I'm at two with nature. Take me to your leaver."
    ]

    quote = random.choice(quotes)

    # Print the quote in a box
    print_boxed(quote, 'green', 'blue')

    # Typewriter effect for outro
    typewriter_effect("Thanks for existentializing with me!", 'cyan')

if __name__ == "__main__":
    main()