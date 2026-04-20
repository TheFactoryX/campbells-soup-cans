"""
Campbell's Soup Can #3372
Produced: 2026-04-20 09:18:24
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['reset']}")

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame():
    frame = r"""
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
"""
    print_colored(frame, 'cyan')

def main():
    quote = (
        "I don't want to achieve immortality through my work;\n"
        "I want to achieve it through not dying.\n"
        "Life is full of misery, loneliness, and suffering - \n"
        "and it's all over much too soon."
    )

    draw_frame()
    time.sleep(1)

    lines = quote.split('\n')
    y_positions = [8, 10, 12, 14]

    for line, y in zip(lines, y_positions):
        for x in range(5, 76):
            sys.stdout.write("\033[{};{}H".format(y, x))
            sys.stdout.write(line[:x-5])
            sys.stdout.flush()
            time.sleep(0.01)
            sys.stdout.write("\033[{};{}H".format(y, x))
            sys.stdout.write(" " * (len(line) - (x-5)))
            sys.stdout.flush()

    print_colored("\n\nPress Enter to exit...", 'yellow')
    input()

if __name__ == "__main__":
    main()