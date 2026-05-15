"""
Campbell's Soup Can #3680
Produced: 2026-05-15 04:18:03
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

quote = "I'm not a complete idiot; I just have a few missing pieces."
inner_width = 57centered_quote = quote.center(inner_width)

print(RED + '+' + '-' * inner_width + '+' + RESET)
print(GREEN + '|' + RESET + YELLOW + centered_quote + RESET + GREEN + '|' + RESET)
print(RED + '+' + '-' * inner_width + '+' + RESET)