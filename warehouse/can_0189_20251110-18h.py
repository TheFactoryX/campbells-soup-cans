"""
Campbell's Soup Can #189
Produced: 2025-11-10 18:43:59
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

def typewriter(text, color, delay=0.05):
    for char in text:
        print(f"\033[{color}m{char}", end='', flush=True)
        time.sleep(delay)
    print()

quote = "I'm not sure if I'm living the dream or if the dream is living me. Probably the latter, since I can't remember applying for the job."

border_length = len(quote) + 4
border = '*' * border_length

print(f"\033[93m{border}")
print(f"\033[93m*  \033[31m", end='')
typewriter(quote, "31")
print(f"\033[93m  *")
print(f"\033[93m{border}")
print("\033[0m")

# Add a spinning cursor animation
print("\033[92m", end='')
for i in range(10):
    for j in ['/', '-', '\\', '|']:
        print(f"\r{j}", end='')
        time.sleep(0.2)
print("\n")