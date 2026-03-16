"""
Campbell's Soup Can #2804
Produced: 2026-03-16 21:54:29
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def main():
    # Woody Allen style quote
    quote = """
    Life is a series of near misses. A lot of what we ascribe to luck is actually due to preparation. The preparation is everything.
    """
    
    # ANSI color codes
    colors = {
        'red': '\033[1;31;40m',
        'green': '\033[1;32;40m',
        'yellow': '\033[1;33;40m',
        'blue': '\033[1;34;40m',
        'magenta': '\033[1;35;40m',
        'cyan': '\033[1;36;40m',
        'reset': '\033[0m'
    }
    
    # Create ASCII art frame
    frame = f"""
    {colors['blue']}╔═══════════════════════════════════════╗{colors['reset']}
    {colors['yellow']}║{colors['reset']}  {colors['cyan']}W O O D Y   A L L E N   S A Y S{colors['reset']}  {colors['yellow']}║{colors['reset']}
    {colors['blue']}║{colors['reset']}  {colors['green']}Life is a series of near misses.{colors['reset']}  {colors['yellow']}║{colors['reset']}
    {colors['blue']}║{colors['reset']}  {colors['red']}A lot of what we ascribe to luck is actually due to preparation.{colors['reset']}  {colors['yellow']}║{colors['reset']}
    {colors['blue']}║{colors['reset']}  {colors['magenta']}The preparation is everything.{colors['reset']}  {colors['yellow']}║{colors['reset']}
    {colors['blue']}╚═══════════════════════════════════════╝{colors['reset']}
    """
    
    # Print with colorful text
    print(frame)
    print(f"{colors['cyan']}  " + quote + f"{colors['reset']}")
    print(f"{colors['blue']}╚═══════════════════════════════════════╝{colors['reset']}")

if __name__ == "__main__":
    main()