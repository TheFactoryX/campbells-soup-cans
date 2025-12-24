"""
Campbell's Soup Can #1152
Produced: 2025-12-24 17:32:19
Worker: Meta: Llama 3.1 405B Instruct (free) (meta-llama/llama-3.1-405b-instruct:free)
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
ENDC = '\033[0m'

# ASCII art Woody Allen
woody_art = """
        _______
       /        \\
      /          \\
     /            \\
    |   o   o   |
     _______/
      |       |
      |  __  |
      | /  \\ |
      | |  | |
      | |__| |
      |_____/
"""

# Philosophical quote
quote = "I'm not a vegetarian because I love animals. I'm a vegetarian because I hate plants."

# Animation
def print_quote(quote):
    for char in quote:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# Main
print(GREEN + woody_art + ENDC)
time.sleep(1)
print(YELLOW + "Woody Allen says:" + ENDC)
time.sleep(1)
print_quote(RED + quote + ENDC)
time.sleep(2)
print(BLUE + "\nThink about it..." + ENDC)
time.sleep(2)