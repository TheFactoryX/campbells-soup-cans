"""
Campbell's Soup Can #3402
Produced: 2026-04-22 17:14:37
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import shutil
import random
import os

# ANSI color codes
CYAN   = '\033[96m'
GREEN  = '\033[92m'
YELLOW = '\033[93m'
MAGENTA= '\033[95m'
RESET  = '\033[0m'

# Quote
QUOTE = (
    "I keep asking myself, ‘What’s the point of living?’ "
    "and then I realize the answer is: "
    "to make a witty joke about existential dread while staring at my Wi‑Fi signal."
)

# Prepare the box
def draw_box(message, width):
    border = MAGENTA + '+' + '-' * (width - 2) + '+' + RESET
    empty  = MAGENTA + '|' + RESET + ' ' * (width - 2) + MAGENTA + '|' + RESET
    msg_line = (
        MAGENTA + '|' + RESET + CYAN + message.center(width - 2) + RESET + MAGENTA + '|' + RESET
    )
    return [border, empty, msg_line, empty, border]

# Clear the screen
def clear():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

# Animate the box moving horizontally like a lazy cat
def animate(box_lines, delay=0.05):
    cols, _ = shutil.get_terminal_size((80, 20))
    max_shift = cols - len(box_lines[0])
    if max_shift < 0:
        max_shift = 0
    direction = 1
    shift = 0
    for _ in range(80):
        clear()
        padding = ' ' * shift
        for line in box_lines:
            print(padding + line)
        sys.stdout.flush()
        time.sleep(delay)
        shift += direction
        if shift == 0 or shift == max_shift:
            direction *= -1

# Main
def main():
    # Shorten quote if too long
    max_width = 60
    words = QUOTE.split()
    lines = []
    current = []
    for word in words:
        if len(' '.join(current + [word])) <= max_width - 4:
            current.append(word)
        else:
            lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))

    boxed = []
    for line in lines:
        boxed.extend(draw_box(line, max_width))
        boxed.append('')  # blank line between boxes

    animate(boxed)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear()
        sys.exit(0)