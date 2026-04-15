"""
Campbell's Soup Can #3293
Produced: 2026-04-15 03:41:31
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
A tiny, self‑contained script that prints a single
Woody‑Allen‑style philosophical quip with a splash of color
and a pleasant “type‑writer” animation.

Run it directly:
    $ python3 woody_quote.py
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# A short palette: cyan, magenta, yellow, white
PALETTE = [
    "\033[96m",  # bright cyan
    "\033[95m",  # bright magenta
    "\033[93m",  # bright yellow
    "\033[97m",  # bright white
]

def rainbow_cycle():
    """Yield colours in an endless cycle."""
    while True:
        for c in PALETTE:
            yield c

# ----------------------------------------------------------------------
# ASCII art "frame"
# ----------------------------------------------------------------------
FRAME_TOP = r"""
┌───────────────────────────────────────────────────────────────┐
│                                                               │
""".strip("\n")

FRAME_BOTTOM = r"""
│                                                               │
└───────────────────────────────────────────────────────────────┘
""".strip("\n")

# ----------------------------------------------------------------------
# The quote – feel free to tweak the wording
# ----------------------------------------------------------------------
QUOTE = (
    "I fear that my existence is like a pretzel—twisted, "
    "over‑cooked, and doomed to be eaten by the inevitable."
)

# ----------------------------------------------------------------------
# Type‑writer animation
# ----------------------------------------------------------------------
def type_writer(text, delay=0.045):
    """Print *text* one character at a time, using a rotating colour."""
    colour_gen = rainbow_cycle()
    for ch in text:
        colour = next(colour_gen)
        sys.stdout.write(f"{colour}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# Main entry point
# ----------------------------------------------------------------------
def main():
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")

    # Print top border
    print(FRAME_TOP)

    # Center the quote line inside the frame (width = 63)
    width = 63
    lines = []
    # simple word‑wrap
    words = QUOTE.split()
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 > width - 4:  # leave padding
            lines.append(cur.rstrip())
            cur = ""
        cur += w + " "
    if cur:
        lines.append(cur.rstrip())

    # Print each wrapped line with animation
    for line in lines:
        padded = f"  {line:<{width-4}}  "   # 2 spaces margin each side
        sys.stdout.write("│")
        type_writer(padded, delay=0.03)
        sys.stdout.write("│\n")

    # Print bottom border
    print(FRAME_BOTTOM)

    # A final pause so the user can savour the colors
    time.sleep(1.5)

if __name__ == "__main__":
    main()