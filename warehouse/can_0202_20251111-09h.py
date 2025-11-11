"""
Campbell's Soup Can #202
Produced: 2025-11-11 09:34:25
Worker: Mistral: Mixtral 8x22B Instruct (mistralai/mixtral-8x22b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def print_fading_text(text, color_code):
    for i in range(10, 0, -1):
        sys.stdout.write(f"\033[1;{color_code}m{text * i}\033[0m\r")
        sys.stdout.flush()
        time.sleep(0.1)

def print_woody_quote():
    quote = "I'm not afraid of dying. I just don't want to be there when it happens. \nIt's like going to a party you didn't plan on attending, and you're not even sure if there's going to be any good snacks."
    color_codes = [31, 32, 33, 34, 35, 36]
    random.shuffle(color_codes)

    print("\033[1;33m" + "=" * 50 + "\033[0m")
    print("\033[1;34m" + " " * 10 + "WOODY ALLEN'S WISDOM" + " " * 10 + "\033[0m")
    print("\033[1;33m" + "=" * 50 + "\033[0m")

    for line in quote.split('\n'):
        print_fading_text(line, random.choice(color_codes))
        print()

    print("\033[1;33m" + "=" * 50 + "\033[0m")
    print("\033[1;34m" + " " * 10 + "ENJOY THE SHOW" + " " * 10 + "\033[0m")
    print("\033[1;33m" + "=" * 50 + "\033[0m")

if __name__ == "__main__":
    print_woody_quote()