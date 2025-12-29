"""
Campbell's Soup Can #1266
Produced: 2025-12-29 22:35:05
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

art = """
   O
  /|\\
 / | \\\
/  |  \\
"""

title = "Woody's Existential Crisis:"
separator = "-" * 30
quote = "I'm starting to think that maybe the universe is just a simulation run by a very bored and slightly sadistic AI."

print(f"\033[32m{art}\033[0m", end='')
print(f"\033[34m{title}\033[0m")
print(f"\033[31m{separator}\033[0m")

border_length = len(quote) + 4
top_bottom_border = "=" * border_length

print(f"\033[31m{top_bottom_border}\033[0m")

color = "\033[33m"
reset = "\033[0m"
print(color, end='')
for char in quote:
    print(char, end='', flush=True)
    time.sleep(0.03)
print(reset)

print(f"\033[31m{top_bottom_border}\033[0m")