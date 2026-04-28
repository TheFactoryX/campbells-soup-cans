"""
Campbell's Soup Can #3486
Produced: 2026-04-28 12:02:14
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, random

QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

def col(c):
    return f'\033[{c}m'

def reset():
    return '\033[0m'

def printc(s, color=None):
    if color:
        s = color + s + reset()
    sys.stdout.write(s + '\n')
    sys.stdout.flush()

def animate_print(s, delay=0.02):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    w = len(QUOTE) + 2
    top = '╔' + '═'*w + '╗'
    for ch in top:
        sys.stdout.write(col(random.choice([31,32,33,34,35,36])) + ch + reset())
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write('\n')

    middle = f'║ {QUOTE} ║'
    printc(middle, col(33))

    bottom = '╚' + '═'*w + '╝'
    for ch in bottom:
        sys.stdout.write(col(random.choice([31,32,33,34,35,36])) + ch + reset())
        sys.stdout.flush()
        time.sleep(0.01)
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()