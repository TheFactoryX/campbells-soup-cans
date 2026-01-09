"""
Campbell's Soup Can #1494
Produced: 2026-01-09 11:31:57
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
CYAN = '\033[36m'
YELLOW = '\033[33m'
RESET = '\033[0m'

quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a colorful box around the quote
border = CYAN + "+" + "-" * (len(quote) + 6) + "+" + RESET
middle = CYAN + "|" + RESET + YELLOW + f" {quote} " + CYAN + "|" + RESET

# Animate each line character‑by‑character
for line in (border, middle, border):
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

# Reset terminal color
sys.stdout.write(RESET)