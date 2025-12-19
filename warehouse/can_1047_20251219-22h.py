"""
Campbell's Soup Can #1047
Produced: 2025-12-19 22:35:04
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

brain_art = """
       __
     /  \\
    |    \\
    \\    |
     \\  /
      \\/
"""

print(brain_art, end='')

quote = "I don't worry about death, just the RSVP."

border_color = '\033[36m'
title_color = '\033[33m'
text_color = '\033[31m'
reset = '\033[0m'

print(border_color + '+' + '-'*40 + '+' + reset)
title_text = "Woody's Thought".center(40)
print(border_color + '|' + title_color + title_text + reset + border_color + '|')
quote_line = quote.center(40)
print(border_color + '|' + text_color + quote_line + reset + border_color + '|')
print(border_color + '+' + '-'*40 + '+' + reset)
print(f"\n{border_color}- Woody Allen (probably){reset}")