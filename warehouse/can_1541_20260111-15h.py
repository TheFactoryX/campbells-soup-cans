"""
Campbell's Soup Can #1541
Produced: 2026-01-11 15:32:24
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
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
import random

# ANSI escape codes
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLINK = "\033[5m"
RESET = "\033[0m"

quote = [
    "  Life is a cosmic joke, but the problem is  ",
    "I don't get the punchline—and I'm pretty sure",
    "         the joke's on me.          "
]

def print_with_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.02))
    print()

def main():
    max_width = max(len(line) for line in quote) + 4
    
    print("\n" * 2)
    print(f"{YELLOW}┌{'─' * (max_width - 2)}┐{RESET}")
    
    for line in quote:
        padded = line.center(max_width - 2)
        sys.stdout.write(f"{YELLOW}│{RESET}{GREEN}")
        print_with_effect(padded, 0.03)
        sys.stdout.write(f"{YELLOW}")
    
    print(f"└{'─' * (max_width - 2)}┘{RESET}")
    
    time.sleep(0.5)
    print("\n" + " " * 12 + f"{BLINK}...{RESET}", end=" ")
    time.sleep(1)
    print(f"{YELLOW}(neurotic sigh){RESET}\n")

if __name__ == "__main__":
    main()