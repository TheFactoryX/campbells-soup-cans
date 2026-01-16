"""
Campbell's Soup Can #1639
Produced: 2026-01-16 06:50:51
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def woody_print(text, color_code, delay=0.05):
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ANSI escape codes for colors
YELLOW = '33'
CYAN = '36'
RED = '31'
MAGENTA = '35'
RESET = '0'

woody_art = r'''
       o_O     O_o
      /|_|\   /|_|\
        |       |
       / \     / \
'''

quote = [
    (" " * 10 + "╔" + "═" * 58 + "╗\n", YELLOW),
    (" " * 10 + "║ ", YELLOW),
    ("I'm terrified of eternity ", RED),
    ("because ", RESET),
    ("I'll probably\n", RESET),
    (" " * 12 + "spend most of it worrying ", RED),
    ("that I left the oven on.", CYAN),
    (" ║", YELLOW),
    ("\n" + " " * 10 + "╚" + "═" * 58 + "╝", YELLOW),
]

print(f"\033[{MAGENTA}m{woody_art}\033[0m")
for line, color in quote:
    woody_print(line, color, delay=0.03)
print(f"\033[{CYAN}m{' '*16}― Woody Allen (probably)\033[0m")