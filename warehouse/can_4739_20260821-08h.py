"""
Campbell's Soup Can #4739
Produced: 2026-08-21 08:58:12
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os
import itertools

# Enable ANSI colors on Windows if needed
if os.name == 'nt':
    os.system('')

# ANSI color codes
COLORS = [
    '\033[31m',  # Red
    '\033[33m',  # Yellow
    '\033[32m',  # Green
    '\033[36m',  # Cyan
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
]
RESET = '\033[0m'
BOLD = '\033[1m'

# Woody Allen‑style quote
QUOTE = (
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "Besides, the afterlife probably has terrible Wi‑Fi."
)

# Simple ASCII nervous figure (will "blink")
FIGURES = [
    r"""
   _____
  /     \
 |  o o  |
 |   ^   |
 |  '-'  |
  \_____/
""",
    r"""
   _____
  /     \
 |  x x  |
 |   ^   |
 |  '-'  |
  \_____/
""",
    r"""
   _____
  /     \
 |  - -  |
 |   ^   |
 |  '-'  |
  \_____/
""",
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, width=60):
    print(text.center(width))

def draw_box(content, border_color):
    lines = content.splitlines()
    max_len = max(len(line) for line in lines)
    top_bottom = border_color + '+' + '-' * (max_len + 2) + '+' + RESET
    print(top_bottom)
    for line in lines:
        padded = line.ljust(max_len)
        print(f"{border_color}| {padded} |{RESET}")
    print(top_bottom)

def animate():
    clear()
    color_cycle = itertools.cycle(COLORS)
    for _ in range(12):  # number of animation frames
        clear()
        border_color = next(color_cycle)
        fig = next(itertools.cycle(FIGURES))
        print_centered(fig)
        print()
        print_centered(f"{BOLD}{border_color}~ Woody Allen Wisdom ~{RESET}")
        print()
        draw_box(QUOTE, border_color)
        time.sleep(0.15)
    # Final static version (white border)
    clear()
    print_centered(next(itertools.cycle(FIGURES)))
    print()
    print_centered(f"{BOLD}\033[37m~ Woody Allen Wisdom ~{RESET}")
    print()
    draw_box(QUOTE, '\033[37m')
    print()
    print_centered("Press Enter to exit...", width=60)
    try:
        input()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    animate()