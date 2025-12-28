"""
Campbell's Soup Can #1245
Produced: 2025-12-28 22:35:17
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

s = "I'm not afraid of death; I just don't want to be there when it happens."
n = len(s)
top = "+" + ("-" * (n+2)) + "+"
middle = "| " + s + " |"
print("\033[32m" + top + "\033[0m")
print("\033[32m| \033[36m" + s + "\033[32m |\033[0m")
print("\033[32m" + top + "\033[0m")