"""
Campbell's Soup Can #1808
Produced: 2026-01-24 04:06:18
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

def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def typewriter_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def draw_box(width, height):
    corners = ['╔', '╗', '╚', '╝']
    horizontal = '═'
    vertical = '║'

    # Top border
    print_color(corners[0] + horizontal * (width - 2) + corners[1], '93')

    # Middle content
    for _ in range(height - 2):
        print_color(vertical + ' ' * (width - 2) + vertical, '93')

    # Bottom border
    print_color(corners[2] + horizontal * (width - 2) + corners[3], '93')

def main():
    # Clear screen
    print("\033c", end="")

    # Box dimensions
    box_width = 60
    box_height = 10

    # Center the box
    terminal_width = 80
    padding = (terminal_width - box_width) // 2
    print(' ' * padding, end='')
    draw_box(box_width, box_height)

    # Position cursor inside the box
    for _ in range(box_height - 2):
        print('\033[1A', end='')  # Move up
    print(' ' * (padding + 2), end='')

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where does one spend it?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't know the question, but sex is definitely the answer.",
        "I'm not a paranoid deranged millionaire. Do I sound like one?"
    ]

    quote = random.choice(quotes)

    # Print quote with typewriter effect
    typewriter_effect("\033[93m" + quote + "\033[0m", 0.03)

    # Add some blinking stars for effect
    time.sleep(1)
    for _ in range(3):
        print('\033[1A', end='')  # Move up
    print(' ' * (padding + len(quote) // 2 - 5), end='')
    print_color("✨", "91")
    time.sleep(0.5)
    print('\033[1A', end='')  # Move up
    print(' ' * (padding + len(quote) // 2 + 5), end='')
    print_color("✨", "92")
    time.sleep(0.5)

    # Final message
    print("\n" * 2)
    print_color("  — Woody Allen (probably)", "94")

if __name__ == "__main__":
    main()