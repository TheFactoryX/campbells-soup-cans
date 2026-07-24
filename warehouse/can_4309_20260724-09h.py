"""
Campbell's Soup Can #4309
Produced: 2026-07-24 09:33:58
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

quote = "I'm not afraid of death, but I'm terrified of the afterlife's unemployment benefits."

max_width = len(quote) + 2

border = '+' + '-' * (max_width - 2) + '+'

print('\033[96m' + border + '\033[0m')

print('\033[94m|', end='')
print('\033[93m', end='')
for c in quote:
    time.sleep(0.05)
    print(c, end='')
    sys.stdout.flush()
print('\033[94m|', end='')
print('\033[0m')
print()

print('\033[96m' + border + '\033[0m')