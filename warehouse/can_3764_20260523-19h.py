"""
Campbell's Soup Can #3764
Produced: 2026-05-23 19:37:37
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

RESET = '\033[0m'
CYAN  = '\033[36m'
MAGENTA = '\033[35m'
YELLOW = '\033[33m'
BOLD = '\033[1m'

def typewriter_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

quote = "I’m not afraid of death; I just don’t want to be there when it happens."
box_width = 48top    = f"{CYAN}{BOLD}┌{'─'*box_width}┐{RESET}"
mid    = f"{MAGENTA}│ {YELLOW}{quote}{MAGENTA} │{RESET}"
bottom = f"{CYAN}{BOLD}└{'─'*box_width}┘{RESET}"
sparkle = " ✨"

for line in (top, mid, bottom, sparkle):
    typewriter_print(line)