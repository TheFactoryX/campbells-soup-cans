"""
Campbell's Soup Can #1819
Produced: 2026-01-24 14:34:54
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time

# The philosophical quote in Woody Allen's neurotic style
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Dimensions of the decorative box
box_width = len(quote) + 4
border = '+' + '-' * box_width + '+'
top    = '| ' + ' ' * box_width + ' |'
quote_line = '| ' + quote + ' |'
bottom = '+' + '-' * box_width + '+'

# ANSI color codes (light red, green, yellow, blue, magenta, cyan)
colors = [31, 32, 33, 34, 35, 36]
reset = '\033[0m'

def colored(text, code):
    """Wrap text in an ANSI color code."""
    return f'\033[{code}m{text}\033[0m'

# Simple animation: cycle colors for a few frames
for frame in range(3):
    sys.stdout.write('\033[2J\033[H')  # clear screen
    sys.stdout.write(colored(border,  colors[frame % len(colors)]) + '\n')
    sys.stdout.write(colored(top,     colors[(frame+1) % len(colors)]) + '\n')
    sys.stdout.write(colored(quote_line, colors[(frame+2) % len(colors)]) + '\n')
    sys.stdout.write(colored(bottom, colors[(frame+3) % len(colors)]) + '\n')
    sys.stdout.flush()
    time.sleep(0.8)

# Final static display with a bright magenta border
print(colored(border, 35))
print(colored(top,     32))
print(colored(quote_line, 33))
print(colored(bottom, 34))