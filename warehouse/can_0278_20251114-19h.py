"""
Campbell's Soup Can #278
Produced: 2025-11-14 19:26:38
Worker: DeepSeek: R1 Distill Llama 70B (free) (deepseek/deepseek-r1-distill-llama-70b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Woody Allen-style quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

# Colors using ANSI escape codes
class Color:
    RESET = '\033[0m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'

def typing_effect(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_quotation():
    # Create a fancy border
    border = Color.MAGENTA + '*' * 80 + Color.RESET
    centered_quote = Color.YELLOW + QUOTE.center(78) + Color.RESET
    author = Color.WHITE + "— Woody Allen (inspired)".center(78)
    
    print(border)
    print(Color.MAGENTA + '*' + Color.RESET)
    typing_effect(centered_quote, speed=0.02)
    print(Color.MAGENTA + '*' + Color.RESET)
    print(author)
    print(border)

print_quotation()