"""
Campbell's Soup Can #1792
Produced: 2026-01-23 09:44:38
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
    print()

def draw_box(width, height, color_code):
    horizontal = '─' * (width - 2)
    print_colored('┌' + horizontal + '┐', color_code)
    for _ in range(height - 2):
        print_colored('│' + ' ' * (width - 2) + '│', color_code)
    print_colored('└' + horizontal + '┘', color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is divided into the horrible and the miserable. That's the two categories.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't believe in an afterlife, although I am bringing a change of underwear.",
        "I'm not afraid of dying, I just don't want to be there when it happens."
    ]

    quote = random.choice(quotes)

    # Get terminal size
    try:
        import os
        terminal_width = os.get_terminal_size().columns
        terminal_height = os.get_terminal_size().lines
    except:
        terminal_width = 80
        terminal_height = 24

    # Center the box
    box_width = min(terminal_width - 4, 70)
    box_height = 7

    # Position cursor
    print(f"\033[{terminal_height//2 - box_height//2}H", end='')

    # Draw the box with random colors
    colors = [31, 32, 33, 34, 35, 36, 37]
    box_color = random.choice(colors)
    draw_box(box_width, box_height, box_color)

    # Position cursor inside the box
    print(f"\033[{terminal_height//2 - box_height//2 + 1}H", end='')
    print(f"\033[{terminal_width//2 - len(quote)//2}C", end='')

    # Typewriter effect for the quote
    typewriter_effect(quote, box_color + 1)

    # Add a blinking cursor effect
    for _ in range(3):
        time.sleep(0.5)
        print_colored(' ', box_color)
        sys.stdout.flush()
        time.sleep(0.5)
        print_colored('▮', box_color)
        sys.stdout.flush()

    # Final message
    print("\n\n")
    print_colored("  — Woody Allen (probably)\n", 33)
    print_colored("  (Press any key to exit...)\n", 34)

    # Wait for key press
    try:
        input()
    except:
        pass

if __name__ == "__main__":
    main()