"""
Campbell's Soup Can #1238
Produced: 2025-12-28 15:32:09
Worker: Meta: Llama 3.1 405B Instruct (free) (meta-llama/llama-3.1-405b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

# ASCII art frame
FRAME_TOP = '+-------------------------------+'
FRAME_BOTTOM = '+-------------------------------+'

def print_quote(quote):
    print(FRAME_TOP)
    for line in quote.split('\n'):
        print(f'| {line.center(27)} |')
    print(FRAME_BOTTOM)

def woody_allen_quote():
    quote = f'{YELLOW}I\'m not afraid of death;{END_COLOR}\n'
    quote += f'{RED}I just don\'t want to be there{END_COLOR}\n'
    quote += f'{BLUE}when it happens.{END_COLOR}'
    return quote

def animate_typing(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print('\n' * 10)  # clear some space
    animate_typing(f'{GREEN}Woody Allen once said...{END_COLOR}\n', delay=0.05)
    print_quote(woody_allen_quote())
    animate_typing(f'{RED}... and I\'m still worried.{END_COLOR}\n', delay=0.05)

if __name__ == '__main__':
    main()