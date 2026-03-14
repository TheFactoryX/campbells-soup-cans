"""
Campbell's Soup Can #2767
Produced: 2026-03-14 17:44:20
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

# ANSI colorpalette
COLORS = [
    "\033[91m",  # bright red    "\033[92m",  # bright green
    "\033[93m",  # bright yellow    "\033[94m",  # bright blue
    "\033[95m",  # bright magenta
]
RESET = "\033[0m"

# ASCII art components
TOP    = "╔═══════════════════════════════════════╗"
BOTTOM = "╚═══════════════════════════════════════╝"
QUOTE  = [
    "║  \"I'm not afraid of death; I just  \"",
    "║   don't want to be there when it   \"",
    "║        happens.\"                  ",
    "║ — Woody Allen (kind of)          ",
    BOTTOM
]

def display(color):
    """Print the whole block wrapped in the given ANSI color."""
    sys.stdout.write(color + TOP + "\n")
    for line in QUOTE[:-1]:
        sys.stdout.write(color + line + "\n")
    sys.stdout.write(color + BOTTOM + "\n")

# Simple flashing animation
for _ in range(2):
    for c in COLORS:
        display(c)
        time.sleep(0.3)

# Final steady display in bright cyan
display("\033[96m")