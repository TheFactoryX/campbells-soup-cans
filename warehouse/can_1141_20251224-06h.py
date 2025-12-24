"""
Campbell's Soup Can #1141
Produced: 2025-12-24 06:50:25
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

# ANSI color codes
RESET = '\033[0m'
COLORS = [
    '\033[31m',  # Red
    '\033[33m',  # Yellow
    '\033[32m',  # Green
    '\033[36m',  # Cyan
    '\033[35m',  # Magenta
    '\033[34m',  # Blue
    '\033[37m',  # White
]

# The Woody‑Allen‑style philosophical quote
QUOTE = (
    "I'm always telling myself the universe is fine; "
    "it's just that my sense of it is so messed up that "
    "even a cosmic joke feels like an existential crisis."
)

# Box dimensions
BOX_WIDTH = 78
TOP_BORDER = f'┌{"─" * BOX_WIDTH}┐'
BOTTOM_BORDER = f'└{"─" * BOX_WIDTH}┘'

def rainbow_print(text, delay=0.05):
    """Print text character by character in a looping rainbow of colors."""
    color_cycle = iter(COLORS)
    for ch in text:
        sys.stdout.write(next(color_cycle) + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after the whole text

def rainbow_words(words, delay=0.2):
    """Print words in rainbow colors with a brief pause between them."""
    color_cycle = iter(COLORS)
    for word in words:
        sys.stdout.write(next(color_cycle) + word + RESET + ' ')
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after all words

def print_boxed_text(indent=2):
    """Print the quote inside a colored ASCII box."""
    # Prepare the list of words for animated printing
    words = QUOTE.split()

    # Print top border
    print(TOP_BORDER)

    # Build the line with the quote, left and right borders
    # We'll wrap the quote to fit within BOX_WIDTH
    line = ''
    for w in words:
        if len(line) + len(w) + 1 > BOX_WIDTH:
            # Print current line and start a new one
            print(f'│{" " * indent}{line.ljust(BOX_WIDTH - indent)}│')
            line = w + ' '
        else:
            line += w + ' '

    # Print the final line
    if line:
        print(f'│{" " * indent}{line.ljust(BOX_WIDTH - indent)}│')

    # Print the bottom border
    print(BOTTOM_BORDER)
    print()  # Blank line for aesthetics

def animated_eye():
    """A tiny text animation: a blinking eye that looks like it is pondering."""
    eye_frames = [
        '\033[33m(o_O)\033[0m',
        '\033[33m(o_o)\033[0m',
        '\033[33m(o_O)\033[0m',
        '\033[33m(o_o)\033[0m',
        '\033[33m(¬_¬)\033[0m',
        '\033[33m(¬_¬)\033[0m',
    ]
    for frame in eye_frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.3)

def main():
    # Clear the screen for a dramatic start
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

    # Animated eye before the quote
    animated_eye()
    print()  # Move to new line after eye animation

    # Show the quote inside a box with rainbow animation
    print_boxed_text()

    # Print the rainbow quote slowly
    rainbow_words(QUOTE.split(), delay=0.18)

if __name__ == "__main__":
    main()