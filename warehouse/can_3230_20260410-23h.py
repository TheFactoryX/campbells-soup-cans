"""
Campbell's Soup Can #3230
Produced: 2026-04-10 23:52:13
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny console show‑time: a Woody‑Allen‑style neurotic
philosophical quote, wrapped in colours and a
flashing ASCII frame.
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

FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}
BG = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    "white": "\033[47m",
}


def colour(text: str, *, fg: str = None, bg: str = None, bold: bool = False, dim: bool = False) -> str:
    parts = []
    if bold:
        parts.append(BOLD)
    if dim:
        parts.append(DIM)
    if fg:
        parts.append(FG.get(fg, ""))
    if bg:
        parts.append(BG.get(bg, ""))
    parts.append(text)
    parts.append(RESET)
    return "".join(parts)


# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑ish)
# ----------------------------------------------------------------------
quote = (
    "I think the meaning of life is like a low‑budget sitcom: "
    "you’re forced to improvise, you forget your lines, "
    "and the audience never shows up for the season finale."
)

# ----------------------------------------------------------------------
# Simple “typewriter” animation
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04) -> None:
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


# ----------------------------------------------------------------------
# Animated flashing frame around the quote
# ----------------------------------------------------------------------
def flashing_frame(lines: list[str], cycles: int = 6, pause: float = 0.3) -> None:
    """Draw a simple box that flashes between two colour schemes."""
    # Pre‑compute the inner width
    width = max(len(line) for line in lines) + 4  # padding + side borders

    top_bottom = lambda c: colour("┌" + "─" * (width - 2) + "┐", **c)
    bottom =     lambda c: colour("└" + "─" * (width - 2) + "┘", **c)
    side =       lambda c, txt: colour("│ " + txt.ljust(width - 4) + " │", **c)

    palettes = [
        {"fg": "yellow", "bg": "blue", "bold": True},
        {"fg": "magenta", "bg": "black", "bold": False},
    ]

    for i in range(cycles):
        palette = palettes[i % len(palettes)]
        sys.stdout.write("\n")
        sys.stdout.write(top_bottom(palette) + "\n")
        for line in lines:
            sys.stdout.write(side(palette, line) + "\n")
        sys.stdout.write(bottom(palette) + "\n")
        sys.stdout.flush()
        time.sleep(pause)
        # erase the box (move cursor up)
        for _ in range(len(lines) + 3):
            sys.stdout.write("\033[F")  # cursor up one line
            sys.stdout.write("\033[K")  # erase line


# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main() -> None:
    # Split the quote into a nicely wrapped list of lines (max 58 chars)
    max_len = 58
    words = quote.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > max_len:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # First, a flashing intro
    intro = colour("~ * * * ~", fg="cyan", bold=True)
    for _ in range(3):
        sys.stdout.write("\r" + intro)
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r" + " " * len(intro))
        sys.stdout.flush()
        time.sleep(0.2)

    # Show the animated box with the quote
    flashing_frame(lines, cycles=8, pause=0.25)

    # Finally, type out the quote in a calm colour
    sys.stdout.write("\n")
    typewriter(colour(quote, fg="white", bg="black", dim=True), delay=0.015)

    # A little closing flourish
    sys.stdout.write(colour("\n— Woody Allen (probably)\n", fg="green", bold=True))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)