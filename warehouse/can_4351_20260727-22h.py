"""
Campbell's Soup Can #4351
Produced: 2026-07-27 22:18:15
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A colorful Woody Allen style philosophical quote (single file, no dependencies)

import sys

# ANSI color codes
class C:
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ONE Woody Allen philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a simple decorative box
width = 60
border = f"{C.CYAN}{C.BOLD}*{'='* (width-2)}{C.END}"
inner = f"{C.MAGENTA}{C.BOLD}{quote}{C.END}"

# Print the formatted output
print(border)
print(f"*{inner.center(width-2)}*")
print(border)