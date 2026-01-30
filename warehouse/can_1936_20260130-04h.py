"""
Campbell's Soup Can #1936
Produced: 2026-01-30 04:50:48
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI escape codes
YELLOW = "\033[93m"
WHITE = "\033[97m"
ITALIC = "\033[3m"
BOLD = "\033[1m"
RESET = "\033[0m"
BOX_COLOR = "\033[38;5;214m"  # orange
TEXT_COLOR = "\033[38;5;229m"  # light yellow

def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    print("\033[2J\033[H", end="")

clear_screen()

# ASCII art box with quote
box_top = BOX_COLOR + """
           o
        o     o
    o_____________o
   |               |
""".strip()

box_bottom = BOX_COLOR + """
   |_______________|
    'O           O'
        '  O  '
""" + RESET

quote = TEXT_COLOR + """
'I thought about the meaning of life,\nbut then I remembered my therapist bill -\nexistence is expensive enough\nwithout cosmic insights.'""" + RESET

author = ITALIC + YELLOW + "\n\t\t— Woody Allen (probably)" + RESET

print(box_top)
slow_print(quote)
slow_print(author, 0.08)
print(box_bottom)

# Create fake "credits" animation
time.sleep(1)
print(BOLD + "\nLife Presents:" + RESET)
for text in [YELLOW + "A Crisis", WHITE + "   of", YELLOW + "Existence"]:
    print("   " + text, end="\r")
    time.sleep(0.7)
print(RESET + "\n\n        (Now with 20% more anxiety!)" + RESET)