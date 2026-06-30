"""
Campbell's Soup Can #4053
Produced: 2026-06-30 10:37:22
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
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
COLORS = [
    '\033[95m',  # Magenta
    '\033[94m',  # Blue
    '\033[96m',  # Cyan
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[91m',  # Red
]
RESET = '\033[0m'

def print_colored(text, color):
    """Print text in specified color"""
    sys.stdout.write(color + text + RESET)
    sys.stdout.flush()

def typewriter_effect(text, delay=0.05):
    """Print text with typewriter effect and alternating random colors"""
    for char in text:
        color = random.choice(COLORS)
        print_colored(char, color)
        time.sleep(delay)
    print()  # Newline after effect

def print_woody_quote():
    # Draw a philosophical box
    box_width = 60
    quote = "I asked my therapist to cure my existential dread. He said 'That'll be $200.' I said 'That's absurd!' He said 'Exactly.'"
    
    # Top border
    print(COLORS[2], end='')
    print('┌' + '─' * (box_width - 2) + '┐')
    
    # Empty line
    print('│' + ' ' * (box_width - 2) + '│')
    
    # Quote line with typewriter effect and colors
    print('│', end='')
    sys.stdout.write(RESET)
    
    # Split quote into words for colored effect
    words = quote.split(' ')
    for word in words:
        color = random.choice(COLORS)
        print_colored(word, color)
        sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(0.2)
    print(' ' * (box_width - 2 - len(quote) - len(words)), end='')
    print('│')
    
    # Empty line
    print('│' + ' ' * (box_width - 2) + '│')
    
    # Bottom border
    print('└' + '─' * (box_width - 2) + '┘', RESET)

if __name__ == "__main__":
    # Fancy header
    print(COLORS[4], end='')
    print('  _    _                                                ')
    print(' | |  | |                                               ')
    print(' | |  | | ___  ___  _ __ __ _ _ __   __ _ ___ _ __      ')
    print(" | |/\\ | |/ _ \\/ __|| '__/ _` | '_ \\ / _` / __| '__|     ")
    print(' \\  /\\  /  __/\\__ \\| | | (_| | | | | (_| \\__ \\ |       ')
    print('  \\/  \\/ \\___||___/| |_|\\__,_|_| |_|\\__, |___/_|       ')
    print('                  _\\___|           |___/             ')
    print(RESET)
    
    # Animate quote display
    quote_line = "=THUNK= A Philosophical Rumination ="
    for char in quote_line:
        print(COLORS[5], end='')
        print(char, end='', flush=True)
        time.sleep(0.1)
    print(RESET)
    
    print()
    print_woody_quote()
    
    # Footer
    print(COLORS[3], end='')
    print('\n — Anonymous Neurotic Philosopher, probably while eating a bagel')
    print(RESET)