"""
Campbell's Soup Can #4370
Produced: 2026-07-29 21:12:17
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import itertools, sys

quote = "I'm not afraid of death; I just don't want to be there when it happens."
border = "┌─────────────────────────────────────────────────────┐"
mid    = "│  " + quote + "  │"
bottom = "└─────────────────────────────────────────────────────┘"

# Cycle through bright colors for each line
palette = itertools.cycle(["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"])

for line in (border, mid, bottom):
    sys.stdout.write(next(palette) + line + "\033[0m" + "\n")