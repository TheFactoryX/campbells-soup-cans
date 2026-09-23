"""
Campbell's Soup Can #5009
Produced: 2026-09-23 00:34:09
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# Woody Allen inspired quote parts with colors
parts = [
    ("I wanted to live forever, ", '\u001b[36m'),   # Cyan
    ("but that's a bit of a problem", '\u001b[31m'),   # Red
    (" because I can't find the manual yet.", '\u001b[32m')  # Green
]

# Uncolored message for calculating box dimensions
uncolored_msg = ''.join(p[0] for p in parts)
msg_length = len(uncolored_msg.rstrip())  # Ensure no trailing whitespace

# Build full colored message with ANSI codes and resets
reset = '\u001b[0m'
full_color_msg = ""
for text, color in parts:
    full_color_msg += color + text + reset

# Create box borders
border = '+' + '-' * (msg_length + 4) + '+'

# Print top border
print(border)

# Start middle line with left border
sys.stdout.write("| ")
sys.stdout.flush()

# Animate full message character by character with delay
for char in full_color_msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)

# Complete middle line and print bottom border
sys.stdout.write(" |")
sys.stdout.flush()
print()  # Newline
print(border)