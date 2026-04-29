"""
Campbell's Soup Can #3495
Produced: 2026-04-29 09:24:43
Worker: OpenAI: GPT-3.5 Turbo Instruct (openai/gpt-3.5-turbo-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote(quote):
    """Print the quote with colors and formatting"""
    print('\x1b[1;32m' + quote + '\x1b[0m')

def animate_quote(quote):
    """Animate the quote with ASCII art and formatting"""
    print('\x1b[1;35m   _______')
    print('\x1b[1;34m  /       \\')
    for i in range(5):
        print('\x1b[1;33m  |  _____ |')
        print('\x1b[1;32m  | | ' + quote[(3 + 2 * i) % len(quote)] + ' | |')
        print('\x1b[1;31m  | |_____| |')
        time.sleep(0.2)
    print('\x1b[1;34m  |         |')
    print('\x1b[1;35m  |_________|' + '\x1b[0m')

quote = "I'm allergic to French optimism."
print_quote(quote)
animate_quote(quote)