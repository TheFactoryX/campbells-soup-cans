"""
Campbell's Soup Can #1930
Produced: 2026-01-29 19:44:47
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
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

# ------------------------------------------------------------
# WOODY ALLEN STYLE QUOTE (Self‑deprecating, neurotic, existential)
# ------------------------------------------------------------
QUOTE = (
    "I'm not afraid of death; I just don't want to be there "
    "when it happens."
)

# ------------------------------------------------------------
# Helper: wrap text in ANSI colour codes (no external libs)
# ------------------------------------------------------------
def col(text, code):
    """Return `text` wrapped in an ANSI colour sequence."""
    return f"\033[{code}m{text}\033[0m"

# ------------------------------------------------------------
# Visual framing – a coloured box with the quote inside
# ------------------------------------------------------------
WIDTH = 70
TOP_BORDER   = col("═" * WIDTH, 90)                     # bright white/gray
BOTTOM_BORDER = TOP_BORDER
MID_BORDER    = col("║", 90) + col("  ", 90)

# Build the middle line: a pipe, two spaces, the quote, two spaces, a pipe
MID_LINE = col(f"{MID_BORDER}  {QUOTE}  ", 33)        # yellow for the text

# ------------------------------------------------------------
# Print everything – the whole thing is a single, self‑contained
# Python script that can be run directly from the command line.
# ------------------------------------------------------------
def main():
    sys.stdout.write(TOP_BORDER + "\n")
    sys.stdout.write(MID_LINE + "\n")
    sys.stdout.write(BOTTOM_BORDER + "\n")

if __name__ == "__main__":
    main()