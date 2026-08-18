"""
Campbell's Soup Can #4680
Produced: 2026-08-18 18:56:34
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

red = '\033[91m'
green = '\033[92m'
reset = '\033[0m'

quote = f"{red}Why do I exist?{reset} {green}To make you question...{reset} even your shadow."

while True:
    print(f"{red}+{'-'*50}+{reset}")
    print(f"{green}|{' ' * 48}|{reset}")
    print(f"{red}|  {quote}  {reset}|")
    print(f"{green}|{' ' * 48}|{reset}")
    print(f"{red}+{'-'*50}+{reset}")
    time.sleep(1)
    red, green = green, red