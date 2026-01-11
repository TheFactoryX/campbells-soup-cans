"""
Campbell's Soup Can #1544
Produced: 2026-01-11 18:45:01
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

quote = "I'm not afraid of death; I just don't want to be there when it happens."
inner_width = len(quote)
top_border = '+' + '-' * inner_width + '+'
bottom_border = top_border

colors = [
    ('\033[91m', '\033[93m'),  # red border, yellow text
    ('\033[92m', '\033[93m'),  # green border, yellow text
    ('\033[93m', '\033[93m'),  # yellow border, yellow text (for contrast)
    ('\033[94m', '\033[93m'),  # blue border, yellow text
    ('\033[95m', '\033[93m'),  # magenta border, yellow text
]

for i in range(5):
    border_color, text_color = colors[i]
    print(border_color + top_border + '\033[0m')
    print(border_color + '|' + text_color + quote + border_color + '|' + '\033[0m')
    print(border_color + bottom_border + '\033[0m')
    print()