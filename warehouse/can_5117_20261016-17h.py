"""
Campbell's Soup Can #5117
Produced: 2026-10-16 17:24:34
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

quote = "I'm not afraid of death; I just don't want to be there when it happens."

RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def type_text(text, delay=0.05, color=RESET):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_border(length=60, char='*', color=CYAN):
    print(color + char * length + RESET)

def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    # Top border
    print_border()
    # Quote with typewriter effect
    type_text(quote, delay=0.05, color=YELLOW)
    # Bottom border
    print_border()

if __name__ == "__main__":
    main()