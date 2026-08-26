"""
Campbell's Soup Can #4852
Produced: 2026-08-26 09:57:19
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_border():
    border = "=" * 60
    print(CYAN + border + RESET)

def typewriter(text, delay=0.05):
    for ch in text:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print_border()
    quote = "I'm not afraid of death; I'm just afraid of being stuck in traffic on the way to the afterlife."
    typewriter(quote)
    print_border()

if __name__ == "__main__":
    main()