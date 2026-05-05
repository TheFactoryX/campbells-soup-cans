"""
Campbell's Soup Can #3575
Produced: 2026-05-05 18:46:58
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import itertools

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m'
}

def animated_print(text, color='cyan', delay=0.05):
    """Prints text with a typing animation and color."""
    for char in text:
        sys.stdout.write(COLORS[color] + char + COLORS['reset'])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_quote():
    # ASCII art header
    print(f"{COLORS['blue']}~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print(f"   W O O D Y   A L L E N   P H I L O S O P H Y  ")
    print(f"~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~{COLORS['reset']}\n")

    # The quote with color effects
    quote = [
        (f"{COLORS['red']}I used to think{COLORS['reset']} I was indecisive,", 'red'),
        (f"but now I'm not sure.", 'yellow'),
        (f"And that{COLORS['magenta']} uncertainty{COLORS['reset']} terrifies me", 'red'),
        (f"more than death itself.", 'blue'),
        (f"At least death is certain...{COLORS['green']} right?{COLORS['reset']}", 'cyan')
    ]

    for line, color in quote:
        animated_print(line, color)
        time.sleep(0.3)

    # Animated border
    print(f"\n{COLORS['blue']}", end='')
    for c in itertools.cycle(['~', '*', '-']):
        print(c, end='', flush=True)
        time.sleep(0.1)
        if _ % 40 == 0:  # Reset after 40 characters
            _ = 0
            print()
            break
        _ = getattr(print_quote, '_count', 0) + 1
        setattr(print_quote, '_count', _)
    print(COLORS['reset'])

if __name__ == "__main__":
    print_quote()