"""
Campbell's Soup Can #221
Produced: 2025-11-12 06:46:03
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

# ANSI escape codes for colors and cursor control
RESET   = "\033[0m"
BOLD    = "\033[1m"
BLUE    = "\033[34m"
CYAN   = "\033[36m"
GREEN  = "\033[32m"
MAGENTA="\033[35m"
RED    = "\033[31m"
YELLOW = "\033[33m"
BLACK  = "\033[30m"
WHITE  = "\033[37m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

# The Woody‑Allen‑style quote
QUOTE = (
    "\"I’m terrified that somewhere between the next coffee shop and my existential crisis, "
    "I’ll find out that the meaning of life is just a very long, very dull gag; so I keep myself "
    "busy by writing the punchlines, hoping that humor protects me from the inevitable existential "
    "disappointment.\""
)

# Build a decorative box around the quote
quote_len   = len(QUOTE)
padding     = 4                      # spaces on each side inside the box
inner_width = quote_len + padding
border_top  = f"{BOLD}{CYAN}┌{'─'*inner_width}┐{RESET}"
border_bot  = f"{BOLD}{CYAN}└{'─'*inner_width}┘{RESET}"
blank_line  = f"{BOLD}{CYAN}│{' '*inner_width}│{RESET}"

# Helper to randomize color of a single character
def random_color_char(ch):
    col = random.choice([BLUE, CYAN, GREEN, MAGENTA, RED, YELLOW, WHITE])
    return f"{col}{ch}{RESET}"

def animated_print():
    # Hide cursor while animating
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()

    # Print the top border and two blank lines
    sys.stdout.write(border_top + "\n" + blank_line + "\n")
    sys.stdout.flush()

    # Animate the quote character by character
    rendered = []
    for ch in QUOTE:
        rendered.append(random_color_char(ch))
        line = "".join(rendered)
        # Pad the line to match inner width
        padded_line = line + " " * (inner_width - len(QUOTE))
        sys.stdout.write(f"{BOLD}{CYAN}│{padded_line}│{RESET}\n")
        sys.stdout.flush()
        time.sleep(0.04)
        # Move cursor up one line to overwrite
        sys.stdout.write("\033[F")
    # Final line with the full quote
    sys.stdout.write(f"{BOLD}{CYAN}│{''.join(rendered)}{' '*(inner_width-len(QUOTE))}│{RESET}\n")
    sys.stdout.flush()

    # Print bottom border
    sys.stdout.write(border_bot + "\n")
    sys.stdout.flush()

    # Show cursor again
    sys.stdout.write(SHOW_CURSOR)
    sys.stdout.flush()

if __name__ == "__main__":
    animated_print()
    # Keep the window for a moment before exiting
    time.sleep(4)