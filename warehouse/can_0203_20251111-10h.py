"""
Campbell's Soup Can #203
Produced: 2025-11-11 10:39:13
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

# ANSI escape codes
ESC = '\033['
RESET = ESC + '0m'
BOLD = ESC + '1m'
DIM = ESC + '2m'
UNDERLINE = ESC + '4m'
BLINK = ESC + '5m'
REVERSE = ESC + '7m'

# Colors
BLACK   = ESC + '30m'
RED     = ESC + '31m'
GREEN   = ESC + '32m'
YELLOW  = ESC + '33m'
BLUE    = ESC + '34m'
MAGENTA = ESC + '35m'
CYAN    = ESC + '36m'
WHITE   = ESC + '37m'

# Bright colors
BRIGHT_BLACK   = ESC + '90m'
BRIGHT_RED     = ESC + '91m'
BRIGHT_GREEN   = ESC + '92m'
BRIGHT_YELLOW  = ESC + '93m'
BRIGHT_BLUE    = ESC + '94m'
BRIGHT_MAGENTA = ESC + '95m'
BRIGHT_CYAN    = ESC + '96m'
BRIGHT_WHITE   = ESC + '97m'


def type_out(text, delay=0.05, color=YELLOW, end="\n"):
    """Print text with a typewriter effect."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + end)


def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write(ESC + '2J' + ESC + 'H')
    sys.stdout.flush()


def print_boxed_quote(quote, width=60):
    """Print a quote inside an ASCII-art box with colors."""
    # Ensure the quote fits the width
    words = quote.split()
    lines = []
    while words:
        line = ""
        while words and len(line + words[0] + " ") <= width - 4:
            line += words.pop(0) + " "
        lines.append(line.rstrip())

    box_width = min(width, max(len(line) for line in lines) + 4)

    # Top border
    type_out(
        BRIGHT_MAGENTA + '┌' + '─' * (box_width - 2) + '┐' + RESET,
        delay=0.0,
        end='\n'
    )
    # Empty line
    type_out(
        BRIGHT_MAGENTA + '│' + ' ' * (box_width - 2) + '│' + RESET,
        delay=0.0,
        end='\n'
    )
    # Quote lines
    for line in lines:
        padded = line.ljust(box_width - 4)
        type_out(
            BRIGHT_MAGENTA + '│ ' + BOLD + BRIGHT_YELLOW + padded + RESET + BRIGHT_MAGENTA + ' │' + RESET,
            delay=0.0,
            end='\n'
        )
    # Empty line
    type_out(
        BRIGHT_MAGENTA + '│' + ' ' * (box_width - 2) + '│' + RESET,
        delay=0.0,
        end='\n'
    )
    # Bottom border
    type_out(
        BRIGHT_MAGENTA + '└' + '─' * (box_width - 2) + '┘' + RESET,
        delay=0.0,
        end='\n'
    )


def animated_intro():
    """Animated intro of a little ASCII coffee mug."""
    frames = [
        r"""      _..._
   .'     '.
  /  o   o  \
 |  . --- . |
 \  '--'--' /
  '._____.'
""",
        r"""      _..._
   .'     '.
  /  o   o  \
 |  . --- . |
 \  '--'--' /
  '._____.'   (   )
""",
        r"""      _..._
   .'     '.
  /  o   o  \
 |  . --- . |
 \  '--'--' /
  '._____'   (   )
          (  ) )
""",
    ]

    for i in range(10):  # repeat pulse
        for frame in frames:
            clear_screen()
            type_out(BRIGHT_CYAN + frame + RESET, delay=0.0)
            time.sleep(0.07)


def main():
    animated_intro()

    clear_screen()

    # The Woody‑Allen‑style philosophical quote
    quote = (
        "I wonder if the universe is just an elaborate prank on humans, "
        "and the only joke I have is that I keep asking myself what I am "
        "doing.  The answer?  'Because I didn't know how to stop being a "
        "philosophical idiot.'"
    )

    print_boxed_quote(quote, width=70)

    type_out("\n" + BRIGHT_BLUE + BOLD + "— Woody Allen‑in‑spirit\n" + RESET, end='')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)