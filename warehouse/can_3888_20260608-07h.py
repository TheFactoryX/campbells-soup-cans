"""
Campbell's Soup Can #3888
Produced: 2026-06-08 07:03:30
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

def type_writer(text, color, delay=0.03):
    for char in text:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print(reset)

# Woody Allen style existentially anxious quote
quote = [
    "I don't fear death, but I do fear missing",
    "the next Marvel movie. So I'll binge-watch",
    "them all, which is practically the same thing.",
    "Also, I checked twice—my calendar is completely",
    "free for eternity. It's a relief, really."
]

width = 60
border_line = f"{green}═{reset}" * (width - 2)

# Decorative top
time.sleep(0.5)
print(f"{cyan}~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/{reset}")
time.sleep(0.5)
type_writer("~        WOODY ALLEN'S GUIDE TO IMMORTALITY        ~", cyan)
time.sleep(0.5)
print(f"{cyan}~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/~/{reset}")
time.sleep(1)

# Animated box with quote
print(f"{green}╔{border_line}╗{reset}")
for _ in range(2):
    print(f"{green}║{reset}" + " " * (width - 2) + f"{green}║{reset}")

for line in quote:
    padded = line.center(width - 4)
    print(f"{green}║{reset}{yellow} {padded} {green}║{reset}")

for _ in range(2):
    print(f"{green}║{reset}" + " " * (width - 2) + f"{green}║{reset}")
print(f"{green}╚{border_line}╝{reset}")

# Signature touch
time.sleep(0.5)
print(f"\n{red}*sighs audibly*{reset}")
time.sleep(0.5)
print(f"{cyan}             (Probably while eating a bagel){reset}")