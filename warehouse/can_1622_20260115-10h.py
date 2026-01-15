"""
Campbell's Soup Can #1622
Produced: 2026-01-15 10:44:00
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
    print(f"\033[{color_code}m{text}\033[0m", end='')

def typewriter_effect(text, color_code, delay=0.05):
    for char in text:
        print_colored(char, color_code)
        sys.stdout.flush()
        time.sleep(delay)

def draw_box(width, height, color_code):
    # Top border
    print_colored('╔', color_code)
    for _ in range(width - 2):
        print_colored('═', color_code)
    print_colored('╗', color_code)
    print()

    # Middle
    for _ in range(height - 2):
        print_colored('║', color_code)
        for _ in range(width - 2):
            print(' ', end='')
        print_colored('║', color_code)
        print()

    # Bottom border
    print_colored('╚', color_code)
    for _ in range(width - 2):
        print_colored('═', color_code)
    print_colored('╝', color_code)
    print()

def main():
    # Clear screen
    print("\033c", end='')

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
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens."
    ]

    # Select a random quote
    quote = random.choice(quotes)

    # Calculate box dimensions
    lines = quote.split('\n')
    max_line_length = max(len(line) for line in lines)
    box_width = max_line_length + 4
    box_height = len(lines) + 4

    # Draw the box with a fun animation
    colors = [31, 33, 32, 36, 34, 35]  # Red, Yellow, Green, Cyan, Blue, Magenta
    for _ in range(3):
        for color in colors:
            draw_box(box_width, box_height, color)
            time.sleep(0.1)
            print("\033[H", end='')  # Move cursor to top-left

    # Final box
    draw_box(box_width, box_height, 33)  # Yellow

    # Print the quote with typewriter effect
    print("\033[2A", end='')  # Move cursor up 2 lines
    print("\033[2C", end='')  # Move cursor right 2 columns

    for line in lines:
        print("\033[2C", end='')  # Move cursor right 2 columns
        typewriter_effect(line, 33)  # Yellow text
        print()
        time.sleep(0.2)

    # Add a little signature
    print("\033[2C", end='')  # Move cursor right 2 columns
    typewriter_effect("— Woody Allen (probably)", 35)  # Magenta text
    print()

    # Add some blinking stars for fun
    for _ in range(5):
        print("\033[1A", end='')  # Move cursor up 1 line
        print("\033[2C", end='')  # Move cursor right 2 columns
        print_colored('✶', random.choice([31, 32, 33, 34, 35, 36]))  # Random color star
        time.sleep(0.3)

if __name__ == "__main__":
    main()