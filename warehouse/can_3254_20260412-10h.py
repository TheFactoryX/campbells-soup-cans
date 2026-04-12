"""
Campbell's Soup Can #3254
Produced: 2026-04-12 10:59:31
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
CYAN  = '\033[96m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'

def c(text, color):
    """Wrap text in ANSI color codes."""
    return f"{color}{text}{RESET}"

# Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a simple colored box around the quote
width = len(quote) + 4                     # interior width (including padding)
top    = c("+" + "-" * width + "+", YELLOW)  # top border
middle = f"| {c(quote, CYAN)} |"               # quoted text in cyan
bottom = top                                   # repeat border for bottom

def main():
    print(top)
    print(middle)
    print(bottom)

    # Tiny sparkle animation to make it visually fun
    for _ in range(3):
        sys.stdout.write(c(" * ", MAGENTA))
        sys.stdout.flush()
        time.sleep(0.5)
    print(RESET, end='\n')  # clean up color state

if __name__ == "__main__":
    main()