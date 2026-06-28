"""
Campbell's Soup Can #4036
Produced: 2026-06-28 11:16:05
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

quote_lines = [
    "I'm not afraid of death. I just don't want to live.",
    "And I'm afraid of the dark, so I'll die in it.",
    "That's the worst of both worlds."
]

top_border = GREEN + "+" + "-" * 48 + "+" + RESET
bottom_border = top_border

print(top_border)
for line in quote_lines:
    centered = line.center(48)
    print(GREEN + "|" + YELLOW + centered + RESET + "|")
print(bottom_border)