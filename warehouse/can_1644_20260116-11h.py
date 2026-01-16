"""
Campbell's Soup Can #1644
Produced: 2026-01-16 11:32:25
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
    horizontal = "\033[" + str(color_code) + "m" + "─" * (width - 2) + "\033[0m"
    vertical = "\033[" + str(color_code) + "m│\033[0m"
    corner = "\033[" + str(color_code) + "m+\033[0m"

    print(corner + horizontal + corner)
    for _ in range(height - 2):
        print(vertical + " " * (width - 2) + vertical)
    print(corner + horizontal + corner)

def main():
    # Clear screen
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
        "I'm not a paranoid deranged millionaire. Goddammit, I'm a billionaire."
    ]

    selected_quote = random.choice(quotes)

    # Draw a fancy box
    box_width = 60
    box_height = 10
    draw_box(box_width, box_height, "33")  # Yellow box

    # Print the quote with typewriter effect and color
    print_colored("\n\n  Woody Allen's Thought of the Day:", "1;36")  # Bold cyan
    print_colored("  " + "─" * (len(selected_quote) + 4), "33")  # Yellow line

    # Center the quote
    quote_lines = selected_quote.split('\n')
    for line in quote_lines:
        padding = (box_width - len(line) - 4) // 2
        sys.stdout.write("  " + " " * padding)
        typewriter_effect(line, 0.03)

    print_colored("  " + "─" * (len(selected_quote) + 4), "33")  # Yellow line

    # Add a little animation
    print_colored("\n  [Press any key to contemplate existence...]", "2;37")  # Dim white
    time.sleep(1)
    print_colored("  [Or just press ENTER to exit.]", "2;37")  # Dim white

    # Wait for user input
    input()

if __name__ == "__main__":
    main()