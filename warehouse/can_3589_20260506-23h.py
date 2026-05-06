"""
Campbell's Soup Can #3589
Produced: 2026-05-06 23:06:31
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# ANSI color codes (hex escapes)
RED   = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW= "\x1b[33m"
BLUE  = "\x1b[34m"
RESET = "\x1b[0m"

def typewrite(s, speed=0.02):
    for ch in s:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# Build a colorful boxW = 70
top    = f"{RED}╔{'═'*(W-2)}╗{RESET}"
bottom = f"{RED}╚{'═'*(W-2)}╝{RESET}"
side   = f"{GREEN}║{RESET}"

print(top)
typewrite(f"{side} {quote} {side}")
print(bottom)