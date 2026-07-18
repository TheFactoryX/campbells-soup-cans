"""
Campbell's Soup Can #4247
Produced: 2026-07-18 19:31:40
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

YELLOW = '\033[93m'
RESET = '\033[0m'
quote = "I'm not afraid of death; I just don't want to be there when it happens."
width = 68
top_border = '+' + '=' * width + '+'
content = quote.center(width)
middle = '|' + content + '|'

print(YELLOW + top_border + RESET)
print(YELLOW + middle + RESET)
print(YELLOW + top_border + RESET)
print(YELLOW + "  (heh)  " + RESET)