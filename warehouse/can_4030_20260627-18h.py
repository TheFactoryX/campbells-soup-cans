"""
Campbell's Soup Can #4030
Produced: 2026-06-27 18:17:59
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

reset = "\033[0m"
colors = [93, 94, 95, 96]  # Yellow, blue, magenta, cyan

quote = "I used to think life was a pretend reality show. Now I realize I'm just the extra who gets cut."

print(f"\033[97m{'#' * 60}{reset}")
for i, char in enumerate(quote):
    color = colors[i % 4]
    print(f"\033[3{color}m{char}", end='', flush=True)
    time.sleep(0.1)
print(f"\n{'#' * 60}{reset}")