"""
Campbell's Soup Can #299
Produced: 2025-11-15 18:39:01
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

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# ASCII art for a thought bubble
thought_bubble = [
    "     ____",
    "    /    \\",
    "   |      |",
    "   |      |",
    "   |      |",
    "  /______\\",
    "|         |",
    "|         |",
    "|         |",
    "|         |",
    "|_________|"
]

# Woody Allen-style philosophical quote
quote = (
    "I've been told I have a lot of potential. "
    "Unfortunately, none of it is in the present tense."
)

# Function to print the thought bubble with the quote
def print_thought_bubble(quote):
    # Split the quote into lines to fit within the thought bubble
    lines = quote.split()
    bubble_lines = []
    current_line = ""

    for word in lines:
        if len(current_line) + len(word) + 1 <= 18:
            current_line += word + " "
        else:
            bubble_lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        bubble_lines.append(current_line.strip())

    # Print the thought bubble with the quote
    for i, line in enumerate(bubble_lines):
        print(f"{CYAN}{thought_bubble[i]}{RESET} {BLUE}{line.center(18)}{RESET}")

    # Print the remaining part of the thought bubble
    for i in range(len(bubble_lines), len(thought_bubble)):
        print(f"{CYAN}{thought_bubble[i]}{RESET}")

# Function to create a typing effect
def typing_effect(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Main function to display the quote with animations
def main():
    # Typing effect for the quote
    typing_effect(f"{YELLOW}Woody Allen once said...{RESET}")
    time.sleep(1)

    # Print the thought bubble with the quote
    print_thought_bubble(quote)

    # Typing effect for the end of the quote
    typing_effect(f"{YELLOW}...and that's just the tip of the existential iceberg.{RESET}")

# Run the main function
if __name__ == "__main__":
    main()