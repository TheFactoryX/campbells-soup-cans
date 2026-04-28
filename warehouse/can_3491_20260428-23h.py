"""
Campbell's Soup Can #3491
Produced: 2026-04-28 23:10:11
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
RESET = '\033[0m'
BOLD = '\033[1m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

def typewriter_print(text, color=None, delay=0.05, end='\n'):
    """Print text with typewriter effect, optionally with color."""
    if color:
        sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(RESET)
    sys.stdout.write(end)
    sys.stdout.flush()

def main():
    # Clear screen (ANSI)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Decorative header
    header = [
        "****************************************",
        "*                                      *",
        "*      W O O D Y   A L L E N' S        *",
        "*         P H I L O S O P H Y          *",
        "*                                      *",
        "****************************************"
    ]
    for line in header:
        print(f"{CYAN}{line}{RESET}")
        time.sleep(0.1)

    time.sleep(0.5)

    # The quote: Woody Allen style (slightly tweaked classic)
    part1 = "I don't mind dying; "
    part2 = "I just don't want to be there when it happens."

    print()  # blank line before quote
    # Print quote with typewriter effect, two colors
    typewriter_print(part1, color=YELLOW, delay=0.04, end='')
    typewriter_print(part2, color=GREEN, delay=0.04, end='\n')

    time.sleep(0.3)

    # Credit
    credit = "- Woody Allen"
    typewriter_print(credit, color=MAGENTA, delay=0.03)

    print()
    # Footer
    footer = "****************************************"
    print(f"{CYAN}{footer}{RESET}")

if __name__ == "__main__":
    main()