"""
Campbell's Soup Can #59
Produced: 2025-11-04 21:29:29
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
import os

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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_quote(quote, color):
    clear_screen()
    print(f"{color}╔══════════════════════════════════════╗{bcolors.ENDC}")
    print(f"{color}║{bcolors.ENDC}                                      {color}║{bcolors.ENDC}")
    print(f"{color}║{bcolors.ENDC}          Philosophical Musings         {color}║{bcolors.ENDC}")
    print(f"{color}║{bcolors.ENDC}                                      {color}║{bcolors.ENDC}")
    print(f"{color}╚══════════════════════════════════════╝{bcolors.ENDC}")
    print()
    print(f"                  {color}{quote}{bcolors.ENDC}")
    print()
    print(f"{color}╔══════════════════════════════════════╗{bcolors.ENDC}")
    print(f"{color}║{bcolors.ENDC}  - Woody Allen (or so I've been told)  {color}║{bcolors.ENDC}")
    print(f"{color}╚══════════════════════════════════════╝{bcolors.ENDC}")

def main():
    quote = "\"I'm not afraid of death; I just don't want to be there when it happens... or at least not without my snack pack\""
    color = bcolors.OKBLUE
    animation_delay = 0.5

    for _ in range(5):
        clear_screen()
        print_quote(quote, bcolors.OKGREEN)
        time.sleep(animation_delay)
        clear_screen()
        print_quote(quote, bcolors.OKBLUE)
        time.sleep(animation_delay)
        clear_screen()
        print_quote(quote, bcolors.OKCYAN)
        time.sleep(animation_delay)

    clear_screen()
    print_quote(quote, bcolors.OKBLUE)

if __name__ == "__main__":
    main()