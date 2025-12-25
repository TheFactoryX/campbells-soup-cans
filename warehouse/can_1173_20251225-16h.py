"""
Campbell's Soup Can #1173
Produced: 2025-12-25 16:42:11
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
    "       ______________",
    "      /              \\",
    "     |                |",
    "     |   I'm not      |",
    "     |   afraid of    |",
    "     |   death; I     |",
    "     |   just don't   |",
    "     |   want to be   |",
    "     |   there when   |",
    "     |   it happens.  |",
    "     |                |",
    "      \\______________/"
]

# Function to print colored text
def print_colored(text, color):
    print(f"{color}{text}{RESET}")

# Function to animate the thought bubble
def animate_thought_bubble():
    for line in THOUGHT_BUBBLE:
        print(line)
        time.sleep(0.1)

# Main function to display the quote
def main():
    # Randomly select a color
    color = random.choice(COLORS)

    # Print the quote with animation
    print_colored("Woody Allen's Philosophical Quote:", color)
    animate_thought_bubble()

    # Randomly cycle through colors for the quote
    for char in itertools.cycle(COLORS):
        print_colored("\n\n" + " ".join(THOUGHT_BUBBLE[3:8]), char)
        time.sleep(0.5)

if __name__ == "__main__":
    main()