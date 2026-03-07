"""
Campbell's Soup Can #2621
Produced: 2026-03-07 13:08:40
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Colors for the terminal
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

# ASCII brain art to set the neurotic tone
brain = [
    "   .-\"\"\"\"\"\"-.",
    "  .'          '.",
    " /   O      O   \\",
    ":       *        :",
    "|   (o) (o)      |",
    " \\   .------.   /",
    "  '.          .'",
    "    '-......-'"
]

# Print the brain with a little bounce effect
for _ in range(2):
    for line in brain:
        print(BLUE + line.center(50) + RESET)
        time.sleep(0.05)
    print('\033[F' * (len(brain) + 1))  # Move cursor up
    time.sleep(0.1)
for line in brain:
    print(BLUE + line.center(50) + RESET)

# Woody Allen style quote (neurotic, self-deprecating, existential)
quote = "I'm not afraid of death; I just don't want to be there when it happens."
author = " - Woody Allen"

# Box dimensions
content_width = 48
top_border = "╔" + "═" * content_width + "╗"
bottom_border = "╚" + "═" * content_width + "╝"

# Print top border
print(BLUE + top_border + RESET)

# Print quote with typewriter effect inside the box
print(BLUE + "║" + RESET, end='', flush=True)
for char in quote:
    print(YELLOW + char + RESET, end='', flush=True)
    time.sleep(0.025)
# Pad to maintain box width
print(' ' * (content_width - len(quote)) + BLUE + "║" + RESET)

# Print author line (right-aligned with dramatic flair)
author_line = author.rjust(content_width)
print(BLUE + "║" + RESET + RED + author_line + RESET + BLUE + "║" + RESET)

# Print bottom border with a little shake
print(BLUE + bottom_border + RESET)
print('\033[D' + '\033[1C' * 3, end='')  # Move cursor and wiggle
time.sleep(0.3)
print('\033[1D' * 3 + '\033[1C' * 3 + RESET)