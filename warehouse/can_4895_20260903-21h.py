"""
Campbell's Soup Can #4895
Produced: 2026-09-03 21:43:02
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen meets the terminal – neurotic, colorful, and philosophical."""
import time, sys

# ANSI color shortcuts
c = lambda t, n: f"\033[{n}m{t}\033[0m"
R, Y, B, M = "\033[91m", "\033[93m", "\033[94m", "\033[95m"
N = "\033[0m"

# A Woody original
q = "I'm not afraid of death. I just don't want to be there when it happens... mostly because I'll panic, forget why I walked in, and apologize to the curtains."

# Box width
w = len(q) + 6

# Subtle pulse prelude
for _ in range(3):
    sys.stdout.write(f"{M}.{N}"); sys.stdout.flush(); time.sleep(0.1)
print()

# Colored ASCII box
print(f"{M}+{'-'*w}+{N}")
print(f"{M}| {Y}{q}{M} |{N}")
print(f"{M}+{'-'*w}+{N}")

# Sign‑off
print(f"\n{M}Stay neurotic, stay brilliant.{N}\n")