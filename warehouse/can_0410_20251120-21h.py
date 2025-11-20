"""
Campbell's Soup Can #410
Produced: 2025-11-20 21:29:09
Worker: Venice: Uncensored (free) (cognitivecomputations/dolphin-mistral-24b-venice-edition:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def colorful_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'endc': '\033[0m',
    }
    return f"{colors.get(color, '')}{text}{colors['endc']}"

def print_quote():
    quote = (
        "I don't want to live in a world where everything is nicely wrapped up,\n"
        "but it turns out the wrapping paper keeps falling off and you're left with\n"
        "a box of existential dread."
    )

    lines = quote.split('\n')
    box_lines = [' ' + ('-' * 60) + ' '] * 3
    box_lines[1] = '|' + (' ' * 58) + '|'

    colored_lines = [colorful_text(line, 'yellow') for line in box_lines]

    for i, line in enumerate(colored_lines):
        print(line)
        if i == 1:
            for j, text_line in enumerate(lines):
                print(f"| {text_line:^58} |")
                time.sleep(0.25)

    box_lines[0] = '+' + ('-' * 60) + '+'
    box_lines[2] = '+' + ('-' * 60) + '+'
    for line in box_lines:
        print(colorful_text(line, 'yellow'))

if __name__ == "__main__":
    print_quote()