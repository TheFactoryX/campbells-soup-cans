"""
Campbell's Soup Can #2676
Produced: 2026-03-10 07:08:43
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

RESET = '\033[0m'
RED   = '\033[31m'
YELLOW= '\033[33m'
CYAN  = '\033[36m'
GREEN = '\033[32m'

def c(text, color):
    return f"{color}{text}{RESET}"

# Box dimensions
BOX_INNER = 55                     # spaces inside the box
BOX_WIDTH = BOX_INNER + 2          # total width including side chars
TOP    = c('┌' + '─'*BOX_INNER + '┐', YELLOW)
BOTTOM = c('└' + '─'*BOX_INNER + '┘', YELLOW)
SIDE   = c('│', YELLOW)
EMPTY  = c('│' + ' '*BOX_INNER + '│', YELLOW)

# The philosophical quote (split for formatting)
PART1 = "I'm not afraid of death; I just don't want to be there when it happens."
PART2 = "Life is full of misery, loneliness, and suffering — and it's over"
PART3 = "much too soon. Yet here I am, trying to make a joke about it."

def pad(s):
    return s.ljust(BOX_INNER)

lines = [
    c('│' + pad(PART1) + '│', CYAN),
    c('│' + pad(PART2) + '│', CYAN),
    c('│' + pad(PART3) + '│', CYAN),
]

# Assemble the full box
box = [
    TOP,
    EMPTY,
    *lines,
    EMPTY,
    BOTTOM,
]

# Print with a tiny pause for a "type‑writer" feel
for line in box:
    sys.stdout.write(line + '\n')
    sys.stdout.flush()
    time.sleep(0.15)

# A little Woody Allen sign‑off
sys.stdout.write(c("\n — Woody Allen would smirk.", GREEN) + '\n')