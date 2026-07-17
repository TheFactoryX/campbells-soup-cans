"""
Campbell's Soup Can #4230
Produced: 2026-07-17 15:40:23
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

def clear():
    print("\033c\033[J", end="")   # clear screen

clear()
# loading animation
dots = ""
for i in range(3):
    dots += "."
    sys.stdout.write(f"\rLoading{dots}")
    sys.stdout.flush()
    time.sleep(0.4)
clear()

# Woody Allen‑style philosophical quote
quote = (
    "I don't want to achieve immortality through my work; "
    "I want to achieve it by dodging the inevitable."
)

# ANSI colour codes
c_red   = "\033[91m"
c_green = "\033[92m"
c_yellow= "\033[93m"
c_magenta= "\033[95m"
c_cyan  = "\033[96m"
c_reset = "\033[0m"

width = 60
border = c_yellow + "╔" + "═"*(width-2) + "╗" + c_reset
bottom = c_yellow + "╚" + "═"*(width-2) + "╝" + c_reset
side   = c_yellow + "║" + c_reset

# print coloured box around the quote
print(border)
print(side, c_magenta + quote.center(width-2) + c_reset, side)
print(bottom)

# twinkling sparkle animation (purely decorative)
stars = ["✨", "⚡", "🌟", "💫"]
for _ in range(5):
    line = " ".join(c_cyan + s + c_reset for s in stars)
    sys.stdout.write("\r" + line)
    sys.stdout.flush()
    time.sleep(0.2)
print()