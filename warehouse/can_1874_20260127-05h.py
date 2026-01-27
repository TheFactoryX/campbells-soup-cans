"""
Campbell's Soup Can #1874
Produced: 2026-01-27 05:44:54
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A tiny Woody‑Allen‑style philosophical monologue,
wrapped in colorful ASCII art and a tiny typing effect.
"""

import sys, time

# ANSI colour codes (feel free to tweak)
HEADER   = "\033[95m"   # magenta
OKBLUE   = "\033[94m"   # blue
OKGREEN  = "\033[92m"   # bright green
WARNING  = "\033[93m"   # bright yellow
FAIL     = "\033[91m"   # bright red
ENDC     = "\033[0m"    # reset

# Helper: print text with optional colour and a tiny delay (typewriter effect)
def animate_print(text: str, delay: float = 0.03, colour: str = ""):
    coloured = f"{colour}{text}{ENDC}" if colour else text
    for ch in coloured:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Woody Allen's favourite existential line (feel free to change)
WOOLY = (
    "I'm not afraid of death; I just don't want to be there when it happens.\n"
    "--- Woody Allen (roughly)"
)

# Print a decorative header
animate_print("\n  ──  A Very Small Existential Thought  ──  ", delay=0.05, colour=HEADER)
time.sleep(0.15)
animate_print("\n🕯️", delay=0.07, colour=OKGREEN)
time.sleep(0.2)

# Animate the quote inside a coloured box
def coloured_box(content: str, delay: float = 0.04):
    """Draw a static box with the given content highlighted."""
    border = f"{OKGREEN}┌─{OKGREEN}{'─'*60}{OKGREEN}┐{ENDC}"
    top    = f"{OKGREEN}│{ENDC}{OKGREEN}{' '*(60)}│{ENDC}"
    quote  = f"{OKGREEN}│ {content.center(60)} │{ENDC}"
    bottom = f"{OKGREEN}│{ENDC}{OKGREEN}{' '*(60)}│{ENDC}"
    bottom = f"{OKGREEN}└─{OKGREEN}{'─'*60}{OKGREEN}┘{ENDC}"
    animate_print(border)
    time.sleep(delay)
    animate_print(top)
    time.sleep(delay)
    animate_print(quote)
    time.sleep(delay)
    animate_print(bottom)

coloured_box(WOOLY, delay=0.04)

# Optional goodbye with a tiny fade‑out effect
for i in range(5, 0, -1):
    animate_print(f"\n   ...{i}...", colour=OKBLUE, delay=0.3)
time.sleep(0.5)
animate_print("\n\n  ──  Thanks for reading the universe ──  ", delay=0.05, colour=FAIL)