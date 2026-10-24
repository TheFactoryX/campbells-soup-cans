"""
Campbell's Soup Can #5157
Produced: 2026-10-24 05:55:04
Worker: Recursive: Flint (free) (recursive/flint-v1.0:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def type_text(text, color_code, delay=0.02):
    sys.stdout.write(f"\033[{color_code}m")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Title
sys.stdout.write("\033[31m")
print("WOODY ALLEN'S PHILOSOPHICAL CORNER")
sys.stdout.write("\033[0m\n")

# Decorative line
print("  ~*~*~*~*~*~*~*~*~")

# Type the quote in bold yellow
type_text(quote, "1;33")

# Footer
print("\033[34m...and I'm pretty sure that's the existential crisis talking.\033[0m")

# Small pause to let the user read
time.sleep(2)