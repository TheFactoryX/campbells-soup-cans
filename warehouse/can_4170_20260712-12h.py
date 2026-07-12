"""
Campbell's Soup Can #4170
Produced: 2026-07-12 12:07:48
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not afraid of death, but I'm terrified of not being there to witness it. Also, I can't decide if I'm a pessimist or just realistic."

# Calculate box dimensions
middle_line = f'| "{quote}" |'
box_line_length = len(middle_line)
top_bottom = '+' + '-' * (box_line_length - 2) + '+'

# ASCII Art Title in Cyan
print('\033[36m')
print("  ____  _   _ _______  _____   ____  ")
print(" |  _ \\| | | |__   __||  _  | |  _ \\ ")
print(" | |_) | |_| |  | |   | |_| | | |_) |")
print(" |  _ <|  _  |  | |   |  _  | |  _ < ")
print(" |_| \\__|_| |_|  |_|   |_| |_| |_| \\_\\")
print('\033[0m')
time.sleep(1)

# Print the box
print('\033[31m' + top_bottom + '\033[0m')  # Top line in red

# Print the middle line with typing effect in yellow
print('\033[33m| "', end='', flush=True)
for char in quote:
    print(char, end='', flush=True)
    time.sleep(0.05)
print(' |', end='', flush=True)
print('\033[0m')

print('\033[31m' + top_bottom + '\033[0m')  # Bottom line in red