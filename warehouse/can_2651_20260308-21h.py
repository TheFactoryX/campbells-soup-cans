"""
Campbell's Soup Can #2651
Produced: 2026-03-08 21:36:59
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

# ANSI colour codes
BOLD   = '\033[1m'
MAGENTA= '\033[35m'
YELLOW = '\033[33m'
CYAN   = '\033[36m'
RESET  = '\033[0m'

# Woody Allen's neurotic wisdom
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Create a colourful box around the quote
border_top    = BOLD + MAGENTA + '+' + '-'*(len(quote)+4) + '+' + RESET
quote_line    = '│ ' + YELLOW + quote + RESET + ' │'
border_bottom = border_top

# Animate a string character‑by‑character
def animate(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# Fancy animated reveal
for line in (border_top, quote_line, border_bottom):
    animate(line, delay=0.015)

# A tiny cosmic wink to finish
animate(CYAN + "★ " + RESET + "— the universe giggles " + CYAN + "★" + RESET, delay=0.02)