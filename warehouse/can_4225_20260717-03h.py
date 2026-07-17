"""
Campbell's Soup Can #4225
Produced: 2026-07-17 03:39:27
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Define ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
RESET = '\033[0m'

# ASCII art header
print(CYAN + "    /\\_/\\ " + RESET)
print(CYAN + "   ( o.o ) " + RESET)
print(CYAN + "    > ^ <  " + RESET)
print()

# Woody Allen-style quote
quote = "I'm not afraid of death, just terrified it's going to be on time and I'll miss the punchline."

# Calculate box dimensions
quote_length = len(quote)
top_line_length = quote_length + 4  # Adding padding for | and spaces
dashes = top_line_length - 2  # Subtract 2 for the '+' symbols
top = '+' + '-' * dashes + '+'
middle = '| ' + quote + ' |'
bottom = '+' + '-' * dashes + '+'

# Print top border with delay
print(RED + top)
time.sleep(0.5)

# Print middle line with typing effect and color
print(GREEN + '| ', end='', flush=True)
for char in quote:
    print(char, end='', flush=True)
    time.sleep(0.04)
print(' |' + RESET)
time.sleep(0.5)

# Print bottom border with delay
print(RED + bottom)