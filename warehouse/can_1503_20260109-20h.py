"""
Campbell's Soup Can #1503
Produced: 2026-01-09 20:38:17
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

    # Funny philosophical quote in Woody Allen style
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't want to achieve immortality through my work... I want to achieve it by not dying.",
        "I'm not afraid of dying, I just don't want to be there when it happens."
    ]

    selected_quote = random.choice(quotes)

    # Draw a fancy box
    box_width = max(len(line) for line in selected_quote.split('\n')) + 4
    box_height = 5
    draw_box(box_width, box_height)

    # Move cursor up to the middle of the box
    for _ in range(box_height - 2):
        sys.stdout.write("\033[1A")

    # Print the quote with typewriter effect and color
    print_colored('║', '93')
    sys.stdout.write(" \033[96m")  # Cyan color
    typewriter_effect(selected_quote)
    sys.stdout.write("\033[0m")
    print_colored('║', '93')

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        print_colored("   ⭐   ", '93')
        time.sleep(0.5)
        sys.stdout.write("\033[1A\033[2K")  # Move up and clear line

    # Final message
    print_colored("\n\033[95m— Woody Allen (probably)\033[0m", '95')

if __name__ == "__main__":
    main()