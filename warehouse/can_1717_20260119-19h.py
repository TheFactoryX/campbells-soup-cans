"""
Campbell's Soup Can #1717
Produced: 2026-01-19 19:30:34
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
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, color_code):
    horizontal = '─' * (width - 2)
    vertical = '│'
    corner = '┌'
    print_color(corner + horizontal + '┐', color_code)
    for _ in range(height - 2):
        print_color(vertical + ' ' * (width - 2) + vertical, color_code)
    print_color('└' + horizontal + '┘', color_code)

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

    quote = random.choice(quotes)

    # Get terminal width
    terminal_width = 80  # Default if we can't get it
    try:
        terminal_width = int(sys.stdout.get_terminal_size().columns)
    except:
        pass

    # Box dimensions
    box_width = min(terminal_width, 70)
    box_height = 10

    # Center the box
    padding = (terminal_width - box_width) // 2
    print(' ' * padding, end='')

    # Draw the box with random color
    color_codes = [31, 32, 33, 34, 35, 36]  # Red, Green, Yellow, Blue, Magenta, Cyan
    box_color = random.choice(color_codes)
    draw_box(box_width, box_height, box_color)

    # Print the quote inside the box with typewriter effect
    for i in range(padding + 1):
        print(' ', end='')
    print_color('│', box_color, end=' ')
    typewriter_effect(quote, 0.03)
    for i in range(padding + 1):
        print(' ', end='')
    print_color('│', box_color)

    # Add some philosophical decoration
    time.sleep(1)
    print("\n" + " " * (padding + 3) + "✦  The universe is expanding... and so is my anxiety  ✦")
    print(" " * (padding + 5) + "~ Woody Allen (probably) ~")

    # Add a little animation
    for _ in range(3):
        time.sleep(0.5)
        print("\033[1A\033[K", end="")  # Move up and clear line
        print(" " * (padding + 3) + "✦  The universe is expanding... and so is my anxiety  ✦")
        time.sleep(0.5)
        print("\033[1A\033[K", end="")  # Move up and clear line
        print(" " * (padding + 3) + "✦  The universe is expanding... and so is my anxiety  ✦")

if __name__ == "__main__":
    main()