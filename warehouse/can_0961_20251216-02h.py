"""
Campbell's Soup Can #961
Produced: 2025-12-16 02:24:46
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

quote = "Why do I exist? To wonder why I exist. And then worry I'll forget the answer."

# Header
print("\033[36m" + "="*40 + "\033[0m")
print("\033[36m" + "  Woody's Existential Dread Generator  " + "\033[0m")
print("\033[36m" + "="*40 + "\033[0m")
print()

# Quote with typing effect in yellow
sys.stdout.write("\033[33m")  # yellow
for c in quote:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
sys.stdout.write("\033[0m\n")
time.sleep(1)  # pause after quote

# ASCII art in red
print("\033[31m")
print("         _.-'`-._")
print("       /_/-._.-'_.-")
print("      /_/-._.-'_.-")
print("     /_/-._.-'_.-")
print("    /_/-._.-'_.-")
print("   /_/-._.-'_.-")
print("  /_/-._.-'_.-")
print(" /_/-._.-'_.-")
print("/____/-._.-'_.-")
print("  `-._.-'_.-")
print("    `-._.-'")
print("      `-._.-'")
print("        `-._.-'")
print("\033[0m")