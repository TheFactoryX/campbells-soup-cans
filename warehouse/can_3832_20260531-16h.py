"""
Campbell's Soup Can #3832
Produced: 2026-05-31 16:36:12
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m'
}

def print_typewriter(text, color, delay=0.05, end=' '):
    for char in text:
        sys.stdout.write(f"{COLORS[color]}{char}{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

quote_lines = [
    ("I've spent my entire life trying to avoid death...", 'red'),
    ("but now I'm starting to think it's avoiding me.", 'green'),
    ("It's probably on a beach somewhere,", 'yellow'),
    ("sipping a mai tai and laughing at my life choices.", 'blue')
]

print(COLORS['magenta'] + "★ Woody Allen's Philosophical Musings ★" + COLORS['reset'])
print()
print(COLORS['cyan'] + "┌" + "─"*48 + "┐" + COLORS['reset'])

for line, color in quote_lines:
    sys.stdout.write(COLORS['cyan'] + "│ " + COLORS['reset'])
    print_typewriter(line, color, 0.03)
    print(COLORS['cyan'] + " │" + COLORS['reset'])
    time.sleep(0.5)

print(COLORS['cyan'] + "└" + "─"*48 + "┘" + COLORS['reset'])