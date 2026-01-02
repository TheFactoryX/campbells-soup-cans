"""
Campbell's Soup Can #1335
Produced: 2026-01-02 04:54:01
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

colors = [31, 32, 33, 34, 35, 36, 37]

print("\033[31m+--------------------------------+\033[0m")
print("\033[31m|    WOODY'S WISDOM CHAMBER     |\033[0m")
print("\033[31m+--------------------------------+\033[0m")
print()

quote = "I'm not neurotic, I'm just an overachiever in the field of existential dread."

color_index = 0
for char in quote:
    print(f"\033[{colors[color_index]}m{char}\033[0m", end='', flush=True)
    color_index = (color_index + 1) % len(colors)
    time.sleep(0.05)
print()