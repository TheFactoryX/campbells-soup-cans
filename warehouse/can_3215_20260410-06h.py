"""
Campbell's Soup Can #3215
Produced: 2026-04-10 06:08:12
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
import itertools

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
}

def c(text, *styles):
    """Apply ANSI styles to text."""
    return ''.join(styles) + text + COLORS['reset']

def type_writer(text, delay=0.03):
    """Print text character by character."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_box(lines, width):
    """Draw a colorful box that pulses."""
    pulse = itertools.cycle([COLORS['red'], COLORS['yellow'], COLORS['green'],
                             COLORS['cyan'], COLORS['blue'], COLORS['magenta']])
    for _ in range(3):  # three pulses
        border = next(pulse) + ('═' * (width - 2)) + COLORS['reset']
        print(border)
        for line in lines:
            print(next(pulse) + '║ ' + line.ljust(width - 4) + ' ║' + COLORS['reset'])
        print(border)
        time.sleep(0.2)
        sys.stdout.write('\033[F' * (len(lines) + 2))  # move cursor up
        sys.stdout.flush()

def main():
    quote = (
        "I'm not afraid of dying; I just don't want to be there when it happens. "
        "Besides, the afterlife sounds like a really long waiting room with bad magazines."
    )
    # Prepare wrapped quote lines (max 50 chars)
    max_width = 58
    words = quote.split()
    lines = []
    current = []
    current_len = 0
    for w in words:
        if current_len + len(w) + (1 if current else 0) > max_width - 4:
            lines.append(' '.join(current))
            current = [w]
            current_len = len(w)
        else:
            current.append(w)
            current_len += len(w) + (1 if current else 1)
    if current:
        lines.append(' '.join(current))

    # Center each line inside the box
    centered = [line.center(max_width - 4) for line in lines]

    # Animate
    animate_box(centered, max_width)

    # Final static display with a different color scheme
    print()
    print(c("“", COLORS['bold'], COLORS['cyan']) + c(quote, COLORS['bold'], COLORS['white']) + c("”", COLORS['bold'], COLORS['cyan']))
    print()
    print(c("- Woody Allen (probably)", COLORS['dim'], COLORS['magenta']))

if __name__ == "__main__":
    main()