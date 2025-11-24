"""
Campbell's Soup Can #497
Produced: 2025-11-24 19:26:11
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI Escape Codes
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

print('\n' * 4)

# Neurotic Woody-esque ASCII face
print(CYAN + r"""
     .-"""-.
    /  ***  \
   |    |    |
    \  ***  /
     '-...-' 
""" + RESET + BOLD + MAGENTA + '   (adjusting glasses nervously)' + RESET)

print('\n' + YELLOW + BOLD + '═' * 72 + RESET + '\n')

# Title
print(BLUE + BOLD + '                  WOODY ALLEN\'S PHILOSOPHICAL PANIC                  ' + RESET + '\n')

print(YELLOW + BOLD + '═' * 72 + RESET + '\n\n')

# The quote
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying... but knowing my luck, I'll probably screw that up too."

colors = [MAGENTA, CYAN, YELLOW, GREEN, BLUE, RED]
print(' ' * 8, end='')  # Indent for centering-ish
for i, char in enumerate(quote):
    color = colors[i % len(colors)]
    sys.stdout.write(color + BOLD + char + RESET)
    sys.stdout.flush()
    time.sleep(0.035)

print('\n\n' + YELLOW + BOLD + '═' * 72 + RESET + '\n')

# Footer zinger
print(GREEN + ITALIC + ' ' * 20 + '^(Eternity: the ultimate awkward pause)^' + RESET + '\n')

# Fun exit animation: existential fade (repeating dots)
print(MAGENTA + ' ' * 25, end='')
for _ in range(20):
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(0.1)
print(RESET + '\n\n')