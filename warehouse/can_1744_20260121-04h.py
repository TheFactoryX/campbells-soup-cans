"""
Campbell's Soup Can #1744
Produced: 2026-01-21 04:14:51
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

def col(txt, code): return f"\033[{code}m{txt}\033[0m"
def typewriter(txt, delay=0.03):
    for ch in txt:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    sys.stdout.write("\n")

quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = " — Woody Allen (maybe)"

border = col("+" + "-" * 58 + "+", 93)          # bright yellow
empty  = col("|" + " " * 58 + "|", 97)          # white
line1  = col("|  " + quote + "  |", 93)        # bright yellow
line2  = col("| " + author + " " + ' ' * 45 + "|", 96)  # bright cyan

def frame():
    lines = [border, empty, line1, line2, empty, border]
    for l in lines:
        typewriter(l, 0.04)

frame()