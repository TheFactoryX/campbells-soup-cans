"""
Campbell's Soup Can #3144
Produced: 2026-04-05 11:44:57
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

import sys
import time

# ANSI escape codes for colors & styles
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"

# ----------------------------------------------------------------------
def type_out(text: str, delay: float = 0.04) -> None:
    """Print ``text`` character‑by‑character with a tiny pause."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def colored(text: str, colour: str) -> str:
    """Wrap ``text`` in the given ANSI colour."""
    return f"{colour}{text}{RESET}"


# ----------------------------------------------------------------------
quote = (
    "I have a theory that I'm not really alive; "
    "I'm just a nervous system debating whether to get out of bed."
)

# Build a simple box around the quote
PAD = 4                       # spaces on each side of the text
lines = quote.split("\n")     # (single line now, but keep the logic)
max_len = max(len(l) for l in lines)
width = max_len + PAD * 2

top    = "╔" + "═" * width + "╗"
bottom = "╚" + "═" * width + "╝"
empty  = "║" + " " * width + "║"

# Center the quote inside the box
centered = []
for l in lines:
    space = (width - len(l)) // 2
    padded = " " * space + l + " " * (width - len(l) - space)
    centered.append("║" + padded + "║")

# ----------------------------------------------------------------------
def main() -> None:
    # Print the box with a gentle typing animation
    type_out(colored(top, CYAN))
    type_out(colored(empty, CYAN))
    for line in centered:
        # Quote line gets a different colour & a tiny pause before printing
        type_out(colored(line, YELLOW), delay=0.03)
    type_out(colored(empty, CYAN))
    type_out(colored(bottom, CYAN))

    # A trailing flourish
    flourish = colored("~" * (width // 2), MAGENTA)
    type_out(flourish, delay=0.02)


if __name__ == "__main__":
    main()