"""
Campbell's Soup Can #3506
Produced: 2026-04-30 09:25:44
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI color codes
BOLD = '\033[1m'
RESET = '\033[0m'
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
CYAN = '\033[96m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'

def type_text(text, delay=0.03, color=None):
    """Print text with a typewriter effect."""
    if color:
        sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(RESET)
    sys.stdout.write('\n')

def print_rainbow_line(char='~', length=60, colors=None):
    """Print a line of char with rainbow colors."""
    if colors is None:
        colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    for i in range(length):
        sys.stdout.write(colors[i % len(colors)] + char)
    sys.stdout.write(RESET + '\n')

def main():
    # Rainbow top border
    print_rainbow_line('~', 60)

    # Prefix
    print(BOLD + YELLOW + 'Woody Allen says:' + RESET)

    # The quote
    quote = "\"I'm not afraid of death; I just don't want to be there when it happens.\""
    type_text(quote, delay=0.05, color=MAGENTA)

    # Rainbow bottom border
    print_rainbow_line('~', 60)

    # A little extra humor
    print(BLUE + "    (He's also terrified of small spaces, large birds, and commitment.)" + RESET)

if __name__ == '__main__':
    main()