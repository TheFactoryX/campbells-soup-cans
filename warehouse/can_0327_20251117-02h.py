"""
Campbell's Soup Can #327
Produced: 2025-11-17 02:17:07
Worker: Qwen: Qwen3 14B (free) (qwen/qwen3-14b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# Define quote and colors
quote = "The most terrifying thing about existence is that it's a profound mystery, yet I'm convinced I'll solve it by tomorrow."
quote_colors = [
    "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m",  # Red, Green, Yellow, Blue, Magenta, Cyan
    "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"   # Bright versions
]
border_color = "\033[46m"  # Cyan background
reset = "\033[0m"
blink = "\033[5m"  # Blink effect for final line

# Create border with dynamic length
border_length = len(quote) + 4
border = border_color + '*' * border_length + reset

# Title with spacing and color
title = f"\033[35m{' ' * 20} Woody Allen's Existential Watch{' ' * 20}{reset}\n"

# Print title
print(title)

# Print the border
print(border)
time.sleep(0.5)

# Typing effect with color cycling for the quote
print(f"{border_color}*{reset} ", end='')
current_color = 0
for char in quote:
    color = quote_colors[current_color % len(quote_colors)]
    print(f"{color}{char}{reset}", end='', flush=True)
    current_color += 1
    time.sleep(0.03)
print(f"{border_color}*{reset}")
print(border)

# Final comment with blinking text
final_comment = f"{blink}\033[31m{' ' * 20} But what if tomorrow is just another day? Fear not — I'm ready.{reset}"
print(final_comment)