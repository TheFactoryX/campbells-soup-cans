"""
Campbell's Soup Can #235
Produced: 2025-11-12 20:34:20
Worker: Mistral: Mistral Small 3.2 24B (free) (mistralai/mistral-small-3.2-24b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# Define colors using ANSI escape codes
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

# Define a list of Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "A relationship, I think, is like a shark. You know? It has to constantly move forward or it dies.",
    "I don't want to live in a world where I'm the only human being. But I don't want to live in a world without me either.",
    "I'm at two with nature. I don't trust it.",
    "I don't believe in an afterlife, so I don't have to spend my whole life worried about getting into heaven.",
    "I'm always surprised when I find myself not dead."
]

# Function to print a colored box with a quote
def print_colored_box(quote, color):
    # Calculate the width of the box
    width = max(len(line) for line in quote.split('\n')) + 4
    # Print the top border
    print(color + '+' + '-' * width + '+')
    # Print each line of the quote centered
    for line in quote.split('\n'):
        print(color + '| ' + line.center(width - 4) + ' |')
    # Print the bottom border
    print(color + '+' + '-' * width + '+' + Colors.RESET)

# Function to animate the quote
def animate_quote(quote):
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Main function
def main():
    # Choose a random quote
    quote = random.choice(quotes)
    # Choose a random color
    colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN, Colors.WHITE]
    color = random.choice(colors)

    # Print the title
    print(Colors.MAGENTA + "Woody Allen's Philosophical Wisdom" + Colors.RESET)
    print()

    # Print the ASCII art of Woody Allen
    woody_art = r"""
          _____
         /     \
        | O   O |
        |   ∆   |
         \  ___ /
          \     /
           \___/
    """
    print(Colors.BLUE + woody_art + Colors.RESET)
    print()

    # Print the quote in a colored box
    print_colored_box(quote, color)

    # Animate the quote
    print("\n" + Colors.YELLOW + "Animating the quote..." + Colors.RESET)
    animate_quote(quote)

if __name__ == "__main__":
    main()