"""
Campbell's Soup Can #4662
Produced: 2026-08-17 23:36:12
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

quote_lines = [
    "I don't want to be remembered for my work.",
    "I want to be remembered for not dying.",
    "But I'm bad at dying, so I'll just keep living."
]

top_border = YELLOW + "+" + "-" * 48 + "+" + RESET
bottom_border = top_border

print(top_border)
for line in quote_lines:
    padded_line = line.ljust(48)
    print(RED + "|" + padded_line + "|" + RESET)
print(bottom_border)