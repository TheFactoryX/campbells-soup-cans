"""
Campbell's Soup Can #3453
Produced: 2026-04-25 22:57:10
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
A tiny terminal showcase that prints a single, Woody‑Allen‑style,
philosophical joke with a splash of colour and a tiny typing animation.

Run it directly:
    $ python3 woody_quote.py
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers ----------------------------------------------------
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# Some pleasant pastel foreground colours
COLS = [
    "\033[38;5;110m",  # teal
    "\033[38;5;215m",  # light orange
    "\033[38;5;221m",  # pale yellow
    "\033[38;5;141m",  # light purple
    "\033[38;5;150m",  # soft green
]

def colored(text: str, colour: str) -> str:
    """Wrap *text* in the given ANSI colour code."""
    return f"{colour}{text}{RESET}"


# ----------------------------------------------------------------------
# Fancy box drawing -----------------------------------------------------
# ----------------------------------------------------------------------
def box_around(lines):
    """Return *lines* surrounded by a nice double‑line box."""
    # Determine the longest line (ignoring ANSI codes)
    plain_lengths = [len(strip_ansi(l)) for l in lines]
    width = max(plain_lengths)
    horiz = "═" * (width + 2)

    top = f"╔{horiz}╗"
    bottom = f"╚{horiz}╝"

    boxed = [top]
    for line in lines:
        padded = line + " " * (width - len(strip_ansi(line)))
        boxed.append(f"║ {padded} ║")
    boxed.append(bottom)
    return boxed


def strip_ansi(s: str) -> str:
    """Remove ANSI escape sequences – used only for length calculations."""
    import re
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


# ----------------------------------------------------------------------
# Typing animation -------------------------------------------------------
# ----------------------------------------------------------------------
def type_out(text, delay=0.04, colour_cycle=None):
    """
    Print *text* char‑by‑char.
    If *colour_cycle* is an iterator of colour codes, each character gets the
    next colour, looping forever.
    """
    if colour_cycle is None:
        colour_cycle = itertools.cycle([RESET])

    for char in text:
        col = next(colour_cycle)
        sys.stdout.write(colored(char, col))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


# ----------------------------------------------------------------------
# Main -----------------------------------------------------------------
# ----------------------------------------------------------------------
def main():
    # The quote – original Woody‑Allen‑style neurotic wisdom
    quote = (
        f"{BOLD}“I’m terrified of the meaning of life, but I’m "
        f"even more terrified of the day it finally "
        f"asks me a question I can’t answer.”{RESET}"
    )

    # Build the visual layout
    header = colored(" ★ ★ ★ Woody Allen‑Style Philosophy ★ ★ ★ ", "\033[38;5;208m")
    footer = colored("   (c) 2026 Neurotic Thoughts Inc.", "\033[38;5;242m")

    # Create a box with the quote inside
    boxed_quote = box_around([quote])

    # Assemble everything
    lines = [header, ""] + boxed_quote + ["", footer]

    # Print with a gentle typing effect and a rainbow colour cycle
    rainbow = itertools.cycle(COLS)
    for line in lines:
        type_out(line, delay=0.02, colour_cycle=rainbow)

    # Keep the terminal bright for a moment before exiting
    time.sleep(0.8)


if __name__ == "__main__":
    main()