"""
Campbell's Soup Can #2954
Produced: 2026-03-25 05:38:48
Worker: Sao10K: Llama 3.3 Euryale 70B (sao10k/l3.3-euryale-70b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_quote(quote, color_code):
    for char in quote:
        sys.stdout.write("\033[" + color_code + "m" + char)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\033[0m\n")

def animate_quote(quote):
    color_codes = ["31", "32", "33", "34", "35", "36", "37"]
    for color_code in color_codes:
        print_quote(quote, color_code)
        time.sleep(0.5)

def main():
    quote = "Life is shorter than you think, but longer than you can tolerate."
    animate_quote(quote)

if __name__ == "__main__":
    main()