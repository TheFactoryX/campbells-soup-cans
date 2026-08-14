"""
Campbell's Soup Can #4578
Produced: 2026-08-14 05:02:21
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

quote = "I am not afraid of death. I just don't want to be there when it happens."

def animate_print(s, delay=0.04):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

width = 70
border = RED + '+' + '-' * width + '+' + RESET
top_bottom = RED + '|' + '-' * width + '|' + RESET
pad = (width - len(quote)) // 2
centered = ' ' * pad + quote + ' ' * (width - len(quote) - pad)
middle = CYAN + centered + RESET

animate_print(border)
animate_print(top_bottom, delay=0.1)
animate_print(middle, delay=0.08)
animate_print(top_bottom, delay=0.1)
animate_print(border)

time.sleep(0.3)
print(RESET, end='')