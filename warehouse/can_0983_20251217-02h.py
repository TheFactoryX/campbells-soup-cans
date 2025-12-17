"""
Campbell's Soup Can #983
Produced: 2025-12-17 02:19:31
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

def typewriter_effect(text, color_code, delay=0.05):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, color_code):
    horizontal = "\033[{}m═\033[0m".format(color_code) * (width - 2)
    vertical = "\033[{}m║\033[0m".format(color_code)
    corner = "\033[{}m╔\033[0m".format(color_code)
    print(corner + horizontal + "\033[{}m╗\033[0m".format(color_code))
    for _ in range(height - 2):
        print(vertical + " " * (width - 2) + vertical)
    print("\033[{}m╚\033[0m".format(color_code) + horizontal + "\033[{}m╝\033[0m".format(color_code))

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's the exit?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I thank God that I am only miserable.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "I'm not afraid of death; I just don't want to be there when it happens."
    ]

    # Randomly select a quote
    quote = random.choice(quotes)

    # Get terminal width
    terminal_width = 80  # Default if we can't get it
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        pass

    # Box dimensions
    box_width = min(terminal_width, 70)
    box_height = 10

    # Draw the box with random colors
    colors = [31, 32, 33, 34, 35, 36]  # Red, Green, Yellow, Blue, Magenta, Cyan
    box_color = random.choice(colors)
    draw_box(box_width, box_height, box_color)

    # Position cursor inside the box
    print("\033[{}A".format(box_height - 2), end="")  # Move up
    print("\033[2C", end="")  # Move right

    # Print the quote with typewriter effect
    quote_color = random.choice(colors)
    typewriter_effect(quote.center(box_width - 4), quote_color)

    # Print author with different color
    author_color = random.choice(colors)
    print("\033[{}B".format(box_height - 4), end="")  # Move down
    print("\033[2C", end="")  # Move right
    typewriter_effect("— Woody Allen".center(box_width - 4), author_color, 0.03)

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        print("\033[{}A".format(box_height - 1), end="")  # Move up
        print("\033[2C", end="")  # Move right
        stars = " " * (box_width - 4)
        positions = random.sample(range(len(stars)), 5)
        for pos in positions:
            stars = stars[:pos] + "\033[5m*\033[0m" + stars[pos+1:]
        print(stars)
        time.sleep(0.5)

if __name__ == "__main__":
    import os
    main()