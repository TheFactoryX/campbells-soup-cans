"""
Campbell's Soup Can #1656
Produced: 2026-01-16 23:32:21
Worker: xAI: Grok Code Fast 1 (x-ai/grok-code-fast-1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI escape codes for colors
colors = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]

reset = "\033[0m"

# Woody Allen-style quote (neurotic, funny, self-deprecating)
quote = "I understand the universe is infinite, but why does my parking space at the deli always seem to be taken?"

# ASCII art frame (simple box)
frame_top = "╔═══════════════════════════════════════════════════════╗"
frame_side = "║"
frame_bottom = "╚═══════════════════════════════════════════════════════╝"

# Animation: Print the frame and fill it with the quote letter by letter, in random colors
print(frame_top)
print(frame_side + " " * (len(frame_top) - 2) + frame_side)

# Build the quote line with animation
quote_line = frame_side + " " * ((len(frame_top) - len(quote) - 2) // 2) + quote + " " * ((len(frame_top) - len(quote) - 2) // 2) + frame_side
accumulated = frame_side + " " * ((len(frame_top) - len(quote) - 2) // 2)

for char in quote:
    color = random.choice(colors)
    accumulated += color + char + reset
    print("\r" + accumulated + " " * ((len(frame_top) - len(accumulated) + len(reset)*len(quote)) - 2) + frame_side, end="")
    time.sleep(0.1)  # Delay for animation effect

print()  # New line after animation
print(frame_side + " " * (len(frame_top) - 2) + frame_side)
print(frame_bottom)