"""
Campbell's Soup Can #3657
Produced: 2026-05-12 18:18:02
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
A tiny standalone script that prints a single, Woody‑Allen‑style philosophical
quip with a little visual flair – coloured ASCII art and a type‑writer effect.
Run it in a terminal that understands ANSI escape sequences.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour / style helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

# Some pleasant foreground colours
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}

# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑inspired)
# ----------------------------------------------------------------------
quote = (
    "I’m terrified of eternity – not because it’s endless, "
    "but because I’m pretty sure I’ll still be me when it finally "
    "arrives, and I’ve not yet figured out how to make myself "
    "interesting."
)

# ----------------------------------------------------------------------
# Fancy frame function – draws a coloured box around the text
# ----------------------------------------------------------------------
def colour_frame(text: str, *, colour: str = "cyan", padding: int = 2) -> str:
    """Return `text` wrapped in a coloured ASCII box."""
    lines = text.splitlines()
    width = max(len(line) for line in lines)
    horiz = colour + "─" * (width + padding * 2) + RESET
    top    = f"{colour}╭{horiz}╮{RESET}"
    bottom = f"{colour}╰{horiz}╯{RESET}"
    middle = []
    for line in lines:
        pad = " " * (width - len(line))
        middle.append(
            f"{colour}│{RESET}"
            f"{' ' * padding}{line}{pad}{' ' * padding}"
            f"{colour}│{RESET}"
        )
    return "\n".join([top, *middle, bottom])

# ----------------------------------------------------------------------
# Type‑writer animation
# ----------------------------------------------------------------------
def typewriter(text: str, *, speed: float = 0.04) -> None:
    """Print `text` one character at a time."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        # a tiny pause (faster for spaces and new‑lines)
        time.sleep(speed if ch not in " \n" else speed / 2)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    # Randomly pick a colour for the frame each run
    frame_colour = itertools.cycle(FG.values())
    colour = next(frame_colour)

    framed = colour_frame(quote, colour="magenta")
    # Print the frame instantly, then animate the quote inside
    # (strip the outer borders, keep only the inner lines)
    lines = framed.splitlines()
    top, *inner, bottom = lines
    print(top)                       # top border
    for line in inner:
        # the actual quote part is between the first and last │
        content = line.split("│")[1]
        # animate only the content, keep the side borders static
        sys.stdout.write(f"{FG['magenta']}│{RESET}")
        typewriter(content, speed=0.03)
        sys.stdout.write(f"{FG['magenta']}│{RESET}\n")
    print(bottom)                    # bottom border

if __name__ == "__main__":
    main()