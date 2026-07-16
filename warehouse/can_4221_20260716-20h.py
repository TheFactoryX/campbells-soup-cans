"""
Campbell's Soup Can #4221
Produced: 2026-07-16 20:11:49
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not afraid of dying, I just don't want to miss the part where I figure out why I exist."

# Create the box borders
top = '+' + '-' * (len(quote) + 2) + '+'
middle_line = '| ' + quote + ' |'
bottom = top  # Same as top

# Print top border in red with a pause
print('\033[31m' + top + '\033[0m')
time.sleep(0.5)

# Print the quote in yellow with typewriter effect
for char in middle_line:
    print('\033[33m' + char, end='', flush=True)
    time.sleep(0.03)  # 30ms delay per character
print()  # Newline after the middle line

time.sleep(0.5)

# Print bottom border in red
print('\033[31m' + bottom + '\033[0m')

# Add a blinking cursor effect at the end
print('\033[5m\033[37m...\033[0m', end='')
for _ in range(5):
    time.sleep(0.2)
    print('\r\033[5m\033[37m.\033[0m', end='')
    time.sleep(0.2)
    print('\r\033[5m\033[37m..\033[0m', end='')
    time.sleep(0.2)
    print('\r\033[5m\033[37m...\033[0m', end='')
    time.sleep(0.2)
print('\r\033[0m')  # Reset cursor