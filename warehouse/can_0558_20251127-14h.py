"""
Campbell's Soup Can #558
Produced: 2025-11-27 14:35:23
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
   ___________
  /           \\
 |   Woood Allen   |
 |  quote generator|
  \\_____________/
"""

import sys
import time
import random

# ANSI escape codes for colors
RESET  = '\033[0m'
BOLD   = '\033[1m'
BLINK  = '\033[5m'

# Foreground colors
COLORS = [
    '\033[38;5;196m',  # red
    '\033[38;5;202m',  # orange
    '\033[38;5;226m',  # yellow
    '\033[38;5;118m',  # green
    '\033[38;5;118m',
    '\033[38;5;123m',  # teal
    '\033[38;5;27m',   # blue
    '\033[38;5;93m',   # purple
    '\033[38;5;205m',  # magenta
]

# Background color for the box
BG = '\033[48;5;236m'  # dark gray

# Quote in Woody Allen style
QUOTE = (
    "I spent thirty minutes pondering whether my existence is an error, "
    "only to realize I have no idea if I am an error or a well‑meaning typo "
    "in God’s script."
)

def type_out(text, delay=0.03, color=None):
    """Print text one character at a time (like a typewriter)."""
    for char in text:
        if color:
            sys.stdout.write(color + char + RESET)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def draw_box(text, width, border_color):
    """Return a list of strings that form a colored box around the text."""
    lines = []
    horizontal = border_color + '+' + '-' * (width + 2) + '+' + RESET
    empty     = border_color + '|' + ' ' * (width + 2) + '|' + RESET
    lines.append(horizontal)
    lines.append(empty)
    # Center the quote
    padded = ' ' + text.ljust(width) + ' '
    lines.append(border_color + '|' + padded + '|' + RESET)
    lines.append(empty)
    lines.append(horizontal)
    return lines

def animate_border(width):
    """Randomly change border colors for a short animation."""
    for _ in range(12):
        border = random.choice(COLORS)
        box_lines = draw_box(QUOTE.split()[0], width, border)
        sys.stdout.write('\n'.join(box_lines) + '\n')
        time.sleep(0.1)
        sys.stdout.write('\033[?25l')  # hide cursor
        sys.stdout.write('\033[H')      # move cursor to top-left
    sys.stdout.write('\033[?25h')  # show cursor

def main():
    # Strip spaces for width calculation
    quote_short = QUOTE.strip()
    max_len = max(len(line) for line in quote_short.split('\n'))
    border_color = random.choice(COLORS)

    # Animation (optional)
    animate_border(max_len)

    # Final box
    box = draw_box(quote_short, max_len, border_color)
    sys.stdout.write('\n'.join(box) + '\n')
    sys.stdout.flush()

    # Type out the quote slowly inside the box
    time.sleep(0.5)
    sys.stdout.write('\n')
    type_out(QUOTE, delay=0.05, color='\033[38;5;228m')  # bright yellow
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()
