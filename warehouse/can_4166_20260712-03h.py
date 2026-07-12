"""
Campbell's Soup Can #4166
Produced: 2026-07-12 03:57:11
Worker: Tencent: Hy3 (free) (tencent/hy3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
import random

def main():
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    quote = ("I'm not afraid of death; I'm afraid of the awkward silence "
             "beforehand, and the fact that my neuroses won't fit in the coffin. "
             "Besides, who will water my hypochondria?")
    
    words = quote.split()
    lines = []
    current = ""
    width = 54
    for w in words:
        if len(current) + len(w) + 1 <= width:
            current += w + " "
        else:
            lines.append(current.strip())
            current = w + " "
    lines.append(current.strip())
    
    print()
    print(BOLD + RED + "        ~ A WOODY ALLEN-ESQUE EXISTENTIAL CRISIS ~" + RESET)
    print()
    print(CYAN + "╔" + "═" * (width + 2) + "╗" + RESET)
    
    for line in lines:
        sys.stdout.write(CYAN + "║ " + RESET + YELLOW)
        for char in line:
            if char != ' ' and random.random() < 0.04:
                wrong = random.choice('qwrtypsdfghjklzxcvbnm')
                sys.stdout.write(wrong)
                sys.stdout.flush()
                time.sleep(0.1)
                sys.stdout.write('\b \b')
                sys.stdout.flush()
                time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(" " * (width - len(line)) + CYAN + " ║" + RESET + "\n")
    
    attr = "- Overheard at the analyst's office"
    sys.stdout.write(CYAN + "║ " + RESET + RED + attr + " " * (width - len(attr)) + CYAN + " ║" + RESET + "\n")
    print(CYAN + "╚" + "═" * (width + 2) + "╝" + RESET)
    print()
    time.sleep(1)
    print(GREEN + "*existential dread intensifies, but the pizza arrives*" + RESET)
    print()

if __name__ == "__main__":
    main()