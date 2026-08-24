"""
Campbell's Soup Can #4803
Produced: 2026-08-24 05:01:37
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

quote = "I'm not afraid of death; I just don't want to be there when it happens."
colors = [31, 32, 33, 34, 35, 36]  # red, green, yellow, blue, magenta, cyan

# simple spinner (no words)
for s in "|/-\\":
    sys.stdout.write("\r" + s)
    sys.stdout.flush()
    time.sleep(0.2)

clear()

# top border
sys.stdout.write("\033[90m+{}-\n".format("-" * (len(quote) + 2)))
# each character with a cycling color
for i, ch in enumerate(quote):
    sys.stdout.write("\033[{}m{}\033[0m".format(colors[i % len(colors)], ch))
sys.stdout.write("\n+{}-\n".format("-" * (len(quote) + 2)))
sys.stdout.flush()