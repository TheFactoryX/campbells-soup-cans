"""
Campbell's Soup Can #3247
Produced: 2026-04-11 22:52:12
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
class C:
    RESET = "\033[0m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    RED = "\033[31m"

def color(text, cls):
    return f"{cls}{text}{C.RESET}"

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def bordered(lines, char="*"):
    width = max(len(l) for l in lines) + 4
    horiz = char * width
    top = f"{char}{horiz}{char}"
    print(color(top, C.CYAN))
    for line in lines:
        padded = f" {line.ljust(width-2)} "
        print(color(padded, C.YELLOW))
    print(color(top, C.CYAN))

# Woody Allen‑style philosophical nugget
quote = [
    "I'm not afraid of death;",
    "I just don't want to be there when it happens."
]

# Simple flicker animation
for _ in range(2):
    clear()
    bordered(quote, char="-")
    time.sleep(0.8)
    clear()
    bordered(quote, char="=")
    time.sleep(0.8)

# Final static display with extra flair
clear()
print(color("    \"I'm not afraid of death; I just don't want to be there when it happens.\"", C.MAGENTA))
print()
print(color("    ― Woody Allen (re‑imagined)", C.CYAN))