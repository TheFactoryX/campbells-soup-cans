"""
Campbell's Soup Can #266
Produced: 2025-11-14 07:30:32
Worker: DeepSeek: R1 (free) (deepseek/deepseek-r1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import sys
import re

# ANSI color codes
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def neurotic_typer(text, delay=0.03):
    """Print text with style-appropriate neurotic hesitation"""
    tokens = re.split(r'(\033\[[0-9;]*m)', text)
    for token in tokens:
        if not token: continue
        if token.startswith('\033'):
            sys.stdout.write(token)
            sys.stdout.flush()
        else:
            for char in token:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(abs(delay + (0.02 if char in ",;" else 0)))  # Extra hesitation for punctuation
    print()

clear()

# Anxious ASCII constellation
print(f"{CYAN}")
print(r"    \              _____")
print(r"     \            /     \    ___")
print(r"      \  ○   ○   /  ✗   \  / _ \ ")
print(r"       \   ∑     \       || (_) |")
print(r"        \________/\_____/  \___/")
print(RESET)
time.sleep(0.8)

# Construct existential panic box
quote = [
    "I'm certain the universe keeps",
    "auto-correcting my existence",
    "to something more absurd",
    "",
    "   ...but draft versions haunt me"
]

max_len = max(len(line.strip()) for line in quote) + 4
border = RED + "▗" + "▄"*(max_len+2) + "▖" + RESET
space_line = RED + "▐" + " "*(max_len+2) + "▌" + RESET

neurotic_typer(border, 0)
neurotic_typer(space_line)
for line in quote:
    colored = f"{RED}▐  {YELLOW}{line.center(max_len)}{RED}  ▌{RESET}"
    neurotic_typer(colored, 0.04 if "..." in line else 0.03)
neurotic_typer(space_line)
neurotic_typer(border, 0)

# Animated sweat drops
for _ in range(3):
    for s in [' 💧', '  💧', '   💧']:
        sys.stdout.write(f"{CYAN}\r{s}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r   ')
print("\n")