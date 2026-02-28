"""
Campbell's Soup Can #2486
Produced: 2026-02-28 15:35:24
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

reset = "\033[0m"
green = "\033[32m"
blue = "\033[34m"

width = 60
top = green + "┌" + "─" * (width-2) + "┐" + reset
side = green + "│" + " " * (width-2) + "│" + reset
bottom = green + "└" + "─" * (width-2) + "┘" + reset

quote = "I don't want to be immortal. I don't have the patience."

inner_width = width - 2

print(top)
print(side)

current = ""
for char in quote:
    current += char
    padding = (inner_width - len(current)) // 2
    sys.stdout.write("\033[3;1H")
    sys.stdout.write(green + "│" + reset)
    sys.stdout.write(green + " " * padding + reset)
    sys.stdout.write(blue + current + reset)
    sys.stdout.write(green + " " * (inner_width - padding - len(current)) + reset)
    sys.stdout.write(green + "│" + reset)
    sys.stdout.write("\n")
    sys.stdout.flush()
    time.sleep(0.05)

print(side)
print(bottom)