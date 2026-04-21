"""
Campbell's Soup Can #3384
Produced: 2026-04-21 08:10:29
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, self‑contained program that prints a single,
Woody‑Allen‑style philosophical one‑liner with a splash of
ANSI colour, a decorative box and a gentle “type‑writer”
animation.
"""

import sys
import time

# ----------------------------------------------------------------------
# Configuration – feel free to tweak the colours or the quote
# ----------------------------------------------------------------------
QUOTE = (
    "I think the meaning of life is just a very elaborate "
    "excuse for us to keep buying new mugs that say “World's "
    "Best Existentialist.”"
)

# ANSI colour codes
RESET = "\u001b[0m"
FG_CYAN = "\u001b[36m"
FG_YELLOW = "\u001b[33m"
FG_MAGENTA = "\u001b[35m"
BG_BLACK = "\u001b[40m"

# Box‑drawing characters
TOP_LEFT = "╔"
TOP_RIGHT = "╗"
BOTTOM_LEFT = "╚"
BOTTOM_RIGHT = "╝"
HORIZ = "═"
VERT = "║"

# Animation speed (seconds per character)
SPEED = 0.03


def colorize(text: str, *styles: str) -> str:
    """Wrap *text* in the given ANSI styles."""
    return "".join(styles) + text + RESET


def type_print(text: str, delay: float = SPEED) -> None:
    """Print *text* one character at a time, flushing after each."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def framed(text: str, width: int = 70) -> str:
    """Return *text* centred inside a coloured ASCII frame."""
    # Ensure the frame is wide enough for the text
    inner_width = max(len(line) for line in text.splitlines())
    width = max(width, inner_width + 4)

    top = (
        colorize(TOP_LEFT + HORIZ * (width - 2) + TOP_RIGHT, FG_MAGENTA)
    )
    bottom = (
        colorize(BOTTOM_LEFT + HORIZ * (width - 2) + BOTTOM_RIGHT, FG_MAGENTA)
    )
    lines = [top]
    for line in text.splitlines():
        padded = line.center(width - 4)
        lines.append(
            colorize(
                f"{VERT} {padded} {VERT}",
                FG_MAGENTA,
            )
        )
    lines.append(bottom)
    return "\n".join(lines)


def main() -> None:
    # Build the coloured, framed quote
    boxed_quote = framed(colorize(QUOTE, FG_CYAN, BG_BLACK))
    # Print it with a gentle type‑writer effect
    type_print(boxed_quote, delay=0.015)


if __name__ == "__main__":
    main()