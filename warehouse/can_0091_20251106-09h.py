"""
Campbell's Soup Can #91
Produced: 2025-11-06 09:34:27
Worker: Meta: Llama 4 Scout (free) (meta-llama/llama-4-scout:free)
Employment: Volunteer
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

def print_boxed_quote(quote, author, color):
    print(f"{color}╔══════════════════════════════════╗{bcolors.ENDC}")
    print(f"{color}║{bcolors.ENDC} {quote} {bcolors.ENDC}║")
    print(f"{color}║{bcolors.ENDC}  - {author} {bcolors.ENDC}║")
    print(f"{color}╚══════════════════════════════════╝{bcolors.ENDC}")

def animate_quote(quote, author):
    colors = [bcolors.HEADER, bcolors.OKBLUE, bcolors.OKCYAN, bcolors.OKGREEN, bcolors.WARNING, bcolors.FAIL]
    for _ in range(5):
        for color in colors:
            sys.stdout.write("\r")
            print_boxed_quote(quote, author, color)
            sys.stdout.flush()
            time.sleep(0.5)

def main():
    quote = "I'm not lazy, I'm just on energy-saving mode."
    author = "Woody Allen (or so I've been told)"
    print_boxed_quote(quote, author, bcolors.OKBLUE)
    time.sleep(2)
    animate_quote(quote, author)

if __name__ == "__main__":
    main()