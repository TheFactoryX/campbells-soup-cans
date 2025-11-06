"""
Campbell's Soup Can #88
Produced: 2025-11-06 06:46:05
Worker: Microsoft: MAI DS R1 (free) (microsoft/mai-ds-r1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def clear_screen():
    print("\033[2J\033[H", end="")

def type_effect(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    clear_screen()
    
    # Box top
    print("\033[33m" + "╔" + "═"*48 + "╗\033[0m")
    
    # Quote lines
    lines = [
        "  I'm convinced there's a cosmic vending machine that sells",
        "meaning, but I keep inserting existential quarters and getting",
        "  out a bag of stale \033[35mexistential pretzels\033[0m. The ",
        "   instructions were probably in Swedish anyway."
    ]
    
    for line in lines:
        print("\033[33m║\033[0m", end="")
        type_effect(f"\033[1;37m{line:48}\033[0m", 0.03)
        time.sleep(0.2)
    
    # Box bottom
    print("\033[33m╚" + "═"*48 + "╝\033[0m")
    
    # Attribution with dramatic effect
    time.sleep(0.5)
    type_effect("\n" + " "*18 + "\033[1;31m- Woody Allen's Plumbing Supplier\033[0m", 0.04)
    time.sleep(2)

if __name__ == "__main__":
    main()