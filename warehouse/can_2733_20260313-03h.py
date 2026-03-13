"""
Campbell's Soup Can #2733
Produced: 2026-03-13 03:08:30
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

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

def typewriter(text, delay=0.03):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def print_boxed_quote(quote):
    """Print the quote inside a colorful box with a little Woody‑Allen‑style face."""
    # Simple neurotic face (Woody Allen vibe)
    face = [
        "  _______  ",
        " /       \\ ",
        "|  o   o  |",
        "|    ^    |",
        "|  '-'   |",
        " \\_______/ "
    ]

    # Choose a random color for the face each run
    face_color = random.choice([RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN])
    # Quote text color
    quote_color = YELLOW

    # Determine box width based on longest line (face or quote)
    lines = [quote]
    max_len = max(len(line) for line in lines + face)
    width = max_len + 4  # padding    # Top border
    sys.stdout.write(CYAN + BOLD + "╔" + "═" * width + "╗" + RESET + "\n")
    # Optional: print the face above the quote
    for f_line in face:
        sys.stdout.write(CYAN + BOLD + "║ " + RESET)
        sys.stdout.write(face_color + f_line.ljust(width) + RESET)
        sys.stdout.write(CYAN + BOLD + " ║" + RESET + "\n")
    # Quote line(s) – we keep it a single line but wrap if needed
    for q_line in lines:
        sys.stdout.write(CYAN + BOLD + "║ " + RESET)
        sys.stdout.write(quote_color + q_line.ljust(width) + RESET)
        sys.stdout.write(CYAN + BOLD + " ║" + RESET + "\n")
    # Bottom border
    sys.stdout.write(CYAN + BOLD + "╚" + "═" * width + "╝" + RESET + "\n")

def main():
    # Original Woody Allen‑style quote (neurotic, funny, self‑deprecating)
    quote = (
        "I'm not afraid of dying; I just don't want to be there "
        "when it happens… preferably with a good snack."
    )
    # Animate the quote appearance
    typewriter("\n", 0.1)  # small leading newline
    print_boxed_quote(quote)
    # A tiny extra flourish
    time.sleep(0.5)
    sys.stdout.write(MAGENTA + "\n*Cue nervous laughter and a sigh*\n" + RESET)

if __name__ == "__main__":
    main()