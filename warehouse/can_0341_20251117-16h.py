"""
Campbell's Soup Can #341
Produced: 2025-11-17 16:44:25
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

"""
A single‑file Python program that prints one funny Woody Allen‑style
philosophical quote in a colorful, animated box.
"""

import sys
import time

# ANSI escape codes for colors and styles
RESET      = "\x1b[0m"
BOLD       = "\x1b[1m"
DIM        = "\x1b[2m"
UNDERSCORE = "\x1b[4m"
REVERSE    = "\x1b[7m"
BLACK      = "\x1b[30m"
RED        = "\x1b[31m"
GREEN      = "\x1b[32m"
YELLOW     = "\x1b[33m"
BLUE       = "\x1b[34m"
MAGENTA    = "\x1b[35m"
CYAN       = "\x1b[36m"
WHITE      = "\x1b[37m"

# Background colors
BG_BLACK   = "\x1b[40m"
BG_RED     = "\x1b[41m"
BG_GREEN   = "\x1b[42m"
BG_YELLOW  = "\x1b[43m"
BG_BLUE    = "\x1b[44m"
BG_MAGENTA = "\x1b[45m"
BG_CYAN    = "\x1b[46m"
BG_WHITE   = "\x1b[47m"


# The Woody‑Allen‑style quote
QUOTE = (
    "\"Sure, everyone says you should find meaning in life, "
    "but all I can say is: if meaning is a cafeteria menu, "
    "I'm still ordering the fries.\""
)

# Width of the box (excluding borders)
BOX_WIDTH = 60

# Small spinner for splash effect
SPINNER_FRAMES = ['◐', '◓', '◑', '◒']

def type_print(text, delay=0.02, color=WHITE, end='\n'):
    """
    Print `text` character by character with a slight delay.
    """
    for ch in text:
        sys.stdout.write(f'{color}{ch}{RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def draw_box():
    """
    Draw the colored, animated quote inside a box.
    """
    # Top border
    top = f'{BG_CYAN}{CYAN}+{"-" * BOX_WIDTH}+{RESET}'
    sys.stdout.write(top + '\n')
    sys.stdout.flush()

    # Empty line padding
    empty = f'{BG_CYAN}{" " * (BOX_WIDTH + 2)}{RESET}'
    sys.stdout.write(empty + '\n')
    sys.stdout.flush()

    # Quote line, wrapped to fit the box
    q_lines = wrap_text(QUOTE, BOX_WIDTH)
    for line in q_lines:
        padding = BOX_WIDTH - len(line)
        left  = f'{BG_CYAN}{BLUE}| {RESET}'
        right = f'{BG_CYAN}{BLUE}|{RESET}'
        sys.stdout.write(f'{left}{line}{" " * padding}{right}{RESET}\n')
        sys.stdout.flush()

    # Bottom empty line
    sys.stdout.write(empty + '\n')
    sys.stdout.flush()

    # Bottom border
    bottom = f'{BG_CYAN}{CYAN}+{"-" * BOX_WIDTH}+{RESET}'
    sys.stdout.write(bottom + '\n')
    sys.stdout.flush()

def wrap_text(text, width):
    """
    Simple word wrap that returns a list of lines.
    """
    words = text.split()
    lines = []
    current = ''
    for word in words:
        if len(current) + len(word) + 1 <= width:
            if current:
                current += ' '
            current += word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def spinner(duration=1.5):
    """
    Show a spinner for a brief period before starting the main display.
    """
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        frame = SPINNER_FRAMES[idx % len(SPINNER_FRAMES)]
        sys.stdout.write(f'\r{YELLOW}{frame}{RESET} Loading...')
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

def main():
    spinner()
    # Type‑writer print the quote line by line
    for line in wrap_text(QUOTE, BOX_WIDTH):
        type_print(line, delay=0.03, color=YELLOW)
    # Draw the boxed version afterward
    type_print('\n', color=RESET)
    draw_box()
    type_print('\nPress Enter to exit.', color=GREEN)
    input()

if __name__ == '__main__':
    main()