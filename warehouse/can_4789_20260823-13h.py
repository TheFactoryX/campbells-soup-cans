"""
Campbell's Soup Can #4789
Produced: 2026-08-23 13:02:00
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
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

quote = "I'm not afraid of death; I'm just not keen on the whole 'being dead' thing, especially since I still have unpaid bills."

# ANSI color codes
colors = [
    '\033[91m',  # red
    '\033[92m',  # green
    '\033[93m',  # yellow
    '\033[94m',  # blue
    '\033[95m',  # magenta
    '\033[96m',  # cyan
]
reset = '\033[0m'

def typewriter(text, delay=0.04):
    for char in text:
        color = random.choice(colors)
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    
    # Print a decorative border
    print('*' * 60)
    print('*' + ' ' * 58 + '*')
    
    # Print quote with typewriter effect
    typewriter(quote, delay=0.03)
    
    print('*' + ' ' * 58 + '*')
    print('*' * 60)

if __name__ == '__main__':
    main()