"""
Campbell's Soup Can #3715
Produced: 2026-05-17 22:08:35
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, itertools, time

quote = "I'm not afraid of death—I just don't want to be there when the universe finally decides to reboot itself."

def rainbow_print(s):
    colors = itertools.cycle([31, 32, 33, 34, 35, 36])  # red, green, yellow, blue, magenta, cyan
    for ch in s:
        sys.stdout.write(f"\033[{next(colors)}m{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

rainbow_print(quote)