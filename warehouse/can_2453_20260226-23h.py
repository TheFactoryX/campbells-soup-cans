"""
Campbell's Soup Can #2453
Produced: 2026-02-26 23:45:55
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

ESC = '\x1b'
RESET = ESC + '[0m'
COLORS = [31, 32, 33, 34, 35, 36]

def rainbow(s):
    for i, ch in enumerate(s):
        sys.stdout.write(f'{ESC}[{COLORS[i % len(COLORS)]}m{ch}{RESET}')
    sys.stdout.write('\n')

quote = "I’m not afraid of death; I just don’t want to be there when it happens—especially when my cat thinks I’m a pretentious philosopher."
border = "╔" + "═" * (len(quote) + 2) + "╗"
middle = f"║ {quote} ║"

for _ in range(3):
    sys.stdout.write(ESC + '[92m' + border + RESET + '\n')
    sys.stdout.write(ESC + '[94m' + middle + RESET + '\n')
    sys.stdout.write('\x1b[2J\x1b[H')
    time.sleep(0.5)

sys.stdout.write(ESC + '[95m' + border + RESET + '\n')
sys.stdout.write(ESC + '[96m' + middle + RESET + '\n')
sys.stdout.write(ESC + '[95m' + border + RESET + '\n')