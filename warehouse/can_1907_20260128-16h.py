"""
Campbell's Soup Can #1907
Produced: 2026-01-28 16:57:31
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
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, color_code, delay=0.03):
    for char in text:
        print(f"\033[{color_code}m{char}\033[0m", end='', flush=True)
        time.sleep(delay)
    print()

def main():
    clear_screen()
    quote = (
        "Life is meaningless, but at least you can delay that realization "
        "by obsessing over whether you left the stove on."
    )
    author = "- Woody Allen's Sleep Paralysis Demon"

    # ASCII art box dimensions
    box_width = len(max(quote.split('\n'), key=len)) + 4
    top_border = f"\033[36m╭{'─'*(box_width-2)}╮\033[0m"
    bottom_border = f"\033[36m╰{'─'*(box_width-2)}╯\033[0m"
    
    print(top_border)
    print("\033[36m│ \033[0m", end='')
    typewriter(quote, "33", 0.04)
    print("\033[36m│ \033[0m", end='')
    typewriter(author, "3;36", 0.05)
    print(bottom_border)
    time.sleep(2)
    print("\n\033[35m(Now go check your stove.)\033[0m")

if __name__ == "__main__":
    main()