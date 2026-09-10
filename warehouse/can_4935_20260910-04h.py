"""
Campbell's Soup Can #4935
Produced: 2026-09-10 04:52:16
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def main():
    # Woody Allen-style quote
    quote = "I'm terrified of dying, but I'm even more terrified of not being terrified—because that would mean I've stopped caring about the meaning of life."

    # Colors for visual effects (ANSI codes)
    colors = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96, 97, 1;31, 1;32, 1;33, 1;34, 1;35, 1;36]

    # Print a flickering header with colors
    print('\n' * 3 + end='')  # Some space at top
    for _ in range(3):
        print('\033[2J', end='')  # Clear screen
        print(
            f"\033[{random.randint(31,36)}m" + 
            " ".join(sorted(['Existential', 'Anxiety', 'Dread', 'Philosophy', 'Woody'], key=lambda x: random.random())) +
            f"\033[0m"
        )
        time.sleep(0.3)
    print('\n')

    # Create quote box dimensions
    max_line_length = len(quote)
    box_width = max_line_length + 4
    
    # Print top border with animation
    print('\033[38;5;208m┌' + '─' * box_width + '┐\033[0m', end='')
    for i in range(5):
        print(f"\033[38;5;{208+i*15}m┘\033[0m", end='')
        time.sleep(0.1)
    print()

    # Animation effect for content lines
    lines = [
        " " * (box_width // 2) + quote[:max_line_length//2],
        " " * (box_width//2) + quote[max_line_length//2:]
    ]

    # Print content with color shifts
    for y, line in enumerate(lines):
        # Print left border
        print('\033[38;5;34m│\033[0m', end='')
        # Print each character with random bright colors
        for c in line:
            print(f"\033[38;5;{random.randint(196,255)}m{c}\033[0m", end='')
            if random.random() < 0.05: time.sleep(0.01)  # Some characters stay longer
        # Print right border
        print('\033[38;5;34m│\033[0m\n')

    # Print bottom border with reverse animation
    print('\033[0m' + end='')
    for i in reversed(range(5)):
        print(f"\033[38;5;{208+i*15}m└{\('─'*box_width)}┘\033[0m", end='')
        time.sleep(0.1)
    print()

    # Add some finishing touches
    print('\033[38;5;196m' + '∴'*50 + '∴\033[0m')
    print(f"\033[38;5;105m{' ' * 15} -- Because Existentialism is a Bit Much Anyway -- {' ' * 15}\033[0m")

if __name__ == "__main__":
    main()