"""
Campbell's Soup Can #2252
Produced: 2026-02-16 03:19:33
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, sys

# ANSI color codes
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAGENTA= "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

# Rainbow header
print(RED + "┌───┐")
print(GREEN + "│" + YELLOW + " WOODY ALLEN " + BLUE + "│".center(56) + RESET + "│")
print(RED + "└───┘")
print()

# Woody‑Allen‑style philosophical quote
quote = "I'm not afraid of death; I'm just too busy to schedule it properly."

# Simple left‑to‑right scroll animation
for offset in range(len(quote) + 20):
    print(f"\r{' ' * offset}{quote}", end="", flush=True)
    time.sleep(0.04)

print()  # newline after animation

# Closing flourish
print(RESET + "\n" + "✧" * 30)