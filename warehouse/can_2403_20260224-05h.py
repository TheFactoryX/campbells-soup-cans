"""
Campbell's Soup Can #2403
Produced: 2026-02-24 05:03:25
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

quote = '"I’m not afraid of death; I just don’t want to be there when it happens."'

border_top    = '╔' + '═'*48 + '╗'
border_bottom = '╚' + '═'*48 + '╝'

def colored(text, color):
    colors = {
        'reset': '\033[0m',
        'cyan'   : '\033[96m',
        'magenta': '\033[95m',
        'yellow' : '\033[93m',
        'green'  : '\033[92m'
    }
    return colors.get(color, '') + text + colors['reset']

for line in (border_top, f'  {quote}  ', border_bottom):
    sys.stdout.write(colored(line, 'cyan') + '\n')
    sys.stdout.flush()
    time.sleep(0.2)