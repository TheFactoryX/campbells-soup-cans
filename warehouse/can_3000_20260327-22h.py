"""
Campbell's Soup Can #3000
Produced: 2026-03-27 22:52:50
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RESET = "\x1b[0m"
GREEN  = "\x1b[92m"
YELLOW = "\x1b[33m"
CYAN   = "\x1b[36m"
MAGENTA= "\x1b[35m"

def slow_print(s, delay=0.03):
    """Print string character‑by‑character for a typewriter effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Woody Allen style philosophical quote
quote = "I am not afraid of death; I just don't want to be there when it happens."

# Build a simple colored ASCII box around the quote
W = 60top    = GREEN   + "┏" + "━"*(W-2) + "┓" + RESETmid    = CYAN    + "┃ " + " "*(W-4) + " ┃" + RESET
quote_l= YELLOW  + "┃ " + quote.center(W-4) + " ┃" + RESET
bottom = GREEN   + "┗" + "━"*(W-2) + "┛" + RESET

# Print the box with a tiny typing animation for extra flair
slow_print(top, 0)
slow_print(mid, 0)
slow_print(quote_l, 0)
slow_print(bottom, 0)
time.sleep(0.5)  # brief pause to emphasize the reveal