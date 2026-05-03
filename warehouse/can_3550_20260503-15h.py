"""
Campbell's Soup Can #3550
Produced: 2026-05-03 15:05:56
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

# ANSI color codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
MAGENTA = "\033[35m"   # border
CYAN    = "\033[96m"   # quote (bright cyan)

def spinner_animation(duration=2.0):
    """Show a simple spinner for the given duration."""
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    end = time.time() + duration
    while time.time() < end:
        sys.stdout.write(f'\r{BOLD}{next(spinner)}{RESET} Thinking...')
        sys.stdout.flush()
        time.sleep(0.1)
    # clear the line
    sys.stdout.write('\r' + ' ' * 30 + '\r')
    sys.stdout.flush()

def print_boxed_quote():
    quote = (
        '"The universe is indifferent, but at least my therapist '\n"
        ' charges by the hour — so I can pretend someone cares."'
    )
    lines = quote.split('\n')
    width = max(len(line) for line in lines) + 4  # padding

    top_bottom = f'{MAGENTA}╔{"═" * width}╗{RESET}'
    middle = []
    for line in lines:
        padded = line.ljust(width - 2)
        middle.append(f'{MAGENTA}║{RESET} {CYAN}{BOLD}{padded}{RESET} {MAGENTA}║{RESET}')
    bottom = f'{MAGENTA}╚{"═" * width}╝{RESET}'

    print(top_bottom)
    for line in middle:
        print(line)
    print(bottom)

def main():
    spinner_animation()
    print_boxed_quote()

if __name__ == "__main__":
    main()