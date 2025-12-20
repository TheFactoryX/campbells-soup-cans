"""
Campbell's Soup Can #1063
Produced: 2025-12-20 16:37:40
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
import random
import sys

def woody_print(text, color='\033[93m', delay=0.05):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.02, 0.02))
    sys.stdout.write('\033[0m\n')

def main():
    quote = (
        "The universe is probably just a cosmic typo",
        "and I'm the grammatical error God keeps trying",
        "to delete with backspace... but just can't bring",
        "Himself to commit to."
    )
    
    width = max(len(line) for line in quote) + 4
    top = f'\033[36m╔{"═"*width}╗\033[0m'
    bottom = f'\033[36m╚{"═"*width}╝\033[0m'
    empty = f'\033[36m║{" "*width}║\033[0m'

    print('\n'*2)
    print(' '*(width//2-8) + '\033[33m(•_•)\033[0m')
    print(' '*(width//2-8) + '\033[33m/ >🧠\033[0m')
    print('\033[36m' + ' '*(width//2-10) + 'Woody Allen\'s Brain:\033[0m')
    
    print(top)
    print(empty)
    for line in quote:
        padded = line.center(width)
        sys.stdout.write('\033[36m║\033[0m')
        woody_print(f'\033[3m{padded}\033[0m', '\033[97m', 0.03)
        sys.stdout.write('\033[36m║\033[0m\n')
    print(empty)
    print(bottom)
    print('\n' + ' '*width + '\033[31mCTRL+S to save your existential crisis\033[0m')

if __name__ == "__main__":
    main()