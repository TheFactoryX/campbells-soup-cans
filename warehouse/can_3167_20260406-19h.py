"""
Campbell's Soup Can #3167
Produced: 2026-04-06 19:19:40
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

import sys, time

# ------------------------------------------------------------
# ANSI colour codes (no external libraries needed)
# ------------------------------------------------------------
RESET  = "\033[0m"
BOLD   = "\033[1m"
CYAN   = "\033[36m"
YELLOW = "\033[33m"
MAGENTA= "\033[35m"

# ------------------------------------------------------------
# The Woody Allen‑style philosophical quote
# ------------------------------------------------------------
quote = (
    "I’m not afraid of death; I just don’t want to be there when it happens… "
    "and I’m terrified I’ll miss my own funeral because I’m stuck in traffic "
    "in the afterlife."
)

# ------------------------------------------------------------
# Simple typing animation (carriage‑return trick)
# ------------------------------------------------------------
def animate_print(text, delay=0.03):
    """Print `text` character‑by‑character with a short pause."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ------------------------------------------------------------
# Build a colourful ASCII‑art box around the quote
# ------------------------------------------------------------
box_width = 70
top    = f"{YELLOW}{BOLD}╔{'=' * (box_width - 2)}╗{RESET}"
bottom = f"{YELLOW}{BOLD}╚{'=' * (box_width - 2)}╝{RESET}"
empty  = " " * (box_width - 2)
mid_left  = f"{CYAN}{BOLD}║{RESET}"
mid_right = f"{CYAN}{BOLD}║{RESET}"

# ------------------------------------------------------------
# Print everything
# ------------------------------------------------------------
# 1️⃣  Intro line (plain, just to set the stage)
print("\n" + "A neurotic musement from the mind of Woody Allen:\n")

# 2️⃣  The coloured box
print(top)
print(mid_left + empty + mid_right)                                 # empty line
print(
    mid_left
    + " " + Magenta + quote + RESET                                   # coloured quote line
    + " " * (box_width - len(mid_left) - len(mid_right) - 2 - len(quote))
    + mid_right
)
print(mid_left + empty + mid_right)                                 # empty line
print(bottom)

# 3️⃣  A tiny “thought bubble” animation after the boxtime.sleep(0.5)
print("\n" + CYAN + "..." + RESET + " " + MAGENTA + "💭" + RESET + "\n")
time.sleep(0.5)
animate_print("Thanks for listening.", delay=0.05)