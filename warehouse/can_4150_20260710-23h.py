"""
Campbell's Soup Can #4150
Produced: 2026-07-10 23:15:49
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

quote = "I don't want immortality through my work; I want it through not dying."
border = "+" + "-" * 62 + "+"
colors = ['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m']

def rainbow_print(s):
    for i,ch in enumerate(s):
        sys.stdout.write(colors[i%len(colors)] + ch + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.03)
    print()

print(colors[0] + border + '\033[0m')
rainbow_print(quote)
print(colors[0] + border + '\033[0m')