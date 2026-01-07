"""
Campbell's Soup Can #1456
Produced: 2026-01-07 17:42:55
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
    "\033[97m",  # White
    "\033[0m"    # Reset
]

# ASCII art for a thought bubble
THOUGHT_BUBBLE = [
    "       _______",
    "      /       \\",
    "     /         \\",
    "    /           \\",
    "   /             \\",
    "  /               \\",
    " /                 \\",
    "/_________________\\",
    "|                  |",
    "|                  |",
    "|                  |",
    "|                  |",
    "|                  |",
    "|                  |",
    "|                  |",
    "|                  |",
    "|__________________|"
]

# Quote to display
QUOTE = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

# Function to print the thought bubble with the quote
def print_thought_bubble(quote):
    lines = THOUGHT_BUBBLE.copy()
    quote_lines = quote.split()
    max_width = max(len(line) for line in lines)
    quote_index = 0

    for i in range(len(lines)):
        if i == 7:
            lines[i] = lines[i][:max_width//2] + ' '.join(quote_lines[quote_index:quote_index+3]) + lines[i][max_width//2:]
            quote_index += 3
        elif i == 8:
            lines[i] = lines[i][:max_width//2] + ' '.join(quote_lines[quote_index:quote_index+3]) + lines[i][max_width//2:]
            quote_index += 3
        elif i == 9:
            lines[i] = lines[i][:max_width//2] + ' '.join(quote_lines[quote_index:quote_index+3]) + lines[i][max_width//2:]
            quote_index += 3
        elif i == 10:
            lines[i] = lines[i][:max_width//2] + ' '.join(quote_lines[quote_index:quote_index+3]) + lines[i][max_width//2:]
            quote_index += 3
        print(''.join(lines[i]))

# Function to animate the thought bubble
def animate_thought_bubble():
    color_cycle = itertools.cycle(COLORS)
    for _ in range(5):  # Number of times to cycle through colors
        for line in THOUGHT_BUBBLE:
            print(next(color_cycle) + line + COLORS[-1])
        time.sleep(0.5)
        print("\033[H\033[J", end="")  # Clear the screen

# Main function
def main():
    animate_thought_bubble()
    print_thought_bubble(QUOTE)

if __name__ == "__main__":
    main()