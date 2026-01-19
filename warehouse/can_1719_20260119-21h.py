"""
Campbell's Soup Can #1719
Produced: 2026-01-19 21:33:15
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
from itertools import cycle

def woody_allen_quote():
    # ANSI color codes
    colors = {
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m',
        'RESET': '\033[0m',
        'BOLD': '\033[1m'
    }
    
    # Woody Allen style quote
    quote = "I worry so much about my mortality that I forget to live. But then again, if I'm not worried, what's the point of being me?"
    
    # ASCII art frame
    border = "═" * 70
    bar = "║"
    
    # Animation cycle
    color_cycle = cycle([colors['RED'], colors['GREEN'], colors['YELLOW'], 
                         colors['BLUE'], colors['MAGENTA'], colors['CYAN']])
    
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Print animated border
    print(f"{colors['MAGENTA']}{border}{colors['RESET']}")
    print(f"{colors['MAGENTA']}{bar}{colors['WHITE']}{'WOODY ALLEN ON EXISTENTIAL ANXIETY':^70}{colors['MAGENTA']}{bar}{colors['RESET']}")
    print(f"{colors['MAGENTA']}{bar}{'':^70}{colors['MAGENTA']}{bar}{colors['RESET']}")
    
    # Print quote with color animation
    print(f"{colors['MAGENTA']}{bar}{colors['WHITE']}", end="")
    for char in quote:
        color = next(color_cycle)
        print(f"{color}{char}{colors['WHITE']}", end="")
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"{colors['MAGENTA']}{bar}{colors['RESET']}")
    
    print(f"{colors['MAGENTA']}{bar}{'':^70}{colors['MAGENTA']}{bar}{colors['RESET']}")
    print(f"{colors['MAGENTA']}{border}{colors['RESET']}")
    
    # Print signature
    print(f"\n{colors['YELLOW']}{colors['BOLD']}- Woody Allen{colors['RESET']:^70}")

if __name__ == "__main__":
    woody_allen_quote()