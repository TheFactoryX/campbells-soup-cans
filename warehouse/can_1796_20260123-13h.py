"""
Campbell's Soup Can #1796
Produced: 2026-01-23 13:53:45
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

CYAN = '\033[96m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'
RESET = '\033[0m'

quote = "‘I’m terrified of dying … but I’m also terrified of living.’ – Woody Allen"

def boxed(text):
    w = len(text) + 4
    horiz = MAGENTA + '-' * w + RESET
    top    = MAGENTA + '+' + '-' * w + '+' + RESET
    middle = '| ' + CYAN + text + RESET + ' |'
    return f"{top}\n{middle}\n{horiz}"

def sparkle():
    art = [
        "   .-''''''-..",
        "  /          \\",
        " |  O    O   |",
        " |    <>    |",
        "  \\  '-'  /  ",
        "   `-----'   "
    ]
    for line in art:
        sys.stdout.write(YELLOW + line + RESET)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def main():
    sparkle()
    print(boxed(quote))

if __name__ == "__main__":
    main()