"""
Campbell's Soup Can #2321
Produced: 2026-02-19 20:49:48
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

import time, sys

# ANSI colour codes
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# ------------------------------------------------------------
def typewriter(text, delay=0.03):
    """Prints text character‑by‑character (typewriter effect)."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

# ------------------------------------------------------------
quote = (
    "\"I'm not afraid of death; I just don't want to be there when it happens.\""
)
author = " — Woody Allen (but it's actually a fake)"

# Determine box width (add a little padding)
padding = 2
box_width = max(len(quote), len(author)) + padding * 2 + 4  # extra space for border chars

# Build the top/bottom borders
top    = "┌" + "─" * (box_width - 2) + "┐"
bottom = "└" + "─" * (box_width - 2) + "┘"

# Helper to centre a line inside the box
def centre(line, width):
    return " " * ((width - len(line)) // 2) + line + " " * ((width - len(line) + 1) // 2)

# ------------------------------------------------------------
print(GREEN + top + RESET)
print(
    YELLOW +
    f"│{centre(quote, box_width - 4)}│" +
    RESET
)
print(
    YELLOW +
    f"│{centre(author, box_width - 4)}│" +
    RESET
)
print(GREEN + bottom + RESET)

# ------------------------------------------------------------
# Add a tiny "sparkle" animation around the box
sparkle = CYAN + "*" * 10 + RESET
for i in range(3):
    sys.stdout.write(sparkle)
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write("\b" * len(sparkle))  # erase
    # Cycle colours for next sparkle
    if i == 0:
        sparkle = MAGENTA + "*" * 10 + RESET
    elif i == 1:
        sparkle = YELLOW + "*" * 10 + RESET
    else:
        sparkle = GREEN + "*" * 10 + RESET

# ------------------------------------------------------------
# Final funny flourish
typewriter("\nEnjoy the absurdity.\n", delay=0.05)