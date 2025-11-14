"""
Campbell's Soup Can #277
Produced: 2025-11-14 18:43:46
Worker: Mistral: Mistral Small 3 (free) (mistralai/mistral-small-24b-instruct-2501:free)
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
import os

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

# ASCII art for a thought bubble
thought_bubble = [
    "       ____",
    "      /    \\",
    "     /      \\",
    "    /        \\",
    "   /          \\",
    "  /            \\",
    " /              \\",
    "/________________\\",
    "  \\______________/",
    "   \\             /",
    "    \\           /",
    "     \\_________/"
]

# Function to print the thought bubble with a quote
def print_thought_bubble(quote):
    os.system('clear')
    print(f"{CYAN}{''.join(thought_bubble)}{RESET}")
    print(f"{WHITE}  {quote}{RESET}")
    print(f"{CYAN}{''.join(thought_bubble)}{RESET}")

# Function to print the quote with a typewriter effect
def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Main function to display the quote
def main():
    quote = "I'm not afraid of dying. I just don't want to be there when it happens."
    print_thought_bubble(" " * 10)
    typewriter_effect(f"{RED}{quote}{RESET}")
    time.sleep(2)

    # Add some animation
    for _ in range(5):
        for color in [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]:
            print_thought_bubble(f"{color}{quote}{RESET}")
            time.sleep(0.5)

    print_thought_bubble(" " * 10)
    typewriter_effect(f"{YELLOW}Thanks for reading!{RESET}")
    time.sleep(1)

if __name__ == "__main__":
    main()