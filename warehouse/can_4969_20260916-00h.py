"""
Campbell's Soup Can #4969
Produced: 2026-09-16 00:21:33
Worker: Meta: Llama 4 Scout (meta-llama/llama-4-scout)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI escape codes for colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_boxed_text(text, color):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    box_length = max_length + 4
    print(f"{color}{'#' * box_length}{bcolors.ENDC}")
    for line in lines:
        print(f"{color}# {' ' * (max_length - len(line))}{line}{' ' * (max_length - len(line))} #{bcolors.ENDC}")
    print(f"{color}{'#' * box_length}{bcolors.ENDC}")

def main():
    quote = f"{bcolors.OKBLUE}Life is like a relationship with a neurotic person - it's full of anxiety, self-doubt, and occasional bouts of crippling despair... but somehow, you still can't help but show up every day.{bcolors.ENDC}"
    print_boxed_text(quote, bcolors.OKCYAN)

if __name__ == "__main__":
    main()