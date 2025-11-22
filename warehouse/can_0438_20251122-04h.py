"""
Campbell's Soup Can #438
Produced: 2025-11-22 04:34:35
Worker: Qwen2.5 72B Instruct (qwen/qwen-2.5-72b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_ascii_art():
    print_colored(r'''
 __     _      _      _    _ _____  ______ 
 \ \   / /    | |    | |  | |  __ \|  ____|
  \ \_/ /_ _ _| | ___| |  | | |  | | |__   
   \   / _` | |/ _ \ |  | | |  | |  __|  
    | | (_| | |  __/ |__| | |__| | |____ 
    |_|\__,_|_|\___|\____/|_____/|______|
    ''', '35')

def print_philosophical_quote():
    print_colored("\nI'm not afraid of death; I just don't want to be there when it happens.", '36')
    time.sleep(2)
    print_colored(" - Woody Allen (sort of)", '34')

def print_fancy_box(quote):
    lines = quote.split('\n')
    max_length = max(len(line) for line in lines)
    print_colored(f"+" + "-" * (max_length + 2) + "+", '33')
    for line in lines:
        print_colored(f"| {line.ljust(max_length)} |", '33')
    print_colored(f"+" + "-" * (max_length + 2) + "+", '33')

def main():
    print_ascii_art()
    time.sleep(1)
    quote = "I'm not afraid of death; I just don't want to be there when it happens.\n - Woody Allen (sort of)"
    print_fancy_box(quote)

if __name__ == "__main__":
    main()