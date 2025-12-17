"""
Campbell's Soup Can #990
Produced: 2025-12-17 09:42:00
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen style philosophical quote with colorful box

quote = "I'm not afraid of death; I just don't want to be there when it happens."

# ANSI escape codes
RED  = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Build the decorative frame
width = len(quote) + 4
top    = YELLOW + BOLD + "+" + "-" * width + "+" + RESET
middle = YELLOW + BOLD + "|" + RESET + CYAN + " " + quote + " " + RESET + YELLOW + BOLD + "|" + RESET

print(top)
print(middle)
print(top)