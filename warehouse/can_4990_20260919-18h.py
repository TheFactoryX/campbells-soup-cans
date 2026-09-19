"""
Campbell's Soup Can #4990
Produced: 2026-09-19 18:01:44
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote, served Python-colored."""

import sys

# ANSI palette for playful colors
C = {
    "reset": "\033[0m",
    "cyan":  "\033[96m",
    "yellow": "\033[93m",
    "magenta": "\033[95m",
    "green":  "\033[92m",
}

# The quote — neurotic, funny, existential, firmly in Woody's vein
quote = ("I spend my life asking 'why?' and the universe replies with more anxiety. "
         "At least I'm consistent.")

# Aesthetic ASCII frame, generous width for the quote
width = 118
top = f"{C['cyan']}╔{('═' * (width - 2))}╗{C['reset']}"
bottom = f"{C['cyan']}╚{('═' * (width - 2))}╝{C['reset']}"
mid = f"{C['cyan']}║{C['yellow']}  {quote}  {C['cyan']}║{C['reset']}"

print(top)
print(mid)
print(bottom)

print(f"\n{C['green']}— Existential wit, Python-delivered —{C['reset']}\n")