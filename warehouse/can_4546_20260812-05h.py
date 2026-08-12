"""
Campbell's Soup Can #4546
Produced: 2026-08-12 05:02:27
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

def rainbow(text):
    colors = [31, 32, 33, 34, 35, 36]  # Red, Green, Yellow, Blue, Magenta, Cyan
    return ''.join(f'\033[{color}m{c}' for c, color in zip(text, [colors[i % len(colors)] for i in range(len(text))]))

quote = "I'm terrified of dying, but not so much that I'll stop going to the dentist."
print('\033[2J', end='')  # Clear screen

# Animate the quote
print('\033[1;1H', end='')  # Move cursor to top-left
for char in quote:
    rainbow_char = rainbow(char if char != ' ' else ' ')
    sys.stdout.write(rainbow_char)
    sys.stdout.flush()
    time.sleep(0.03)

# Create animated border
border = '+' + '-' * len(quote) + '+'
for _ in range(5):
    for i, line in enumerate([quote] * 4):
        sys.stdout.write(f'\033[{(i+1)*2}C\033[{2 + i}B')
        side = '|' if i % 2 == 0 else ' '
        print(f'\033[31m{side}\033[37m{line if line == quote else " " * len(quote)}{side}\033[0m')
    for col in range(len(quote) + 2):
        sys.stdout.write(f'\033[{2 + (col//40)}B\033[{3 + col}C:')
        sys.stdout.flush()
        time.sleep(0.05)

# Blinking punchline
sys.stdout.write(f'\033[{6 + len(quote)//2 + 4}B')
for _ in range(10):
    print(f'\033[5m{rainbow("*")}\033[0m')
    time.sleep(0.3)
    print(f'\033[5m{" " * len(quote)}\033[0m')
    time.sleep(0.3)

print('\033[0m')  # Reset colors