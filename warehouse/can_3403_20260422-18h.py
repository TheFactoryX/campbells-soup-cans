"""
Campbell's Soup Can #3403
Produced: 2026-04-22 18:13:57
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def woody_allen_quote():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # ASCII art frame
    print("\033[1;36m" + "╔" + "═" * 80 + "╗")
    print("║" + " " * 28 + "\033[5;33mWOODY ALLEN ON EXISTENCE\033[0;36m" + " " * 28 + "║")
    print("╚" + "═" * 80 + "╝\033[0m")
    print()
    
    # The quote with different colors
    quote = "\033[1;37mI spent my entire life worrying about being insignificant,\033[0;31m and it turns out I was right all along.\033[1;37m The universe doesn't care,\033[0;33m and neither should you...\033[1;37m but I'll probably keep worrying anyway.\033[0m"
    
    # Center the quote in a box
    print("\033[1;36m" + "╔" + "═" * 80 + "╗")
    print("\033[4;37m" + "║" + quote.center(78) + "║\033[0m")
    print("\033[1;36m" + "╚" + "═" * 80 + "╝\033[0m")
    
    # Sign off with italics
    print("\033[3;35m" + "                 - Woody Allen")
    print("\033[0m")
    
    # Add a subtle animation
    time.sleep(0.5)
    print("\033[3;37m" + "                 (probably)")
    print("\033[0m")

if __name__ == "__main__":
    woody_allen_quote()