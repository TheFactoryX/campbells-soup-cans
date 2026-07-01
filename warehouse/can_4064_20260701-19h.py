"""
Campbell's Soup Can #4064
Produced: 2026-07-01 19:11:54
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# Woodie Allen's philosophical quote
quote = "I don't want to describe a world where human purpose is extinct, just one where it's fantastically useless."

# Print setup
colors = [31, 35, 32, 36, 33]
print("\033[H\033[J", end="")
print("\033[33m┌───────────────────────────┐\033[m")
print("\033[31m│\033[37m             ", end="")
print("\033[36m" + '|'.join([''] * len(quote) // 2 + [quote] + [''] * len(quote) // 2 + ['\033[37m']).center(60),
      end="")
print("\033[35m│\033[m")
print("\033[33m│\033[37m             ", end="")
print("\033[36m" + '|'.join([''] * len(quote) // 2 + [quote[::-1]] + [''] * len(quote) // 2 + ['\033[37m']).center(60),
      end="")
print("\033[31m│\033[33m    \033[34mV\033[m\033[37m\033[35m\033[m\033[33m│\033[m")
time.sleep(0.5)
for i in range(len(quote)):
    print("\033[33m|", end="")
    for j in range(len(quote)):
        if random.randint(0, 10) < 5:
            print("\033[35m▓", end="")
        else:
            print("\033[37m░", end="")
    print("\033[33m|\033[m")
    time.sleep(0.1)
print("\033[33m└───────────────────────────┘\033[m")
print()
time.sleep(1)
for c in colors:
    print("\033[3" + str(c) + "m" + quote + "\033[m")