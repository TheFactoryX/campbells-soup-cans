"""
Campbell's Soup Can #1014
Produced: 2025-12-18 11:31:17
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
    top_bottom = '+' + '-' * (width - 2) + '+'
    middle = '|' + ' ' * (width - 2) + '|'
    print_colored(top_bottom, '93')  # Yellow
    for _ in range(height - 2):
        print_colored(middle, '93')  # Yellow
    print_colored(top_bottom, '93')  # Yellow

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
        "I'm not a hypochondriac; I'm an alarmist."
    ]

    selected_quote = random.choice(quotes)

    # Calculate box dimensions based on quote length
    quote_lines = selected_quote.split('\n')
    max_line_length = max(len(line) for line in quote_lines)
    box_width = max_line_length + 4
    box_height = len(quote_lines) + 4

    # Draw the box
    draw_box(box_width, box_height)

    # Print the quote with typewriter effect and colors
    print_colored("\n  \033[1mWoody Allen's Thought of the Day:\033[0m\n", '95')  # Purple

    colors = ['91', '92', '93', '94', '95', '96']  # Red, Green, Yellow, Blue, Purple, Cyan
    for line in quote_lines:
        color = random.choice(colors)
        print_colored("  ", '93')  # Yellow for indentation
        typewriter_effect(line, 0.03)
        time.sleep(0.1)

    # Draw the box again
    draw_box(box_width, box_height)

    # Add some animated dots for effect
    print_colored("\n  \033[1mContemplating...\033[0m", '95')  # Purple
    for _ in range(3):
        for i in range(4):
            sys.stdout.write('\033[95m.\033[0m')
            sys.stdout.flush()
            time.sleep(0.3)
        sys.stdout.write('\b\b\b\b    \b\b\b\b')
        sys.stdout.flush()
        time.sleep(0.3)

    print("\n")

if __name__ == "__main__":
    main()