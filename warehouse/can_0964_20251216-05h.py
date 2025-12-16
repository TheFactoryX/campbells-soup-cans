"""
Campbell's Soup Can #964
Produced: 2025-12-16 05:38:59
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

# Define ANSI color codes
COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m"
}

# Define ASCII art for a thought bubble
THOUGHT_BUBBLE = [
    "       _______________",
    "      /               \\",
    "     |   I'm not afraid  |",
    "     |    of death; I    |",
    "     |   just don't want  |",
    "     |  to be there when  |",
    "     |      it happens.  |",
    "      \\_______________/"
]

# Define the quote and its color
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."
COLOR = COLORS["YELLOW"]

# Function to print the thought bubble with the quote
def print_thought_bubble():
    for line in THOUGHT_BUBBLE:
        print(line)
    print(f"{COLOR}{QUOTE}{COLORS['RESET']}")

# Function to create a typing effect
def typing_effect(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to create a blinking effect
def blinking_effect(text, delay=0.5):
    for _ in itertools.cycle([text, ""]):
        print(f"\r{text}", end='', flush=True)
        time.sleep(delay)
        print(f"\r{' ' * len(text)}", end='', flush=True)
        time.sleep(delay)

# Main function to display the quote with effects
def main():
    # Typing effect for the quote
    typing_effect("Woody Allen once said:", delay=0.05)
    time.sleep(1)

    # Blinking effect for the quote
    blinking_effect("I'm not afraid of death; I just don't want to be there when it happens.", delay=0.5)
    time.sleep(1)

    # Print the thought bubble with the quote
    print_thought_bubble()

if __name__ == "__main__":
    main()