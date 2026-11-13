"""
Campbell's Soup Can #5237
Produced: 2026-11-13 07:59:16
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def color(text, code, bold=False):
    if bold:
        return f"\033[1;{code}m{text}\033[0m"
    else:
        return f"\033[{code}m{text}\033[0m"

print(color("* W O O D Y   A L L E N ' S   B R A I N *", 31, bold=True))
print()

width = 55
border = color("+" + "-"*width + "+", 31, bold=True)
print(border)
print(color("|" + " "*width + "|", 31, bold=True))
quote_lines = [
    "  \"I'm not afraid of the meaning of life; I'm just",
    "   afraid I left the oven on and the universe is",
    "   laughing.\""
]
for line in quote_lines:
    padded = line.ljust(width-2)
    print(color("| " + padded + " |", 36))
print(color("|" + " "*width + "|", 31, bold=True))
print(border)
print()

print(color("   (  )   (  )  ", 33))
print(color("    (  \\  /  ) ", 33))
print(color("     \\  V  / ", 33))
print(color("      \\___/ ", 33))