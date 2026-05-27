"""
Campbell's Soup Can #3799
Produced: 2026-05-27 19:32:55
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
A tiny on‑screen theater for a Woody‑Allen‑style existential one‑liner.
It types out a neon‑colored quote inside a whimsical ASCII frame.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
# Some pastel/neon tones that look decent on most terminals
COLORS = [
    "\033[38;5;208m",  # orange
    "\033[38;5;45m",   # cyan
    "\033[38;5;219m",  # pink
    "\033[38;5;82m",   # green
    "\033[38;5;225m",  # magenta
]

def colour_cycle():
    """Yield colours endlessly."""
    while True:
        for c in COLORS:
            yield c

# ----------------------------------------------------------------------
# ASCII frame utilities
# ----------------------------------------------------------------------
TOP_LEFT, TOP_RIGHT = "╔", "╗"
BOTTOM_LEFT, BOTTOM_RIGHT = "╚", "╝"
HORIZ, VERT = "═", "║"

def framed_lines(text_lines, padding=2):
    """Wrap a list of strings in a colourful box."""
    max_len = max(len(line) for line in text_lines)
    width = max_len + padding * 2
    top = TOP_LEFT + HORIZ * width + TOP_RIGHT
    bottom = BOTTOM_LEFT + HORIZ * width + BOTTOM_RIGHT
    # Build middle rows
    middle = []
    for line in text_lines:
        spaces = " " * (width - len(line) - padding)
        middle.append(f"{VERT}{' ' * padding}{line}{spaces}{' ' * padding}{VERT}")
    return [top] + middle + [bottom]

# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑style)
# ----------------------------------------------------------------------
quote = (
    "I told my therapist that I’m terrified of the meaning of life… "
    "she said, “That’s a very common fear. "
    "Did you also forget to buy milk?”"
)

# Split into manageable width for the frame
def wrap(text, width=50):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())
    return lines

# ----------------------------------------------------------------------
# Animation: typewriter effect with colour cycling
# ----------------------------------------------------------------------
def typewriter(lines, delay=0.03):
    colour_gen = colour_cycle()
    for line in lines:
        for ch in line:
            sys.stdout.write(next(colour_gen) + ch + RESET)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
        sys.stdout.flush()
        # Slight pause at line breaks
        time.sleep(delay * 10)

def main():
    # Prepare the visual box
    wrapped = wrap(quote, width=48)
    boxed = framed_lines(wrapped, padding=3)

    # Clear screen (ANSI) and move cursor to centre (roughly)
    sys.stdout.write("\033[2J\033[H")  # clear screen + home
    sys.stdout.flush()

    # Animate inside the box
    typewriter(boxed, delay=0.02)

    # End with a gentle flash
    for _ in range(2):
        sys.stdout.write("\033[5m")  # blink on
        time.sleep(0.1)
        sys.stdout.write("\033[25m")  # blink off
        time.sleep(0.1)

    sys.stdout.write("\n")  # final newline
    sys.stdout.flush()

if __name__ == "__main__":
    main()