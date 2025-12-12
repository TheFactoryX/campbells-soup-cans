"""
Campbell's Soup Can #875
Produced: 2025-12-12 04:46:53
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

brain = [
    "      .-'''''-.",
    "     /         \\",
    "    |  BRAIN    |",
    "     \\         //",
    "      '-...-'",
]

for line in brain:
    print(f"\033[35m{line}\033[0m")

border = "\033[36m+--------------------------------+\033[0m"
title = "Woody's Wisdom"
quote = "Why am I here? To worry, mostly."

print(border)
print(f"\033[36m|  {title:<15}  |\033[0m")
print(border)
print(f"\033[34m| {quote.center(34)} |\033[0m")
print(border)
time.sleep(2)