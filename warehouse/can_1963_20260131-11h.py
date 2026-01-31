"""
Campbell's Soup Can #1963
Produced: 2026-01-31 11:33:39
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

# ANSI escape codes
YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

def print_animated(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear screen
    print("\033[2J\033[H")
    
    quote = [
        "  I'm convinced there's a small alien in my brain that",
        "controls my anxiety, but when I called NASA they said",
        "they don't do home visits and suggested I try meditation",
        "       or at least stop watching CSPAN at 3AM.  "
    ]
    
    max_width = max(len(line) for line in quote) + 4
    
    print(f"{MAGENTA}╔{'═' * max_width}╗{RESET}")
    for line in quote:
        padded_line = line.center(max_width)
        print(f"{MAGENTA}║{YELLOW}{padded_line}{MAGENTA}║{RESET}")
        time.sleep(0.3)
    print(f"{MAGENTA}╚{'═' * max_width}╝{RESET}")
    
    time.sleep(0.5)
    print(f"\n{RED}{ITALIC}        — Woody Allen's Inner Monologue{RESET}")
    
    # Sparkles animation
    time.sleep(1)
    print(f"\n{CYAN}")
    for _ in range(3):
        print("       ✨" + "★" * 10 + "✨")
        time.sleep(0.2)
    print(RESET)

if __name__ == "__main__":
    main()