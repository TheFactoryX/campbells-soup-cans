"""
Campbell's Soup Can #1969
Produced: 2026-01-31 17:41:14
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

# ANSI color codes
COLORS = [
    '\033[31m',   # red
    '\033[32m',   # green
    '\033[33m',   # yellow
    '\033[34m',   # blue
    '\033[35m',   # magenta
    '\033[36m',   # cyan
    '\033[91m',   # bright red
    '\033[92m',   # bright green
    '\033[93m',   # bright yellow
    '\033[94m',   # bright blue
    '\033[95m',   # bright magenta
    '\033[96m',   # bright cyan
    '\033[0m'    # reset
]

def colorize(text, color_code):
    return f"{color_code}{text}\033[0m"

def random_color():
    return random.choice(COLORS)

def animate_print(text, delay=0.05, erase=True):
    """Print characters one‑by‑one with random colors and optional backspace animation."""
    line = ''
    for ch in text:
        line += ch
        c = random_color()
        sys.stdout.write(colorize(line, c))
        sys.stdout.flush()
        if erase:
            # Optionally erase the whole line for a flicker effect
            sys.stdout.write('\r\033[K')
            sys.stdout.flush()
        time.sleep(delay)
    # Final newline
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_ascii_art(name):
    """A tiny ASCII Woody Allen silhouette."""
    art = f"""
         ___
      ___/   \\
     /          \\
    |   o     o  |
    |   \___/    |
     \\   _.     /
      '-'\'-\   /
        \   \_/
   (c) Woody Allen {name}
"""
    sys.stdout.write(colorize(art, '\033[95m'))
    sys.stdout.flush()
    time.sleep(0.7)

def main():
    # Title
    sys.stdout.write(colorize("\n" + "="*30 + " Woody Allen's Existential Musings " + "="*30 + "\n", '\033[91m'))
    time.sleep(0.8)

    # Woody ASCII art
    print_ascii_art("— a.k.a. The Neurotic Philosopher")

    # The quote
    quote = (
        "I'm not a pessimist; I'm just a realist with a bad habit of "
        "seeing the dark side of the sun.\n"
        "Or, as I like to say: the universe is a very friendly place, "
        "except for the fact that it's trying to kill us all."
    )
    # Print quote in a colored box
    border = "╔" + "═" * 56 + "╗"
    start_line = colorize(border, '\033[92m')
    end_line = colorize("\n" + "║" + " " * 58 + "║\n" + colorize(border, '\033[92m'), '\033[92m')
    # Pad to fill the box nicely
    padded_quote = " ".join(quote.splitlines())
    centered = padded_quote.center(56 - 4)
    box = [
        start_line,
        "║ " + centered + " ║",
        end_line
    ]
    for line in box:
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
        time.sleep(0.15)

    # Animate the quote character by character
    animate_print(quote.strip(), delay=0.04)

    # Closing flourish
    sys.stdout.write(colorize("\nIn the end, we’re all just standing in line at the deli,\n"
                              "waiting for the cheese to be sliced—philosophically,\n"
                              "we’re already sliced.\n\n", '\033[93m'))
    sys.stdout.flush()
    time.sleep(1.2)

    # End with a blinking cursor
    cursor_blink = ''
    for i in range(12):
        cursor_blink += '|' if i % 2 == 0 else ' '
    sys.stdout.write(colorize(cursor_blink + '\r', random_color()))
    time.sleep(0.2)
    sys.stdout.write(colorize(' ' * len(cursor_blink) + '\r', '\033[0m'))
    time.sleep(0.2)
    # Final reset
    sys.stdout.write(colorize(cursor_blink + '\r', '\033[37m'))
    sys.stdout.flush()
    # Keep the cursor visible for a moment
    time.sleep(0.6)

if __name__ == "__main__":
    main()