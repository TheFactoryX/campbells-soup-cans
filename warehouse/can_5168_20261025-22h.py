"""
Campbell's Soup Can #5168
Produced: 2026-10-25 22:33:54
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

def colored(text, code):
    """Wrap text in ANSI color codes."""
    return f"\033[{code}m{text}\033[0m"

# Woody Allen‑style philosophical quote
quote = "Life is misery, and it ends far too soon."

# Box dimensions
width = 60  # total width of the box

# Create the box parts
top = "+" + "-" * (width - 2) + "+"
middle = "| " + quote.center(width - 4) + " |"

# Print with colors: green borders, yellow text
print(colored(top, "1;32"))        # green top border
print(colored(middle, "1;33"))     # yellow quote
print(colored(top, "1;32"))        # green bottom border