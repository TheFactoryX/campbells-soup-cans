"""
Campbell's Soup Can #4511
Produced: 2026-08-10 02:34:26
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
import os

def clear():
    """Clear the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    
    # Title with Woody Allen's flair
    title = "\033[1;31m" + "   WOODY'S WISDOM".center(60) + "\033[0m"
    print(title)
    print("\033[1;31m" + "="*60 + "\033[0m")
    print()
    
    # The philosophical quote (Woody Allen style)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Build a nicely colored ASCII box around the quote
    border_width = len(quote) + 6
    border = "\033[1;32m+" + "-"*border_width + "+\033[0m"
    print(border)
    interior = "\033[1;32m| \033[1;33m" + quote + "\033[1;32m  |\033[0m"
    print(interior)
    print(border)
    
    # Fun sparkle animation to punctuate the wisdom
    sparkle = "\033[1;34m*.* \033[0m"
    for _ in range(5):
        sys.stdout.write(sparkle)
        sys.stdout.flush()
        time.sleep(0.2)
    print()

if __name__ == "__main__":
    main()