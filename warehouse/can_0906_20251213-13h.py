"""
Campbell's Soup Can #906
Produced: 2025-12-13 13:37:28
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
    # Top border
    print_colored('╔' + '═' * (width - 2) + '╗', color_code)
    # Middle
    for _ in range(height - 2):
        print_colored('║' + ' ' * (width - 2) + '║', color_code)
    # Bottom border
    print_colored('╚' + '═' * (width - 2) + '╝', color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quotes
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

    # Get terminal width (approximate)
    try:
        terminal_width = int(sys.stdout.get_terminal_size().columns)
    except:
        terminal_width = 80

    # Box dimensions
    box_width = min(terminal_width - 4, 70)
    box_height = 7

    # Center the box
    padding = (terminal_width - box_width) // 2
    print(' ' * padding, end='')

    # Draw the box with random colors
    colors = [31, 32, 33, 34, 35, 36]  # Red, Green, Yellow, Blue, Magenta, Cyan
    box_color = random.choice(colors)
    draw_box(box_width, box_height, box_color)

    # Position cursor inside the box for the quote
    print(f"\033[{box_height//2 + 1}F", end='')  # Move up to the middle of the box
    print(' ' * (padding + 2), end='')  # Move to inside the box

    # Print the quote with typewriter effect
    quote_color = random.choice(colors)
    typewriter_effect(quote, quote_color, 0.03)

    # Print author with different color
    print(' ' * (padding + 2), end='')
    author_color = random.choice(colors)
    typewriter_effect("— Woody Allen (probably)", author_color, 0.05)

    # Add some blinking stars for fun
    print('\n')
    for _ in range(3):
        print(' ' * (terminal_width // 2 - 5), end='')
        print_colored("✨", random.choice(colors))
        time.sleep(0.5)

if __name__ == "__main__":
    main()