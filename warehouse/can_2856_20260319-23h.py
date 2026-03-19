"""
Campbell's Soup Can #2856
Produced: 2026-03-19 23:44:39
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# -*- coding: utf-8 -*-
# Woody Allen style philosophical quote in a colorful animated box
quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = " — Woody Allen"

# ANSI bright foreground color codes
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
MAGENTA= "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
RESET  = "\033[0m"

def make_box(text, border_col, text_col):
    """Return a colored boxed string around *text*."""
    lines = text.splitlines()
    width = max(len(l) for l in lines)          # longest line length
    # top and bottom borders
    top    = border_col + "┌" + "─" * (width + 2) + "┐" + RESET
    bottom = border_col + "└" + "─" * (width + 2) + "┘" + RESET
    # middle lines with text alignment
    middle = [text_col + f"│ {l:<{width}} │" + RESET for l in lines]
    return "\n".join([top] + middle + [bottom])

# Three animation frames with different color schemes
frame1 = make_box(quote + "\n" + author, RED,    YELLOW)
frame2 = make_box(quote + "\n" + author, GREEN,  CYAN)
frame3 = make_box(quote + "\n" + author, MAGENTA, WHITE)

# Animation utilities
import time, sys

def clear():
    """Clear the terminal screen (ANSI escape code)."""
    print("\033[2J", end="")
    sys.stdout.flush()

# Simple animated display
clear()
print(frame1)
time.sleep(1.2)
clear()
print(frame2)
time.sleep(1.2)
clear()
print(frame3)