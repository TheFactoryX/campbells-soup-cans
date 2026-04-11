"""
Campbell's Soup Can #3246
Produced: 2026-04-11 21:48:14
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

# ANSI escape codes for colors and styles
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BRIGHT_BLACK = '\033[90m'
BRIGHT_WHITE = '\033[97m'

# The Woody‑Allen‑style quote
quote = (
    f"{ITALIC}{BOLD}{CYAN}“I’m terrified of the speed at which I die, "
    f"and the fact that the cake survived my nap in the freezer.”{RESET}"
)

# Function to draw a squiggly outline that moves
def squiggly_frame(offset):
    bar = ["   _____   ",
           "  /     \\  ",
           " |  {0}  | ",
           "  \\_____/  "]
    top = bar[0]
    middle = bar[1].format(quote[0:7].ljust(6))
    bottom = bar[3]
    # create a moving dash line in middle
    dash_line = '■' * (offset % 10 + 1)
    middle = middle[:8] + dash_line + middle[9:]
    return f"{MAGENTA}{top}\n{top}\n{middle}\n{top}\n{bottom}\n{bottom}{RESET}"

# Animation loop
def animate():
    frames = 30
    delay = 0.1
    for i in range(frames):
        sys.stdout.write('\033[?25l')  # Hide cursor
        sys.stdout.write('\033[H')     # Move cursor to home
        sys.stdout.write(squiggly_frame(i))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[?25h')  # Show cursor

if __name__ == "__main__":
    # Clear screen
    sys.stdout.write('\033[2J')
    animate()
    # Finally print the full quote centered
    box_width = len(quote) + 4
    print('\n' + BOLD + BRIGHT_WHITE + "+" + "-" * box_width + "+")
    print("|  " + quote + "  |")
    print("+" + "-" * box_width + "+")
    sys.stdout.flush()