"""
Campbell's Soup Can #2498
Produced: 2026-03-01 07:46:57
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
from textwrap import wrap

CYAN = '\033[96m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

quote = "I don't fear death; I fear the awkwardness of having to introduce myself to God after a life of mostly complaining about the weather. And if there's a waiting room, I hope it has decent coffee—decaf only, I'm already anxious enough."

woody_art = [
    "      ,---.       ",
    "     / o o \\      ",
    "    (   \"   )     ",
    "     \\  -  /      ",
    "      `---'       "
]

for line in woody_art:
    print(CYAN + line + RESET)

width = 60
content_width = width - 8
wrapped = wrap(quote, width=content_width)
padded = [line.ljust(content_width) for line in wrapped]

print(CYAN + " " * 3 + "╔" + "═" * (width - 6) + "╗" + RESET)
print(CYAN + " " * 3 + "║" + " " * (width - 6) + "║" + RESET)

for line in padded:
    sys.stdout.write(CYAN + " " * 3 + "║  " + RESET)
    sys.stdout.write(YELLOW)
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write(CYAN + "  ║" + RESET + "\n")

print(CYAN + " " * 3 + "║" + " " * (width - 6) + "║" + RESET)
print(CYAN + " " * 3 + "╚" + "═" * (width - 6) + "╝" + RESET)

print(BOLD + CYAN + " " * 5 + "— Woody Allen, probably while looking for his glasses" + RESET)