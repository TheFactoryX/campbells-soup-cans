"""
Campbell's Soup Can #5062
Produced: 2026-10-04 00:38:18
Worker: Space Bunny Alpha (stealth/space-bunny-alpha)
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
COLORS = [
    "\033[38;5;205m",
    "\033[38;5;213m",
    "\033[38;5;221m",
    "\033[38;5;228m",
    "\033[38;5;231m",
]

quote = "Life is mostly just trying to remember what I was doing while being terrified that none of it matters."

def centered(text, width):
    return text.center(width)

def draw_thought_bubble():
    art = [
        "                 .----------------.",
        "              .-'                  '-.",
        "             /       _________       \\",
        "            |       /         \\       |",
        "            |      |  ?     ?  |      |",
        "             \\      \\_________/      /",
        "              '-.                .- '",
        "                 '--------------'",
        "                        O",
        "                       O",
        "                     O",
    ]
    for line in art:
        print(centered(line, 78))

def reveal(text):
    sys.stdout.write("\033[?25l")
    try:
        for color in COLORS:
            sys.stdout.write(color)
            for character in text:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.018)
            sys.stdout.write("\n" + RESET)
            if color != COLORS[-1]:
                time.sleep(0.35)
                sys.stdout.write("\033[1A\r\033[K")
    finally:
        sys.stdout.write(RESET + "\033[?25h\n")

print("\033[38;5;213m" + centered("AN EXISTENTIAL STATUS REPORT", 78) + RESET)
print()
draw_thought_bubble()
print()
reveal(quote)