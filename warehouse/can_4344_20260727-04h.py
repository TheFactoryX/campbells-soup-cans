"""
Campbell's Soup Can #4344
Produced: 2026-07-27 04:04:19
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = '"' + "I'm not afraid of death; I just don't want to be there when it happens." + '"'

# Print top border in cyan
print('\033[36m+' + '-' * 74 + '+\033[0m')

# Animate the quote in yellow
print('\033[33m|', end='')
for char in quote:
    print(char, end='')
    time.sleep(0.05)
print('|\033[0m')

# Print bottom border in cyan
print('\033[36m+' + '-' * 74 + '+\033[0m')