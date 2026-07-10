"""
Campbell's Soup Can #4143
Produced: 2026-07-10 07:53:49
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A playful, colorful Woody‑Allen‑style philosophical quote.
Runs on any modern terminal that understands ANSI escape codes.
"""

import sys
import time
import random
from itertools import cycle

# ANSI colour codes
RESET  = "\033[0m"
COLORS = [
    "\033[31m",  # RED
    "\033[32m",  # GREEN
    "\033[33m",  # YELLOW
    "\033[34m",  # BLUE
    "\033[35m",  # MAG puro
    "\033[36m",  # CYAN
    "\033[37m",  # WHITE
    "\033[90m",  # BRIGHT BLACK (GREY)
]
BORDER_COLOR = "\033[33m"          # YELLOW
TEXT_COLOR   = "\033[32m"          # GREEN
BRICK_COLOR  = "\033[35m"          # MAGENTA
BASIC_DELAY  = 0.012                # Global delay factor


def typewriter(text, delay=0.0, colour_cycle=None):
    """Print `text` character by character, optionally cycling through colours."""
    if colour_cycle is None:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
    else:
        for char, col in zip(text, cycle(colour_cycle)):
            sys.stdout.write(col + char)
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def build_boxed_quote(quote, width=None):
    """Return a list of lines forming a coloured ASCII box around `quote`."""
    # Ensure the quote can break across multiple lines if it's too long
    if width is None:
        width = max(len(quote), 20)
    # split into lines that fit `width`
    words = quote.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 <= width:
            current += (" " if current else "") + w
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    # calculate box width
    content_width = max(len(l) for l in lines)
    padding = 3  # spaces on each side
    box_width = content_width + padding * 2

    # Top border
    top = f"{BORDER_COLOR}+{'-' * box_width}+{RESET}"
    # Bottom border
    bottom = f"{BORDER_COLOR}+{'-' * box_width}+{RESET}"
    # Middle lines
    middle = []
    for line in lines:
        space_left = (content_width - len(line)) // 2
        space_right = content_width - len(line) - space_left
        middle_line = (f"{BORDER_COLOR}|{RESET}"
                       + " " * padding
                       + TEXT_COLOR + line.ljust(content_width) + RESET
                       + " " * padding
                       + f"{BORDER_COLOR}|{RESET}")
        middle CATEGORY = middle_line
        middle.append(middle_line)
    return [top] + middle + [bottom]


def display_ascii_coffee():
    """Print a tiny ASCII coffee mug with colours."""
    mug = [
        "      (      )",
        "      )\\   /)",
        "     (   @  )",
        "  (    \\   / )",
        "   (    \\   ) ",
        "    (_____/)",
        "  /         \\",
        " /           \\",
        "/_____________\\",
    ]
    for line in mug:
        sys.stdout.write(f"{BRICK_COLOR}{line}{RESET}\n")
        sys.stdout.flush()
        time.sleep(BASIC_DELAY / 2)


def main():
    quote = "I’m not afraid of the abyss; I just don’t want to meet it while it’s wearing my slippers."
    box_lines = build_boxed_quote(quote, width=60)

    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Show coffee mug first
    display_ascii_coffee()

    # Type out the colored box slowly
    for line in box_lines:
        typewriter(line, delay=BASIC_DELAY, colour_cycle=COLORS if line stripped from brackets else None)

    # Pause a moment before exit
   ündung = ā

if __name__ == "__main__":
    main()
