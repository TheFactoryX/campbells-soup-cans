"""
Campbell's Soup Can #1162
Produced: 2025-12-25 05:41:09
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
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
END_COLOR = "\033[0m"

# ASCII art frame
def print_frame(text):
    print(RED + "*" * 60 + END_COLOR)
    print(RED + "* " + " " * 56 + "*" + END_COLOR)
    for line in text.split("\n"):
        print(RED + "* " + YELLOW + line.center(56) + RED + "*" + END_COLOR)
    print(RED + "* " + " " * 56 + "*" + END_COLOR)
    print(RED + "*" * 60 + END_COLOR)

# Quote
quote = "I'm not a vegetarian because I love animals.\n"
quote += "I'm a vegetarian because I hate plants."

# Animation
def print_quote():
    for i in range(5):
        sys.stdout.write("\r" + " " * 30 + GREEN + "Philosophical Quote of the Day" + END_COLOR)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r" + " " * 30 + YELLOW + "Philosophical Quote of the Day" + END_COLOR)
        sys.stdout.flush()
        time.sleep(0.5)
    print()
    print_frame(quote)

print_quote()