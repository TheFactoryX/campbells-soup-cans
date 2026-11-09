"""
Campbell's Soup Can #5225
Produced: 2026-11-09 17:29:53
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

# A wonderfully neurotic Woody Allen-esque quote
quote_lines = [
    "I'm not afraid of",
    "dying; I just don't want to be",
    "alive when it happens.",
]

max_len = max(len(line) for line in quote_lines)
inner_width = max_len + 2  # one space padding each side

top = "+" + "-" * inner_width + "+"
bottom = "+" + "-" * inner_width + "+"

# Cyan border
print(f"\033[36m{top}\033[0m")

for i, line in enumerate(quote_lines):
    # Alternate yellow and white for a quirky feel
    color = "\033[33m" if i % 2 == 0 else "\033[37m"
    padded = line.center(inner_width)
    colored_padded = f"{color}{padded}\033[0m"
    print(f"|{colored_padded}|")

print(f"\033[36m{bottom}\033[0m")

# A little neurotic sign-off
print("\033[35m*...sigh...*\033[0m")