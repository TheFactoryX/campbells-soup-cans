"""
Campbell's Soup Can #1723
Produced: 2026-01-20 04:15:13
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
    vertical = '│'
    corners = ['┌', '┐', '└', '┘']

    print_colored(corners[0], color_code)
    print_colored(horizontal, color_code)
    print_colored(corners[1], color_code)

    for _ in range(height - 2):
        print_colored(vertical, color_code)
        print_colored(' ' * (width - 2), color_code)
        print_colored(vertical, color_code)

    print_colored(corners[2], color_code)
    print_colored(horizontal, color_code)
    print_colored(corners[3], color_code)

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

    quote = random.choice(quotes)

    # Get terminal size
    try:
        import os
        rows, columns = os.popen('stty size', 'r').read().split()
        width = int(columns)
        height = int(rows)
    except:
        width = 80
        height = 24

    # Draw a nice box
    box_width = min(width, 70)
    box_height = 7
    draw_box(box_width, box_height, "93")  # Yellow box

    # Position cursor inside the box
    print(f"\033[{box_height//2 + 1}A\033[2C", end='')

    # Print the quote with typewriter effect
    typewriter_effect("Woody Allen once said:", "96")  # Cyan
    print()
    print_colored("  ", "93")
    typewriter_effect(quote, "92")  # Green
    print()

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")
        print_colored("  ", "93")