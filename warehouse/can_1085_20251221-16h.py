"""
Campbell's Soup Can #1085
Produced: 2025-12-21 16:38:26
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not afraid of death; I just don't want to be there when it happens... again."

# Top sparkles
print("\033[36m", end="")
print("*" * 20)
print("\033[0m")

# Header in blue
print("\033[34m", end="")
print(" " * 10 + "=== Woody's Wisdom ===")
print(" " * 10 + "---------------------")
print("\033[0m", end="")

# Typing effect in green
print("\033[32m", end="")
for c in quote:
    print(c, end="", flush=True)
    time.sleep(0.03)
print("\033[0m")