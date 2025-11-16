"""
Campbell's Soup Can #312
Produced: 2025-11-16 09:29:58
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
A quick, colors‑filled, little theatrical program that prints
one (deeply neurotic) Woody Allen‑style quote with a typewriter
effect.  No external libraries – just pure Python and ANSI escapes.
"""

import sys
import time
import itertools

# ANSI colour codes
RESET   = "\033[0m"
YELLOW  = "\033[33m"
CYAN    = "\033[36m"
MAGENTA = "\033[35m"
GREEN   = "\033[32m"
RED     = "\033[31m"

# Quote – Woody‑Allen, whole thing in one line.
QUOTE = (
    "I went to a cooking class to lose weight, "
    "but all I lost was my dignity and the left side "
    "of my soul, which is still sitting on a salad."
)

# ---------- Helper functions ----------
def typewriter(text, delay=0.04, colour=YELLOW):
    """Print a string one character at a time with a delay."""
    for ch in text:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after the text

def box(lines, border_colour=CYAN, text_colour=GREEN):
    """Print a decorative box around a list of text lines."""
    max_len = max(len(line) for line in lines)
    tl, tr, bl, br = '╭', '╮', '╰', '╯'
    h_line = '─' * (max_len + 2)

    sys.stdout.write(border_colour + tl + h_line + tr + RESET + '\n')
    for line in lines:
        sys.stdout.write(
            border_colour + '│' + RESET +
            ' ' + text_colour + line.ljust(max_len) + RESET +
            border_colour + ' │' + RESET + '\n'
        )
    sys.stdout.write(border_colour + bl + h_line + br + RESET + '\n')

def spinner_animation(iterations=30, delay=0.05):
    """A tiny spinner to simulate loading before the quote appears."""
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    sys.stdout.write(MAGENTA + "Preparing thoughts… " + RESET)
    sys.stdout.flush()
    for _ in range(iterations):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\b')
    print()  # Move to new line after animation

# ---------- Main program ----------
def main():
    spinner_animation(iterations=18, delay=0.08)

    # Split the quote into chunks for the box
    words = QUOTE.split()
    chunks = [' '.join(words[i:i+12]) for i in range(0, len(words), 12)]

    box(chunks, border_colour=RED, text_colour=YELLOW)

    # Dramatic reveal of the quote itself
    typewriter("And the moral?  "
               "I am terrified that I might be dead before the salad is over.", delay=0.05, colour=GREEN)

if __name__ == "__main__":
    main()