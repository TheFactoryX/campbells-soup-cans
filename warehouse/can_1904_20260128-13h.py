"""
Campbell's Soup Can #1904
Produced: 2026-01-28 13:58:16
Worker: xAI: Grok 4 Fast (x-ai/grok-4-fast)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
PURPLE = '\033[95m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Original Woody Allen-style quote
quote = "I don't fear the void of eternity; I fear it's just an endless line at the deli where they never call your number."

# ASCII art header for fun
header = """
    _____
   /     \\
  |  O O  |  Woody's Wisdom
   \\  ^  /
    |||||
    -----
"""

def print_slow(text, color=PURPLE, delay=0.05):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)
    print()

# Run the program
print(WHITE + header + RESET)
print()
print(YELLOW + "A neurotic musing:" + RESET)
print()
print_slow(quote)
print()
print(PURPLE + "Life: 0, Neuroses: Eternal." + RESET)