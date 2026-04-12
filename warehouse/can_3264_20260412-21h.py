"""
Campbell's Soup Can #3264
Produced: 2026-04-12 21:50:48
Worker: Free Models Router (openrouter/free)
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
import time
import itertools

# ----------------------------------------------------------------------
# ANSI color helpers
# ----------------------------------------------------------------------
CSI = "\033["
RESET = CSI + "0m"

def color(code):
    return CSI + str(code) + "m"

RED = color(31)
GREEN = color(32)
YELLOW = color(33)
BLUE = color(34)
MAGENTA = color(35)
CYAN = color(36)
WHITE = color(37)
BRIGHT = CSI + "1m"

# ----------------------------------------------------------------------
# Fancy box drawing
# ----------------------------------------------------------------------
TOP_LEFT = "╔"
TOP_RIGHT = "╗"
BOTTOM_LEFT = "╚"
BOTTOM_RIGHT = "╝"
HORIZONTAL = "═"
VERTICAL = "║"

def boxed(lines, fg=CYAN, bg=""):
    """Return a string that draws `lines` inside a coloured box."""
    width = max(len(line) for line in lines)
    top = fg + bg + TOP_LEFT + HORIZONTAL * (width + 2) + TOP_RIGHT + RESET
    bottom = fg + bg + BOTTOM_LEFT + HORIZONTAL * (width + 2) + BOTTOM_RIGHT + RESET
    middle = []
    for line in lines:
        padded = line + " " * (width - len(line))
        middle.append(fg + bg + VERTICAL + RESET + " " + padded + " " + fg + bg + VERTICAL + RESET)
    return "\n".join([top] + middle + [bottom])

# ----------------------------------------------------------------------
# The quote (Woody‑Allen‑ish)
# ----------------------------------------------------------------------
quote = (
    "I told my therapist I was afraid of my own thoughts. "
    "She said, \"That's normal; most people are scared "
    "of the bills they'd get for thinking too much.\""
)

# split for nicer layout
words = quote.split()
lines = []
current = ""
for w in words:
    if len(current) + len(w) + 1 > 60:
        lines.append(current)
        current = w
    else:
        current = (current + " " + w).strip()
if current:
    lines.append(current)

# ----------------------------------------------------------------------
# Animation: typewriter effect with a little flicker
# ----------------------------------------------------------------------
def typewriter(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def flicker_effect(line, repeats=3, pause=0.2):
    """Briefly flash the line in a brighter colour."""
    for _ in range(repeats):
        sys.stdout.write(BRIGHT + GREEN + line + RESET + "\r")
        sys.stdout.flush()
        time.sleep(pause/2)
        sys.stdout.write(" " * len(line) + "\r")
        sys.stdout.flush()
        time.sleep(pause/2)

# ----------------------------------------------------------------------
# Main display
# ----------------------------------------------------------------------
def main():
    # Clear screen
    sys.stdout.write(CSI + "2J" + CSI + "H")
    sys.stdout.flush()

    # Print the boxed quote with a soft cyan border
    boxed_text = boxed(lines, fg=CYAN)
    for line in boxed_text.split("\n"):
        typewriter(line + "\n", delay=0.005)

    # Small pause before the "punch line" flash
    time.sleep(0.6)

    # Flash the last line (the punch line) in bright green a few times
    punch = lines[-1]
    padded = " " * (len(punch) - len(punch.lstrip())) + punch  # keep original indent
    flicker_effect(padded, repeats=4, pause=0.15)

    # End with a gentle fade out (just wait a moment)
    time.sleep(0.8)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)