"""
Campbell's Soup Can #2239
Produced: 2026-02-15 11:36:24
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

quote = "I don't know if I'm a person. Or a good person. Or if I'll be remembered."

# ANSI color codes for rainbow effect
colors = [31, 32, 34, 35, 36, 33]  # red, green, blue, magenta, cyan, yellow

# Precompute the box dimensions
box_width = len(quote) + 4
top_bottom = '+' + '-' * (box_width - 2) + '+'
middle = '|' + ' ' * (box_width - 2) + '|'

# Clear screen (works in many terminals)
print("\033[2J", end="")

# Draw the box once with the first color to establish the frame
print(f"\033[31m{top_bottom}\033[0m")
for _ in range(4):
    print(f"\033[31m{middle}\033[0m")
print(f"\033[31m{top_bottom}\033[0m")

# Position cursor for quote inside box
sys.stdout.write(f"\033[{6};{3}H")
sys.stdout.flush()

# Animate quote with rainbow colors
for _ in range(10):
    for color in colors:
        # Clear current quote position
        sys.stdout.write("\033[1K\033[1A")
        # Print new colored quote
        sys.stdout.write(f"\033[{color}m{quote}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
    # Bounce effect: slightly move down then up
    sys.stdout.write("\033[1B")
    time.sleep(0.05)
    sys.stdout.write("\033[1A")
    time.sleep(0.05)

# Final state: quote in green with decorative border
print("\033[2J", end="")
print(f"\033[32m{top_bottom}\033[0m")
for _ in range(4):
    print(f"\033[32m{middle}\033[0m")
print(f"\033[32m{top_bottom}\033[0m")
sys.stdout.write(f"\033[6;3H\033[32m{quote}\033[0m")
sys.stdout.write("\033[0m")
sys.stdout.flush()
time.sleep(1)  # Give user time to see the result