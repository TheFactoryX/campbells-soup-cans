"""
Campbell's Soup Can #622
Produced: 2025-11-30 12:56:02
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

# Define colors using ANSI escape codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Define the quote
quote = [
    "I've been on a diet for two weeks and all I've lost is fourteen days.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "More than any time in history, mankind faces a crossroads. One path leads to despair and utter hopelessness. The other, to total extinction. Let us pray we have the wisdom to choose correctly."
]

# Choose a random quote
selected_quote = random.choice(quote)

# Define the box frame
frame = [
    "+-----------------------------------------------------+",
    "|                                                         |",
    "|                                                         |",
    "|                                                         |",
    "|                                                         |",
    "|                                                         |",
    "+-----------------------------------------------------+"
]

# Define the colors for the quote
colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]

# Function to print the quote with animation
def print_quote_with_animation(quote, colors):
    for char in quote:
        color = random.choice(colors)
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)

# Function to print the frame
def print_frame(frame):
    for line in frame:
        print(line)

# Main function to display the quote
def main():
    print_frame(frame)
    print("| " + " " * 56 + " |")
    print("| " + " " * 20 + "W O O D Y   A L L E N" + " " * 20 + " |")
    print("| " + " " * 56 + " |")
    print("| " + " " * 56 + " |")
    print("| " + " " * 56 + " |")
    print("| " + " " * 56 + " |")
    print("| " + " " * 20 + selected_quote.center(36) + " " * 20 + " |")
    print("| " + " " * 56 + " |")
    print("| " + " " * 56 + " |")
    print("| " + " " * 56 + " |")
    print_frame(frame)

    # Print the quote with animation
    print("\n" + " " * 20 + "W O O D Y   A L L E N" + " " * 20)
    print_quote_with_animation(selected_quote, colors)

# Run the main function
if __name__ == "__main__":
    main()