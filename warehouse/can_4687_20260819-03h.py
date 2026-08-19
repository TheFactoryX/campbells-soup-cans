"""
Campbell's Soup Can #4687
Produced: 2026-08-19 03:10:55
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time, sys

# ANSI color codes
C_RED   = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW= "\033[33m"
C_BLUE  = "\033[34m"
C_MAGENTA= "\033[35m"
C_RESET = "\033[0m"

def colored(text, color):
    return f"{color}{text}{C_RESET}"

quote = [
    "“Life is like an unopened birthday present:",
    "the wrapping is always weird,",
    "you never know what you'll get,",
    "and you might be stuck with it forever.”",
    "- (a neurotic philosopher who can't stop overthinking)"
]

# Decorative box dimensions
WIDTH  = 60
HEIGHT = len(quote) + 4   # extra lines for top/bottom borders

# Build top and bottom borders
top    = C_BLUE + "╔" + "═"*(WIDTH-2) + "╗" + C_RESET
bottom = C_BLUE + "╚" + "═"*(WIDTH-2) + "╝" + C_RESET

# Build side borders
def side(text):
    padded = text.center(WIDTH)
    return f"║{padded}║"

print(top)

# Typewriter animation for each line of the quote
for line in quote:
    for ch in side(colored(line, C_YELLOW)):
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write("\n")
    time.sleep(0.2)

print(bottom)