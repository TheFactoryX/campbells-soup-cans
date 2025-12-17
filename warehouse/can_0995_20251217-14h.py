"""
Campbell's Soup Can #995
Produced: 2025-12-17 14:42:04
Worker: Nous: Hermes 3 405B Instruct (free) (nousresearch/hermes-3-llama-3.1-405b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time

woody_quote = """
  I don't want to achieve immortality through my work. 
   I want to achieve it through not dying. 
        ~*~ Woody Allen ~*~
"""

for i in range(1, 6):
    print(f"\033[{i}m{woody_quote}\033[0m")
    time.sleep(0.5)

for i in range(6, 1, -1):
    print(f"\033[{i}m{woody_quote}\033[0m")
    time.sleep(0.5)

print(woody_quote)
print("Just kidding. We're all going to die.")