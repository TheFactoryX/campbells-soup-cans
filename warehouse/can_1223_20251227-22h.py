"""
Campbell's Soup Can #1223
Produced: 2025-12-27 22:34:14
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
    corner = '┌'
    corner2 = '┐'
    corner3 = '└'
    corner4 = '┘'

    print_colored(corner + horizontal + corner2, color_code)
    for _ in range(height - 2):
        print_colored(vertical + ' ' * (width - 2) + vertical, color_code)
    print_colored(corner3 + horizontal + corner4, color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where is it going to end?",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "My one regret in life is that I am not someone else.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I'm not a paranoid deranged millionaire. Do I sound like I'm a paranoid deranged millionaire?",
        "I don't believe in the after life, although I am bringing a change of underwear."
    ]

    selected_quote = random.choice(quotes)

    # ASCII art of Woody Allen (simplified)
    woody_art = r"""
          .-""""""-.
         /          \
        |            |
        |  O    O    |
        |    __      |
        |   /  \     |
        |  /    \    |
        \            /
         \          /
          '-......-'
    """

    # Print Woody Allen ASCII art with color
    print_colored(woody_art, "33")  # Yellow

    # Print a box around the quote
    box_width = max(len(line) for line in selected_quote.split('\n')) + 4
    box_height = 5
    draw_box(box_width, box_height, "36")  # Cyan

    # Print the quote with typewriter effect
    print_colored("  ", "36")
    typewriter_effect(selected_quote, 0.03)
    print_colored("  ", "36")

    # Print another box
    draw_box(box_width, box_height, "36")  # Cyan

    # Print a funny footer
    footer = "--- Woody Allen (probably)"
    print_colored(footer.center(box_width), "35")  # Magenta

if __name__ == "__main__":
    main()