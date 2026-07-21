"""
Campbell's Soup Can #4279
Produced: 2026-07-21 14:22:05
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
A tiny happy little console program that prints a Woody‑Allen‑style
philosophical quote surrounded by an animated, colorized ASCII box.
"""

import sys
import time

# ANSI colour codes
CYAN   = '\033[36m'
MAGENTA = '\033[35m'
YELLOW = '\033[33m'
RESET  = '\033[0m'

# The quote – feel free to tweak it!
QUOTE = (
    "I always thought my existential crisis was a private joke "
    "until I realized it was a public service ad for anxiety."
)

width = len(QUOTE)
box_width = width + 4  # 2 spaces on each side

border = f'{CYAN}+{"-" * box_width}+{RESET}'
left  = f'{MAGENTA}|  '
right = f'  |{RESET}'

# Print the top border
print(border)

# Animate the quote inside the box
for i in range(width + 1):
    # Empty the line first, then print the growing lunes
    partial = QUOTE[:i]
    padding = ' ' * (width - i)
    line = f'{left}{YELLOW}{partial}{RESET}{padding}{right}'
    sys.stdout.write('\r' + line)
    sys.stdout.flush()
    time.sleep(0.05)

# Finish the animation and print the bottom border
print()          # move to the next line
print(border)