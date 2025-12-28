"""
Campbell's Soup Can #1240
Produced: 2025-12-28 17:32:30
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

quote = 'Anxiety is the mind\'s way of saying \'I care, but this is too much.\'

border = "=" * 71

title = "WOODY'S QUOTE".center(71)
print(f"\033[1;34m{border}\033[0m")
print(f"\033[1;34m{title}\033[0m")
print(f"\033[1;34m{border}\033[0m")
print()

colors = [31, 32, 33, 34, 35, 36, 37]  # 7 ANSI colors

for i, char in enumerate(quote):
    sys.stdout.write(f"\033[{colors[i % len(colors)]]m{char}")
    sys.stdout.flush()
    time.sleep(0.03)
sys.stdout.write("\033[0m")