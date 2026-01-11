"""
Campbell's Soup Can #1531
Produced: 2026-01-11 05:41:25
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
    print_color(corners[0] + horizontal * (width - 2) + corners[1], '93')

    # Middle content
    for _ in range(height - 2):
        print_color(vertical + ' ' * (width - 2) + vertical, '93')

    # Bottom border
    print_color(corners[2] + horizontal * (width - 2) + corners[3], '93')

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
        "I'm very thankful I was born. It's the second best thing that ever happened to me.",
        "I'm not afraid of dying, I just don't want to be there when it happens.",
        "I don't believe in the after life, although I am bringing a change of underwear."
    ]

    selected_quote = random.choice(quotes)

    # Calculate box dimensions based on quote length
    max_line_length = max(len(line) for line in selected_quote.split('\n')) + 4
    box_height = 7

    # Center the box
    terminal_width = 80  # Default assumption
    try:
        terminal_width = int(sys.stdout.get_terminal_size().columns)
    except:
        pass

    left_margin = max(0, (terminal_width - max_line_length) // 2)

    # Print the box with quote
    print(' ' * left_margin, end='')
    draw_box(max_line_length, box_height)

    # Move cursor up to write inside the box
    for i in range(box_height - 2):
        sys.stdout.write("\033[1A")  # Move cursor up
        sys.stdout.write("\033[2K")  # Clear line

    # Print the quote with typewriter effect
    print(' ' * left_margin + '\033[93m║\033[0m', end='')
    print(' ' * 2, end='')
    typewriter_effect('\033[91m' + selected_quote + '\033[0m', 0.03)
    print(' ' * left_margin + '\033[93m║\033[0m')

    # Add some blinking stars for fun
    for _ in range(3):
        time.sleep(0.5)
        print('\033[1A\033[2K' + ' ' * left_margin + '\033[93m║\033[0m' + ' ' * 2 + '\033[91m' + selected_quote + ' \033[93m✨\033[0m', end='')
        time.sleep(0.5)
        print('\033[1A\033[2K' + ' ' * left_margin + '\033[93m║\033[0m' + ' ' * 2 + '\033[91m' + selected_quote + '\033[0m', end='')

    print()
    print(' ' * left_margin + '\033[93m║\033[0m')

    # Add a funny footer
    time.sleep(1)
    print()
    print_color("   — Woody Allen (probably)", '90')
    print_color("   (or someone equally neurotic)", '90')
    print()
    typewriter_effect("\033[92mRemember: The universe is expanding, and so is your waistline.\033[0m", 0.02)

if __name__ == "__main__":
    main()