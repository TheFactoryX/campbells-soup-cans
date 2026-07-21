"""
Campbell's Soup Can #4280
Produced: 2026-07-21 16:41:19
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def print_animated(text, color):
    print(f"{color}", end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print(RESET)

print(f"{GREEN}*************************************************\n*** Woody Allen's Philosophical Musings ***\n*************************************************{RESET}")
print()
time.sleep(1)
quote = "I spent so much time worrying about what to write, I forgot to write anything at all. That's a pretty neat trick."
print_animated(quote, YELLOW)
print()
print(f"{GREEN}  /|\\\\{RESET}")
print(f"{GREEN} ( o o ){RESET}")
print(f"{GREEN}  ) ( {RESET}")