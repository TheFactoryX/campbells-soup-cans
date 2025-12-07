"""
Campbell's Soup Can #765
Produced: 2025-12-07 04:45:32
Worker: Mistral: Mistral Small 3.1 24B (free) (mistralai/mistral-small-3.1-24b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import itertools
import sys

# Define colors using ANSI escape codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "end": "\033[0m"
}

# Define ASCII art for a thought bubble
THOUGHT_BUBBLE = [
    "       ________________",
    "      /                \\",
    "     /                  \\",
    "    /                    \\",
    "   /                      \\",
    "  /                        \\",
    " /                          \\",
    "/__________________________\\",
    "|                          |",
    "|                          |",
    "|                          |",
    "|                          |",
    "|                          |",
    "|__________________________|"
]

# Define the philosophical quote
QUOTE = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

# Function to print the thought bubble with the quote
def print_thought_bubble(quote):
    lines = quote.split()
    bubble_lines = THOUGHT_BUBBLE[:]
    max_width = max(len(line) for line in bubble_lines)
    quote_lines = [lines[i:i + max_width] for i in range(0, len(lines), max_width)]

    for i, line in enumerate(quote_lines):
        formatted_line = ' '.join(line).ljust(max_width)
        bubble_lines[6 + i] = f"| {formatted_line} |"

    for line in bubble_lines:
        print(line)

# Function to print the quote with color animation
def print_animated_quote(quote):
    colors = list(COLORS.keys())[:-1]  # Exclude the "end" color
    random.shuffle(colors)
    color_cycle = itertools.cycle(colors)

    for char in quote:
        color = next(color_cycle)
        print(f"{COLORS[color]}{char}{COLORS['end']}", end='', flush=True)
        time.sleep(0.05)
    print()

# Main function to run the program
def main():
    print("\n" * 3)  # Add some space at the top
    print_thought_bubble(QUOTE)
    print("\n" * 2)  # Add some space before the animated quote
    print_animated_quote(QUOTE)

if __name__ == "__main__":
    main()