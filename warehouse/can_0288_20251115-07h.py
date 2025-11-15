"""
Campbell's Soup Can #288
Produced: 2025-11-15 07:27:23
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

def print_boxed_quote(quote):
    print(f"{bcolors.OKBLUE}*********************************{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}*                               *{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}*  {bcolors.BOLD}{quote}{bcolors.ENDC}  *{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}*                               *{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}*********************************{bcolors.ENDC}")

def animate_quote(quote):
    for char in quote:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def main():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "If only God would give me some clear sign! Like making a large deposit in my name in a Swiss bank.",
        "I was smart enough to go through college, but not smart enough to drop out."
    ]
    quote = random.choice(quotes)
    print(f"{bcolors.HEADER}The Wisdom of Woody Allen:{bcolors.ENDC}")
    print_boxed_quote(quote)
    print(f"{bcolors.OKCYAN}~ Woody Allen, Neurotic Philosopher{bcolors.ENDC}")

if __name__ == "__main__":
    main()