"""
Campbell's Soup Can #137
Produced: 2025-11-08 10:32:47
Worker: Mistral: Mistral Small 3.2 24B (free) (mistralai/mistral-small-3.2-24b-instruct:free)
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
from itertools import cycle

# Define colors using ANSI escape codes
COLORS = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m',  # White
    '\033[30m',  # Black (for contrast)
]
RESET = '\033[0m'

# Define the quote
QUOTE = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

# Define ASCII art for a thought bubble
THOUGHT_BUBBLE = [
    "       _______________",
    "      /               \\",
    "     /                 \\",
    "    /                   \\",
    "   /                     \\",
    "  /                       \\",
    " /                         \\",
    "/                           \\",
    "-----------------------------",
    "|                           |",
    "|                           |",
    "|                           |",
    "|                           |",
    "|                           |",
    "-----------------------------"
]

# Function to print colored text
def print_colored(text, color):
    print(f"{color}{text}{RESET}")

# Function to print the thought bubble with the quote
def print_thought_bubble(quote):
    # Calculate the maximum width of the thought bubble
    max_width = max(len(line) for line in THOUGHT_BUBBLE)

    # Split the quote into lines that fit within the thought bubble
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= max_width - 4:  # Subtract 4 for padding
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(' '.join(current_line))

    # Print the thought bubble with the quote inside
    for i, line in enumerate(THOUGHT_BUBBLE):
        if i < len(lines):
            # Center the quote line within the thought bubble
            centered_line = lines[i].center(max_width - 2)
            print(f"{THOUGHT_BUBBLE[i][:2]}{centered_line}{THOUGHT_BUBBLE[i][-2:]}")
        else:
            print(THOUGHT_BUBBLE[i])

# Function to animate the thought bubble
def animate_thought_bubble():
    color_cycle = cycle(COLORS)
    for _ in range(5):  # Number of animation cycles
        for i, line in enumerate(THOUGHT_BUBBLE):
            if i == 0 or i == len(THOUGHT_BUBBLE) - 1:
                # Animate the top and bottom lines with different colors
                print_colored(line, next(color_cycle))
            else:
                print(line)
        time.sleep(0.5)
        sys.stdout.write("\033[F" * (len(THOUGHT_BUBBLE) + len(QUOTE.split('\n'))))  # Move cursor up

# Main function
def main():
    print("\n" * 3)  # Add some space at the top
    animate_thought_bubble()
    print_thought_bubble(QUOTE)
    print("\n" * 3)  # Add some space at the bottom

if __name__ == "__main__":
    main()