"""
Campbell's Soup Can #4943
Produced: 2026-09-11 14:26:20
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

RESET = '\033[0m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
BOLD = '\033[1m'

quote = "The secret to a happy life is never achieving your goals."

def create_box(s):
    middle_line = '║ ' + s + ' ║'
    line_length = len(middle_line)
    top = '╔' + '═' * (line_length - 2) + '╗'
    bottom = '╚' + '═' * (line_length - 2) + '╝'
    return top, bottom

top, bottom = create_box(quote)

# Print title with animation
print(f"{MAGENTA}{'=' * 50}{RESET}")
print(f"{BOLD}{CYAN}Pondering Existential Dread...{RESET}")
time.sleep(0.3)
print(f"{MAGENTA}{'=' * 50}{RESET}")
time.sleep(0.2)

# Print the box top
print(f"{CYAN}{top}{RESET}")

# Animate the middle line
print(f"{CYAN}║ {YELLOW}", end="")
for char in quote:
    print(char, end='')
    time.sleep(0.05)
print(f"{CYAN} ║{RESET}")

# Print the box bottom
print(f"{CYAN}{bottom}{RESET}")

time.sleep(1)