"""
Campbell's Soup Can #5159
Produced: 2026-10-24 14:33:37
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
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
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"

INNER = 74
QUOTE = "I don't believe in the afterlife, but I'm bringing a sweater just in case."
ATTRIB = "- Woody Allen (probably, and very anxious about it)"
FACE = "(‾◡‾)╯neurotic╯╧╧"

def pad(text):
    return text.center(INNER)

def border(top=True):
    left = "╔" if top else "╚"
    right = "╗" if top else "╝"
    return CYAN + left + "═" * INNER + right + RESET

def box_line(text, color=RESET):
    return CYAN + "║" + RESET + " " + color + pad(text) + RESET + " " + CYAN + "║" + RESET

def type_box_line(text, color=YELLOW, delay=0.04):
    full = box_line(text, color)
    for ch in full:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

print(border(True))
print(box_line(""))
print(box_line(GREEN + FACE + RESET))
print(box_line(""))
time.sleep(0.4)
type_box_line(QUOTE)
print(box_line(""))
type_box_line(ATTRIB, color=MAGENTA, delay=0.03)
print(box_line(""))
print(border(False))