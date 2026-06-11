"""
Campbell's Soup Can #3911
Produced: 2026-06-11 16:20:13
Worker: Nex AGI: Nex-N2-Pro (free) (nex-agi/nex-n2-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import sys
import time

quote = "I used to think the universe had a plan, but then I got invited to a committee meeting in my own head, and now I think even the universe is just winging it."

RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wrap_text(text, width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = word if not current else current + " " + word
        if len(test) > width:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    return lines

def main():
    width = max(48, min(78, os.get_terminal_size().columns - 8))
    lines = wrap_text(quote, width - 4)
    box_width = max(len(line) for line in lines) + 4

    top = "╔" + "═" * (box_width - 2) + "╗"
    bottom = "╚" + "═" * (box_width - 2) + "╝"

    clear()
    print("\n")
    print(CYAN + "    .-.")
    print("   (o.o)      ~ tiny existential panic detected ~")
    print("    |=|")
    print("   __|__" + RESET)

    print(RED + top + RESET)

    for line in lines:
        line = line.center(box_width - 4)
        print(MAGENTA + "║" + RESET, end="")
        for ch in line:
            color = [GREEN, YELLOW, CYAN, MAGENTA][sum(map(ord, ch)) % 4]
            print(color + ch + RESET, end="", flush=True)
            time.sleep(0.006)
        print(MAGENTA + "║" + RESET)

    print(RED + bottom + RESET)
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET)