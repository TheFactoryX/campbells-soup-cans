"""
Campbell's Soup Can #4555
Produced: 2026-08-12 18:07:14
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random

# ANSI color codes
COLORS = [
    '\033[31m',  # Red
    '\033[32m',  # Green
    '\033[33m',  # Yellow
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
    '\033[36m',  # Cyan
]
RESET = '\033[0m'

# The Woody‑Allen‑style quote
QUOTE = ("I think the only thing I can control is my existential dread, "
         "and even that is just a very elaborate joke.")

# Simple ASCII art of a coffee mug
COFFEE_MUG = [
    "   ( (",
    "    ) )",
    "  ........",
    "  |      |",
    "  |      |",
    "  |______|",
]

def typewriter(text, delay=0.05):
    """Print text with a typewriter effect, coloring each word randomly."""
    words = text.split()
    for word in words:
        color = random.choice(COLORS)
        for ch in word:
            sys.stdout.write(f"{color}{ch}{RESET}")
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_boxed_quote(quote):
    """Print the quote inside a simple ASCII box."""
    width = len(quote)
    top = '+' + '-' * width + '+'
    bottom = top
    empty = '|' + ' ' * width + '|'

    sys.stdout.write(top + '\n')
    sys.stdout.flush()
    time.sleep(0.1)

    # Empty line inside the box
    sys.stdout.write(empty + '\n')
    sys.stdout.flush()
    time.sleep(0.1)

    # Quote line with typewriter effect
    sys.stdout.write('|')
    sys.stdout.flush()
    typewriter(quote, delay=0.04)
    sys.stdout.write('|\n')
    sys.stdout.flush()
    time.sleep(0.1)

    sys.stdout.write(empty + '\n')
    sys.stdout.flush()
    time.sleep(0.1)

    sys.stdout.write(bottom + '\n')
    sys.stdout.flush()

def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

    # Print coffee mug
    for line in COFFEE_MUG:
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(0.1)

    # Empty line
    sys.stdout.write('\n')
    sys.stdout.flush()
    time.sleep(0.2)

    # Print the boxed quote
    print_boxed_quote(QUOTE)

    # Pause before exit
    time.sleep(1)

if __name__ == "__main__":
    main()