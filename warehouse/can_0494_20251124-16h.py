"""
Campbell's Soup Can #494
Produced: 2025-11-24 16:36:50
Worker: xAI: Grok 4.1 Fast (free) (x-ai/grok-4.1-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

CLEAR = '\033[2J\033[H'
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'  # Some terminals support

colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m'
}

color_list = [
    colors['cyan'],
    colors['magenta'],
    colors['yellow'],
    colors['green'],
    colors['blue'],
    colors['red']
]

quote = "I'm not afraid of the universe's indifference; what really scares me is if it suddenly decides to notice me."
inside_width = len(quote) + 4
border_color = colors['yellow'] + BOLD
top_line = '╔' + '═' * inside_width + '╗'
space_line = '║' + ' ' * inside_width + '║'
bot_line = '╚' + '═' * inside_width + '╝'

sys.stdout.write(CLEAR)
sys.stdout.flush()

# Animated title
title = "  WOODY ALLEN'S  NEUROTIC  WISDOM  "
sys.stdout.write(BOLD + colors['white'] + title + RESET + '\n')
sys.stdout.flush()
time.sleep(0.5)

# Twinkling stars for existential void
stars = ['*   ', ' *  ', '  * ', '   *', '  * ', ' *  ', '*   ']
for _ in range(6):
    for star in stars:
        sys.stdout.write('\r' + colors['cyan'] + BOLD + star + 'Entering the void...' + RESET)
        sys.stdout.flush()
        time.sleep(0.2)
print('\n' * 2)

# Box
print(border_color + top_line + RESET)
print(border_color + space_line + RESET)
print(border_color + bot_line + RESET)
sys.stdout.flush()

# Typewriter effect inside the box with color cycling
sys.stdout.write('\033[3;2H')  # Position inside the box (adjust for title + stars + box lines)
sys.stdout.flush()

for i, char in enumerate(quote):
    col = color_list[i % len(color_list)]
    sys.stdout.write(col + BOLD + char + RESET)
    sys.stdout.flush()
    time.sleep(0.06)

# Final flourish
time.sleep(1)
sys.stdout.write('\n\033[5;1H')  # Move below
sys.stdout.write(colors['magenta'] + ITALIC + "  (A totally original Woody-esque musing)" + RESET + '\n')
sys.stdout.flush()

# Fade out effect? Nah, let it shine.
input("\nPress Enter to contemplate your own neuroses...")