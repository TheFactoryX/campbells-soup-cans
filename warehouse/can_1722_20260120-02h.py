"""
Campbell's Soup Can #1722
Produced: 2026-01-20 02:29:49
Worker: TNG: R1T Chimera (free) (tngtech/tng-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Woody Allen-esque quote
quote = [
    ("I'm convinced the universe is just a cosmic pratfall - ", 33),
    ("we're all \033[1;31mslipping on existence\033[0m", 33),
    ("while desperately trying to ", 33),
    ("pretend we meant to do that.", 33)
]

# ASCII art border
border_top = color_text(r'''
  _________________________________________________________
 /                                                        \
''', 36)

border_bottom = color_text(r''' \_________________________________________________________/
    \                                                   /
     \                                                 /
      \                                               /
       \                  \033[3m...and yet we keep getting up\033[0m                  /
''', 36)

# Print everything with effects
print(border_top)
for text, color in quote:
    slow_print(color_text(text, color), delay=0.02)
time.sleep(0.5)
print(border_bottom)
time.sleep(0.3)
slow_print(color_text("\n          (\033[3mneurotic sigh\033[0m)", 90), delay=0.05)