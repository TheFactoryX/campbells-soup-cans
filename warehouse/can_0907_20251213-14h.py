"""
Campbell's Soup Can #907
Produced: 2025-12-13 14:32:54
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

def draw_box(width, height):
    top_bottom = '╔' + '═' * (width - 2) + '╗'
    middle = '║' + ' ' * (width - 2) + '║'
    print_colored(top_bottom, '93')  # Yellow
    for _ in range(height - 2):
        print_colored(middle, '93')
    print_colored('╚' + '═' * (width - 2) + '╝', '93')

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where is it going to end?",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "It's not that I'm afraid to die, I just don't want to be there when it happens.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I thank God that I am only miserable.",
        "I don't want to achieve immortality through my work... I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown."
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

    # Print the art with color
    print_colored(woody_art, '96')  # Cyan

    # Draw a box around the quote
    box_width = max(len(line) for line in selected_quote.split('\n')) + 4
    box_height = 5
    draw_box(box_width, box_height)

    # Print the quote with typewriter effect and color
    print_colored("    ", '93', end='')
    typewriter_effect(selected_quote, 0.03)
    print_colored("    ", '93')

    # Draw the bottom of the box
    print_colored('╚' + '═' * (box_width - 2) + '╝', '93')

    # Add a little animation
    for _ in range(3):
        time.sleep(0.5)
        print_colored("   ⌐■_■", '91')  # Red (nervous look)
        time.sleep(0.5)
        print_colored("   ⊙▂⊙", '92')  # Green (relieved look)

if __name__ == "__main__":
    main()