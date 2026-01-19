"""
Campbell's Soup Can #1708
Produced: 2026-01-19 10:48:29
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
import random

def type_effect(text, delay=0.03):
    colors = ['\033[93m', '\033[95m', '\033[96m']
    for i, char in enumerate(text):
        sys.stdout.write(random.choice(colors) + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay * (0.8 if i % 2 else 1.2))
    print()

def main():
    thought_cloud = r'''
       _____,-.___ 
     .'`   .'  _)
    /    ,'  _/`-)
   (    /  _/`-.__)
    \  _/,-'      
     `._/         
    '''
    
    quote = "I'm convinced the universe is just God's way of avoiding commitment."
    epilogue = "\033[3m(Except on weekends, when He ghosts us entirely)\033[0m"
    
    print('\033[36m' + thought_cloud + '\033[0m')
    time.sleep(0.5)
    
    print('\033[1m', end='')
    type_effect(' ' * 10 + '« ' + quote + ' »')
    print('\033[0m', end='')
    
    time.sleep(1)
    words = epilogue.split()
    for i, word in enumerate(words):
        print(f'\033[90m{word}\033[0m', end=' ' if i < len(words)-1 else '', flush=True)
        time.sleep(0.5 if i == len(words)-1 else 0.15)
    
    print('\n\n\033[35m\t\t— Nervous Human #7,123,456\033[0m')
    time.sleep(0.5)
    print('\033[5m\t\t\t(pants irrevocably soiled)\033[0m')

if __name__ == "__main__":
    main()