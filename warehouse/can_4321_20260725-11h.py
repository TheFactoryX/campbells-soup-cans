"""
Campbell's Soup Can #4321
Produced: 2026-07-25 11:34:35
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def print_colored(text, delay=0.02):
    colors = [31, 33, 32, 36, 34, 35]  # Red, Yellow, Green, Cyan, Blue, Magenta
    for char in text:
        color = random.choice(colors)
        print(f"\033[{color}m{char}\033[0m", end='', flush=True)
        time.sleep(delay)

# Woody Allen-style existential quote
quote = """I've spent so much time worrying about the future
that I've probably already lived it and died in it twice,
which would explain why my anxiety feels so retroactively futuristic."""

lines = [line.strip() for line in quote.strip().split('\n')]
max_length = max(len(line) for line in lines)
border = '+' + '-' * (max_length + 2) + '+'

# Print box with animated text
print(f"\033[1;35m{border}\033[0m")  # Bold magenta top border

for line in lines:
    print("\033[1;35m|\033[0m", end='')  # Left border
    print_colored(line.ljust(max_length), delay=0.015)  # Colorful animated text
    print("\033[1;35m|\033[0m")  # Right border with new line

print(f"\033[1;35m{border}\033[0m")  # Bold magenta bottom border