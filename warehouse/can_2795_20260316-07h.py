"""
Campbell's Soup Can #2795
Produced: 2026-03-16 07:48:30
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ----- ANSI colour codes -----
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
RESET  = "\033[0m"

# ----- The Woody Allen quote -----
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

# ----- Build a colourful ASCII‑art box around it -----border = f"{RED}*{'*' * (len(quote) + 2)}{RESET}"
top    = f"{RED}*{'' * (len(quote) + 2)}{RESET}"
mid    = f"{RED}* {quote} {RESET}"
bottom = border

# ----- Print with a tiny typing animation for extra flair -----
def slow_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

slow_print(top)
slow_print(mid)
slow_print(bottom)

print(f"\n{CYAN}Hovering over the void since 1975...{RESET}")