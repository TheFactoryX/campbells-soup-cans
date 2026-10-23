"""
Campbell's Soup Can #5152
Produced: 2026-10-23 10:04:23
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap

quote = "I'm not worried about the meaning of life; I'm just worried about the meaning of the meaning of life, and whether I left the oven on."

wrapper = textwrap.wrap(quote, width=50)
max_len = max(len(line) for line in wrapper) + 4
border = '+' + '-' * max_len + '+'

print("\033[1;33m")
print("   ) (")
print("  (   )")
print(" (     )")
print(" (     )")
print("  )   (")
print("   ) (")
print("    )")
print()
print(border)
for line in wrapper:
    print("| " + line + " |")
print(border)
print("\033[0m")
print("\033[1;34m  -- Woody Allen-ish")
print("\033[0m")