"""
Campbell's Soup Can #1408
Produced: 2026-01-05 13:51:46
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
import time

# ANSI colour codes (pure Python, no external libs)
RESET = "\033[0m"
BOLD   = "\033[1m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
MAGENTA= "\033[35m"
GREEN  = "\033[32m"

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

def typewriter_print(txt, delay=0.02):
    """Prints text character‑by‑character with a slight delay."""
    for ch in txt:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

# Container dimensions
WIDTH = 60
TOP    = "┌" + "─" * (WIDTH - 2) + "┐"
BOTTOM = "└" + "─" * (WIDTH - 2) + "┘"
MID    = "│" + " " * (WIDTH - 2) + "│"

# Print a colourful box
def draw_box():
    print(BOLD + YELLOW + TOP)
    print(MID)
    # Front‑load the quote with colour changes on each word
    words = quote.split()
    coloured_words = []
    for i, w in enumerate(words):
        colour = [CYAN, MAGENTA, GREEN, YELLOW][i % 4]
        coloured_words.append(colour + w + RESET)
    line = " ".join(coloured_words)
    # Pad to width
    line = line.center(WIDTH - 2)
    print("│ " + line + " │")
    print(MID)
    print(BOLD + YELLOW + BOTTOM)

if __name__ == "__main__":
    draw_box()
    # Optional: animate the quote inside the box
    typewriter_print(BOLD + CYAN + quote + RESET, delay=0.015)