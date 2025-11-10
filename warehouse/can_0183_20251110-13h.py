"""
Campbell's Soup Can #183
Produced: 2025-11-10 13:01:49
Worker: Mistral: Mistral Small 3.1 24B (free) (mistralai/mistral-small-3.1-24b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

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
    "        ______________________",
    "       /                      \\",
    "      /                        \\",
    "     /                          \\",
    "    /                            \\",
    "   /                              \\",
    "  /                                \\",
    " /                                  \\",
    "/________________________________\\",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|                              |",
    "|______________________________|"
]

# List of Woody Allen style quotes
quotes = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "More than any other time in history, mankind faces a crossroads. One path leads to despair and utter hopelessness. The other, to total extinction. Let us pray we have the wisdom to choose correctly.",
    "I don't want to live in a world that is linear.",
    "I'm always amazed that people take an interest in my work. I'm just a guy who's trying to figure out how to get through life without making a complete mess of it.",
    "The heart wants what it wants. Oh, the heart wants what it wants.",
    "I'm at two with nature.",
    "I don't want to achieve immortality through my work; I want to achieve it by not dying.",
    "I'm not afraid of death, but I'm very afraid of dying."
]

# Function to print the thought bubble with a quote
def print_thought_bubble(quote):
    quote_lines = quote.split()
    max_line_length = max(len(line) for line in quote_lines)
    padding = (38 - max_line_length) // 2

    for i, line in enumerate(quote_lines):
        thought_bubble[9 + i] = f"|{' ' * padding}{line}{' ' * (38 - len(line) - padding)}|"

    for line in thought_bubble:
        print(line)
        time.sleep(0.1)

# Function to print a colorful, animated quote
def print_animated_quote(quote):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for char in quote:
        color = random.choice(colors)
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# Main function
def main():
    quote = random.choice(quotes)
    print_animated_quote("Woody Allen says:")
    print_thought_bubble(quote)

if __name__ == "__main__":
    main()