"""
Campbell's Soup Can #4503
Produced: 2026-08-09 16:54:20
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

RESET = '\033[0m'
COLORS = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[95m']  # red, yellow, green, cyan, magenta

def color_cycle():
    return itertools.cycle(COLORS)

def typewriter_print(text, delay=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def spinner(duration=1.5, delay=0.1):
    spinner_chars = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write('\r' + next(spinner_chars))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\r ')
    sys.stdout.flush()

def main():
    quote = "I spend so much time worrying about the future that I forget to enjoy the present, which is why I'm always late to my own existential crisis."
    width = len(quote) + 4  # padding for borders

    # Top border with color cycling
    top_border = []
    cc = color_cycle()
    for _ in range(width):
        top_border.append(next(cc) + '*' + RESET)
    sys.stdout.write(''.join(top_border) + '\n')
    sys.stdout.flush()

    # Left border, quote with typewriter, right border
    sys.stdout.write(next(color_cycle()) + '| ' + RESET)
    sys.stdout.flush()
    typewriter_print(quote, 0.04)
    sys.stdout.write(next(color_cycle()) + ' |' + RESET + '\n')
    sys.stdout.flush()

    # Bottom border with color cycling (reverse)
    bottom_border = []
    cc = color_cycle()
    for _ in range(width):
        bottom_border.append(next(cc) + '*' + RESET)
    sys.stdout.write(''.join(bottom_border) + '\n')
    sys.stdout.flush()

    # A little spinner to show "thinking"
    spinner(1.2, 0.08)

if __name__ == "__main__":
    main()