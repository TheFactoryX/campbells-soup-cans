"""
Campbell's Soup Can #473
Produced: 2025-11-23 17:29:34
Worker: xAI: Grok 4.1 Fast (free) (x-ai/grok-4.1-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_PURPLE = '\033[95m'
    BRIGHT_CYAN = '\033[96m'

colors = Colors()
width = 85

# Fancy borders
top = colors.BRIGHT_BLUE + '╔' + '═' * (width - 2) + '╗' + colors.RESET
side = colors.BRIGHT_BLUE + '║' + colors.RESET
bottom = colors.BRIGHT_BLUE + '╚' + '═' * (width - 2) + '╝' + colors.RESET
empty_line = side + ' ' * (width - 2) + colors.BRIGHT_BLUE + '║' + colors.RESET

quote = "I'm not afraid of death; I'm afraid of being the punchline in God's cosmic joke."

# Neurotic Woody ASCII art
woody_art = [
    colors.BRIGHT_YELLOW + "     .-\"\"\"\"\"\"-.     ",
    "    /          \\    ",
    colors.BRIGHT_PURPLE + "   |  O    O   |   ",
    "    \\    --    /    ",
    "     '-.  .-.'     ",
    colors.BRIGHT_YELLOW + "       ''\"\"\"\"       " + colors.RESET
]

print('\n' * 2)
for line in woody_art:
    print('  ' + line.center(width))
print()

# Title
print(colors.BRIGHT_RED + colors.BOLD + "WOODY ALLEN'S NEUROTIC PHILOSOPHY".center(width) + colors.RESET)
print()

# Loading spinner
print("Loading existential dread".center(width))
spinner_chars = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
for _ in range(30):
    for char in spinner_chars:
        sys.stdout.write('\r' + colors.BRIGHT_GREEN + colors.BOLD + char + colors.RESET + ' ' * 10)
        sys.stdout.flush()
        time.sleep(0.08)
print('\r' + ' ' * width + '\n')

# Box top
print(top)
print(empty_line)

# Quote typing line
sys.stdout.write(side)
sys.stdout.flush()

# Rainbow typing effect
rainbow_colors = [colors.BRIGHT_YELLOW, colors.BRIGHT_PURPLE, colors.BRIGHT_CYAN, colors.BRIGHT_GREEN, colors.BRIGHT_RED, colors.BRIGHT_BLUE]
for i, char in enumerate(quote):
    color = rainbow_colors[i % len(rainbow_colors)]
    sys.stdout.write(color + colors.BOLD + char + colors.RESET)
    sys.stdout.flush()
    time.sleep(0.06)

# Pad to end of line
pad_length = width - 2 - len(quote)
sys.stdout.write(' ' * pad_length)
sys.stdout.write(colors.BRIGHT_BLUE + '║' + colors.RESET + '\n')
sys.stdout.flush()

# Empty line below
print(empty_line)
print(bottom)

print('\n' * 2)
print(colors.BRIGHT_PURPLE + colors.ITALIC + "(A custom Woody Allen-style musing)" + colors.RESET)