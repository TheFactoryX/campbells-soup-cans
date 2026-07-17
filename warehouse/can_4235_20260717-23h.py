"""
Campbell's Soup Can #4235
Produced: 2026-07-17 23:08:13
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not afraid of death; I just don't want to be there when it happens. It's a logistical nightmare."
max_len = len(quote)
border = '═' * (max_len + 2)

print(f"\033[36m╔{border}╗")
time.sleep(0.3)
print(f"\033[36m║ {' ' * max_len} ║")
time.sleep(0.3)
print(f"\033[36m║\033[33m {quote} \033[36m║")
time.sleep(0.3)
print(f"\033[36m║ {' ' * max_len} ║")
time.sleep(0.3)
print(f"\033[36m╚{border}╝")