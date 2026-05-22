"""
Campbell's Soup Can #3752
Produced: 2026-05-22 18:04:35
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A tiny, colorful Woody‑Allen‑style philosophical quote printer.
Run it directly – no external libraries required.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour utilities
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# Some pastel shades that work on most terminals
PALETTE = [
    "\033[38;5;221m",  # light yellow
    "\033[38;5;215m",  # peach
    "\033[38;5;180m",  # lilac
    "\033[38;5;173m",  # light pink
    "\033[38;5;159m",  # light cyan
]

def colored(text, color):
    """Wrap text in an ANSI colour."""
    return f"{color}{text}{RESET}"

# ----------------------------------------------------------------------
# Fancy box drawing
# ----------------------------------------------------------------------
def draw_box(lines, pad=2, color=PALETTE[0]):
    """Return a box (list of strings) containing the given lines."""
    max_len = max(len(line) for line in lines)
    horiz = "─" * (max_len + pad * 2)
    top    = f"┌{horiz}┐"
    bottom = f"└{horiz}┘"
    boxed = [top]
    for line in lines:
        space = " " * (max_len - len(line))
        boxed.append(f"│{' '*pad}{line}{space}{' '*pad}│")
    boxed.append(bottom)
    return [colored(l, color) for l in boxed]

# ----------------------------------------------------------------------
# Type‑writer animation
# ----------------------------------------------------------------------
def type_out(text, speed=0.04, colour=PALETTE[2]):
    """Print text character‑by‑character."""
    for ch in text:
        sys.stdout.write(colored(ch, colour))
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Main program
# ----------------------------------------------------------------------
def main():
    quote = (
        "I think the meaning of life is to find a comfortable chair, "
        "realise it’s just a fancy place to sit and then be terrified that "
        "the universe will eventually rearrange the furniture."
    )

    # Build a colourful frame around the quote
    wrapped = []
    line_len = 60
    for i in range(0, len(quote), line_len):
        wrapped.append(quote[i:i+line_len])

    # Cycle colours for each line of the box
    box_lines = draw_box(wrapped, pad=4, color=next(itertools.cycle(PALETTE)))

    # Print the animated box
    for line in box_lines:
        type_out(line, speed=0.015, colour=PALETTE[1])

    # A final punch‑line in bold, flashing colour
    punch = "— Woody Allen (probably)"
    for _ in range(3):
        sys.stdout.write(colored(BOLD + punch + RESET, PALETTE[4]))
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * len(punch) + "\r")
        time.sleep(0.2)
    # Final stable print
    sys.stdout.write(colored(BOLD + punch + RESET + "\n"))

if __name__ == "__main__":
    main()