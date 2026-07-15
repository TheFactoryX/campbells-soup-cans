"""
Campbell's Soup Can #4211
Produced: 2026-07-15 22:15:28
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriter(text, delay=0.03, color_code='\033[36m'):
    sys.stdout.write(color_code)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    quote = "I have a profound fear of success, which is why I avoid it entirely, but then I get disappointed when I don't succeed, which is exactly what I expected."
    width = len(quote) + 2

    top = '+' + '-' * (width - 2) + '+'
    middle = '|' + quote + '|'
    bottom = top

    # Print top border in red with typewriter effect
    typewriter(top, color_code='\033[31m')

    # Print middle line in cyan with typewriter effect
    typewriter(middle, color_code='\033[36m')

    # Print bottom border in red with typewriter effect
    typewriter(bottom, color_code='\033[31m')

    # Reset color
    sys.stdout.write('\033[0m')

if __name__ == "__main__":
    main()