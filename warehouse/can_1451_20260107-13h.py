"""
Campbell's Soup Can #1451
Produced: 2026-01-07 13:07:46
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

reset = '\033[0m'
red = '\033[31m'
blue = '\033[34m'
green = '\033[32m'
yellow = '\033[33m'

print(f"\033[1;31m┌──────────────────────────────────────────────┐{reset}")
print(f"\033[1;31m│                                            {reset}")
print(f"\033[1;31m│       ″I don’t fear death; I just           {reset}")
print(f"\033[1;31m│       don’t want to be there when it        {reset}")
print(f"\033[1;31m│       arrives—like a bad punchline to a    {reset}")
print(f"\033[1;31m│       joke nobody laughed at.″             {reset}")
print(f"\033[1;31m│                                            {reset}")
print(f"\033[1;31m└──────────────────────────────────────────────┘{reset}")

quote = "I don’t fear death; I just don’t want to be there when it arrives—like a bad punchline to a joke nobody laughed at."
colors = [blue, green, yellow, red]
for char in quote:
    color = colors.pop(0)
    colors.append(color)
    print(f"\033[{color}m{char}", end='', flush=True)
    time.sleep(0.05)