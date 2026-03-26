"""
Campbell's Soup Can #2980
Produced: 2026-03-26 20:55:19
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (nvidia/nemotron-3-nano-30b-a3b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

ESC = "\033["
RESET = ESC + "0m"
RED = ESC + "31m"
GREEN = ESC + "32m"
YELLOW = ESC + "33m"
MAGENTA = ESC + "35m"
CYAN = ESC + "36m"

WIDTH = 45

def col(s, *attrs):
    return ESC + "".join(str(a) for a in attrs) + s + RESET

top = col("╔" + "═"*WIDTH + "╗", CYAN)
quote = "I’m not afraid of death; I just don’t want to be there when it happens."
mid = col("║ {:<{w}} ║".format(quote, w=WIDTH), GREEN)
bottom = col("╚" + "═"*WIDTH + "╝", CYAN)

for s in (top, mid, bottom):
    print(s)
    time.sleep(0.6)