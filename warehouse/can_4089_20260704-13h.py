"""
Campbell's Soup Can #4089
Produced: 2026-07-04 13:58:31
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

def colorize(text, color):
    return f"{color}{text}{RESET}"

# The Woody Allen‑style philosophical quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."
QUOTE2 = "— Woody Allen (in his mind)"

# Simple border constants
BORDER_LEN = 55
HORIZ_BORDER = "═" * BORDER_LEN
VERT_SIDES = " " * BORDER_LEN

def draw_box(color):
    sys.stdout.write(color)
    sys.stdout.write(f"+{HORIZ_BORDER}+\n")
    sys.stdout.write(color)
    sys.stdout.write(f"|{VERT_SIDES}|\n")
    sys.stdout.write(color)
    sys.stdout.write(f"|{VERT_SIDES}|\n")
    sys.stdout.write(color)
    sys.stdout.write(f"+{HORIZ_BORDER}+\n")
    sys.stdout.write(RESET)

def type_animated(s, color, delay=0.03):
    for ch in s:
        sys.stdout.write(colorize(ch, color))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    draw_box(CYAN)
    type_animated(QUOTE, MAGENTA)
    type_animated(QUOTE2, YELLOW)
    time.sleep(0.5)

    # Little closing animation
    for _ in range(3):
        sys.stdout.write(colorize("«", CYAN))
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(colorize("»", CYAN))
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()