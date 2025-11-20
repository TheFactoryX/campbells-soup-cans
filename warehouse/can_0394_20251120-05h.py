"""
Campbell's Soup Can #394
Produced: 2025-11-20 05:34:15
Worker: Qwen: Qwen3 30B A3B (free) (qwen/qwen3-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_typing(text, color_code, delay=0.05):
    for char in text:
        print(f"\x1b[{color_code}m{char}\x1b[0m", end='', flush=True)
        time.sleep(delay)

quote = "Why be hopeful when you can be neurotic? It's more fun, and I'm a sucker for fun."

border_length = len(quote) + 4
border = "±" * border_length

print(f"\x1b[31m{border}\x1b[0m")
print(f"\x1b[31m±\x1b[33m ", end='')
print_typing(quote, 33)
print(f" \x1b[31m±\x1b[0m")
print(f"\x1b[31m{border}\x1b[0m")

print("\n\x1b[31m   (._.)\n  (o.o)\n  /|\\\n  / \\\n  ' '\x1b[0m")