"""
Campbell's Soup Can #2948
Produced: 2026-03-24 19:30:04
Worker: Qwen: Qwen3 Next 80B A3B Thinking (qwen/qwen3-next-80b-a3b-thinking)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

width = 60
quote = "I don't believe in an afterlife, but I brought extra underwear anyway. Just in case they have dry cleaning there."

top_bottom = "+" + "-" * (width - 2) + "+"
middle_space = "|" + " " * (width - 2) + "|"

print(f"\033[34m{top_bottom}\033[0m")
print(f"\033[34m{middle_space}\033[0m")

print("\033[34m|", end='')
for char in quote.center(width - 2):
    if char == ' ':
        print(f"\033[33m{char}\033[0m", end='', flush=True)
    else:
        color = 32 if char in "aeiouAEIOU" else 33
        print(f"\033[{color}m{char}\033[0m", end='', flush=True)
    time.sleep(0.05)
print("\033[34m|\033[0m")

print(f"\033[34m{middle_space}\033[0m")
print(f"\033[34m{top_bottom}\033[0m")