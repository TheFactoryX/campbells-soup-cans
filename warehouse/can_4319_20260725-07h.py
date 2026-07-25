"""
Campbell's Soup Can #4319
Produced: 2026-07-25 07:28:05
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'yellow': '\033[93m',
        'cyan': '\033[96m',
        'magenta': '\033[95m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

def create_box(text, width=70):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    box_width = max_length + 4
    top = '+' + '-' * (box_width - 2) + '+'
    bottom = top
    middle = []
    for line in lines:
        padded = line.center(box_width - 4)
        middle.append(f"| {padded} |")
    return [top] + middle + [bottom]

def main():
    title = print_colored("Philosophical Wisdom from Woody Allen (Probably)", 'magenta')
    print(title)
    time.sleep(0.3)
    
    quote = """I'm not afraid of death; I just don't want to be there when it happens.
But I'm also terrified of not achieving my full potential, which is why I never leave the house."""
    
    box_lines = create_box(quote, width=70)
    
    for line in box_lines:
        if line.startswith('+'):
            print(print_colored(line, 'red'))
        else:
            print(print_colored(line, 'yellow'))
        time.sleep(0.1)
    
    time.sleep(0.5)
    
    print("\n" + print_colored("   *", 'white'))
    print(print_colored("  ***", 'white'))
    print(print_colored(" *****", 'white'))
    print(print_colored("*******", 'white'))
    print(print_colored(" *****", 'white'))
    print(print_colored("  ***", 'white'))
    print(print_colored("   *\n", 'white'))
    
    print(print_colored("And remember: If you're going through hell, keep going!", 'cyan'))

if __name__ == "__main__":
    main()