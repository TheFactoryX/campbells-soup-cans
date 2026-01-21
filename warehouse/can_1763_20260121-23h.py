"""
Campbell's Soup Can #1763
Produced: 2026-01-21 23:40:01
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
            print(' ', end='')
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
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "It's not that I'm afraid to die, I just don't want to be there when it happens.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I'm in the miserable category.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I'm not afraid of dying, I just don't want to be there when it happens."
    ]

    # Randomly select a quote
    quote = random.choice(quotes)

    # Get terminal size
    try:
        import os
        terminal_size = os.get_terminal_size()
        width = terminal_size.columns
        height = terminal_size.lines
    except:
        width = 80
        height = 24

    # Center the box
    box_width = min(width - 4, 70)
    box_height = 7

    # Draw the box with random colors
    colors = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]
    box_color = random.choice(colors)

    # Draw the box
    draw_box(box_width, box_height, box_color)

    # Print the quote with typewriter effect
    time.sleep(0.5)
    print("\033[1A" * (box_height - 2))  # Move cursor up

    # Center the quote
    lines = []
    words = quote.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= box_width - 4:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    if current_line:
        lines.append(current_line)

    # Print each line centered
    for i, line in enumerate(lines):
        print("\033[1A")  # Move cursor up
        print("\033[2K")  # Clear line
        padding = (box_width - len(line) - 2) // 2
        print_color('║' + ' ' * padding, box_color)
        typewriter_effect(line.strip(), random.choice(colors))
        print_color(' ' * (box_width - len(line) - padding - 2) + '║', box_color)
        time.sleep(0.2)

    # Print the bottom border again
    print_color('╚', box_color)
    for _ in range(box_width - 2):
        print_color('═', box_color)
    print_color('╝', box_color)
    print()

    # Add a little animation
    time.sleep(1)
    print("\n\033[33m   \   /")
    print("    .-.")
    print("  ( o o )")
    print("   |  🄽  |")
    print("   '-----'")
    print("   Woody Allen\033[0m")

if __name__ == "__main__":
    main()