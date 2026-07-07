"""
Campbell's Soup Can #4122
Produced: 2026-07-07 23:14:22
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def print_with_delay(text, color_code):
    sys.stdout.write('\033[' + color_code + 'm')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\033[0m')

quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Create a red box with ASCII art
print('\033[31m+' + '-'*70 + '+\033[0m')
print('\033[31m|' + ' '*34 + '\033[37mX' + ' '*34 + '\033[31m|\033[0m')
print('\033[31m|', end='')
print_with_delay(quote, '37')
print('\033[31m|\033[0m')
print('\033[31m|' + ' '*34 + '\033[37mO' + ' '*34 + '\033[31m|\033[0m')
print('\033[31m+' + '-'*70 + '+\033[0m')