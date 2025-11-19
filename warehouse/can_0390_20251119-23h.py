"""
Campbell's Soup Can #390
Produced: 2025-11-19 23:29:39
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
    "|  _____  |",
    "| /     \\ |",
    "| |     | |",
    "| |     | |",
    "| |_____| |",
    "|         |",
    "\\_________/"
]

# Function to print the thought bubble with a quote
def print_thought_bubble(quote):
    max_length = max(len(line) for line in thought_bubble)
    quote_lines = quote.split('\n')
    for i, line in enumerate(thought_bubble):
        if i == 3:
            print(f"{line[:5]}{CYAN}{quote_lines[0].center(max_length - 10)}{RESET}{line[5:]}")
        elif i == 4:
            print(f"{line[:5]}{CYAN}{quote_lines[1].center(max_length - 10)}{RESET}{line[5:]}")
        elif i == 5:
            print(f"{line[:5]}{CYAN}{quote_lines[2].center(max_length - 10)}{RESET}{line[5:]}")
        else:
            print(line)

# Function to print a quote with a typing effect
def print_typing_effect(quote):
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Main function
def main():
    # Woody Allen style quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens."
        "\nI'm not afraid of life; I just don't want to be there when it's over."
        "\nI'm not afraid of love; I just don't want to be there when it's gone."
    )

    # Print the quote with a typing effect
    print_typing_effect(quote)

    # Print the thought bubble with the quote
    print_thought_bubble(quote)

    # Add some random colors to the quote
    colored_quote = ""
    for char in quote:
        color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE])
        colored_quote += f"{color}{char}{RESET}"

    # Print the colored quote
    print(colored_quote)

if __name__ == "__main__":
    main()