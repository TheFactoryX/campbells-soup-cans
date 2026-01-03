"""
Campbell's Soup Can #1375
Produced: 2026-01-03 22:35:01
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

quote = "I keep telling myself it's all a dream, but my credit card bills keep arriving."

thought_bubble = [
    "    __",
    "  _/  \\_",
    ",'     ',",
    " \\_   _/",
    "  `---'",
]

colors = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]

for line in thought_bubble:
    print(line)

for char in quote:
    color_code = random.choice(colors)
    print(f"\033[{color_code}m{char}\033[0m", end='', flush=True)
    time.sleep(0.02)
print()