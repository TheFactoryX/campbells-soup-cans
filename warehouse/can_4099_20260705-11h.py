"""
Campbell's Soup Can #4099
Produced: 2026-07-05 11:13:25
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

red = '\033[91m'
cyan = '\033[96m'
yellow = '\033[93m'
magenta = '\033[95m'
reset = '\033[0m'

def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_box(quote):
    max_length = len(quote) + 4
    border = '+' + '-' * max_length + '+'
    print(red + border + reset)
    print(red + '|' + ' ' * max_length + '|' + reset)
    print(red + '|  ' + cyan, end='')
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print(red + '  |' + reset)
    print(red + '|' + ' ' * max_length + '|' + reset)
    print(red + border + reset)

def print_frown():
    print(magenta + "   .-''-.   " + reset)
    print(magenta + "  /      \\  " + reset)
    print(magenta + "  |      |  " + reset)
    print(magenta + "  |  .-. |  " + reset)
    print(magenta + "  \\      /  " + reset)
    print(magenta + "   '-..-'   " + reset)
    print()

print(cyan + "\n" + yellow + "Existential crisis detected..." + reset + cyan + "..." + reset)
print()
print_frown()

quote = "I'm terrified of dying, but I'm even more terrified of living through all my terrible decisions."
print_box(quote)

print(yellow + "\nAnd that's why I never leave the house." + reset)
print(cyan + "\nPress Ctrl+C to escape reality." + reset)