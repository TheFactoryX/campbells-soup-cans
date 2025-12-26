"""
Campbell's Soup Can #1201
Produced: 2025-12-26 22:35:10
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
    "       __________",
    "      /          \\",
    "     /            \\",
    "    /              \\",
    "   /                \\",
    "  /                  \\",
    " /                    \\",
    "/____________________\\",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|                      |",
    "|______________________|"
]

# Woody Allen style quote
quote = "The heart wants what the heart wants, but the brain says, 'Are you sure about this?'"

# Function to print the thought bubble with the quote
def print_thought_bubble(quote):
    max_width = max(len(line) for line in thought_bubble)
    quote_lines = quote.split()
    quote_width = max(len(word) for word in quote_lines)

    # Calculate the starting position for the quote
    start_pos = (max_width - quote_width) // 2

    # Print the thought bubble
    for i, line in enumerate(thought_bubble):
        if i == 8:
            # Insert the quote into the thought bubble
            quote_line = ' '.join(quote_lines[:max_width])
            print(f"{line[:start_pos]}{CYAN}{quote_line}{RESET}{line[start_pos+len(quote_line):]}")
            quote_lines = quote_lines[max_width:]
        else:
            print(line)

    # Print the remaining quote lines if any
    for line in quote_lines:
        print(f"|{CYAN}{' ' * start_pos}{line}{' ' * (max_width - start_pos - len(line))}{RESET}|")

# Function to print a spinning loader
def spinning_loader():
    spinner = ['|', '/', '-', '\\']
    for _ in range(30):
        sys.stdout.write(f"\r{YELLOW}{random.choice(spinner)}{RESET} Loading wisdom...")
        sys.stdout.flush()
        time.sleep(0.1)

# Main function
def main():
    print(f"{RED}Welcome to the Woody Allen Philosophy Generator!{RESET}")
    print(f"{BLUE}Let's ponder the mysteries of life...{RESET}")
    spinning_loader()
    print("\n")
    print_thought_bubble(quote)

if __name__ == "__main__":
    main()