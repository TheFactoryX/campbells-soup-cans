"""
Campbell's Soup Can #5098
Produced: 2026-10-12 17:55:57
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style: neurotic philosophy served with ANSI-colored ASCII flair."""
import time, sys

# ANSI palette
R = "\033[0m"   # reset
G = "\033[32m"  # green
Y = "\033[33m"  # yellow
C = "\033[36m"  # cyan
M = "\033[35m"  # magenta

# The Woody Allen style quote — neurotic, existential, gently self-deprecating
quote = (
    "I'm not afraid of death. I just don't want to be there when it happens. "
    "Mostly because I'd hate to be the only person at the cosmic party "
    "who doesn't know the dress code."
)

# Box width with breathing room
w = len(quote) + 6

# Top border — vibrant green
sys.stdout.write(G + "+" + "-" * (w - 2) + "+" + R + "\n")

# The quote itself: cyan borders, yellow text (Woody’s favorite hue)
sys.stdout.write(C + "| " + Y + quote + C + " |" + R + "\n")

# Bottom border — matching green
sys.stdout.write(G + "+" + "-" * (w - 2) + "+" + R + "\n")

# A brief neurotic pause, then a parting existential wink
time.sleep(0.4)
sys.stdout.write(M + "~ if you relate, welcome to the club ~" + R + "\n")