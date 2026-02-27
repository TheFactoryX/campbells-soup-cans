"""
Campbell's Soup Can #2471
Produced: 2026-02-27 21:43:56
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, random, time

# The Woody Allen style philosophical quote
QUOTE = "I’m not afraid of death; I just don’t want to be there when it happens."

# ANSI color palette (no external deps)
COLORS = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

def colored(text, name):
    """Wrap text in the specified ANSI color."""
    return f"{COLORS[name]}{text}{COLORS['reset']}"

def typewriter(s, delay=0.03):
    """Print string character‑by‑character with random colors and a tiny pause."""
    for ch in s:
        # Skip spaces for a cleaner look
        if ch == " ":
            sys.stdout.write(" ")
        else:
            sys.stdout.write(colored(ch, random.choice(list(COLORS.keys())[1:])))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Build a decorative frame around the quote
TOP    = "╔" + "═"*44 + "╗"
BOTTOM = "╚" + "═"*44 + "╝"
FRAME  = f"\n{TOP}\n| {colored(QUOTE, 'yellow')} |\n{BOTTOM}\n"

# Animate the frame line‑by‑line for extra drama
for line in FRAME.splitlines():
    typewriter(line, delay=0.02)