"""
Campbell's Soup Can #1512
Produced: 2026-01-10 07:30:49
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

quote = "I'm not afraid of death; I just don't want to be there when it happens."
width = len(quote) + 4
border = "+" + "-" * width + "+"
middle = "| " + quote + " |"

def typewriter(s, delay=0.02):
    for ch in s:
        sys.stdout.write("\033[93m" + ch + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

typewriter(border)
typewriter(middle)
typewriter(border)