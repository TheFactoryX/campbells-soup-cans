"""
Campbell's Soup Can #377
Produced: 2025-11-19 10:38:44
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A single‑file, pure‑Python program that prints one Woody Allen‑style philosophical
quote with colorful ASCII framing and a gentle typing animation.
"""

import sys
import time

# ANSI colour codes
RESET = "\033[0m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"

# The (plain) quote to display – no colour codes inside
QUOTE_LINES = [
    "\"I keep looking for meaning like a librarian searching for a book on consciousness… "
    "but it turns out I'm just in the wrong part of the library.\"",
    "– Woody-ish"
]

# Calculate the width needed for the longest line
MAX_LEN = max(len(line) for line in QUOTE_LINES)

def type_text(text, delay: float = 0.04):
    """Print a string one character at a time with a short pause."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def print_animated_box(lines):
    """Print an animated quote inside a coloured ASCII box."""
    border = CYAN + '+' + '-' * (MAX_LEN + 2) + '+' + RESET
    print(border)
    for line in lines:
        # left border + opening space, set text colour
        sys.stdout.write(CYAN + '|' + RESET + YELLOW + ' ')
        type_text(line)
        # closing space + right border
        sys.stdout.write(YELLOW + ' ' + CYAN + '|' + RESET)
        print()
    print(border)

def show_intro():
    """A tiny, playful intro before the quote."""
    intro = f"{BOLD}Here’s a Woody‑inspired existential musings, displayed with theatrical flair:{RESET}"
    print(intro)
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.35)
    print('\n')

def main() -> None:
    show_intro()
    print_animated_box(QUOTE_LINES)

if __name__ == "__main__":
    main()