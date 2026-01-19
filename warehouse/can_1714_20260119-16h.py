"""
Campbell's Soup Can #1714
Produced: 2026-01-19 16:48:25
Worker: Qwen: Qwen2.5-VL 7B Instruct (free) (qwen/qwen-2.5-vl-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote_with_ascii(quote):
    print("\033[31m" + "+___________________+")
    print("\033[32m" + "|                   |")
    print("\033[33m" + "|   α_d.meta!       |")
    print("\033[34m" + "|                     |")
    print("\033[35m" + "|                     |")
    print("\033[36m" + "|                     |")
    print("\033[37m" + "|                     |")
    print("\033[31m" + "|                   |")
    print("\033[32m" + "|                     |")
    print("\033[33m" + "|                  β  |")
    print("\033[34m" + "+___________________+" + "\n")
    print("\033[1m\033[37m" + quote + "\033[0m")
    time.sleep(3.5)
    print("\033[31m" + "+___________________+")
    print("\033[32m" + "|       .ng_stop.py       |")
    print("\033[33m" + "|_________________________|")
    print("\033[0m")

quote = "A man is not old until regrets take the place of opportunities."
print_quote_with_ascii(quote)