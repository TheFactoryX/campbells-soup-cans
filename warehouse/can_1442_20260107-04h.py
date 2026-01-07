"""
Campbell's Soup Can #1442
Produced: 2026-01-07 04:10:09
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
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't know the question, but sex is definitely the answer.",
        "I'm not a paranoid deranged millionaire. Goddammit, I'm a billionaire!"
    ]

    # Select a random quote
    quote = random.choice(quotes)

    # Calculate box dimensions
    lines = quote.split('\n')
    max_line_length = max(len(line) for line in lines)
    box_width = max_line_length + 4
    box_height = len(lines) + 2

    # Draw the box with a fun color
    draw_box(box_width, box_height, "93")  # Yellow

    # Print the quote with typewriter effect
    for line in lines:
        # Center the line in the box
        padding = (box_width - len(line) - 2) // 2
        print_colored('│' + ' ' * padding, "93")
        typewriter_effect(line, "91")  # Red text
        print_colored(' ' * (padding + (box_width - len(line) - 2 - padding * 2)) + '│', "93")

    # Draw the bottom of the box again to complete it
    print_colored('└' + '─' * (box_width - 2) + '┘', "93")

    # Add a little animation
    time.sleep(1)
    print("\n\033[92mWoody Allen's Neurotic Wisdom Generator\033[0m")
    print("\033[94m(Press Ctrl+C to exit, or just sit and ponder your existence)\033[0m")

    # Blinking cursor effect
    try:
        while True:
            print_colored('▮', "95")
            time.sleep(0.5)
            print_colored('\b▯', "95")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n\033[91mExistence is futile. Goodbye.\033[0m")

if __name__ == "__main__":
    main()