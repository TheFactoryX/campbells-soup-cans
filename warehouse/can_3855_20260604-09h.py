"""
Campbell's Soup Can #3855
Produced: 2026-06-04 09:01:06
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys,time

# ANSI colors
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
WHITE  = '\033[37m'
RESET  = '\033[0m'

def slow_print(s, col=WHITE, delay=0.03):
    for ch in s:
        sys.stdout.write(f"{col}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a colorful frame
width = len(quote) + 4
border = f"{RED}+{'-'*width}+{RESET}"
print(border)
left  = f"{RED}|{WHITE} "
padding = ' ' * (width - len(quote))
inner = f"{quote}"
print(f"{left}{inner}{WHITE}{padding}|{RESET}")
print(border)

# Simple star animation around the box
for _ in range(4):
    star_line = f"{CYAN}*{RESET} " + " " * width + f"{CYAN}*{RESET}"
    slow_print(star_line, CYAN, 0.02)