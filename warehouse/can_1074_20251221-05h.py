"""
Campbell's Soup Can #1074
Produced: 2025-12-21 05:36:00
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time

print("\033[1m\033[34mWoody Allen's Existential Dread:\033[0m")

quote = "I don't believe in an afterlife, but if there is one, I'm sure I'll mess it up."

colors = [31,32,33,34,35,36,37]

for char in quote:
    color = random.choice(colors)
    print(f"\033[{color}m{char}\033[0m", end='', flush=True)
    time.sleep(0.05)
print()