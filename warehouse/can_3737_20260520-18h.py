"""
Campbell's Soup Can #3737
Produced: 2026-05-20 18:32:10
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
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
A tiny, colorful, animated script that prints a single
Woody‑Allen‑style philosophical gag.

Run it directly:
    $ python3 woody_quote.py
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"

# Some pleasant pastel colours (foreground)
FG = [
    "\033[38;5;215m",  # orange
    "\033[38;5;117m",  # teal
    "\033[38;5;180m",  # pink
    "\033[38;5;151m",  # mint
    "\033[38;5;220m",  # yellow
]

# A simple rainbow cycle for the border
def rainbow_cycle():
    while True:
        for colour in FG:
            yield colour

# ----------------------------------------------------------------------
# Text to display
# ----------------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is to keep looking for meaning, "
    "while secretly hoping "
    "the universe will finally apologise for all the existential "
    "inconvenience."
)

# ----------------------------------------------------------------------
# Fancy box drawing
# ----------------------------------------------------------------------
TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = "╭", "╮", "╰", "╯"
HLINE, VLINE = "─", "│"

def draw_box(text_lines, colour):
    """Return a coloured box string around the given list of lines."""
    width = max(len(line) for line in text_lines)
    top = f"{colour}{TOP_LEFT}{HLINE * (width+2)}{TOP_RIGHT}{RESET}"
    bottom = f"{colour}{BOTTOM_LEFT}{HLINE * (width+2)}{BOTTOM_RIGHT}{RESET}"
    middle = "\n".join(
        f"{colour}{VLINE}{RESET} {line.ljust(width)} {colour}{VLINE}{RESET}"
        for line in text_lines
    )
    return "\n".join([top, middle, bottom])

# ----------------------------------------------------------------------
# Animated printing
# ----------------------------------------------------------------------
def type_out(text, colour, delay=0.045):
    """Print `text` one character at a time using the given colour."""
    for ch in text:
        sys.stdout.write(f"{colour}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Split the quote into reasonably sized lines
    words = QUOTE.split()
    lines = []
    cur = ""
    max_len = 50
    for w in words:
        if len(cur) + len(w) + 1 > max_len:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # Prepare a rainbow border
    border_colour = next(rainbow_cycle())
    box = draw_box(lines, border_colour)

    # Print the box with a fade‑in effect (character by character)
    for line in box.split("\n"):
        type_out(line + "\n", border_colour, delay=0.015)

    # Leave a little pause before the "punchline" (we already have a punchline)
    time.sleep(0.6)

    # Highlight the quote itself inside the box (a different colour)
    highlight = "\033[38;5;207m"  # bright magenta
    for line in lines:
        type_out(line + "\n", highlight, delay=0.03)

    # End with a friendly wink
    wink = "\n" + "\033[38;5;226m" + "   ;-)   " + RESET + "\n"
    sys.stdout.write(wink)

if __name__ == "__main__":
    main()