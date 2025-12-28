"""
Campbell's Soup Can #1237
Produced: 2025-12-28 14:34:17
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

def print_woody_allen_quote():
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

    def animate_text(text, color, delay=0.1):
        for char in text:
            sys.stdout.write(f"{colors[color]}{char}{colors['reset']}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def draw_box(text, color):
        lines = text.split('\n')
        width = max(len(line) for line in lines)
        animate_text('┌' + '─' * (width + 2) + '┐\n', color)
        for line in lines:
            animate_text(f'│ {line.center(width)} │\n', color)
        animate_text('└' + '─' * (width + 2) + '┘', color)

    animate_text(quote, 'cyan', 0.05)
    animate_text(author, 'magenta', 0.05)
    print()
    draw_box("Life is divided into the horrible and the miserable.", 'yellow')

print_woody_allen_quote()