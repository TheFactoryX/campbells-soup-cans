"""
Campbell's Soup Can #4545
Produced: 2026-08-12 02:44:33
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
RED  = '\033[91m'
GREEN = '\033[92m'
CYAN  = '\033[96m'
RESET = '\033[0m'

# The Woody‑Allen‑style philosophical quote
quote = "I’m terrified of oblivion, so I stay up late hoping the universe will forget to turn off the lights."

# Build a simple colored box around the quote
border = "+" + "-" * (len(quote) + 4) + "+"
top    = border
middle = "| " + quote + " |"
bottom = border

def typewriter(s, delay=0.03):
    """Prints a string character‑by‑character for a typewriter effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def colored(text, color):
    """Wraps text in the given ANSI color and resets afterwards."""
    return f"{color}{text}{RESET}"

# Print a little spacing
sys.stdout.write("\n\n")
typewriter(colored(top, CYAN))
typewriter(colored(middle, GREEN))
typewriter(colored(bottom, CYAN))

# Clean up color codes (optional)
sys.stdout.write(RESET)