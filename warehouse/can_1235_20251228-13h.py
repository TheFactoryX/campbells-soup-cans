"""
Campbell's Soup Can #1235
Produced: 2025-12-28 13:00:21
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors and styles
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
ITALIC = "\033[3m"
RESET = "\033[0m"

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Create our Woody Allen-esque quote with emphasized words
quote = f"I'm{tty certain the meaning of life is{RED} pizza{RESET}{IT c}, but existence keeps serving me{YELLOW} gluten-free crackers{RESET}{ITALIC} instead."

# Calculate box dimensions
padding = 4
text_width = len("".join([part.replace("\033", "") for part in quote.split("\033") if "m" not in part])) + padding
box_top = CYAN + "╭" + "─" * (text_width + 2) + "╮" + RESET
box_bottom = CYAN + "╰" + "─" * (text_width + 2) + "╯" + RESET

# Create animated elements
print("\n"*2)
print(box_top)
print(CYAN + "│ " + RESET, end="")
typewriter(quote, 0.04)
print(CYAN + "│ " + RESET)
print(box_bottom)

# Add some neurotic blinking text
time.sleep(1.2)
print(f"\n{CYAN}{ITALIC}(He checks his watch nervously){RESET}", end="\r")
time.sleep(1.5)
print(" " * 30 + "\r", end="")