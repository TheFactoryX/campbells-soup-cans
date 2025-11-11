"""
Campbell's Soup Can #196
Produced: 2025-11-11 03:52:58
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
    "\033[97m"   # White
]
RESET = "\033[0m"

# ASCII art for a thought bubble
THOUGHT_BUBBLE = [
    "       _____",
    "     /       \\",
    "    |         |",
    "    |  o    o  |",
    "    |    >     |",
    "    |   _____  |",
    "    \\_________/"
]

# Philosophical quote in Woody Allen's style
QUOTE = "I'm not afraid of dying, I just don't want to be around when it happens. After all, who wants to be the last one to leave the party?"

# Function to print colored text
def print_colored_text(text, color):
    print(f"{color}{text}{RESET}")

# Function to print the thought bubble
def print_thought_bubble():
    for line in THOUGHT_BUBBLE:
        print(line)

# Function to print the quote with animation
def print_animated_quote(quote):
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# Main function
def main():
    # Clear the screen
    print("\033[2J\033[H")

    # Print the thought bubble
    print_thought_bubble()

    # Print the quote with random colors
    for char in QUOTE:
        color = random.choice(COLORS)
        print_colored_text(char, color)
        time.sleep(0.1)

    # Print the thought bubble again
    print()
    print_thought_bubble()

if __name__ == "__main__":
    main()