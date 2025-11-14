"""
Campbell's Soup Can #262
Produced: 2025-11-14 03:30:25
Worker: Meta: Llama 4 Maverick (free) (meta-llama/llama-4-maverick:free)
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

def print_quote(quote):
    # Create a box around the quote
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    print(f'{BLUE}{"+" + "-" * (max_len + 2) + "+"}{END_COLOR}')
    for line in lines:
        print(f'{BLUE}|{END_COLOR} {YELLOW}{line.ljust(max_len)}{END_COLOR} {BLUE}|{END_COLOR}')
    print(f'{BLUE}{"+" + "-" * (max_len + 2) + "+"}{END_COLOR}')

def animate_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def main():
    quote = f'{GREEN}I told my wife she was drawing her eyebrows too high.\nShe looked surprised.{END_COLOR}'
    print('\n' * 10)
    print(' ' * 20 + f'{RED}Wisdom of the Ages:{END_COLOR}')
    time.sleep(1)
    print_quote(quote)
    time.sleep(2)
    print('\n' * 5)
    animate_text(f'{YELLOW}-- Anonymous (but definitely not me){END_COLOR}')

if __name__ == "__main__":
    main()