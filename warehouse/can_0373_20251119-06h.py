"""
Campbell's Soup Can #373
Produced: 2025-11-19 06:45:28
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
import sys
import os

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print a colorful box with a quote
def print_quote(quote, color):
    clear_screen()
    lines = quote.split('\n')
    max_length = max(len(line) for line in lines)
    box = f"{color}╔{'═' * (max_length + 4)}╗{RESET}\n"
    for line in lines:
        box += f"{color}║ {' ' * 2}{line}{' ' * (max_length - len(line))} {' ' * 2}║{RESET}\n"
    box += f"{color}╚{'═' * (max_length + 4)}╝{RESET}"
    print(box)

# Animation function
def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Woody Allen style quote
quote = f"{RED}The meaning of life is to find your gift. The purpose of life is to give it away. But first, you have to find it, and that's the tricky part. Especially when you're as directionally challenged as I am.{RESET}"

# Main function
def main():
    clear_screen()
    animate_text("Welcome to the existential crisis simulator!\n", 0.05)
    time.sleep(1)
    print_quote(quote, CYAN)
    time.sleep(2)
    clear_screen()
    animate_text("Thanks for joining the existential fun!\n", 0.05)

if __name__ == "__main__":
    main()