"""
Campbell's Soup Can #3018
Produced: 2026-03-28 21:44:59
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys,time

def col(c, txt):
    return f"\033[{c}m{txt}\033[0m"

quote = "I'm not afraid of death; I just don't want to be there when it happens."

art = [
    '   _____________________________',
    '  /                           \\',
    " |  " + quote + "                |",
    ' |                               |',
    ' |   (Neurotic musings of a man)   |',
    '  \\_____________________________/  '
]

colors = [31, 33, 32, 34, 35, 36]  # red, yellow, green, blue, magenta, cyan

for i, line in enumerate(art):
    sys.stdout.write(col(colors[i % len(colors)], line) + "\n")
    sys.stdout.flush()
    time.sleep(0.3)

sys.stdout.write(col(37, "\nEnjoy the existential comedy!\n"))
sys.stdout.flush()