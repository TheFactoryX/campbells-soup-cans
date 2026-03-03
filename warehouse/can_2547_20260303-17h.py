"""
Campbell's Soup Can #2547
Produced: 2026-03-03 17:06:35
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

quote = "I don't know what I'm doing with my life, but I'm sure I'm doing it wrong."

width = 80
x_center = (width - len(quote)) // 2
y_center = 10

# Print the box
top_line = "+" + "-" * (len(quote) + 2) + "+"
middle_line = "|" + " " * len(quote) + "|"
bottom_line = top_line

sys.stdout.write(f"\033[{y_center - 1};{x_center}H{top_line}")
sys.stdout.flush()
sys.stdout.write(f"\033[{y_center};{x_center}H{middle_line}")
sys.stdout.flush()
sys.stdout.write(f"\033[{y_center + 1};{x_center}H{bottom_line}")
sys.stdout.flush()

# Print the quote with color animation
for i, char in enumerate(quote):
    color_code = (i % 6) + 31
    sys.stdout.write(f"\033[{color_code}m{char}")
    sys.stdout.flush()
    time.sleep(0.1)

sys.stdout.write("\033[0m")
sys.stdout.flush()

# Bouncing ball animation
x_ball = 78
y_ball = 23
direction = 1

for _ in range(50):
    sys.stdout.write(f"\033[{y_ball};{x_ball}H ")
    sys.stdout.flush()
    y_ball += direction
    if y_ball >= 25 or y_ball <= 23:
        direction *= -1
    sys.stdout.write(f"\033[{y_ball};{x_ball}Ho")
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(1)