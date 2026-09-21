"""
Campbell's Soup Can #4999
Produced: 2026-09-21 01:06:38
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
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

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'reset': '\033[0m'
}

def typewriter(text, color=COLORS['white'], delay_range=(0.03, 0.08)):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(color + ch + COLORS['reset'])
        sys.stdout.flush()
        time.sleep(random.uniform(*delay_range))
    print()

def main():
    quote = "I’m not afraid of dying; I just don’t want to be there when it happens."
    # Choose a random color for each word for extra fun
    words = quote.split()
    colored_words = []
    for w in words:
        c = random.choice([COLORS['red'], COLORS['green'], COLORS['yellow'],
                           COLORS['blue'], COLORS['magenta'], COLORS['cyan']])
        colored_words.append(c + w + COLORS['reset'])
    colored_quote = ' '.join(colored_words)

    # Box dimensions
    padding = 2
    width = len(colored_quote) + 2 * padding
    top_bottom = COLORS['bold'] + '╔' + '═' * width + '╗' + COLORS['reset']
    sides = COLORS['bold'] + '║' + COLORS['reset']

    # Print top border
    print(top_bottom)
    # Print quote line with padding
    line = sides + ' ' * padding + colored_quote + ' ' * padding + sides
    # Use typewriter effect for the quote itself
    sys.stdout.write(sides + ' ' * padding)
    sys.stdout.flush()
    typewriter('', delay_range=(0,0))  # just to move to correct line
    # Re-print the line with typewriter effect on the quote part only
    sys.stdout.write(sides + ' ' * padding)
    sys.stdout.flush()
    typewriter(colored_quote, delay_range=(0.03,0.07))
    sys.stdout.write(' ' * padding + sides + COLORS['reset'] + '\n')
    # Print bottom border
    print(top_bottom)

if __name__ == "__main__":
    main()