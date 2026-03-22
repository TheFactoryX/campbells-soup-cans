"""
Campbell's Soup Can #2914
Produced: 2026-03-22 20:45:11
Worker: OpenAI: gpt-oss-20b (openai/gpt-oss-20b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A tiny Python program that prints a neurotic, Woody‑Allen‑style
philosophical quote in a colorful box, preceded by a blinking
ASCII cat.  All done with ANSI escape codes – no external modules.
"""

import sys
import time

# ANSI colour & style codes
RESET    = "\033[0m"
BOLD     = "\033[1m"
CYAN     = "\033[36m"
YELLOW   = "\033[33m"
MAGENTA  = "\033[35m"
MAGENTA_FG = "\033[95m"

# The quote – keep it neat and short
quote = ("I’m not afraid of death; I just don’t want to be there "
         "when it happens, because the universe will need a final punchline.")

# A little neurotic cat
cat_art = [
    "  /\\_/\\",
    " ( o.o )",
    "  > ^ <"
]

# Build a coloured box around the quote
border_len     = len(quote) + 2  # two spaces padding
box_top   = f"{BOLD}{CYAN}┌{'─' * border_len}┐{RESET}"
box_mid   = f"{BOLD}{CYAN}│ {quote} │{RESET}"
box_bottom= f"{BOLD}{CYAN}└{'─' * border_len}┘{RESET}"
box = [box_top, box_mid, box_bottom]

def slow_print(lines, delay=0.05):
    """Print each line with a tiny delay for a typing effect."""
    for line in lines:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Clear screen & reset cursor
    sys.stdout.write("\033[2J\033[H")
    # Print the cat in yellow
    slow_print([f"{YELLOW}{c}{RESET}" for c in cat_art], 0.08)
    time.sleep(0.6)
    # Print the quote in a colourful box
    slow_print(box, 0.12)

    # A tiny blinking animation: hide and show cursor a few times
    for _ in range(4):
        sys.stdout.write("\033[s")    # Save cursor
        sys.stdout.write("\033[?25l") # Hide cursor
        time.sleep(0.15)
        sys.stdout.write("\033[u")    # Restore cursor
        time.sleep(0.15)

    sys.stdout.write("\n" + RESET)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
