"""
Campbell's Soup Can #2198
Produced: 2026-02-13 11:02:23
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import sys
import time

def clear_screen():
    """Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_top_border():
    """Draw the top border with a slow‑typewriter effect."""
    border = '+' + '-' * 78 + '+'  # width = 80 chars (2 borders + 78 interior)
    delay = 0.04
    for ch in border:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def print_line(line, interior_width):
    """Print one interior line with coloured border and a typing effect."""
    red_code = 91          # bright red for borders
    quote_color = 96       # bright cyan for the quote
    delay = 0.04

    # left border, red
    sys.stdout.write(f"\033[{red_code}m")
    sys.stdout.write('|')
    sys.stdout.flush()
    time.sleep(delay)

    # interior quote, cyan
    sys.stdout.write(f"\033[{quote_color}m")
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m")  # reset colour after quote

    # fill remaining interior space with blank spaces (uncoloured)
    remaining = interior_width - len(line)
    for _ in range(remaining):
        sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(delay)

    # right border, red
    sys.stdout.write(f"\033[{red_code}m")
    sys.stdout.write('|')
    sys.stdout.write("\033[0m\n")
    sys.stdout.flush()

def main():
    clear_screen()
    quote_lines = [
        "I’m not afraid of death;",
        "I just don’t want to be there",
        "when it happens."
    ]
    interior_width = 78

    # top border
    sys.stdout.write("\033[91m")
    animate_top_border()
    sys.stdout.write("\033[0m\n")
    time.sleep(0.2)

    # interior lines (typing effect)
    for line in quote_lines:
        print_line(line, interior_width)
        time.sleep(0.2)

    # bottom border
    sys.stdout.write("\033[91m")
    animate_top_border()
    sys.stdout.write("\033[0m\n")

    # brief pause before clearing again
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    main()