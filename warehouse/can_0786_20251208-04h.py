"""
Campbell's Soup Can #786
Produced: 2025-12-08 04:03:20
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_woody_quote():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    author = "- Woody Allen"

    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'reset': '\033[0m'
    }

    def animate_text(text, color):
        for char in text:
            sys.stdout.write(color + char + colors['reset'])
            sys.stdout.flush()
            time.sleep(0.05)

    def print_colored_box(text, color):
        lines = text.split('\n')
        longest_line = max(len(line) for line in lines)

        sys.stdout.write(color)
        print('+{}+'.format('-' * (longest_line + 2)))
        for line in lines:
            print('| {} |'.format(line.ljust(longest_line)))
        print('+{}+'.format('-' * (longest_line + 2)))
        sys.stdout.write(colors['reset'])

    print_colored_box('Funny Philosophical Quote', colors['yellow'])
    animate_text(quote + '\n', colors['magenta'])
    animate_text(author + '\n', colors['cyan'])

print_woody_quote()