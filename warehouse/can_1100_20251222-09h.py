"""
Campbell's Soup Can #1100
Produced: 2025-12-22 09:42:55
Worker: AllenAI: Olmo 3.1 32B Think (free) (allenai/olmo-3.1-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = "I'm not afraid; I just don't want to be there when it's my turn."

# Thinking animation
print("Thinking...", end='', flush=True)
for _ in range(3):
    print('.', end='', flush=True)
    time.sleep(0.5)
print("\n" + "-"*30 + "\n")

# Box setup
width = 68
inner_width = width - 2
border = '+' + '-'*(width-2) + '+'

# ANSI colors
red = "\033[31m"
blue = "\033[34m"
yellow_blink = "\033[5;33m"  # Blinking yellow
reset = "\033[0m"

# Top and bottom borders
top_bottom = red + border + reset

# Side lines
side_line = blue + '|' + ' ' * inner_width + '|' + reset

# Quote line with blinking text
quote_line_parts = [
    blue, '|',
    yellow_blink, ' ', quote, ' ',
    blue, '|',
    reset
]
quote_line = ''.join(quote_line_parts)

# Display
print(top_bottom)
print(side_line)
print(quote_line)
print(side_line)
print(top_bottom)