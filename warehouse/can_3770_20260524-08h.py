"""
Campbell's Soup Can #3770
Produced: 2026-05-24 08:00:20
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys,time

# Woody Allen‑style philosophical quipquote = "I'm not afraid of death; I just don't want to be there when it happens."

# ANSI colour codes
RED    = "\033[91m"
GREEN  = "\033[92m"
RESET  = "\033[0m"

def make_box(txt):
    w = len(txt) + 4
    top    = RED  + '+' + '-' * w + '+' + RESET
    middle = GREEN + f'| {txt} |' + RESET
    bot    = RED  + '+' + '-' * w + '+' + RESET
    return (top, middle, bot)

box = make_box(quote)

# Typewriter‑style reveal for visual flair
for line in box:
    sys.stdout.write(line + '\n')
    sys.stdout.flush()
    time.sleep(0.07)