"""
Campbell's Soup Can #806
Produced: 2025-12-08 23:31:02
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

# ANSI escape codes for colors
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
    "\033[0m"    # Reset
]

# ASCII art for a thought bubble
THOUGHT_BUBBLE = [
    "       ______________",
    "      /              \\",
    "     |                |",
    "     |   I'm not      |",
    "     |  afraid of     |",
    "     |  death; I just |",
    "     |  don't want to |",
    "     |  be there when |",
    "     |  it happens.   |",
    "     \\______________/"
]

# Function to print colored text
def print_colored(text, color):
    print(f"{color}{text}\033[0m")

# Function to print the thought bubble with animation
def print_thought_bubble():
    for line in THOUGHT_BUBBLE:
        print_colored(line, random.choice(COLORS))
        time.sleep(0.1)

# Function to print the quote with animation
def print_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    for char in quote:
        print_colored(char, random.choice(COLORS))
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# Main function to run the animation
def main():
    print_colored("Woody Allen's Wisdom:\n", "\033[93m")
    print_thought_bubble()
    print_quote()

if __name__ == "__main__":
    main()