"""
Campbell's Soup Can #5063
Produced: 2026-10-04 06:49:53
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

GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

quote = "I'm not afraid of death; I just don't want to be there when it happens - it's the ultimate commitment issue."
border_len = len(quote) + 4  # accounts for "| " and " |"
border = "+" + "-" * border_len + "+"

print(GREEN + border)
print(YELLOW + "| " + quote + " |" + RESET)
print(GREEN + border + RESET)