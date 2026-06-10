"""
Campbell's Soup Can #3903
Produced: 2026-06-10 11:03:46
Worker: Nex AGI: Nex-N2-Pro (free) (nex-agi/nex-n2-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def ansi(code):
    return f"\033[{code}m"

def typewrite(text, delay=0.025):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

quote = (
    "Life is a cosmic practical joke; "
    "I just wish the universe would stop making me the punch line "
    "and start offering a refund."
)

frame_top = "╔" + "═" * 66 + "╗"
frame_bottom = "╚" + "═" * 66 + "╝"

print()
print(ansi("38;5;45") + ansi("1") + frame_top + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 66 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + ansi("38;5;226") + ansi("1") + "    *  *  *  EXISTENTIAL REFUND DESK  *  *  *    " + ansi("0") + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 66 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 18 + ansi("38;5;201") + "╭" + "─" * 28 + "╮" + ansi("0") + " " * 18 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 18 + ansi("38;5;201") + "│" + ansi("0") + ansi("38;5;220") + "   .-\"\"\"-.   " + ansi("0") + ansi("38;5;201") + "│" + ansi("0") + " " * 18 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 18 + ansi("38;5;201") + "│" + ansi("0") + ansi("38;5;220") + "  /  o o  \\  " + ansi("0") + ansi("38;5;201") + "│" + ansi("0") + " " * 18 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 18 + ansi("38;5;201") + "│" + ansi("0") + ansi("38;5;220") + "  \\  ~  /   " + ansi("0") + ansi("38;5;201") + "│" + ansi("0") + " " * 18 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 18 + ansi("38;5;201") + "╰" + "─" * 28 + "╯" + ansi("0") + " " * 18 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0") + " " * 66 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + "║" + ansi("0"), end=" ")
typewrite(ansi("38;5;15") + ansi("1") + quote + ansi("0"), delay=0.018)
print(ansi("38;5;45") + "║" + ansi("0") + " " * 66 + ansi("38;5;45") + "║" + ansi("0"))
print(ansi("38;5;45") + ansi("1") + frame_bottom + ansi("0"))
print()