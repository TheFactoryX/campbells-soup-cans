"""
Campbell's Soup Can #3525
Produced: 2026-05-01 22:06:00
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time

RESET = '\033[0m'
RED   = '\033[31m'
CYAN  = '\033[36m'

quote = "i'm not afraid of dying; i just keep wondering if my life will finally get a decent punchline before the curtain falls."

def draw_boxed(text):
    lines = text.split('\n')
    max_len = max(len(l) for l in lines)
    top = f"+{'-'*(max_len+2)}+"
    print(RED + top)
    for l in lines:
        print(f"| {CYAN}{l.ljust(max_len)} {RED}|")
    print(RESET + top)

if __name__ == "__main__":
    time.sleep(0.4)          # tiny pause for dramatic effect
    draw_boxed(quote)