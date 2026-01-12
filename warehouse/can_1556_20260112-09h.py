"""
Campbell's Soup Can #1556
Produced: 2026-01-12 09:47:28
Worker: Mistral: Mistral Medium 3 (mistralai/mistral-medium-3)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def print_color(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
    reset = '\033[0m'
    print(f"{colors[color]}{text}{reset}")

def print_woody_quote():
    quote = "I don't want to achieve immortality through my work; I want to achieve it by living forever and having people say, 'Hey, he never dies! What's his secret?' And then I'll say, 'It's the hummus.'"
    words = quote.split()
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

    # Print a fancy box top
    print_color("+" + "-" * 70 + "+", 'white')
    print_color("|" + " " * 70 + "|", 'white')

    # Print the quote with random colors and delays
    line = ""
    for word in words:
        color = random.choice(colors)
        line += f" {word}"
        if len(line) > 60:
            print_color("|" + line.ljust(70) + "|", color)
            line = ""
            time.sleep(0.1)
    if line:
        print_color("|" + line.ljust(70) + "|", color)

    # Print the box bottom
    print_color("|" + " " * 70 + "|", 'white')
    print_color("+" + "-" * 70 + "+", 'white')

    # Print a little Woody Allen ASCII art
    woody_art = r"""
          .-""""""-.
         /          \
        |            |
        |   O    O   |
        |     ∆      |
         \  \__/  /
          '------'
    """
    print_color(woody_art, 'yellow')

if __name__ == "__main__":
    print_woody_quote()