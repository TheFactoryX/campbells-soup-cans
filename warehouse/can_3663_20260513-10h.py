"""
Campbell's Soup Can #3663
Produced: 2026-05-13 10:43:26
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny, colorful, animated display of a single
Woody‑Allen‑style philosophical gem.
Run the script directly – no external libraries required.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour definitions (foreground)
# ----------------------------------------------------------------------
FG = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "reset": "\033[0m",
}
# Background colours (just a few for fun)
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

# ----------------------------------------------------------------------
# The quote – feel free to modify the text if you like
# ----------------------------------------------------------------------
QUOTE = (
    "I think, therefore I panic.  "
    "If life is a rehearsal, the director must have lost the script."
)

# ----------------------------------------------------------------------
# Helper: print a line with a typewriter effect
# ----------------------------------------------------------------------
def type_line(text: str, delay: float = 0.03, colour=FG["cyan"]):
    for ch in text:
        sys.stdout.write(colour + ch + FG["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Helper: draw a colourful box around the quote
# ----------------------------------------------------------------------
def draw_box(text: str):
    lines = text.split("\n")
    width = max(len(line) for line in lines) + 2   # padding

    # Choose a rotating colour sequence for the border
    border_cols = itertools.cycle([FG["red"], FG["green"], FG["yellow"], FG["blue"], FG["magenta"], FG["cyan"]])

    top = next(border_cols) + "┌" + "─" * width + "┐" + FG["reset"]
    bottom = next(border_cols) + "└" + "─" * width + "┘" + FG["reset"]
    side_col = next(border_cols)

    print(top)
    for line in lines:
        padded = f" {line.ljust(width-1)}"
        print(f"{side_col}│{FG['reset']}{padded}{side_col}│{FG['reset']}")
    print(bottom)

# ----------------------------------------------------------------------
# Main animation sequence
# ----------------------------------------------------------------------
def main():
    # Fade‑in background colour (just a simple trick)
    for bg in [BG["black"], BG["blue"], BG["magenta"], BG["cyan"]]:
        sys.stdout.write(bg)
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write(FG["reset"])  # ensure we start clean

    # Animated introduction
    intro = ">>> A philosophical nugget, Woody‑Allen style <<<"
    type_line(intro, delay=0.04, colour=FG["yellow"])
    time.sleep(0.6)

    # Print the box with the quote
    draw_box(QUOTE)

    # Typewriter the quote itself (inside the box we already saw it, but this adds flair)
    time.sleep(0.5)
    type_line(QUOTE, delay=0.02, colour=FG["white"])

    # Outro
    outro = "— End of the existential crisis —"
    type_line(outro, delay=0.05, colour=FG["green"])

    # Reset colours before exiting
    sys.stdout.write(FG["reset"] + BG["reset"])
    sys.stdout.flush()


if __name__ == "__main__":
    main()