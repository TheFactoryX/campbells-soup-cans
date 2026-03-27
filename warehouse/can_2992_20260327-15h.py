"""
Campbell's Soup Can #2992
Produced: 2026-03-27 15:09:25
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

# ANSI color codes
RESET = '\033[0m'
MAGENTA = '\033[35m'
YELLOW = '\033[33m'

def cprint(s, col):
    sys.stdout.write(col + s + RESET + '\n')

# Neurotic ASCII art (typewriter effect)
art = r'''
      ___________
     /           /|
    /   _   _   / |
   |    (o) (o) |  |
   |      <     | /
    \   _   _   /  /
     \_________/  /
'''

quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Print the ASCII art slowly for a playful effect
for ch in art:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.02)
sys.stdout.write("\n")

# Build a colorful box around the quote
width = len(f"| {quote} |")               # total width of the inner line
border = YELLOW + "+" + "-" * (width - 2) + "+" + RESET
inner_line = f"| {quote} |"
boxed = "\n".join([border, inner_line, border])

cprint(boxed, MAGENTA)