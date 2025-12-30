"""
Campbell's Soup Can #1282
Produced: 2025-12-30 16:44:52
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
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

os.system('clear')

def woody_print(text, delay=0.05):
    colors = ['\033[93m', '\033[91m', '\033[92m']
    border = '\033[91m╭──────────────────────────────────────────────────────╮\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n╰──────────────────────────────────────────────────────╯\033[0m'

    print(border[:133])
    x = 30
    y = 3
    
    for line in border.split('\n')[1:-1]:
        if y == 6:
            print(f'\033[{y};{x}H\033[93m', end='')
            for char in text:
                print(char, end='')
                sys.stdout.flush()
                time.sleep(delay)
            print('\033[0m')
        else:
            print(line)
        y += 1

    print(border[-93:])
    print("\n" * 3)

quote = "I'm terrified of eternity - mostly because I'll probably spend \nit learning to play the accordion and still be terrible at it."
woody_print(quote)
time.sleep(2)