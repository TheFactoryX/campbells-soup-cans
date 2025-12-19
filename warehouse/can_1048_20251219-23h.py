"""
Campbell's Soup Can #1048
Produced: 2025-12-19 23:30:30
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# Classic Woody Allen neurotic philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = " — Woody Allen"

# ANSI color codes
RED    = "\033[31m"
YELLOW = "\033[33m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
MAGENTA= "\033[35m"
RESET  = "\033[0m"

def typewriter(text, speed=0.04):
    """Prints text with a cycling rainbow effect."""
    colors = [CYAN, YELLOW, GREEN, MAGENTA]
    for i, ch in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")

# Build a decorative box
box_width = max(len(quote), len(author)) + 4
border = RED + "+" + "-" * box_width + "+" + RESET
top    = RED + "|" + " " * box_width + "|" + RESET
bottom = border

# Center the text inside the box
quote_line = " " + quote + " "
author_line = " " + author + " "

print(border)
print(top)
print(f"|{YELLOW}{quote_line:<{box_width}}{RESET}|")
print(f"|{GREEN}{author_line:<{box_width}}{RESET}|")
print(top)

# Tiny sparkle animation
def sparkle():
    stars = MAGENTA + "*" * 5 + RESET
    typewriter(f"{stars} BOOM! {stars}", 0.1)

sparkle()
typewriter(f"{CYAN} — A neurotic Python thought{RESET}", 0.07)