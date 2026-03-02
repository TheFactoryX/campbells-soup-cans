"""
Campbell's Soup Can #2522
Produced: 2026-03-02 11:03:05
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
MAGENTA= '\033[35m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a colorful, bordered display
border = f"{CYAN}+{'-'*48}{CYAN}+{RESET}"
line   = f"|{BLUE}{' ' * 22}{YELLOW}{quote}{BLUE}{' ' * 22}{CYAN}|{RESET}"

# Simple typing animation for extra fun
def typewriter(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# Print the visual
sys.stdout.write(border + "\n")
sys.stdout.write(line + "\n")
sys.stdout.write(border + "\n")

# Add a tiny pause before the quote appears in the box
time.sleep(0.5)
typewriter(YELLOW + quote + RESET)