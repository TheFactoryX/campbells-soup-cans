"""
Campbell's Soup Can #945
Produced: 2025-12-15 08:48:31
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

def woody_allen_quote():
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
            sys.stdout.write(f'{colors[color]}{char}{colors["reset"]}')
            sys.stdout.flush()
            time.sleep(0.05)
        print()

    def box_text(text):
        lines = text.split('\n')
        max_width = max(len(line) for line in lines)
        box = f'+{"-" * (max_width + 2)}+\n'
        for line in lines:
            box += f'| {line:^{max_width}} |\n'
        box += f'+{"-" * (max_width + 2)}+'
        return box

    animate_text(box_text(quote), 'cyan')
    animate_text(box_text(author), 'magenta')

if __name__ == '__main__':
    woody_allen_quote()