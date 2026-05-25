"""
Campbell's Soup Can #3786
Produced: 2026-05-25 19:58:56
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

def typewriter(s, speed=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()

quote = "I'm not afraid of death; I just don't want to be there when it happens, and also I'm terrified of being dead."
box_top    = "+" + "-" * (len(quote) + 2) + "+"
box_mid    = "| " + quote + " |"
box_bottom = "+" + "-" * (len(quote) + 2) + "+"

color_codes = ["31","33","32","34","35","36"]

def colored(text, code):
    return f"\033[{code}m{text}\033[0m"

for i, line in enumerate([box_top, box_mid, box_bottom]):
    print(colored(line, color_codes[i]))

time.sleep(0.5)
typewriter(colored(quote, "36"))