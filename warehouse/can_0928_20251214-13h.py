"""
Campbell's Soup Can #928
Produced: 2025-12-14 13:38:14
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

frame_top = r'''
  __/\__/\__/\__/\__/\__/\__/\__
 / \                           / \
''' 

frame_btm = r'''
 \_/                           \_/ 
  ‾\/‾\/‾\/‾\/‾\/‾\/‾\/‾\/‾\/‾  
'''

quote = "I wouldn't say I'm afraid of the eternal void - just\nterrified it might be like one of those Brooklyn apartments\nwhere the previous tenant's existential dread never\nfully airs out."
author = "- Woody Allen's Neurotic Cousin"

print(MAGENTA)
typewriter(frame_top)
print(YELLOW)
typewriter(f"   {quote}")
print(CYAN)
typewriter(f"{' ' * 25}{author}")
print(MAGENTA)
typewriter(frame_btm)
print(RESET)