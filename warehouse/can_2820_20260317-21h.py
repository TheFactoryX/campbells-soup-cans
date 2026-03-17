"""
Campbell's Soup Can #2820
Produced: 2026-03-17 21:53:55
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import random
import time

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
quote = "I'm not neurotic, I'm just deeply in love with my own anxieties."

print("\033[36m")
print("┌──────────────────────────────────────────────┐")
print("│                                            │")
print(f"│ {quote}           │")
print("│                                            │")
print("└──────────────────────────────────────────────┘")
print("\033[0m")

for color in colors:
    print(f"\033[{color}m{quote}\033[0m")
    time.sleep(0.2)