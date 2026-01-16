"""
Campbell's Soup Can #1640
Produced: 2026-01-16 07:37:25
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

def draw_box(width, height, color_code):
    horizontal = '─' * (width - 2)
    vertical = '│'
    corner = '┌' + horizontal + '┐'
    middle = vertical + ' ' * (width - 2) + vertical
    bottom = '└' + horizontal + '┘'

    print_colored(corner, color_code)
    for _ in range(height - 2):
        print_colored(middle, color_code)
    print_colored(bottom, color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Woody Allen style quote
    quotes = [
        "Eternity is a terrible thought. I mean, where's it going to end?",
        "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
        "I don't believe in the after life, although I am bringing a change of underwear.",
        "Life is divided into the horrible and the miserable. The horrible are the terminal cases, the blind, the crippled. I thank God that I'm only miserable.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "I'm very proud of my gold pocket watch. My grandfather, on his deathbed, sold me this watch.",
        "I'm not afraid of dying, I just don't want to be there when it happens.",
        "I don't believe in the after life, although I am bringing a change of underwear."
    ]

    selected_quote = random.choice(quotes)

    # Get terminal size
    try:
        import os
        terminal_width = os.get_terminal_size().columns
        terminal_height = os.get_terminal_size().lines
    except:
        terminal_width = 80
        terminal_height = 24

    # Calculate box dimensions
    box_width = min(terminal_width - 4, len(selected_quote) + 4)
    box_height = 7

    # Center the box
    print("\n" * (terminal_height // 2 - box_height // 2))

    # Draw the box with random colors
    colors = [31, 32, 33, 34, 35, 36, 37]
    box_color = random.choice(colors)
    draw_box(box_width, box_height, box_color)

    # Print the quote with typewriter effect
    print("\033[1A" * (box_height - 2))  # Move cursor up
    print("\033[1C" * 2)  # Move cursor right

    # Add some empty lines for the quote
    print("\033[1B" * (box_height // 2 - 1))

    # Print the quote with typewriter effect
    print_colored("   Woody Allen's Thought:", random.choice(colors))
    print_colored("   ", random.choice(colors))
    typewriter_effect(f"   \"{selected_quote}\"", 0.03)

    # Add a blinking cursor effect
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write("\033[?25h")  # Show cursor
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\033[?25l")  # Hide cursor
        sys.stdout.flush()

    # Print a little ASCII art
    print("\n" * 2)
    print_colored("        \\", random.choice(colors))
    print_colored("         \\", random.choice(colors))
    print_colored("          O", random.choice(colors))
    print_colored("         / \\", random.choice(colors))
    print_colored("        /   \\", random.choice(colors))
    print_colored("       /     \\", random.choice(colors))
    print_colored("      /       \\", random.choice(colors))
    print_colored("     /         \\", random.choice(colors))
    print_colored("    /           \\", random.choice(colors))
    print_colored("   /             \\", random.choice(colors))
    print_colored("  /               \\", random.choice(colors))
    print_colored(" /                 \\", random.choice(colors))
    print_colored("/                   \\", random.choice(colors))
    print_colored("|     WOODY         |", random.choice(colors))
    print_colored("\\                   /", random.choice(colors))
    print_colored(" \\                 /", random.choice(colors))
    print_colored("  \\               /", random.choice(colors))
    print_colored("   \\             /", random.choice(colors))
    print_colored("    \\           /", random.choice(colors))
    print_colored("     \\         /", random.choice(colors))
    print_colored("      \\       /", random.choice(colors))
    print_colored("       \\     /", random.choice(colors))
    print_colored("        \\   /", random.choice(colors))
    print_colored("         \\ /", random.choice(colors))
    print_colored("          V", random.choice(colors))

if __name__ == "__main__":
    main()