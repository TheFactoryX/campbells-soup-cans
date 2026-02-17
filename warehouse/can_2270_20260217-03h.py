"""
Campbell's Soup Can #2270
Produced: 2026-02-17 03:14:10
Worker: Aurora Alpha (openrouter/aurora-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, colorful Woody‑Allen‑style philosophical quote printer.
Run this script directly – no external dependencies required.
"""

import sys
import time

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"
FG = {
    "red":    "\033[31m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "blue":   "\033[34m",
    "magenta":"\033[35m",
    "cyan":   "\033[36m",
    "white":  "\033[37m",
}
BG = {
    "red":    "\033[41m",
    "green":  "\033[42m",
    "yellow": "\033[43m",
    "blue":   "\033[44m",
    "magenta":"\033[45m",
    "cyan":   "\033[46m",
    "white":  "\033[47m",
}

def colour(text: str, *styles: str) -> str:
    """Wrap *text* with the given ANSI styles."""
    return "".join(styles) + text + RESET

# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑style, neurotic, self‑deprecating)
# ----------------------------------------------------------------------
quote = (
    "I think, therefore I'm terrified—"
    "the universe is a cosmic therapist and I'm the patient who never shows up."
)

# ----------------------------------------------------------------------
# Build a simple ASCII box around the quote
# ----------------------------------------------------------------------
def build_box(q: str, width: int = 70) -> list[str]:
    """Return a list of strings that form a coloured box containing *q*."""
    # Ensure the box is at least as wide as the longest line
    inner_width = max(len(q), width - 4)
    horiz = "─" * inner_width
    top    = colour("┌" + horiz + "┐", BOLD, FG["cyan"])
    bottom = colour("└" + horiz + "┘", BOLD, FG["cyan"])
    empty  = colour("│" + " " * inner_width + "│", BOLD, FG["cyan"])

    # Center the quote
    padded = q.center(inner_width)
    quote_line = colour("│" + padded + "│", BOLD, FG["magenta"])

    return [top, empty, quote_line, empty, bottom]

# ----------------------------------------------------------------------
# Simple "typing" animation
# ----------------------------------------------------------------------
def type_out(lines: list[str], delay: float = 0.03) -> None:
    """Print each line character‑by‑character with a tiny pause."""
    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
        sys.stdout.flush()
        time.sleep(0.1)  # pause between lines

# ----------------------------------------------------------------------
# Main entry point
# ----------------------------------------------------------------------
def main() -> None:
    box = build_box(quote)
    type_out(box)

if __name__ == "__main__":
    main()