"""
Campbell's Soup Can #624
Produced: 2025-11-30 14:31:51
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import os

os.system('clear')

def rainbow_text(text, delays):
    colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m']
    for i, char in enumerate(text):
        print(f"{colors[i % 5]}{char}", end='', flush=True)
        time.sleep(delays[i % len(delays)])
    print('\033[0m')

def typewriter(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print('\033[36m', end='')
print(r'''   ___                     
  / _ \__ _ _ __ ___  ___ 
 / /_)/ _` | '__/ __|/ _ \
/ ___/ (_| | |  \__ \  __/
\/    \__,_|_|  |___/\___|''')
print('\033[0m')

time.sleep(0.5)

rainbow_text(" ✨ ✨ ✨ ✨ ✨", [0.1, 0.2, 0.1, 0.2, 0.1])
print()
time.sleep(0.3)

quote = [
    "\033[34m╔═══════════════════════════════════════════════════╗\033[0m",
    "\033[34m║ \033[3m\"I'm convinced the universe is fundamentally flawed, ║",
    "\033[34m║  but I can't decide if it's an design error         ║",
    "\033[34m║  or just poor maintenance.\"\033[23m                     \033[94m-\033[93m Woody Allen's Coffee Cup \033[34m║",
    "\033[34m╚═══════════════════════════════════════════════════╝\033[0m"
]

for line in quote:
    typewriter(line, 0.02)
    time.sleep(0.2)

print("\n\n")
time.sleep(0.5)
rainbow_text(" (̶◉͛‿◉̶)", [0.2, 0.1])