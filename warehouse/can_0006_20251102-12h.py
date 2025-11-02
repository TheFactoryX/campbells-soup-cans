"""
Campbell's Soup Can #6
Produced: 2025-11-02 12:53:06
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
RESET = "\033[0m"
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

def print_quote(quote):
    print(f"{GREEN}****************************************************{RESET}")
    print(f"{GREEN}*                                                  *{RESET}")
    print(f"{GREEN}*               Philosophical Musings              *{RESET}")
    print(f"{GREEN}*                                                  *{RESET}")
    print(f"{GREEN}****************************************************{RESET}")
    print()
    print(f"{BLUE}  ~ Woody Allen ~{RESET}")
    print()
    print(f"{YELLOW}      {quote}{RESET}")
    print()

def animate_quote(quote):
    for _ in range(3):
        print_quote(quote)
        time.sleep(0.5)
        sys.stdout.write("\033[2J")  # clear screen
        sys.stdout.write("\033[H")  # move cursor to top

def main():
    quote = f"{RED}I'm not arguing, I'm just explaining why I'm right. There's a difference.{RESET}"
    animate_quote(quote)

if __name__ == "__main__":
    main()