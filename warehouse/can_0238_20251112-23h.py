"""
Campbell's Soup Can #238
Produced: 2025-11-12 23:30:20
Worker: Meta: Llama 4 Maverick (free) (meta-llama/llama-4-maverick:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

def print_quote(quote):
    print(f"{BLUE}*************************************{END_COLOR}")
    print(f"{YELLOW}*                                   *{END_COLOR}")
    for line in quote.split('\n'):
        print(f"{YELLOW}* {GREEN}{line.ljust(33)} *{END_COLOR}")
    print(f"{YELLOW}*                                   *{END_COLOR}")
    print(f"{BLUE}*************************************{END_COLOR}")

def animate_quote(quote):
    lines = quote.split('\n')
    print(f"{BLUE}*************************************{END_COLOR}")
    print(f"{YELLOW}*                                   *{END_COLOR}")
    for line in lines:
        sys.stdout.write(f"{YELLOW}* {GREEN}")
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f"{' ' * (33 - len(line))} *{END_COLOR}\n")
        time.sleep(0.2)
    print(f"{YELLOW}*                                   *{END_COLOR}")
    print(f"{BLUE}*************************************{END_COLOR}")

def main():
    quote = "I'm not a vegetarian because I love animals.\nI'm a vegetarian because I hate plants."
    print("\033[2J")  # clear screen
    animate_quote(quote)

if __name__ == "__main__":
    main()