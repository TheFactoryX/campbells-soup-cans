"""
Campbell's Soup Can #1149
Produced: 2025-12-24 14:35:18
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
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ASCII art border
BORDER = f"{CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}"
BORDER_MID = f"{CYAN}║{RESET}"

# Function to print the quote with animation
def print_quote_animated(quote):
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# Function to print the quote with color
def print_quote_colored(quote):
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for char in quote:
        color = random.choice(colors)
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(0.05)

# Woody Allen style quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Print the border
print(BORDER)
print(BORDER_MID + " " * 20 + "A Woody Allen Moment" + " " * 20 + BORDER_MID)
print(BORDER)

# Print the quote with animation and color
print_quote_colored(f"{BORDER_MID} {quote.center(60)}{BORDER_MID}")
print(BORDER)