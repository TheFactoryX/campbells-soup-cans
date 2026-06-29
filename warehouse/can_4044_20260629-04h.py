"""
Campbell's Soup Can #4044
Produced: 2026-06-29 04:59:36
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def type_print(text, delay=0.03):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the whole string

def main():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "Eighty percent of success is showing up. The other twenty percent is just showing up again after you've been shown the door.",
        "Money is better than poverty, if only for financial reasons.",
        "I am thankful for laughter, except when milk comes out of my nose.",
        "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
    ]
    quote = random.choice(quotes)

    # ANSI colour codes
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    border_color = CYAN
    text_color = YELLOW

    # Build a coloured box around the quote
    interior_width = len(quote) + 2          # one space each side
    total_width = interior_width + 2         # add the two border chars
    top = f"{border_color}╔{'═' * interior_width}╗{RESET}"
    middle = f"{border_color}║ {text_color}{quote}{border_color} ║{RESET}"
    bottom = f"{border_color}╚{'═' * interior_width}╝{RESET}"

    # Animate the box appearance
    for line in (top, middle, bottom):
        type_print(line, delay=0.005)
        time.sleep(0.1)

    # A tiny Woody‑Allen‑style ASCII face
    face = [
        "   _____ ",
        "  /     \\",
        " | () () |",
        "  |   ^  |",
        "   | '-' |",
        "    \\___/",
    ]
    for line in face:
        print(MAGENTA + line + RESET)
        time.sleep(0.05)

if __name__ == "__main__":
    main()