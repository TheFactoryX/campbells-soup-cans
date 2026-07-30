"""
Campbell's Soup Can #4381
Produced: 2026-07-30 20:34:20
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken, missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random

COLORS = ['\033[38;5;220m', '\033[38;5;117m', '\033[38;5;27m', '\033[38;5;31m', '\033[m']
CARS = [
    ('\\_/', "',o|o' '("),
    (' o ', "+---|'),
    ('_ _', "`---'`)
]

def animate_car(pos, side):
    return next(
        (CARS[i] for i in range(len(CARS)))
        if pos < len(CARS)
        else CARS[-1]
    )

QUOTE = "I realized just last Tuesday\nthat the universe is a cryptocurrency scam:\nwe mine data, spend attention,\nand pray the cosmic blockchain holds."
PREVIEW = [
    (