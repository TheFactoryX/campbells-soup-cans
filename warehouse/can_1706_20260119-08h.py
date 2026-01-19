"""
Campbell's Soup Can #1706
Produced: 2026-01-19 08:50:36
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

def typewriter(s, speed=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write('\n')
    sys.stdout.flush()

def col(s, code):
    return f"\033[{code}m{s}\033[0m"

quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = " — Woody Allen (sort of)"

WIDTH = 70
INNER = WIDTH - 2
border_top = "╔" + "═"*INNER + "╗"
border_mid = "╠" + "─"*INNER + "╣"
border_bot = "╚" + "═"*INNER + "╝"

def make_line(text):
    return "║" + text.ljust(INNER) + "║"

lines = [
    border_top,
    make_line(f"\"{quote}\""),
    border_mid,
    make_line(author),
    border_bot
]

color_codes = ["92", "93", "92", "96", "92"]  # green, yellow, green, cyan, green

for line, code in zip(lines, color_codes):
    typewriter(col(line, code))