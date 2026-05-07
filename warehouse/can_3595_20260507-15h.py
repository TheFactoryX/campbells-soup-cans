"""
Campbell's Soup Can #3595
Produced: 2026-05-07 15:36:20
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Wisdom Generator
A neurotic philosopher's guide to existential dread (with style!)
"""

import time
import sys

# ANSI color codes
RESET = '\033[0m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def typewriter_print(text, delay=0.03, color=RESET):
    """Print text with a typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def main():
    # Print header
    print()
    print(CYAN + "╔" + "═" * 50 + "╗" + RESET)
    print(CYAN + "║" + WHITE + "   WOODY ALLEN WISDOM GENERATOR  ".center(50) + CYAN + "║" + RESET)
    print(CYAN + "╚" + "═" * 50 + "╝" + RESET)
    print()
    
    # The quote
    quote = "I used to think I wanted immortality through my work... then I realized I'm not particularly good at any work that would be worth being immortal for. Plus, death seems so much more convenient - no reviews, no pressure, just... done. It's the only career move I can make that guarantees 100% job security."
    
    # Decorative border
    print(MAGENTA + "★" * 50 + RESET)
    print()
    
    # Print quote with typewriter effect
    typewriter_print(quote, delay=0.02, color=YELLOW)
    
    print()
    print(MAGENTA + "★" * 50 + RESET)
    print()
    
    # Attribution with styling
    print(BOLD + BLUE + "                           - A Neurotic Philosopher" + RESET)
    print()
    
    # Footer
    print(CYAN + "╔" + "═" * 50 + "╗" + RESET)
    print(CYAN + "║" + WHITE + "   Wisdom is knowing you're doomed... ".center(50) + CYAN + "║" + RESET)
    print(CYAN + "╚" + "═" * 50 + "╝" + RESET)
    print()

if __name__ == "__main__":
    main()