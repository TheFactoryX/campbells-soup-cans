"""
Campbell's Soup Can #439
Produced: 2025-11-22 05:32:10
Worker: Meta: Llama 3.2 3B Instruct (free) (meta-llama/llama-3.2-3b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def print_quote():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;31;40m\033[2J") # Clear screen and print in red on black
    print("          You're only given a little spark of madness.")
    print("         You make good use of it, you burn out that spark.")
    print("\033[1;32;40m\033[2J") # Clear screen and print in green on black
    print("       That's why you have lived—remain alive.")
    time.sleep(1)
    print("\033[0m\033[0;37m\033[2J") # Clear screen and print in default color
    print("      - Friedrich Nietzsche")

print_quote()