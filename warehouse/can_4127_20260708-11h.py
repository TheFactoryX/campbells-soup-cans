"""
Campbell's Soup Can #4127
Produced: 2026-07-08 11:57:11
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

RESET = '\033[0m'
COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

def colored(text, color):
    return COLORS.get(color, '') + text + RESET

def print_with_delay(text, color='white', delay=0.05):
    for ch in text:
        sys.stdout.write(colored(ch, color))
        sys.stdout.flush()
        time.sleep(delta if (delta := delay) else 0)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    quote_lines = [
        "I'm not afraid of dying;",
        "I just don't want to be there",
        "when it happens, especially",
        "if it's during my nap."
    ]

    max_len = max(len(line) for line in quote_lines)
    inner_width = max_len + 4  # two spaces padding each side

    top = '╔' + '═' * inner_width + '╝'
    bottom = '╚' + '═' * inner_width + '╝'
    middle = []
    for line in quote_lines:
        middle.append('║ ' + line.ljust(inner_width - 2) + ' ║')

    # Animate the box
    print_with_delay(top, color='cyan', delay=0.02)
    time.sleep(0.1)
    for line in middle:
        print_with_delay(line, color='yellow', delay=0.02)
        time.sleep(0.05)
    print_with_delay(bottom, color='cyan', delay=0.02)

    # Footer
    footer = " — Woody Allen (probably)"
    print_with_delay(footer, color='magenta', delay=0.03)

if __name__ == "__main__":
    main()