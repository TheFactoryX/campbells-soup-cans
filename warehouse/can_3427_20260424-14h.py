"""
Campbell's Soup Can #3427
Produced: 2026-04-24 14:07:15
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Printer
With typewriter effect and rainbow colors.
"""

import sys
import time

# ANSI escape codes
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# Foreground colors (standard and bright)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

def typewriter(text, delay=0.03, colors=None):
    """
    Print text with a typewriter effect.
    If colors is a list, cycle through them for each character.
    """
    if colors is None:
        colors = ['']
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        if color:
            sys.stdout.write(color + char + RESET)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)  # just in case
    print()

def main():
    # Clear the screen (ANSI escape sequence)
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

    # Decorative header
    header = " WOODY ALLEN'S EXISTENTIAL CINEMA "
    print(BOLD + BRIGHT_YELLOW + header.center(60, '=') + RESET)
    print()

    # The quote (original Woody Allen style)
    quote = "I don't want to achieve immortality through my work; " \
            "I want to achieve it through not dying."

    # Optional: a more original quote (uncomment to use):
    # quote = "I asked the universe for the meaning of life, but it put me on hold " \
    #         "and then transferred me to a department that closed early."

    # List of colors to cycle through for each character
    rainbow = [BRIGHT_CYAN, BRIGHT_MAGENTA, BRIGHT_YELLOW,
               BRIGHT_GREEN, BRIGHT_BLUE, BRIGHT_RED]

    # Print the quote with typewriter effect and rainbow colors
    typewriter(quote, delay=0.03, colors=rainbow)

    # Brief pause
    time.sleep(0.5)

    # Signature with a slower, dimmer typewriter
    signature = "— Woody Allen"
    sys.stdout.write(DIM + BRIGHT_BLACK)  # dim gray
    for ch in signature:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.1)
    print(RESET)

    # Optional: keep the terminal clean
    print()
    print(DIM + "(Press Enter to exit)" + RESET)
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Graceful exit on Ctrl-C
        sys.stdout.write(RESET)
        print("\nGoodbye!")