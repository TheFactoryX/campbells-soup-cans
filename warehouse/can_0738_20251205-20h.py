"""
Campbell's Soup Can #738
Produced: 2025-12-05 20:35:48
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def woody_print(text):
    colors = ['\033[93m', '\033[92m', '\033[96m']
    for char in text:
        sys.stdout.write(random.choice(colors) + char)
        sys.stdout.flush()
        time.sleep(0.05)
    print('\033[0m')

def pulse_border():
    for _ in range(3):
        print('\033[36m' + '# ' * 30 + '\033[0m')
        time.sleep(0.3)
        print('\033[35m' + '# ' * 30 + '\033[0m')
        time.sleep(0.3)

def main():
    quote = (
        "I've come to accept the meaninglessness of existence, "
        "but what really keeps me up at night is that I might have "
        "left the oven on in the vast cosmic void."
    )
    
    pulse_border()
    print('\n')
    print('\033[36m' + '  ' + '░' * 56 + '  \033[0m')
    print('\033[36m░ \033[0m', end='')
    woody_print(quote)
    print('\033[36m  ' + '░' * 56 + '  \033[0m')
    print('\n')
    print(' ' * 18 + '\033[33m☕\033[0m' + ' ' * 18)
    print(' ' * 15 + '\033[33m/ anxiety /\033[0m')
    pulse_border()

if __name__ == "__main__":
    main()