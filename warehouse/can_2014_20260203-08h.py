"""
Campbell's Soup Can #2014
Produced: 2026-02-03 08:57:28
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time

# ANSI color codes
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
MAGENTA= "\033[35m"
CYAN   = "\033[36m"
WHITE  = "\033[37m"
RESET  = "\033[0m"

# Woody Allen‑style philosophical quote
QUOTE = ("I'm not afraid of death; I just don't want to be there when it happens. "
         "Life's like an uptight, neurotic teenager who's constantly worried "
         "that the universe will ask it for a homework extension.")

# Visual layout settings
WIDTH = 80                     # total characters per line
DELAY = 0.03                   # type‑writer speed (seconds)

def typewrite(txt, color):
    """Print txt character‑by‑character in the given ANSI color."""
    for ch in txt:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(DELAY)
    sys.stdout.flush()

def main():
    # Top and bottom borders
    top    = YELLOW + "╔" + "═" * (WIDTH - 2) + "╗" + RESET
    bottom = YELLOW + "╚" + "═" * (WIDTH - 2) + "╝" + RESET
    side   = YELLOW + "║" + RESET

    # Calculate filler spaces so the line is exactly WIDTH characters wide
    filler_len = WIDTH - 4 - len(QUOTE)
    filler = ' ' * max(filler_len, 0)

    # Build the centered‑looking line
    line = f"{side}{CYAN}{QUOTE}{filler}{RESET}{side}"

    # Print the animated box
    print(top)
    typewrite(line, MAGENTA)
    print()               # move to next line
    print(bottom)

if __name__ == "__main__":
    main()