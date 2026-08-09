"""
Campbell's Soup Can #4498
Produced: 2026-08-09 11:45:16
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to miss the afterlife’s opening night."

def typewriter(s, delay=0.03):
    """Prints a string character‑by‑character for a type‑writer effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# ANSI colour codes
RESET   = "\033[0m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
BOLD    = "\033[1m"

# Decorative ASCII art (coloured)
top    = CYAN + "╔" + "═"*48 + "╗" + RESET
bottom = CYAN + "╚" + "═"*48 + "╝" + RESET
quote_line = CYAN + BOLD + quote + RESET

# Animate the bordered quote
typewriter(top)
typewriter(quote_line)
typewriter(bottom)