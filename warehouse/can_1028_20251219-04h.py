"""
Campbell's Soup Can #1028
Produced: 2025-12-19 04:04:18
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

# ANSI color codes
RED    = '\033[31m'
CYAN   = '\033[36m'
YELLOW = '\033[33m'
GREEN  = '\033[32m'
RESET  = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."
WIDTH = 81  # total width of the box (including borders)

# Build the frame
top    = f"{RED}+{'-'*(WIDTH-2)}{RESET}"
middle = f"{CYAN}| {quote}{' '*6}|{RESET}"
bottom = f"{RED}+{'-'*(WIDTH-2)}{RESET}"

# Print the colorful box
print(top)
print(middle)
print(bottom)
print(f"{YELLOW} — a neurotic thought from a nervous coder{RESET}")