"""
Campbell's Soup Can #5186
Produced: 2026-10-30 07:07:26
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

quote = "I can't decide whether my anxiety is worse than death, or if both are just different types of boredom."

def colorize(text, code):
    return f"\033[{code}m{text}\033[0m"

def animate(text, colors):
    for i, char in enumerate(text):
        if i == 0:
            sys.stdout.write('\r')
        color_code = colors[i % len(colors)]
        sys.stdout.write(colorize(char, color_code))
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write('\n')

max_width = 80
border_style = '-' if time.time() * 2 % 2 < 1 else '='

top = colorize('+' + '-' * (max_width - 2) + '+', '31') + '\n'
sys.stdout.write(top)
sys.stdout.flush()

lines = []
line_start = 0
for i, char in enumerate(quote):
    if quote[i:i+1] == ' ' and (i - line_start) > 40:
        lines.append(quote[line_start:i])
        line_start = i + 1
        time.sleep(0.1)
if line_start <= len(quote):
    lines.append(quote[line_start:])

for line in lines:
    pad = ' ' * (max_width - 4 - len(line))
    inner = colorize('|' + ' ' * 2, '36') + line + colorize(' ' * 2 + '|', '36')
    colors = ['36'] * (max_width)
    animate(inner, colors)
    sys.stdout.flush()

bottom = colorize('+' + '-' + '='*(max_width - 4) + '-', '31') + '+'
sys.stdout.write(bottom)
sys.stdout.flush()