"""
Campbell's Soup Can #3942
Produced: 2026-06-15 21:21:18
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

quote = "I'm not afraid of death; I just don't want to be there when it happens."
lines = [
    "I'm not afraid of death; I just don't want to",
    "be there when it happens."
]

inner_width = 75
top_border = '+' + '-' * inner_width + '+'
bottom_border = '+' + '-' * inner_width + '+'

print(GREEN + top_border + RESET)
for line in lines:
    print(YELLOW + '| ' + line + ' |' + RESET)
print(GREEN + bottom_border + RESET)