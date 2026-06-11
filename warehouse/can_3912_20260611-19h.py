"""
Campbell's Soup Can #3912
Produced: 2026-06-11 19:45:10
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

def color(text, fg=''):
    colors = {
        'reset': '\033[0m',
        'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m',
        'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m', 'white': '\033[37m',
        'bright_red': '\033[91m', 'bright_green': '\033[92m', 'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m', 'bright_magenta': '\033[95m', 'bright_cyan': '\033[96m', 'bright_white': '\033[97m',
    }
    return colors.get(fg, colors['reset']) + text + colors['reset']

quote = "Life is like an eggplant: it looks boring, but inside there's a lot of potential... and maybe a hidden nut allergy."

border = color('+', 'bright_green')
hline  = color('-', 'bright_green')
vline  = color('|', 'bright_green')
fill   = ' ' * 38centered = quote.center(38)
centered_color = color(centered, 'bright_cyan')

top    = color('+', 'bright_green') + hline*38 + color('+', 'bright_green')
mid_buf  = vline + fill + vline
mid_line = vline + centered_color + vline
bottom = color('+', 'bright_green') + hline*38 + color('+', 'bright_green')

for _ in range(2):
    sys.stdout.write('\r')
    print(top)
    time.sleep(0.12)
    sys.stdout.write('\r')
    print(mid_buf)
    sys.stdout.write('\r')
    print(mid_line)
    sys.stdout.write('\r')
    print(bottom)
    time.sleep(0.12)

print()
print(color('\n — Woody Allen (if he wrote Python)', 'magenta'))