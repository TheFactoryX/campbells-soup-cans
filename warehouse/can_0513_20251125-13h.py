"""
Campbell's Soup Can #513
Produced: 2025-11-25 13:45:59
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time

def color_print(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
    }
    end_color = '\033[0m'
    print(colors[color] + text + end_color)

def print_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "- Woody Allen"

    color_print('', 'blue')
    color_print(' ' * 10 + quote + ' ' * 10, 'yellow')
    color_print(' ' * 50, 'blue')
    color_print(' ' * 50, 'blue')
    color_print(' ' * 15 + author + ' ' * 15, 'yellow')
    color_print(' ' * 50, 'blue')
    color_print('', 'blue')

def animate_text(text):
    for i in range(len(text)):
        print(text[:i], end='\r')
        time.sleep(0.1)
    print(text)

def main():
    animate_text("Woody Allen once said...")
    time.sleep(1)
    print_quote()

if __name__ == "__main__":
    main()