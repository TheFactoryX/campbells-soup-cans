"""
Campbell's Soup Can #1142
Produced: 2025-12-24 07:35:13
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

reset = '\033[0m'
colors = [31, 32, 33, 34, 35, 36]  # red, green, yellow, blue, magenta, cyan

def rainbow(s):
    out = ""
    for i, ch in enumerate(s):
        out += f"\033[{colors[i % len(colors)]}m{ch}{reset}"
    return out

quote = "I’m not afraid of death; I just don’t want to be there when it happens."
width = 60
border = "*" * width
inner = f"* {quote} *"

print(rainbow(border))
print(rainbow(inner))
print(rainbow(border))