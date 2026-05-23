"""
Campbell's Soup Can #3767
Produced: 2026-05-23 23:11:29
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

def type_out(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the text

def main():
    # Original Woody Allen‑style quote
    quote = "\"I spend my life trying to avoid awkward silences, yet somehow I end up talking to my plants.\""

    # ANSI colour codes
    RED   = '\033[31m'
    GREEN = '\033[32m'
    YELLOW= '\033[33m'
    BLUE  = '\033[34m'
    MAGENTA= '\033[35m'
    CYAN  = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

    # Create a simple box around the quote
    width = len(quote) + 4
    top    = '+' + '-' * width + '+'
    middle = '| ' + quote + ' |'
    bottom = '+' + '-' * width + '+'

    # Print each line with a typing effect and rotating colours
    for line, colour in zip([top, middle, bottom], itertools.cycle(colors)):
        sys.stdout.write(colour)
        type_out(line, 0.05)
        sys.stdout.write(RESET)
        time.sleep(0.2)

    # A tiny blinking emoticon for extra flair
    for _ in range(3):
        sys.stdout.write('\r' + YELLOW + ' (•̀ᴗ•́)و  ' + RESET)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + YELLOW + ' (•́ᴗ•̀)و  ' + RESET)
        sys.stdout.flush()
        time.sleep(0.5)

    print()  # final newline

if __name__ == '__main__':
    main()