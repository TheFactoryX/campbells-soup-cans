"""
Campbell's Soup Can #322
Produced: 2025-11-16 19:24:58
Worker: Sherlock Think Alpha (openrouter/sherlock-think-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

clear_screen()

width = 64
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Top border
print(CYAN + BOLD + "╔" + "═" * (width - 2) + "╗" + RESET)

# Middle line with typewriter effect
print(CYAN + BOLD + "║" + RESET, end="")
sys.stdout.flush()

# Calculate left padding
left_pad = (width - 2 - len(quote)) // 2
print(" " * left_pad, end="")
sys.stdout.flush()

# Typewriter effect for quote
for char in quote:
    sys.stdout.write(YELLOW + BOLD + char + RESET)
    sys.stdout.flush()
    time.sleep(0.08)

# Right padding
right_pad = width - 2 - len(quote) - left_pad
print(" " * right_pad + CYAN + BOLD + "║" + RESET)

# Bottom border
print(CYAN + BOLD + "╚" + "═" * (width - 2) + "╝" + RESET)

# Flair
print()
print(MAGENTA + BOLD + "          ~ A Woody Allen Neurotic Revelation ~          " + RESET)
time.sleep(1)
print(RED + "                    (Therapy sold separately)                  " + RESET)