"""
Campbell's Soup Can #1791
Produced: 2026-01-23 08:47:07
Worker: Mistral: Devstral 2 2512 (free) (mistralai/devstral-2512:free)
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

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, color_code):
    horizontal = '─' * (width - 2)
    vertical = '│'
    corner = '┌' + horizontal + '┐'
    middle = vertical + ' ' * (width - 2) + vertical
    bottom = '└' + horizontal + '┘'

    print_colored(corner, color_code)
    for _ in range(height - 2):
        print_colored(middle, color_code)
    print_colored(bottom, color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't know the question, but sex is definitely the answer.",
        "I'm not a paranoid deranged millionaire. Goddammit, I'm a billionaire."
    ]

    selected_quote = random.choice(quotes)

    # ASCII art of Woody Allen's glasses
    glasses = r"""
        ______
      /        \
     /          \
    |    O  O    |
    |      △     |
     \          /
      \________/
    """

    # Print glasses with color
    print_colored(glasses, "33")  # Yellow

    # Print quote in a box with typewriter effect
    box_width = max(len(line) for line in selected_quote.split('\n')) + 4
    box_height = 5

    draw_box(box_width, box_height, "36")  # Cyan

    # Move cursor up to print inside the box
    for _ in range(box_height - 2):
        sys.stdout.write("\033[F")  # Move cursor up

    # Print quote with typewriter effect
    print_colored(" " * 2, "36"),  # Cyan
    typewriter_effect(selected_quote, 0.03)
    print_colored(" " * 2, "36")  # Cyan

    # Print author with color
    print_colored("\n\t\t- Woody Allen (probably)\n", "35")  # Magenta

if __name__ == "__main__":
    main()