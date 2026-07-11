"""
Campbell's Soup Can #4162
Produced: 2026-07-11 21:07:11
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def type_print(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Woody Allen-style quote with color variations
quote_start = '"I\'m not afraid of '
quote_death = '\033[31mdeath\033[0m'  # Red for "death"
quote_end = ', just afraid of the paperwork."'

# Calculate box dimensions
full_quote = quote_start + quote_death + quote_end
box_width = len(full_quote) + 2  # +2 for the | on each side

# Box borders with different colors
top = '\033[36m+' + '-' * (box_width - 2) + '+\033[0m'  # Cyan top
bottom = '\033[35m+' + '-' * (box_width - 2) + '+\033[0m'  # Magenta bottom

# Print the box with animated quote
print(top)
print('\033[36m|\033[0m ', end='')  # Cyan |, reset, space
sys.stdout.write('\033[33m')  # Yellow start
type_print(quote_start)
sys.stdout.write(quote_death)  # Already colored "death"
type_print(quote_end)
sys.stdout.write('\033[0m')  # Reset to default
print('\033[36m|\033[0m')  # Cyan | and reset

print(bottom)

# Add a cheeky sign-off in a different color
sys.stdout.write('\033[32m')  # Green
print("\n— Woody Allen (probably)")
sys.stdout.write('\033[0m')  # Reset