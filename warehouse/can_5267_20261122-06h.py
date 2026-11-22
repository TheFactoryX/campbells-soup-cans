"""
Campbell's Soup Can #5267
Produced: 2026-11-22 06:49:35
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

quote = "I'm not afraid of death; I just don't want to be there when it happens."

inner = " " + quote + " "
width = len(inner)
top = "+" + "-" * width + "+"
mid = "|" + inner + "|"
bottom = "+" + "-" * width + "+"

print("\033[1;31m" + top + "\033[0m")
print("\033[44m\033[1;33m" + mid + "\033[0m")
print("\033[1;31m" + bottom + "\033[0m")