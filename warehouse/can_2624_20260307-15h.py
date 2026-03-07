"""
Campbell's Soup Can #2624
Produced: 2026-03-07 15:37:18
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'

def rainbow_print(s, delay=0.04):
    """Prints text with a cycling rainbow of colors for visual fun."""
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for i, ch in enumerate(s):
        color = colors[i % len(colors)]
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Woody Allen‑style philosophical quote (self‑deprecating & existential)
quote = ("Life is like an old sweater: it looks cozy and familiar, "
         "but eventually it unravels, leaving you wondering "
         "if the wear was worth the warmth.")

# Simple ASCII box with a twist
box_top    = "┌───────────────────────────────────────────────┐"
box_mid    = "│                                               │"
box_bottom = "└───────────────────────────────────────────────┘"

# Print the wrapper with color cycling
rainbow_print(box_top)
rainbow_print(box_mid)
rainbow_print(f"{BLUE}{' ' + quote + ' '}{RESET}")
rainbow_print(box_mid)
rainbow_print(box_bottom)

# A tiny celebratory sparkle animation to finish the show
sparkle = "✨"
for _ in range(2):
    rainbow_print(sparkle, delay=0.25)