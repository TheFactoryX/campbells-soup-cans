"""
Campbell's Soup Can #2558
Produced: 2026-03-04 07:07:07
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

quote = "I'm not afraid of death. I just don't want to be there when it happens. But mostly, I'm afraid of being alive."
colored_quote = quote.replace("afraid", RED + "afraid" + END).replace("alive", GREEN + "alive" + END)

box_width = len(quote) + 2
top_border = '*' * box_width
print(top_border)
print('*' + colored_quote + '*')
print(top_border)