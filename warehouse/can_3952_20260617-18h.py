"""
Campbell's Soup Can #3952
Produced: 2026-06-17 18:34:37
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

cyan  = "\033[36m"
yellow = "\033[33m"
reset = "\033[0m"

quote = "I'm not afraid of death; I just don't want to be there when it happens."
width = 78

border = cyan + "╔" + "═"*(width-4) + "╗" + resetinner  = cyan + "║ " + yellow + quote.center(width-4) + cyan + " ║" + reset

def typewriter(s, delay=0.03):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print(border, end='', flush=True)
typewriter(inner)
print(border)