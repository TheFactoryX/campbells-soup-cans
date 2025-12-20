"""
Campbell's Soup Can #1060
Produced: 2025-12-20 13:37:18
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
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ASCII art Woody Allen
woody_art = """
 _______
|       |
|  O   O  |
|  > ^ <  |
| _______ |
"""

def print_quote():
    # clear the screen
    print("\033[H\033[J")

    # print ASCII art Woody Allen
    print(bcolors.HEADER + woody_art + bcolors.ENDC)

    # print quote with animation
    quote = "I'm not afraid of death; I just don't want to be there when it happens... and also when the Wi-Fi is slow."
    for char in quote:
        sys.stdout.write(bcolors.OKGREEN + char + bcolors.ENDC)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

    # print "— Woody Allen" with underline
    print(bcolors.UNDERLINE + "— Woody Allen" + bcolors.ENDC)

# run the program
print_quote()