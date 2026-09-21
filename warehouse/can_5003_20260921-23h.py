"""
Campbell's Soup Can #5003
Produced: 2026-09-21 23:17:35
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen Style Philosophical Quote - Visual Edition"""
import time

# ANSI color codes
R = "\033[0m"    # reset
C = "\033[96m"   # bright cyan
Y = "\033[93m"   # bright yellow
M = "\033[95m"   # bright magenta

# The quote — neurotic, funny, existential, very Woody
quote = "I'm not afraid of death. I just don't want to be there when it happens. Mostly because I'm usually too busy wondering if I left the gas on."

# Calculate box width
w = len(quote) + 4

# Print colorful box surrounding the quote
print(f"{C}+{'-' * w}+{R}")
print(f"{C}| {Y}{quote}{C} |{R}")
print(f"{C}+{'-' * w}+{R}")

# Tiny ASCII "neurotic thought" cloud
print(f"{M}     ,     {R}")
print(f"{M}    (o o)    {R}")
print(f"{M}     > ^ <   {R}")
print(f"{M}    /_|_|_   {R}")

# Brief dramatic pause (the pause we all feel about existence)
time.sleep(0.5)