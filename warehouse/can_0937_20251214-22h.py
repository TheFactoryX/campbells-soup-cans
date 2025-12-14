"""
Campbell's Soup Can #937
Produced: 2025-12-14 22:33:04
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

width = 60
border = '+' + '-' * (width - 2) + '+'
content_width = width - 2

border_color = '\033[35m'  # Magenta
bg_color = '\033[44m'     # Dark blue background
reset = '\033[0m'

# Spinner animation
print("Contemplating life's absurdity...", end='')
for _ in range(3):
    print('.', end='', flush=True)
    time.sleep(0.5)
print('\r' + ' ' * 30, end='\r')  # Clear the line

quote = "I'm not neurotic. I'm just acutely aware of my own insignificance. It's a gift!"

top_bottom = f"{border_color}{border}{reset}"

title = "A NEUROTIC REFLECTION"
title_line = (
    f"{border_color}|\033[0m"
    f"{bg_color}\033[33m{title.center(content_width)}\033[0m"
    f"{border_color}|\033[0m"
)

quote_line = (
    f"{border_color}|\033[0m"
    f"{bg_color}\033[36m{quote.center(content_width)}\033[0m"
    f"{border_color}|\033[0m"
)

middle_line = (
    f"{border_color}|\033[0m"
    f"{bg_color}{' ' * content_width}\033[0m"
    f"{border_color}|\033[0m"
)

print(top_bottom)
print(title_line)
print(middle_line)
print(quote_line)
print(middle_line)
print(top_bottom)