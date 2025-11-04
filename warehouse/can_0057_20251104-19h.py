"""
Campbell's Soup Can #57
Produced: 2025-11-04 19:26:51
Worker: Sao10K: Llama 3.1 70B Hanami x1 (sao10k/l3.1-70b-hanami-x1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time

_quote = "Life is full of misery, loneliness, and suffering - and it's all over much too soon."

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

RED = '\033[1;31m'
GREEN = '\033[1;32m'
BLUE = '\033[1;34m'
YELLOW = '\033[1;33m'
PURPLE = '\033[1;35m'
CYAN = '\033[1;36m'
RESET = '\033[0m'

def print_quote(quote):
    print(f"\n{CYAN}{' ' * len(quote) + ' '}{RESET}")
    print(f" {YELLOW}{quote}{RESET} ")
    print(f"{PURPLE}{' ' * len(quote) + ' '}{RESET}\n")

clear_screen()
colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
i = 0

while i < len(colors):
    clear_screen()
    color = colors[i % len(colors)]
    print_quote(f"{color}{_quote}{RESET}")
    time.sleep(0.3)
    i += 1