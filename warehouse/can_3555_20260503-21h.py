"""
Campbell's Soup Can #3555
Produced: 2026-05-03 21:02:58
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
A little colorful, animated Woody‑Allen‑style philosophical quote.
Run directly – no external packages required.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# some pleasant pastel colours
COLORS = [
    "\033[38;5;208m",  # orange
    "\033[38;5;219m",  # pink
    "\033[38;5;45m",   # cyan
    "\033[38;5;39m",   # blue
    "\033[38;5;155m",  # light green
]

def colour_cycle():
    """Yield colours forever, rotating through the list."""
    while True:
        for c in COLORS:
            yield c

# ----------------------------------------------------------------------
# Pretty‑box drawing
# ----------------------------------------------------------------------
def draw_box(text_lines, colour):
    """Print a simple box around the given lines with the supplied colour."""
    width = max(len(line) for line in text_lines) + 4   # padding
    top    = colour + "╔" + "═" * (width - 2) + "╗" + RESET
    bottom = colour + "╚" + "═" * (width - 2) + "╝" + RESET
    side   = colour + "║" + RESET

    sys.stdout.write(top + "\n")
    for line in text_lines:
        padded = f"  {line}{' ' * (width - len(line) - 4)}  "
        sys.stdout.write(f"{side}{padded}{side}\n")
    sys.stdout.write(bottom + "\n")

# ----------------------------------------------------------------------
# Animated typing effect
# ----------------------------------------------------------------------
def type_out(message, colour, delay=0.04):
    """Print `message` one character at a time in the given colour."""
    for ch in message:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Main program
# ----------------------------------------------------------------------
def main():
    quote = (
        "I think the universe has a sense of humor — "
        "it gave us free will just so we’d waste it "
        "arguing about whether it exists."
    )
    # split into lines that fit nicely inside the box
    words = quote.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > 48:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # colour animation
    col_gen = colour_cycle()
    border_colour = next(col_gen)

    # draw the decorative box (static)
    draw_box(lines, border_colour)

    # now type the quote line‑by‑line with a shifting colour
    for line in lines:
        type_out(line, next(col_gen), delay=0.03)
        time.sleep(0.2)       # short pause between lines

    # final flourish
    sys.stdout.write("\n")
    for _ in range(3):
        sys.stdout.write(next(col_gen) + BOLD + "« " + RESET)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)