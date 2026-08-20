"""
Campbell's Soup Can #4724
Produced: 2026-08-20 16:50:28
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
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

# ANSI colour helpers -------------------------------------------------
def colour(text, code):
    """Wrap *text* in an ANSI colour code."""
    return f'\033[{code}m{text}\033[0m'

def clear():
    """Clear the terminal screen."""
    sys.stdout.write('\033[2J\033[9;0f')
    sys.stdout.flush()

# The Woody Allen‑style philosophical quote ---------------------------
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Make a little animated, colour‑ful box around the quote ------------
def animate_quote():
    # Box width adapts to the quote length
    w = len(quote) + 4
    border = '*' * w
    top    = colour(border, 31)          # red
    middle = colour('*' + ' ' + quote + ' ' + '*', 32)  # green
    bottom = colour(border, 31)
    lines  = [top, middle, bottom]

    for i in range(3):
        clear()
        for j, line in enumerate(lines):
            # Cycle colours for a psychedelic effect
            col = 31 + (i + j) % 6
            sys.stdout.write(colour(line, col) + '\n')
        sys.stdout.flush()
        time.sleep(0.9)

if __name__ == '__main__':
    animate_quote()
    # Print the quote one final time in bright magenta for emphasis
    clear()
    sys.stdout.write(colour(quote + '\n', 35) + '\n')
    sys.stdout.flush()
    input("\nPress ENTER to exit...")   # pause so the viewer can read it