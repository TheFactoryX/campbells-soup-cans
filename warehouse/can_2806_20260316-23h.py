"""
Campbell's Soup Can #2806
Produced: 2026-03-16 23:43:51
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

# ANSI colors
RESET = '\033[0m'
CYAN  = '\033[36m'
MAGENTA = '\033[35m'

def typewriter(text, color='', delay=0.02):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

quote = "I'm not afraid of death; I just keep forgetting to RSVP to the after-life."
box_w = len(quote) + 4
top    = CYAN + '+' + '-' * box_w + '+' + RESET
side   = CYAN + '| ' + RESET

print(top)
typewriter(CYAN + '| ' + MAGENTA + quote + ' ' * (box_w - len(quote)) + ' |' + RESET, color=MAGENTA)
print(top)