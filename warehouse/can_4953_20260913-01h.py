"""
Campbell's Soup Can #4953
Produced: 2026-09-13 01:01:13
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
DIM = '\033[2m'
RESET = '\033[0m'
REVERSE = '\033[7m'

def clear_screen():
    print('\033[2J\033[H', end='')

def typewriter(text, color, delay=0.03, bold=False):
    style = BOLD if bold else ''
    for char in text:
        sys.stdout.write(f"{style}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(text, color, width=60):
    padded = text.center(width - 4)
    top = f"{color}╔{'═' * (width - 2)}╗{RESET}"
    mid = f"{color}║ {padded} ║{RESET}"
    bot = f"{color}╚{'═' * (width - 2)}╝{RESET}"
    print(top)
    print(mid)
    print(bot)

def print_skull():
    skull = f"""
{RED}        .,,       .,,
       (oo)       (oo)
   /|--/|       /|--/|
  ( |  | )     ( |  | )