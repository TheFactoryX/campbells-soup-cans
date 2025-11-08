"""
Campbell's Soup Can #133
Produced: 2025-11-08 06:41:10
Worker: Mistral: Mistral Small 3 (free) (mistralai/mistral-small-24b-instruct-2501:free)
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

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ASCII art for a thought bubble
thought_bubble = [
    "  _______",
    " /       \\",
    "|         |",
    "|         |",
    "|         |",
    "|         |",
    " \\_______/"
]

# Function to print the thought bubble with a quote
def print_thought_bubble(quote):
    max_width = max(len(line) for line in thought_bubble)
    quote_lines = quote.split('\n')

    # Calculate the width of the quote
    quote_width = max(len(line) for line in quote_lines)

    # Center the quote within the thought bubble
    for i, line in enumerate(thought_bubble):
        if i == 2:
            print(f"{' ' * ((max_width - quote_width) // 2)}{quote_lines[0]}")
        elif i == 3:
            print(f"{' ' * ((max_width - quote_width) // 2)}{quote_lines[1]}")
        elif i == 4:
            print(f"{' ' * ((max_width - quote_width) // 2)}{quote_lines[2]}")
        else:
            print(line)

# Function to print the quote with animations
def print_quote_with_animation(quote):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    for char in quote:
        color = random.choice(colors)
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Main function
def main():
    quote = (
        "I'm not afraid of dying, I just don't want to be there when it happens.\n"
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "I'm not afraid of death; I just don't want to be there when it happens."
    )

    # Print the thought bubble with the quote
    print_thought_bubble(quote)

    # Print the quote with animations
    print_quote_with_animation(quote)

if __name__ == "__main__":
    main()