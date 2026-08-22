"""
Campbell's Soup Can #4767
Produced: 2026-08-22 13:44:28
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_writer(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    quote = (
        "I'm not afraid of dying; I just don't want to be there when it happens, "
        "especially if I'm wearing socks with sandals."
    )
    width = 58
    wrapped = textwrap.wrap(quote, width=width)

    # Top border
    print(CYAN + BOLD + "╔" + "═" * (width + 2) + "╗" + RESET)
    for line in wrapped:
        sys.stdout.write(CYAN + BOLD + "║ " + RESET)
        type_writer(line.ljust(width), delay=0.05)
        print(CYAN + BOLD + " ║" + RESET)
    # Bottom border
    print(CYAN + BOLD + "╚" + "═" * (width + 2) + "╝" + RESET)

    # A tiny neurotic Woody‑Allen‑style face
    face = [
        "   _____ ",
        "  /     \\",
        " |  o o  |",
        " |   ^   |",
        " |  '-'  |",
        "  \\_____/"
    ]
    print(MAGENTA)
    for ln in face:
        print(ln)
    print(RESET)

if __name__ == "__main__":
    main()