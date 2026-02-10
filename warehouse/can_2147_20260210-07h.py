"""
Campbell's Soup Can #2147
Produced: 2026-02-10 07:32:09
Worker: Aurora Alpha (openrouter/aurora-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

# ANSI color codes
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RESET  = "\033[0m"

# The Woody‑Allen‑style philosophical gem
QUOTE = "I think, therefore I’m terrified… and that’s the only thing I’m certain about."

def type_print(text: str, delay: float = 0.03, color: str = YELLOW) -> None:
    """Print text character‑by‑character with a tiny pause for effect."""
    for ch in text:
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)

def main() -> None:
    width = len(QUOTE)

    # Build the three parts of the box
    top    = f"{CYAN}┌{'─' * (width + 2)}┐{RESET}"
    left   = f"{CYAN}│ {RESET}"
    right  = f"{CYAN} │{RESET}"
    bottom = f"{CYAN}└{'─' * (width + 2)}┘{RESET}"

    # Print top border
    print(top)

    # Print left border, then the animated quote, then right border
    sys.stdout.write(left)
    type_print(QUOTE, delay=0.03, color=YELLOW)
    sys.stdout.write(right + "\n")

    # Print bottom border
    print(bottom)

if __name__ == "__main__":
    main()