"""
Campbell's Soup Can #1106
Produced: 2025-12-22 15:35:13
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not existential, I just have a really bad case of déjà vu with the meaning of life."

border_color = "\033[31m"  # red
text_color = "\033[33m"    # yellow
reset = "\033[0m"

pad = 4
text_length = len(quote)
box_width = text_length + pad * 2 + 2  # total width

# Animation
print("Thinking", end='', flush=True)
for _ in range(3):
    print('.', end='', flush=True)
    time.sleep(0.5)
print('\b'*3 + '!!!', end='\n', flush=True)

# Now the box
print(border_color + "+" + "-"*(box_width - 2) + "+" + reset)

print(border_color + "|" + " "*(box_width - 2) + "|" + reset)

text_part = " " * pad + quote + " " * pad
text_part = text_part.center(box_width - 2)
print(f"{border_color}|{text_color}{text_part}{reset}{border_color}|{reset}")

print(border_color + "+" + "-"*(box_width - 2) + "+" + reset)