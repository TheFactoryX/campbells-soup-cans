"""
Campbell's Soup Can #1114
Produced: 2025-12-22 23:31:34
Worker: Mistral: Mistral 7B Instruct (free) (mistralai/mistral-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
from itertools import cycle

# ANSI color codes
COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
    "\033[30m",  # Black (for contrast)
]

RESET = "\033[0m"

def color_cycle(text):
    """Cycle through colors for each character in the text."""
    colored_text = ""
    for i, char in enumerate(text):
        color = COLORS[i % len(COLORS)]
        colored_text += f"{color}{char}{RESET}"
    return colored_text

def print_woody_quote():
    """Print a Woody Allen-style quote with color cycling."""
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The heart's memory eliminates the bad and magnifies the good, and thanks to this artifice we're able to endure the burdens of the past.",
        "If it turns out that there is a God, I don't think he's evil. But the worst that you can say about him is that basically he's an underachiever.",
    ]

    quote = random.choice(quotes)
    colored_quote = color_cycle(quote)

    print("\n" + "=" * 50)
    print(" " * 15 + "WOODY ALLEN'S WISDOM" + " " * 15)
    print("=" * 50)

    # Print the quote with a typewriter effect
    for char in colored_quote:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n" + "=" * 50 + "\n")

def main():
    print_woody_quote()

if __name__ == "__main__":
    main()