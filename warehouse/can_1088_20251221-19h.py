"""
Campbell's Soup Can #1088
Produced: 2025-12-21 19:26:44
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
    corner = '┌'
    print_colored(corner + horizontal + '┐', color_code)
    for _ in range(height - 2):
        print_colored(vertical + ' ' * (width - 2) + vertical, color_code)
    print_colored('└' + horizontal + '┘', color_code)

def main():
    # Clear screen (works on most terminals)
    print("\033c", end="")

    # Box dimensions
    box_width = 60
    box_height = 10

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
        "I'm not a paranoid deranged millionaire. Goddammit, I'm a billionaire."
    ]

    # Select a random quote
    quote = random.choice(quotes)

    # Draw the box with random color
    colors = [31, 32, 33, 34, 35, 36]  # Red, Green, Yellow, Blue, Magenta, Cyan
    box_color = random.choice(colors)
    draw_box(box_width, box_height, box_color)

    # Position cursor inside the box
    print(f"\033[{box_height//2}F", end="")  # Move up half the box height
    print(f"\033[2C", end="")  # Move right 2 columns

    # Print the quote with typewriter effect and different color
    text_color = random.choice([c for c in colors if c != box_color])
    print_colored("Woody Allen's Thought:", text_color)
    print_colored(" ", text_color)  # Empty line
    typewriter_effect(quote, 0.03)

    # Add a blinking cursor effect
    for _ in range(5):
        print_colored(" █", text_color, end="")
        time.sleep(0.3)
        print_colored("\b\b", text_color, end="")
        time.sleep(0.3)

    # Final message
    print_colored("\n\n", text_color)
    print_colored("  (Press any key to exit the existential crisis)", text_color)
    input()  # Wait for user input

if __name__ == "__main__":
    main()