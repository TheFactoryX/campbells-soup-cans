"""
Campbell's Soup Can #5223
Produced: 2026-11-08 23:43:20
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."
WIDTH = 70

TOP_BORDER = "\033[36m+" + "-" * (WIDTH - 2) + "\033[0m"
MID_BORDER = "\033[36m|" + " " * (WIDTH - 2) + "\033[0m"
QUOTE_LINE = "\033[33m|" + " " * ((WIDTH - 2 - len(QUOTE)) // 2) + QUOTE + " " * ((WIDTH - 2 - len(QUOTE)) // 2) + "\033[0m"
BOTTOM_BORDER = "\033[36m+" + "-" * (WIDTH - 2) + "\033[0m"

print(TOP_BORDER)
print(MID_BORDER)
print(QUOTE_LINE)
print(MID_BORDER)
print(BOTTOM_BORDER)