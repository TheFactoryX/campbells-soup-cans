"""
Campbell's Soup Can #1997
Produced: 2026-02-02 05:41:56
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
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
import textwrap

def colored(text, fg, bg):
    """Return text wrapped in ANSI escape codes for foreground (fg) and background (bg) colors."""
    return f"\033[{fg};{bg}m{text}\033[0m"

def print_colored_char(char, fg, bg):
    """Print a single character with the given colors and flush immediately."""
    sys.stdout.write(colored(char, fg, bg))
    sys.stdout.flush()

def display_quote_in_box(quote):
    """Print the quote inside a padded box with a typing‑like animation and a flashing border."""
    # Wrap the quote to a reasonable width
    lines = textwrap.wrap(quote, width=45)
    max_len = max(len(l) for l in lines)
    box_width = max_len + 4               # 2 spaces padding + border thickness
    border = '+' + '-' * box_width + '+'

    # Choose a base colour pair for the whole box
    base_fg, base_bg = random.choice([(31, 42), (32, 43), (33, 44),
                                     (34, 45), (35, 46), (36, 47), (37, 40)])

    # Fade‑in the top border
    for _ in range(5):
        sys.stdout.write(border + '\r')
        sys.stdout.flush()
        time.sleep(0.1)
    print()

    # Type out each line of the quote with colour cycling
    for line in lines:
        cycle = [(31, 42), (32, 43), (33, 44), (34, 45), (35, 46), (36, 47), (37, 40)]
        for char in line:
            fg, bg = random.choice(cycle)
            print_colored_char(char, fg, bg)
            time.sleep(0.03)             # typing speed
        # Pad to full box width
        padding = ' ' * (box_width - len(line))
        for char in padding:
            print_colored_char(char, base_fg, base_bg)
            time.sleep(0.02)
        print()                         # newline after the line

    # Flash the bottom border a few times
    for _ in range(3):
        sys.stdout.write(border + '\r')
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write('\r' + ' ' * len(border))
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def main():
    # Woody Allen‑style philosophical quote
    quote = (
        "I'm not afraid of death; I'm terrified that when the afterlife starts, "
        "it will immediately charge me for the Wi‑Fi I never paid for."
    )

    # ASCII header (just for fun)
    header = r"""
   ____   __   __   __   __   __   __   __   __   __
  / __/  / /_ / /_ / /_ / /_ / /_ / /_ / /_ / /_ / /_
 / _/   _\ __/ __/ __/ __/ __/ __/ __/ __/ __/ __/ __/
/___/  /____/__/__/__/__/__/__/__/__/__/__/__/__/

                  (Woody Allen)
"""
    # Print header lines in bright cyan on white background
    for line in header.strip().splitlines():
        if line.strip():
            print(colored(line, 36, 47))

    # Show the quote with animation
    display_quote_in_box(quote)

if __name__ == "__main__":
    main()