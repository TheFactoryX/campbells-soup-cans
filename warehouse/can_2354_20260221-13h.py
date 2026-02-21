"""
Campbell's Soup Can #2354
Produced: 2026-02-21 13:11:21
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import itertools

# ANSI escape codes
RESET = "\033[0m"
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
CYAN  = "\033[36m"

def typewriter(text, delay=0.03):
    """Print text character‑by‑character with cycling colors."""
    colors = itertools.cycle([RED, GREEN, YELLOW])
    for ch in text:
        sys.stdout.write(colors.__next__() + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)

def spin(delay=0.15, frames=30):
    """A tiny neurotically spinning symbol."""
    symbols = itertools.cycle([CYAN + "●", GREEN + "○", YELLOW + "✦", RED + "⚡"])
    for _ in range(frames):
        sys.stdout.write(next(symbols))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def main():
    # Width of the dash line inside the box
    border_width = 70
    total_len = border_width + 2               # dash line + two borders

    # Woody Allen quote (the ONE philosophical statement)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Compute left padding so the text appears roughly centered
    left_spaces = " " * ((total_len - len(quote)) // 2)

    # ----- PRINT THE TOP BORDER -----
    sys.stdout.write(CYAN + "╔" + "-" * border_width + "╗" + RESET + "\n")
    sys.stdout.flush()

    # ----- PRINT THE QUOTE -----
    sys.stdout.write(left_spaces)               # pure spaces, no color
    sys.stdout.flush()
    typewriter(left_spaces + quote, delay=0.025)

    # ----- PRINT THE BOTTOM BORDER -----
    sys.stdout.write(CYAN + "╚" + "-" * border_width + "╝" + RESET + "\n")
    sys.stdout.flush()

    # ----- ADD A SMALL SPINNING ANIMATION -----
    sys.stdout.write("\n")
    spin()
    sys.stdout.write(RESET)

if __name__ == "__main__":
    main()