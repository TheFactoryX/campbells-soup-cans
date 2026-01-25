"""
Campbell's Soup Can #1838
Produced: 2026-01-25 13:03:43
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

# ANSI color palette
COL = {
    "reset": "\033[0m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "magenta": "\033[95m",
    "green": "\033[92m",
    "blue": "\033[94m",
}

def cprint(txt, color="reset"):
    """Print text with an ANSI color."""
    sys.stdout.write(COL.get(color, "") + txt + COL["reset"] + "\n")

# ----- Woody Allen‑style existential punchline -----
quote = "I’m not afraid of death; I just don’t want to be there when it happens."
border = "┌───────────────────────────────────────────────────────┐"
inner  = "│                                                   │"

# Build the framed layout
frame = [
    border,
    inner,
    f"│ {quote} │",
    inner,
    border,
]

# ----- Fancy typing animation for the quote line -----
def typewriter(line, delay=0.03):
    for i in range(len(line)):
        sys.stdout.write("\r" + line[:i+1])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# ----- Print everything with colors -----
cprint(border, "cyan")
cprint(inner, "cyan")

# Animate the quote line in bright yellow
cprint(f"│ {quote} │", "yellow")
typewriter(f"│ {quote} │", delay=0.02)

cprint(inner, "cyan")
cprint(border, "cyan")

# A tinyfooter with a wink
cprint("\n   Embrace the absurd – it’s the only thing that makes sense.\n", "magenta")