"""
Campbell's Soup Can #3615
Produced: 2026-05-09 08:52:18
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

def main():
    # Hide cursor and clear screen
    sys.stdout.write("\033[?25l\033[2J\033[H")
    sys.stdout.flush()

    quote = "I'm not terrified of eternity; I just don't want to have to fill out the paperwork."
    padding = 2
    max_len = len(quote)
    width = max_len + 2 * padding

    # Foreground colors: red, green, yellow, blue, magenta, cyan
    colors = itertools.cycle([31, 32, 33, 34, 35, 36])

    def color_char(ch):
        if ch == "\n":
            return ch
        code = next(colors)
        return f"\033[{code}m{ch}\033[0m"

    colored_quote = "".join(color_char(c) for c in quote)

    # Top border
    top_border = f"\033[36m┌{'─' * width}┐\033[0m"
    sys.stdout.write(top_border + "\n")
    time.sleep(0.05)

    # Inner empty line
    empty_line = f"\033[36m│{' ' * width}│\033[0m"
    sys.stdout.write(empty_line + "\n")
    time.sleep(0.05)

    # Quote line with padding
    line_inner = f"{' ' * padding}{colored_quote}{' ' * padding}"
    quote_line = f"\033[36m│{line_inner}│\033[0m"
    sys.stdout.write(quote_line + "\n")
    time.sleep(0.05)

    # Inner empty line
    sys.stdout.write(empty_line + "\n")
    time.sleep(0.05)

    # Bottom border
    bottom_border = f"\033[36m└{'─' * width}┘\033[0m"
    sys.stdout.write(bottom_border + "\n")
    sys.stdout.flush()

    # Show cursor again
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass