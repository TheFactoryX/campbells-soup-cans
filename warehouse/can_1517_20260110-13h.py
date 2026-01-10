"""
Campbell's Soup Can #1517
Produced: 2026-01-10 13:00:05
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
    print(f"\033[{color_code}m{text}\033[0m", end='')

def typewriter_effect(text, color_code, delay=0.05):
    for char in text:
        print_color(char, color_code)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, color_code):
    # Top border
    print_color('╔', color_code)
    for _ in range(width - 2):
        print_color('═', color_code)
    print_color('╗', color_code)
    print()

    # Middle
    for _ in range(height - 2):
        print_color('║', color_code)
        for _ in range(width - 2):
            print_color(' ', color_code)
        print_color('║', color_code)
        print()

    # Bottom border
    print_color('╚', color_code)
    for _ in range(width - 2):
        print_color('═', color_code)
    print_color('╝', color_code)
    print()

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where does one spend it?",
        "I don't believe in the afterlife, although I am bringing a change of underwear.",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "My one regret in life is that I am not someone else.",
        "I don't want to achieve immortality through my work... I want to achieve it by not dying.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I thank God I'm only miserable.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have."
    ]

    # Randomly select a quote
    quote = random.choice(quotes)

    # Get terminal size (approximate)
    width = 60
    height = 10

    # Draw a fancy box
    draw_box(width, height, "93")  # Yellow

    # Position cursor inside the box
    print("\033[2A")  # Move up 2 lines
    print("\033[2C")  # Move right 2 columns

    # Print the quote with typewriter effect
    typewriter_effect("  Woody Allen once said:", "93")  # Yellow
    time.sleep(0.5)
    print("\033[1B")  # Move down 1 line
    print("\033[2C")  # Move right 2 columns
    typewriter_effect(f'  "{quote}"', "96")  # Cyan

    # Add some blinking stars for fun
    time.sleep(1)
    print("\033[3B")  # Move down 3 lines
    print("\033[2C")  # Move right 2 columns
    stars = ["✦", "✧", "✦", "✧", "✦"]
    for star in stars:
        print_color(star, "95")  # Magenta
        time.sleep(0.3)
        print_color(" ", "95")
        time.sleep(0.2)

    # Final message
    print("\033[2B")  # Move down 2 lines
    print("\033[2C")  # Move right 2 columns
    typewriter_effect("  (Now ponder this while eating a pastrami sandwich...)", "92")  # Green

if __name__ == "__main__":
    main()