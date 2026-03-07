"""
Campbell's Soup Can #2630
Produced: 2026-03-07 21:34:07
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Define ANSI escape codes for colors
colors = [
    "\033[31m",  # Red
    "\033[33m",  # Yellow
    "\033[32m",  # Green
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
]

# Woody Allen style quote (original creation)
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."

# Set up box dimensions (50 characters wide)
width = 50
top_border = '*' * width
bottom_border = '*' * width
centered_quote = quote.center(width)

# ANSI escape for reset color
reset = "\033[0m"

# Initial print with blue border
print(f"{colors[3]}{top_border}{reset}")
print(f"{colors[2]}{centered_quote}{reset}")
print(f"{colors[3]}{bottom_border}{reset}")

# Animation: Flicker the border with colors for 1 second
for i in range(10):
    color_code = colors[i % len(colors)]
    # Move to top border and reprint
    print(f"\033[1;1H{color_code}{top_border}{reset}", end='')
    # Move to bottom border and reprint
    print(f"\033[3;1H{color_code}{bottom_border}{reset}", end='')
    time.sleep(0.1)

# Final reset for clean terminal
print(reset)