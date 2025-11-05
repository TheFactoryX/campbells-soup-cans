"""
Campbell's Soup Can #76
Produced: 2025-11-05 16:43:46
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'bold': '\033[1m'
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, color='reset', delay=0.05):
    for char in text:
        sys.stdout.write(COLORS[color] + char + COLORS['reset'])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_see_saw():
    frames = [
        r"""
          O           ___           ,
         /|\         /   \        / \
         / \        /     \      /   \
        /___\_______/       \____/_____\__
        """,
        r"""
          ,           ___           O
         / \         /   \        /|\
        /   \       /     \      / \\
        \___/______/       \____/___\\__
        """
    ]
    
    for _ in range(3):
        for frame in frames:
            clear()
            print(COLORS['cyan'] + frame + COLORS['reset'])
            time.sleep(0.5)

def main():
    clear()
    animate_see_saw()
    
    clear()
    print(COLORS['yellow'] + r"""
        __   __                   __        __
        \ \ / /__  _   _ _ __     \ \      / /_ ___   _____ 
         \ V / _ \| | | | '_ \     \ \ /\ / / _` \ \ / / _ \
          | | (_) | |_| | | | |     \ V  V / (_| |\ V /  __/
          |_|\___/ \__,_|_| |_|      \_/\_/ \__,_| \_/ \___|
    """ + COLORS['reset'])
    
    quote = [
        ("Love is like an eternal ", 'reset'),
        ("see-saw", 'yellow'),
        ("; terrifying ", 'reset'),
        ("commitment", 'red'),
        (" on one end, paralyzing ", 'reset'),
        ("loneliness", 'cyan'),
        (" on the other", 'reset'),
        ("—", 'green'),
        (" and me, ", 'reset'),
        ("stuck in the middle", 'bold'),
        (", just trying not to vomit from the ", 'reset'),
        ("motion sickness", 'green'),
        (".", 'reset')
    ]
    
    for text, color in quote:
        typewriter(text, color, delay=0.03)
    
    print("\n" + COLORS['yellow'] + "(Inspired by Woody Allen's neuroses)" + COLORS['reset'] + "\n")

if __name__ == "__main__":
    main()