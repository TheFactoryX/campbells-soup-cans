"""
Campbell's Soup Can #1299
Produced: 2025-12-31 11:29:56
Worker: Mistral: Mistral Small 3.1 24B (free) (mistralai/mistral-small-3.1-24b-instruct:free)
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
RESET = "\033[0m"

# ASCII art for a philosophical thought bubble
thought_bubble = [
    "       ___________",
    "      /           \\",
    "     |             |",
    "     |    O        |",
    "     |   \\|/       |",
    "     |   ( )       |",
    "     |   / \\       |",
    "     |___________|",
    "      |         |",
    "      |         |",
    "      |         |",
    "      |_________|"
]

# List of Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The heart wants what it wants, but the brain wants a nap.",
    "I don't want to live in a world that is in love with itself.",
    "I'm at two with nature.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens.",
    "I'm not a pessimist, I'm a realist.",
    "I'm not afraid of death, I just don't want to be there when it happens."
]

# Function to print the thought bubble with a quote
def print_thought_bubble(quote):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for line in thought_bubble:
        print(f"{random.choice(colors)}{line}{RESET}")

    # Print the quote in the middle of the thought bubble
    quote_lines = quote.split()
    max_length = max(len(word) for word in quote_lines)
    padding = " " * ((max_length + 4) // 2)
    for word in quote_lines:
        print(f"{padding}{word}{padding}")
        padding = " " * (max_length - len(word) + 4)

    print("\n" + "-"*40 + "\n")

# Function to animate the thought bubble
def animate_thought_bubble(quote):
    for _ in range(3):
        print_thought_bubble(quote)
        time.sleep(1)
        sys.stdout.write("\033[H\033[J")  # Clear the screen

# Main function
def main():
    quote = random.choice(quotes)
    animate_thought_bubble(quote)

if __name__ == "__main__":
    main()