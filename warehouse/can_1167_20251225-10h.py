"""
Campbell's Soup Can #1167
Produced: 2025-12-25 10:39:03
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(text, color_code, delay=0.05):
    for char in text:
        sys.stdout.write(f"{color_code}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BRIGHT_WHITE = "\033[97m"

def main():
    quote = (
        "The universe is a vast, indifferent void, and the only thing more terrifying\n"
        "than eternity is that my therapist charges by the hour."
    )
    author = "― Woody Allen (probably)"

    border_top = f"{BRIGHT_WHITE}╭{'─' * 78}╮\033[0m"
    border_bottom = f"{BRIGHT_WHITE}╰{'─' * 78}╯\033[0m"
    border_side = f"{BRIGHT_WHITE}│\033[0m"

    print()
    typewriter(border_top, BRIGHT_WHITE, 0.01)
    for line in quote.split('\n'):
        formatted_line = f"{border_side}{YELLOW}{line.center(78)}{BRIGHT_WHITE}{border_side}"
        typewriter(formatted_line, "", 0.02)
    typewriter(f"{border_side}{CYAN}{author.center(78)}{BRIGHT_WHITE}{border_side}", "", 0.02)
    typewriter(border_bottom, BRIGHT_WHITE, 0.01)
    print()

    time.sleep(1)
    typewriter(f"{MAGENTA}P.S. I'm not saying it's meaningless, but if it is... can we at least get better snacks?\033[0m", MAGENTA, 0.04)

if __name__ == "__main__":
    main()