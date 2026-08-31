"""
Campbell's Soup Can #4875
Produced: 2026-08-31 05:36:20
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

quote = "I'm not afraid of death; I just don't want to be there when it happens."

top_border = GREEN + "+" + ("-" * 71) + "+" + RESET
bottom_border = top_border

print(top_border)
print(GREEN + "|" + RED + quote + RESET + GREEN + "|" + RESET)
print(bottom_border)