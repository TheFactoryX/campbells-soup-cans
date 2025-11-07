"""
Campbell's Soup Can #112
Produced: 2025-11-07 08:42:03
Worker: Meta: Llama 3.3 8B Instruct (free) (meta-llama/llama-3.3-8b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def print_quote():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{YELLOW}
 ___________________________________)
|                                     |
|  Life is like a movie, but without  |
|  the leading man, the plot, or the  |
|  ending. It's just a bunch of random |
|  scenes and poor lighting.          |
|                                     |
 ___________________________________")
    print(f"{RESET}")
    time.sleep(2)
    print(f"{GREEN} - Woody Allen{RESET}")
    time.sleep(1)

if __name__ == "__main__":
    print_quote()