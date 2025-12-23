"""
Campbell's Soup Can #1131
Produced: 2025-12-23 18:47:41
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

BORDER_COLOR = '\033[34m'
QUOTE_COLOR = '\033[33m'
WARNING = '\033[93m'
RESET = '\033[0m'

quote = "I'm starting to think my existential crisis is just a midlife panic attack."

thought_art = '''      __
    _/  \_
  ,'     `.
 (         )
  \\  ^  ^  //
   `-----'
'''

symbols = '|/-\\'
for symbol in symbols:
    print(f'\r{symbol}', end='', flush=True)
    time.sleep(0.1)
print('\r', end='', flush=True)

print(f"\n{WARNING}{thought_art}{RESET}")

width = 75
border = BORDER_COLOR + '+' + '-' * width + '+'
middle_line = BORDER_COLOR + '|' + ' ' * width + '|'

top_bottom = f"{border}{RESET}"
middle = f"{middle_line}{RESET}"

padded_quote = quote.center(width)
quote_line = f"{BORDER_COLOR}|{QUOTE_COLOR}{padded_quote}{RESET}{BORDER_COLOR}|{RESET}"

print(top_bottom)
print(middle)
print(quote_line)
print(middle)
print(top_bottom)