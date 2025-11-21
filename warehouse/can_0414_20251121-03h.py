"""
Campbell's Soup Can #414
Produced: 2025-11-21 03:27:55
Worker: Microsoft: MAI DS R1 (free) (microsoft/mai-ds-r1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

# ANSI escape codes
YELLOW = "\033[38;5;214m"
CYAN = "\033[38;5;123m"
RED = "\033[38;5;196m"
BOLD = "\033[1m"
RESET = "\033[0m"

def main():
    # Clear screen
    print("\033c", end="")

    # ASCII art border
    print(f"{YELLOW}╔{'═'*60}╗{RESET}")
    for _ in range(3):
        print(f"{YELLOW}║{' '*60}║{RESET}")
    
    # Neurotic quote with typewriter effect
    quote = [
        "  The universe is utterly indifferent to human existence.",
        "  Yet here I am, obsessing that it remembered to leave",
        "  the cosmic lights on. I mean, does entropy come with",
        "  a return policy?"
    ]
    
    for line in quote:
        print(f"{YELLOW}║{RESET}  ", end="")
        for char in line:
            print(f"{CYAN}{BOLD}{char}{RESET}", end="")
            sys.stdout.flush()
            time.sleep(0.03)
        print(f"{YELLOW}  ║{RESET}")
        time.sleep(0.2)
    
    # Closing border and attribution
    for _ in range(3):
        print(f"{YELLOW}║{' '*60}║{RESET}")
    print(f"{YELLOW}╚{'═'*60}╝{RESET}")
    time.sleep(0.5)
    print(f"\n{RED}  – Woody Allen (probably){RESET}")
    input("\n\nPress Enter to face existential reality...")

if __name__ == "__main__":
    main()