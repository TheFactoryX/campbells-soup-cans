"""
Campbell's Soup Can #1157
Produced: 2025-12-24 22:35:00
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

quote = "I'm an existentialist. Or maybe just someone who's really bad at hiding from himself."

# ASCII art brain
brain_art = '''\
  _______
 |       |
 |  o   o|
 |       |
  --------
'''

print('\033[32m' + brain_art + '\033[0m')  # green color

title = "Woody Allen's Existential Musings:"
print('\033[32m' + title + '\033[0m')  

text = quote
text_length = len(text)
pad = 2
total_width = text_length + pad *2 + 2

border_color = '\033[33m'
reset = '\033[0m'

border = border_color + '+' + '-' * total_width + '+' + reset

content_bg = '\033[44m'
content_fg = '\033[37m'
content = content_bg + content_fg + '|' + text.center(total_width - 2) + '|' + reset

print(border)
print(content)
print(border)