"""
Campbell's Soup Can #3768
Produced: 2026-05-24 00:12:38
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time

RED   = "\033[31m"
YELLOW= "\033[33m"
RESET = "\033[0m"

quote = [
    "I’m not afraid of death; I just don’t want to be there when it happens.",
    " — Woody Allen",
    "Life’s a joke, and the punchline is you’re still trying",
    "to understand why you’re laughing at the punchline."
]

WIDTH = 68

top    = RED + "┌" + "─"*(WIDTH-2) + "┐" + RESETbottom = RED + "└" + "─"*(WIDTH-2) + "┘" + RESET

print(top)
for line in quote:
    padded = line.center(WIDTH-4)
    print("│ " + YELLOW + padded + RESET + " │")
    time.sleep(0.4)
print(bottom)
print(RESET, end='')