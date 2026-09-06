"""
Campbell's Soup Can #4915
Produced: 2026-09-06 19:11:44
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen–style neurotic philosophy, beautifully formatted."""
import sys

# The quote — neurotic, funny, existential, Woody‑esque
QUOTE = "I don't want to achieve immortality through my work. I just want to live long enough to see if my coffee habit kills me first."

# ANSI color palette
COLORS = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[94m",  # blue
    "\033[95m",  # magenta
]
R = "\033[0m"  # reset

# A tiny ASCII coffee cup — Woody’s favorite companion
COFFEE = r"""
   .---.
  / o o \
  \  ^  /
   | | |
  /'-'/- 
 (    )
  `---´
"""

if __name__ == "__main__":
    # Header in magenta
    print(f"\033[95m{'Woody\'s Philosophical Corner':^40}\033[0m")
    # Colored quote: each word a different color, reset after each
    words = QUOTE.split()
    for i, w in enumerate(words):
        print(f"{COLORS[i % len(COLORS)]}{w}{R}", end=" ")
    print()
    # ASCII coffee cup
    print(f"\033[93m{COFFEE}\033[0m")
    # Footer
    print(f"\033[96m— Stay neurotic. Stay philosophical. —\033[0m")