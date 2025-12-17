"""
Campbell's Soup Can #999
Produced: 2025-12-17 18:48:46
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

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's the exit?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I thank God that I'm only miserable.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "I think being funny is not anyone's first choice.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch."
    ]

    # Select a random quote
    quote = random.choice(quotes)

    # Colors
    colors = [31, 33, 32, 36, 34, 35]  # Red, Yellow, Green, Cyan, Blue, Magenta
    box_color = random.choice(colors)
    text_color = random.choice([c for c in colors if c != box_color])

    # Box dimensions
    width = max(len(line) for line in quote.split('\n')) + 4
    height = 5

    # Draw the box with typewriter effect for the quote
    draw_box(width, height, box_color)

    # Position cursor inside the box
    print(f"\033[{height//2}F", end='')  # Move up
    print(f"\033[2C", end='')           # Move right

    # Print the quote with typewriter effect
    typewriter_effect(quote, text_color)

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        print_colored("   ⋆", 33)
        time.sleep(0.5)
        print_colored("\b\b\b   ", 33)
        sys.stdout.flush()

    # Final thought
    time.sleep(1)
    print("\n\033[1m\033[3m(Now ponder this while eating a pastrami sandwich...)\033[0m")

if __name__ == "__main__":
    main()