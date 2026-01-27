"""
Campbell's Soup Can #1885
Produced: 2026-01-27 16:49:18
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def color(text, name):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'reset': '\033[0m'
    }
    return colors.get(name, '') + text + colors['reset']

quote = "I’m not afraid of death; I just don’t want to be there when it happens."
border = [
    "╔══════════════════════════════════════════════╗",
    "║                                            ║",
    f"║  {quote}                                   ║",
    "║                                            ║",
    "╚══════════════════════════════════════════════╝"
]

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
for i, line in enumerate(border):
    sys.stdout.write(color(line, colors[i % len(colors)]))
    sys.stdout.write('\n')