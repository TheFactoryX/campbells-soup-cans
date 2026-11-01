"""
Campbell's Soup Can #5194
Produced: 2026-11-01 01:10:43
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.05, color=''):
    for c in text:
        sys.stdout.write(color + c)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    clear()
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    
    quote = "Life is a series of awkward silences, and I'm the only one who notices."
    
    padding = 2
    inner_width = len(quote) + 2 * padding
    top = '+' + '-' * inner_width + '+'
    bottom = '+' + '-' * inner_width + '+'
    
    print(YELLOW + top + RESET)
    print(YELLOW + '|' + RESET + ' ' * inner_width + YELLOW + '|' + RESET)
    
    sys.stdout.write(YELLOW + '|' + RESET)
    sys.stdout.write(' ' * padding)
    type_text(quote, color=CYAN)
    sys.stdout.write(' ' * padding)
    sys.stdout.write(YELLOW + '|' + RESET)
    print()
    
    print(YELLOW + '|' + RESET + ' ' * inner_width + YELLOW + '|' + RESET)
    print(YELLOW + bottom + RESET)

if __name__ == '__main__':
    main()