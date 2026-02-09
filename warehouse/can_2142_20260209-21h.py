"""
Campbell's Soup Can #2142
Produced: 2026-02-09 21:56:34
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, itertools

# ANSI color codes
RED   = "\033[91m"
GREEN = "\033[92m"
YELLOW= "\033[93m"
BLUE  = "\033[94m"
MAGENTA= "\033[95m"
RESET = "\033[0m"

# Our Woody Allen‑ish philosophical gem
QUOTE = (
    "Life is like an Onion: you keep peeling away the layers, "
    "and all you get is tears and a sudden urge to quit."
)

# Simple typewriter effect
def typewriter(txt, delay=0.04):
    for ch in txt:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

# Fancy box drawing characters
TOP    = "┌" + "─" * 55 + "┐"
BOTTOM = "└" + "─" * 55 + "┘"
MID    = "│" + " " * 55 + "│"
SPACE  = " " * 27   # center spacer

# Center the quote inside the box
lines = QUOTE.split()
centered = " ".join(lines)
spaces = len(TOP) - len("│ " + centered + " │")
left  = " " * ((spaces - 2) // 2)
right = " " * (spaces - len(left) - 2)

# Build the colored, animated output
def print_boxed_quote():
    sys.stdout.write(RED + TOP + RESET + "\n")
    sys.stdout.write(
        BLUE + f"│ {left}{YELLOW}{centered}{left}{RESET}│" + BLUE + "\n"
    )
    sys.stdout.write(RED + BOTTOM + RESET + "\n")

# Animate the box appearing
def animate():
    # flicker the box a few times
    for _ in range(3):
        print_boxed_quote()
        time.sleep(0.2)
        sys.stdout.write("\033[2J\033[H")  # clear screen
        time.sleep(0.1)
    # finally print in green with the quote typing
    typewriter(f"{GREEN}{QUOTE}{RESET}", delay=0.02)

if __name__ == "__main__":
    animate()