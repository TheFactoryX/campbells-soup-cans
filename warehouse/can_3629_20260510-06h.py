"""
Campbell's Soup Can #3629
Produced: 2026-05-10 06:46:58
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
import itertools

# ANSI colour palette (top‑to‑bottom rainbow)
RAINBOW = [
    "\033[38;5;196m",  # red
    "\033[38;5;202m",  # orange
    "\033[38;5;220m",  # yellow
    "\033[38;5;118m",  # green
    "\033[38;5;27m",   # blue
    "\033[38;5;99m",   # indigo
    "\033[38;5;129m",  # violet
]
RESET = "\033[0m"

QUOTE = (
    "I laugh at myself, but I don't laugh at the fact that "
    "I think twice before I murder my own sense of meaning."
)

# Build a colourful, animated banner
def rainbow_banner(text, width=70, delay=0.07):
    """
    Prints `text` with each character in a different rainbow colour,
    scrolling across the terminal like a neon sign.
    """
    # Pad the text with spaces so it can scroll cleanly
    padded = ' ' * width + text + ' ' * width
    cycle = itertools.cycle(RAINBOW)

    for i in range(len(quote)):
        sys.stdout.write("\r")  # return to start of line
        # pull a slice of the padded text
        fragment = padded[i:i+width]
        coloured = "".join(f"{next(cycle)}{ch}{RESET}" for ch in fragment)
        sys.stdout.write(coloured)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# --- Main execution ---------------------------------------------------------

if __name__ == "__main__":
    # clear screen and center the banner
    sys.stdout.write("\033[2J\033[H")   # clear terminal
    terminal_width = 80
    quote = QUOTE
    # Pad with spaces to center
    padded_quote = quote.center(terminal_width)
    try:
        rainbow_banner(padded_quote, width=terminal_width, delay=0.1)
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.exit(0)