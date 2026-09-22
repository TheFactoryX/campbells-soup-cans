"""
Campbell's Soup Can #5007
Produced: 2026-09-22 18:55:07
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"

def typewriter(text, color=""):
    """Print text character by character with a delay for a typing effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.04)

def main():
    # ASCII art top border
    top = f"{CYAN}   _____________{RESET}"
    # ASCII art side frame (left part)
    left = f"{CYAN}  (             )_{RESET}"
    # ASCII art bottom border
    bottom = f"{CYAN}   _____________{RESET}"

    print(top)
    print(left)

    # The philosophical quote in Woody Allen's style (enclosed in fancy quotes)
    quote = f"{YELLOW}{BOLD}“I'm not afraid of death; I just don't want to be there when the universe decides to end the party.”{RESET}"
    typewriter(quote + "\n")

    # A playful signature
    sig = f"{GREEN}{BOLD}— Woody-ish{RESET}"
    typewriter(sig + "\n")

    print(bottom)

if __name__ == "__main__":
    main()