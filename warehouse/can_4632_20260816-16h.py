"""
Campbell's Soup Can #4632
Produced: 2026-08-16 16:42:01
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

# ANSI color codes
RED   = '\033[91m'
GREEN = '\033[92m'
YELLOW= '\033[93m'
RESET = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a simple box around the quote
border = GREEN + '+' + '-' * (len(quote) + 2) + '+' + RESET
boxed  = f"{GREEN}| {YELLOW}{quote}{GREEN} |{RESET}"

# Print with a tiny pause for a “dramatic” effect
print(border)
time.sleep(0.4)
print(boxed)
time.sleep(0.4)
print(border)