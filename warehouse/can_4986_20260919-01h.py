"""
Campbell's Soup Can #4986
Produced: 2026-09-19 01:10:32
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

CYAN = '\033[36m'  # Border color
MAGENTA = '\033[35m'  # Quote text color
RESET = '\033[0m'

def display_char_with_delay(char, color, delay=0.02):
    sys.stdout.write(f"{color}{char}{RESET}")
    sys.stdout.flush()
    time.sleep(delay)

def animate_text(text, color, delay=0.02):
    for c in text:
        if c == ' ':
            display_char_with_delay(c, '\033[0m', delay)
        else:
            display_char_with_delay(c, color, delay)
    print()

def build_box_line(length, border_char='-', fill_char=' ', color=RESET):
    return color + ('+' + border_char * (length - 2) + '+') + RESET if border_char else color + (fill_char * length) + RESET

# Quote settings
quote_lines = [
    "I'm not afraid of dying; I just hate that it might happen when I'm ",
    "mid-philosophical thought, and I get to die mid-sentence: ",
    "'This is the meaning of—'"
]

box_width = 60  # 60 characters including the '+' and borders

# Print top border
top = build_box_line(box_width + 2, '-', CYAN)  # +2 for the outer '+'
print(top)

# Print empty line above quote
empty_line = build_box_line(box_width + 2, ' ', CYAN)
print(empty_line)

# Print each quote line with animation
for line in quote_lines:
    # Center the line within the box (58 chars between '+')
    centered_line = line.center(58)
    # Print left border |
    print(f"{CYAN}|{RESET}", end='')
    animate_text(centered_line, MAGENTA)
    # Print right border |
    print(f"{CYAN}|{RESET}")

# Print bottom border
bottom = build_box_line(box_width + 2, '-', CYAN)
print(bottom)

# Reset terminal color
print(RESET)