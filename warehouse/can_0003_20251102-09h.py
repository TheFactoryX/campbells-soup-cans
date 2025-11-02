"""
Campbell's Soup Can #3
Produced: 2025-11-02 09:27:50
Worker: Microsoft: MAI DS R1 (free) (microsoft/mai-ds-r1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import re

def strip_ansi(text):
    ansi_escape = re.compile(r'\x1B\[[0-9;]*[a-zA-Z]')
    return ansi_escape.sub('', text)

RED = "\033[91m"
GOLD = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

lines = [
    "I don't fear the void of existence – what keeps me up at night",
    "is the possibility that my therapist is secretly rolling her eyes."
]
author = "- Woody Allen (probably)"

max_length = max(len(line) for line in lines)
total_width = max_length + 4  # Account for borders

top_border = f"{RED}╭{'─' * (max_length + 2)}╮{RESET}"
bottom_border = f"{RED}╰{'─' * (max_length + 2)}╯{RESET}"

# Print animated top border
for char in top_border:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.015)
print()

# Animated quote lines
for line in lines:
    padded_line = line.ljust(max_length)
    full_line = f"{RED}│ {GOLD}{padded_line}{RED} │{RESET}"
    
    for i, char in enumerate(full_line):
        if i < 2 or i >= max_length + 3:
            sys.stdout.write(RED + char + RESET)
        else:
            sys.stdout.write(GOLD + char + RESET)
        sys.stdout.flush()
        time.sleep(0.02 if i < max_length + 3 else 0)
    print()

# Pulse the bottom border
for char in bottom_border:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.015)
print()

# Animated author credit
author_line = f"{' '*(total_width - len(strip_ansi(author)) - 1)}{CYAN}{author}{RESET}"
for i, char in enumerate(author_line):
    if i >= total_width - len(author) - 1:
        sys.stdout.write(CYAN + char + RESET)
    else:
        sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
print()