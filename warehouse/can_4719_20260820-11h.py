"""
Campbell's Soup Can #4719
Produced: 2026-08-20 11:42:28
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def typewriterprint(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def makebox(quote):
    q_len = len(quote)
    border_length = q_len + 4
    top = f"\033[36m+{('-' * border_length)}+\033[0m\n"
    middle = f"\033[36m|\033[37m \"{quote}\" \033[36m|\033[0m\n"
    bottom = f"\033[36m+{('-' * border_length)}+\033[0m"
    return f"{top}{middle}{bottom}"

quote = "I'm not scared of death, but I really hate getting old. At least you won't have to worry about me being dead again next week."
box = makebox(quote)

typewriterprint(box)