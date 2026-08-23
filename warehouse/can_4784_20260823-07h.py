"""
Campbell's Soup Can #4784
Produced: 2026-08-23 07:47:08
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
RED = '\033[31m'

def draw_boxed_quote(quote, width=80):
    """Draw a simple ASCII box around the quote with colored borders."""
    border = '+' + '-' * width + '+'
    print(CYAN + BOLD + border + RESET)
    print(YELLOW + f"| {quote.ljust(width-2)} |" + RESET)
    print(CYAN + BOLD + border + RESET)

def main():
    # A witty Woody‑Allenesque philosophical quote (original)
    quote = "I don't fear death; I just don't want to be stuck in the afterlife queue."

    # ASCII art: a pair of glasses with a pipe (Woody style)
    art = r"""
         .-.-.
        /   \\
       | o o |
        \___/
    """
    print(RED + art + RESET)
    time.sleep(0.5)

    # Print the quote in a fancy box
    draw_boxed_quote(quote)

if __name__ == "__main__":
    main()