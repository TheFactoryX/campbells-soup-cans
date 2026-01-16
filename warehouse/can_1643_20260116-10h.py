"""
Campbell's Soup Can #1643
Produced: 2026-01-16 10:43:26
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
    corners = ['╔', '╗', '╚', '╝']
    horizontal = '═'
    vertical = '║'

    # Top border
    print_colored(corners[0] + horizontal * (width - 2) + corners[1], '93')

    # Middle content
    for _ in range(height - 2):
        print_colored(vertical + ' ' * (width - 2) + vertical, '93')

    # Bottom border
    print_colored(corners[2] + horizontal * (width - 2) + corners[3], '93')

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Box dimensions
    box_width = 60
    box_height = 10

    # Draw the box
    draw_box(box_width, box_height)

    # Move cursor up to the middle of the box
    for _ in range(box_height - 3):
        sys.stdout.write("\033[1A")  # Move cursor up one line

    # Center the cursor
    sys.stdout.write("\033[1C" * ((box_width // 2) - 10))

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's the exit?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I thank God I'm only miserable.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "I think being funny is not anyone's first choice.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch."
    ]

    selected_quote = random.choice(quotes)

    # Print the quote with typewriter effect and color
    print_colored("\033[1;33m", '93')  # Yellow
    typewriter_effect("  " + selected_quote + "  ")
    print_colored("\033[0m", '93')  # Reset

    # Move cursor down and print author
    sys.stdout.write("\033[1B" * 2)
    sys.stdout.write("\033[1C" * ((box_width // 2) - 5))
    print_colored("\033[1;36m- Woody Allen\033[0m", '96')

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write("\033[1A")  # Move up
        sys.stdout.write("\033[1C" * (box_width - 10))
        print_colored("✧", '95')
        sys.stdout.write("\033[1B")  # Move down
        time.sleep(0.5)
        sys.stdout.write("\033[1A")  # Move up
        sys.stdout.write("\033[1C" * (box_width - 10))
        print_colored(" ", '95')
        sys.stdout.write("\033[1B")  # Move down

if __name__ == "__main__":
    main()