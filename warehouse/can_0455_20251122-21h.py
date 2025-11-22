"""
Campbell's Soup Can #455
Produced: 2025-11-22 21:28:06
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

# ANSI escape codes for colors
RESET   = '\033[0m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
BRIGHT  = '\033[1m'

# Glory of colors for the typewriter
COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

# The Woody‑Allen‑style quote
quote = ("I asked the universe for meaning, and all I got was a shrug, a spam folder," 
         " and a pizza box that says \"Existential Crisis – please eat before it expires.\"")

# --------- Helper Functions ----------

def typewriter(text, delay=0.05):
    """Print text one character at a time, cycling through random colors."""
    for c in text:
        sys.stdout.write(random.choice(COLORS) + c + RESET)
        sys.stdout.flush()
        if c != '\n':
            time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_frame(width, title=''):
    """Print a simple ASCII frame around the quote."""
    line = '+' + '-'*(width-2) + '+'
    print(BRIGHT + CYAN + line + RESET)
    if title:
        # center title
        t = f"| {title.center(width-4)} |"
        print(BRIGHT + CYAN + t + RESET)
        print(BRIGHT + CYAN + line + RESET)
    else:
        # empty middle empty line before content
        print(BRIGHT + CYAN + ('|' + ' '*(width-2) + '|') + RESET)

# --------- Main Program -------------

def main():
    # Prepare the frame based on quote length
    frame_width = max(len(quote.splitlines()[0]), 60) + 4
    print_frame(frame_width, title='Woody, but maybe not wise...')

    # Simulate the typewriter effect
    typewriter(quote)

    # Some trailing visual flourish
    print(BRIGHT + YELLOW + '+' + '-'*(frame_width-2) + '+' + RESET)

    # Pause before exit
    time.sleep(1.0)

if __name__ == '__main__':
    main()