"""
Campbell's Soup Can #2781
Produced: 2026-03-15 11:40:06
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, itertools, textwrap

QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."
WRAP_WIDTH = 48  # inner width of the box

def type_print(s, delay=0.03):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    color_cycle = itertools.cycle([31, 32, 33, 34, 35, 36])  # red..cyan
    wrapped = textwrap.fill(QUOTE, width=WRAP_WIDTH)
    lines = wrapped.split('\n')
    inner_width = WRAP_WIDTH    # top border
    sys.stdout.write('\033[36m')  # cyan
    sys.stdout.write('┌' + '─'*inner_width + '┐\n')
    sys.stdout.write('\033[0m')
    sys.stdout.flush()

    for line in lines:
        padded = line.ljust(inner_width)
        sys.stdout.write('\033[36m│ ')  # cyan left border
        sys.stdout.write('\033[0m')
        col = next(color_cycle)
        sys.stdout.write(f'\033[{col}m')
        type_print(padded, delay=0.04)
        sys.stdout.write('\033[0m')
        sys.stdout.write('\033[36m │\n\033[0m')
        sys.stdout.flush()

    # bottom border
    sys.stdout.write('\033[36m')  # cyan
    sys.stdout.write('└' + '─'*inner_width + '┘\n')
    sys.stdout.write('\033[0m')
    sys.stdout.flush()

if __name__ == '__main__':
    main()