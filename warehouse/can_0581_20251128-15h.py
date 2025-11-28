"""
Campbell's Soup Can #581
Produced: 2025-11-28 15:32:14
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
A tiny, self‑contained program that prints a single, Woody‑Allen‑style
philosophical quote.  The output is decorated with ANSI colors,
simple ASCII art, and a bit of animated typing.
"""

import sys
import time
import random

# ---------- ANSI colour codes ----------
COLS = [
    "\033[91m",  # bright red
    "\033[92m",  # bright green
    "\033[93m",  # bright yellow
    "\033[94m",  # bright blue
    "\033[95m",  # bright magenta
    "\033[96m",  # bright cyan
]
RESET = "\033[0m"

# ---------- ASCII art ----------------------------------------------
ART = r"""
   (\ . . /)   \
    ( ^-^- )\   |
     (___)  /\__/
    / | | \   |  /
   \_|_|_/   /_/
"""

# ---------- The quote ----------------------------------------------
QUOTE = (
    "I once tried to find meaning in life, but all I got was "
    "a very expensive toaster that wouldn't make toast on purpose."
)

# ---------- Helper functions ---------------------------------------
def colour_print(text, delay=0.05):
    """Print a string word‑by‑word with random colours and a small delay."""
    words = text.split()
    for i, word in enumerate(words):
        # Pick a colour (avoid the same colour as the previous word)
        colour = random.choice(COLS)
        sys.stdout.write(f"{colour}{word}{RESET} ")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def clear_screen():
    """Clear the terminal screen (does not work on all terminals)."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

# ---------- Main ----------------------------------------------------
def main():
    clear_screen()
    # Print the ASCII art at the top
    for line in ART.splitlines():
        sys.stdout.write(f"{random.choice(COLS)}{line}{RESET}\n")
    sys.stdout.flush()
    time.sleep(0.4)

    # Print a nice border around the quote
    border = f"{random.choice(COLS)}{'=' * 60}{RESET}"
    sys.stdout.write(border + "\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # Animate the quote
    colour_print(QUOTE, delay=0.08)

    # Bottom border
    sys.stdout.write(border + "\n")
    sys.stdout.flush()
    time.sleep(0.2)

    # Small fade‑out
    for _ in range(3):
        time.sleep(0.3)
        clear_screen()

if __name__ == "__main__":
    main()