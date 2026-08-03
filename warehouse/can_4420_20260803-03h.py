"""
Campbell's Soup Can #4420
Produced: 2026-08-03 03:56:16
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

quote = "I don't want to die, but I'm not sure I want to live either. And I'm afraid of the dark, which is the absence of light, which is the absence of everything. And I'm also afraid of being forgotten. But mostly, I'm afraid of the fact that I'm going to die."

inner_width = 80
centered_quote = quote.center(inner_width)

top = RED + '+' + '-' * inner_width + '+' + RESET
middle = '|' + YELLOW + centered_quote + RESET + '|'
bottom = top

print(top)
print(middle)
print(bottom)