"""
Campbell's Soup Can #4340
Produced: 2026-07-26 21:11:13
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen‑style philosophical quote with a splash of color and a tiny typewriter effect.
Run the script directly – no external dependencies needed.
"""

import sys
import time
import itertools

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"

# Simple spinner frames for a little animation while typing
SPINNER = itertools.cycle(['|', '/', '-', '\\'])

def typewriter(text: str, delay: float = 0.04):
    """Print text character‑by‑character with a tiny spinner."""
    for ch in text:
        sys.stdout.write(next(SPINNER))
        sys.stdout.flush()
        time.sleep(0.05)          # spinner speed
        sys.stdout.write('\b')    # erase spinner
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def print_boxed_quote():
    quote = (
        "I’m not afraid of dying; I just don’t want to be there when it happens – "
        "especially if there’s no Wi‑Fi."
    )
    width = len(quote) + 4  # padding inside the box

    # Top border
    print(f"{CYAN}{BOLD}┌{'─' * width}┐{RESET}")
    # Empty line inside box
    print(f"{CYAN}{BOLD}│{' ' * width}│{RESET}")
    # Quote line (with color)
    print(f"{CYAN}{BOLD}│ {RESET}{YELLOW}{quote}{RESET}{CYAN}{BOLD} │{RESET}")
    # Empty line inside box
    print(f"{CYAN}{BOLD}│{' ' * width}│{RESET}")
    # Bottom border
    print(f"{CYAN}{BOLD}└{'─' * width}┘{RESET}")

def main():
    # Optional: clear the screen (works on most terminals)
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    print_boxed_quote()
    # Add a little flourish after the quote
    time.sleep(0.5)
    print(f"{MAGENTA}{BOLD}«‑‑ (Woody would probably agree) ‑‑»{RESET}")

if __name__ == "__main__":
    main()