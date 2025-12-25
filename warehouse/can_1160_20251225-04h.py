"""
Campbell's Soup Can #1160
Produced: 2025-12-25 04:07:14
Worker: Venice: Uncensored (free) (cognitivecomputations/dolphin-mistral-24b-venice-edition:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'

# ASCII art border
border = f"{YELLOW}={CYAN}=" * 40 + f" {YELLOW}={CYAN}={ENDC}"

# Woody Allen style quote
quote = (
    f"{RED}Life is a game of chess,\n"
    f"played by pawns, fucked by kings!\n"
    f"Everything's a tragedy or a joke,\n"
    f"the only question is: which one?{ENDC}"
)

# Function to print quote with animation
def print_quote():
    print(border)
    print()
    for line in quote.split('\n'):
        print(line)
        time.sleep(1)
    print()
    print(border)

# Run the quote print function
if __name__ == "__main__":
    print_quote()