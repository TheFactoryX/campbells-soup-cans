"""
Campbell's Soup Can #699
Produced: 2025-12-04 02:19:53
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"

# Woody Allen style quote
quote = "I'm not saying life is meaningless, but if it does have meaning," + \
        "\n" + "I'm pretty sure it's 'Buy one get one free' at the existential dread store."
author = "- Woody Allen (probably)"

def print_with_effect(text, color=YELLOW, delay=0.05):
    print(color, end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(RESET)

def blinking_cursor():
    for _ in range(3):
        print("\u2588", end='', flush=True)
        time.sleep(0.3)
        print("\b ", end='', flush=True)
        time.sleep(0.3)

def main():
    print(CLEAR)
    
    # Top border
    print(YELLOW + "╔" + "═" * 68 + "╗" + RESET)
    
    # Quote box
    print(YELLOW + "║" + RESET, end='')
    print_with_effect(quote.center(68), YELLOW, 0.04)
    print(YELLOW + "║" + RESET)
    
    # Author line
    print(YELLOW + "║" + " " * 68 + "║" + RESET)
    print(YELLOW + "║" + RESET, end='')
    print_with_effect(author.rjust(68), CYAN, 0.02)
    
    # Bottom border
    print(YELLOW + "╚" + "═" * 68 + "╝" + RESET)
    
    # Playful blinking cursor
    print("\n" + BOLD + " pondering..." + RESET, end='')
    blinking_cursor()
    print("\b \n")

if __name__ == "__main__":
    main()