"""
Campbell's Soup Can #3553
Produced: 2026-05-03 18:03:42
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
A tiny console‑art program that prints a single
Woody‑Allen‑style neurotic philosophical quote,
with a splash of colour and a simple animation.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"

# Some nice foreground colours
FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

# Background colours (used for a subtle box)
BG = {
    "dark": "\033[48;5;236m",   # a dark grey background
    "light": "\033[48;5;250m",
}


def colour_text(text: str, fg: str = "white", bg: str = None) -> str:
    """Wrap *text* in ANSI colour codes."""
    seq = FG.get(fg, "")
    if bg:
        seq += BG.get(bg, "")
    return f"{seq}{text}{RESET}"


# ----------------------------------------------------------------------
# The quote and its layout
# ----------------------------------------------------------------------
quote = (
    "I think the meaning of life is like a bad movie: "
    "you keep watching, hoping for a plot twist, "
    "but you realise the director forgot the script."
)

# Split into lines of a given max width
MAX_WIDTH = 58
words = quote.split()
lines = []
current = ""
for w in words:
    if len(current) + len(w) + 1 > MAX_WIDTH:
        lines.append(current)
        current = w
    else:
        current += (" " if current else "") + w
if current:
    lines.append(current)

# Create a "box" around the text
def boxed(lines):
    top = "╔" + "═" * (MAX_WIDTH + 2) + "╗"
    bottom = "╚" + "═" * (MAX_WIDTH + 2) + "╝"
    boxed_lines = [top]
    for line in lines:
        padded = line.ljust(MAX_WIDTH)
        boxed_lines.append(f"║ {padded} ║")
    boxed_lines.append(bottom)
    return boxed_lines


box_lines = boxed(lines)


# ----------------------------------------------------------------------
# Simple animation: fade‑in colour line by line
# ----------------------------------------------------------------------
def animate(lines, delay=0.12):
    """Print *lines* one after another with a colour cycle."""
    colour_cycle = itertools.cycle(["red", "magenta", "blue", "cyan", "green", "yellow"])
    for line in lines:
        fg = next(colour_cycle)
        sys.stdout.write(colour_text(line, fg=fg, bg="dark") + "\n")
        sys.stdout.flush()
        time.sleep(delay)


if __name__ == "__main__":
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    animate(box_lines)
    # Keep the final picture on screen a moment longer
    time.sleep(2)