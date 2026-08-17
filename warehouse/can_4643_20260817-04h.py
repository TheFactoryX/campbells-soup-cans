"""
Campbell's Soup Can #4643
Produced: 2026-08-17 04:58:05
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic, colorful Woody Allen quote experience."""
import time, sys, random

quote = ("I'm not afraid of death. I just don't want to be there when it happens… "
         "mainly because I'll probably end up apologizing to the undertaker "
         "for how nervous I was about living.")

# ANSI palette of "neurotic" colors
COLORS = [
    "\033[92m", "\033[93m", "\033[94m", "\033[95m",
    "\033[91m", "\033[96m", "\033[0m"  # green, yellow, blue, magenta, red, cyan, reset
]

def typewriter(text, delay=0.035):
    """Print text character-by-character in random neurotic colors."""
    for ch in text:
        c = random.choice(COLORS)
        sys.stdout.write(c + ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

# Decorative ANSI box borders
width = len(quote) + 4
print("\033[95m" + "╔" + "═" * width + "╗" + "\033[0m")
typewriter(quote)
print("\033[95m" + "╚" + "═" * width + "╝" + "\033[0m")