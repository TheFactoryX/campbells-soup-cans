"""
Campbell's Soup Can #4091
Produced: 2026-07-04 17:19:22
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

def main():
    # ANSI color codes
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    def color(text, code):
        return f"{code}{text}{RESET}"

    # Original Woody Allen‑style quote
    quote_lines = [
        '"I don\'t want to achieve immortality through my work;"',
        '"I want to achieve it through not dying."',
        ' — Woody Allen (imagined)'
    ]

    # Simple spinner while "loading"
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    sys.stdout.write(color('Loading', CYAN))
    for _ in range(20):
        sys.stdout.write(f'\r{color("Loading", CYAN)} {next(spinner)}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 30 + '\r')  # clear line
    sys.stdout.flush()

    # Box dimensions
    width = 60
    top_bottom = color('╔' + '═' * (width - 2) + '╚', CYAN)
    middle = color('║' + ' ' * (width - 2) + '║', CYAN)

    # Draw top border
    print(top_bottom)
    print(middle)

    # Typewriter effect for each quote line
    for line in quote_lines:
        line_content = f'║ {line:<{width-4}} ║'
        if line.startswith('"'):
            colored = color(line_content, YELLOW)
        else:
            colored = color(line_content, MAGENTA)

        for ch in colored:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(0.2)

    # Draw bottom border
    print(middle)
    print(top_bottom)

if __name__ == "__main__":
    main()