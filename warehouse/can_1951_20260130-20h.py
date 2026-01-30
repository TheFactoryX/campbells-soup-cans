"""
Campbell's Soup Can #1951
Produced: 2026-01-30 20:47:22
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

def woody_print():
    colors = {
        'yellow': '\033[93m',
        'red': '\033[91m',
        'end': '\033[0m',
        'bold': '\033[1m',
    }
    
    quote = (
        "I'm terrified of the cosmic void,\n"
        "but what really keeps me awake is\n"
        "whether 'void' is spelled with two 'o's."
    )
    
    border = f"{colors['red']}╔{'═' * 36}╗{colors['end']}"
    middle = f"{colors['red']}║{colors['end']}" 
    footer = f"{colors['red']}╚{'═' * 36}╝{colors['end']}"
    
    author = f"{colors['yellow']}    — Woody Allen (probably){colors['end']}"
    
    sys.stdout.write(border + '\n')
    sys.stdout.write(f"{middle}{colors['yellow']}{' ' * 2}{quote.center(34)}{' ' * 2}{colors['end']}{middle}\n")
    sys.stdout.write(f"{middle}{author.center(36)}{middle}\n")
    sys.stdout.write(footer + '\n')
    
    # Add dramatic delay between lines
    time.sleep(0.5)
    for _ in range(3):
        sys.stdout.write(f"{colors['red']}...{colors['end']} ")
        sys.stdout.flush()
        time.sleep(0.8)
    print()

woody_print()