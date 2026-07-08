"""
Campbell's Soup Can #4125
Produced: 2026-07-08 06:38:36
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "Success is like death, but with a bigger paycheck and worse dental plans."

box_width = len(quote) + 4

top = '+' + '-' * (box_width - 2) + '+'
middle = '| ' + quote + ' |'
bottom = top

# Print top line in cyan with delay
print('\033[36m' + top + '\033[0m')
time.sleep(0.3)

# Print middle line with typewriter effect in yellow
print('\033[33m', end='')
for c in middle:
    print(c, end='', flush=True)
    time.sleep(0.05)
print('\033[0m')
time.sleep(0.3)

# Print bottom line in cyan
print('\033[36m' + bottom + '\033[0m')
time.sleep(0.2)

# Add a philosophical flourish
print('\n\033[37m"Ah, but what does success *really* mean?\033[0m')
print('\033[37m...let me get back to you after I finish this existential crisis.\033[0m')