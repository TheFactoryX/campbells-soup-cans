"""
Campbell's Soup Can #256
Produced: 2025-11-13 19:26:09
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

"""
A playful, colored, animated Woody‑Allen‑style philosophical quote.
Run directly to see the effect in your terminal.
"""

import sys
import time

# ANSI colors and attributes
BOLD      = '\033[1m'
CYAN      = '\033[36m'
YELLOW    = '\033[33m'
GREEN     = '\033[32m'
RESET     = '\033[0m'

def clear_screen():
    """Clear terminal screen (ANSI)."""
    sys.stdout.write('\033[H\033[J')
    sys.stdout.flush()

def type_out(text, delay=0.03, color=YELLOW):
    """Print text character‑by‑character with a delay."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def make_box(message):
    """Return top, middle and bottom lines of a simple ASCII box."""
    inner = message
    width = len(inner)
    top    = '╔' + '═' * width + '╗'
    middle = '║' + inner + '║'
    bottom = '╚' + '═' * width + '╝'
    return top, middle, bottom

def main():
    clear_screen()

    # The funny Woody Allen‑style quote
    quote = (
        "\"I think I'm only here because I'm a "
        "recurring character in the absurd drama "
        "of my own incompetence—and that's the great "
        "philosophical joke.\""
    )

    # Build the box
    top, middle, bottom = make_box(quote)

    # Slightly slower typing for the quote, faster for the borders
    for line in (top, bottom):
        type_out(line, delay=0.06, color=CYAN)
    type_out(middle, delay=0.02, color=GREEN)

    # Light pause before exiting
    time.sleep(0.8)

if __name__ == "__main__":
    main()