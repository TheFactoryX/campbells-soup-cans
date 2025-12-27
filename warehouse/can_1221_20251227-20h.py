"""
Campbell's Soup Can #1221
Produced: 2025-12-27 20:34:26
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

def col(txt, name):
    colors = {
        'reset': '\033[0m',
        'cyan': '\033[36m',
        'yellow': '\033[33m',
        'magenta': '\033[35m',
    }
    return colors.get(name, '') + txt + colors['reset']

quote = "I'm not afraid of death; I just don't want to be there when it happens."
w = len(quote) + 4
border = col('╔' + '═' * w + '╗', 'cyan')
top    = col('║ ' + quote + ' ║', 'yellow')
bottom = col('╚' + '─' * w + '╝', 'cyan')

def typew(s, delay=0.025):
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.flush()

typew('\n')
typew(border)
typew(top)
typew(bottom)
typew('\n')