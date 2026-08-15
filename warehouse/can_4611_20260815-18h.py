"""
Campbell's Soup Can #4611
Produced: 2026-08-15 18:47:14
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, os

# ---------- ANSI color codes ----------
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# ---------- Data ----------
quote = (
    "I don't want to achieve immortality through my work; "
    "I want to achieve it through simply not dying."
)

# ---------- Visual helpers ----------
def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def rainbow(s):
    """Print a string with each character in a cycling rainbow of colors."""
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for i, ch in enumerate(s):
        sys.stdout.write(colors[i % len(colors)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.02)          # tiny pause for effect
    sys.stdout.write("\n")

def border(width=60):
    """Return a string of `width` asterisks."""
    return "*" * width

# ---------- Main visualisation ----------
clear()
print("\n" * 3)

# Top border
print(RED + border() + RESET)
# Centered title
title = "WOODY ALLEN'S PHILOSOPHY"
print(
    RED
    + f"* {title.center(58)} *"
    + RESET
)
print(RED + border() + RESET)

# The quote, typed with rainbow colors
rainbow(quote)

# Bottom border
print(RED + border() + RESET)

# Small reflective line after a brief pause
time.sleep(0.5)
print(CYAN + "Stay neurotic! Stay alive!" + RESET)