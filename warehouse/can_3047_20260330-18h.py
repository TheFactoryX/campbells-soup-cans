"""
Campbell's Soup Can #3047
Produced: 2026-03-30 18:06:45
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# ANSI color codes
RED   = '\033[31m'
GREEN = '\033[32m'
YELLOW= '\033[33m'
BLUE  = '\033[34m'
MAGENTA = '\033[35m'
CYAN  = '\033[36m'
RESET = '\033[0m'

def color(txt, col):
    return f"{col}{txt}{RESET}"

def typewriter(t, d=0.025):
    for ch in t:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(d)
    sys.stdout.write('\n')

# Woody Allen‑style philosophical quote
quote = ("I’m not afraid of death; I just don’t want to miss the dessert "
         "at my own funeral.")

# Simple cat‑ascii with tuna can (makes it look like a therapist’s couch)
art = [
    " /\\   /\\   /\\",
    " /  \\_/  \\_/  \\",
    " |  o   o |   o  |",
    " |      |      |",
    "  \\____/  \\____/"
]

# Determine frame width
w = max(len(l) for l in art) + 4
border = color("+" + "-" * w + "+", YELLOW)

def display():
    print("\n")
    print(border)
    for line in art:
        padded = line + " " * (w - len(line) - 2)
        print(color(f"| {padded} |", CYAN))
    print(border)
    print()
    # Print the quote with a little drama
    print(color(">>> ", MAGENTA), end="")
    typewriter(quote, 0.018)

if __name__ == "__main__":
    # Flicker effect (optional)
    for _ in range(3):
        sys.stdout.write("\a")   # ASCII bell rings
        sys.stdout.flush()
        time.sleep(0.3)
    display()