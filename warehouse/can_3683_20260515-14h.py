"""
Campbell's Soup Can #3683
Produced: 2026-05-15 14:35:45
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

Cyan = "\033[96m"
Yellow = "\033[93m"
Reset = "\033[0m"

quote = "I'm terrified of death, but I'm even more terrified that my jokes will outlive me."
width = 100

top = Cyan + "╔" + "═" * (width - 2) + "╗" + Reset
bottom = Cyan + "╚" + "═" * (width - 2) + "╝" + Reset

print(top)
print(Yellow + "║ " + quote + " ║" + Reset)
print(bottom)