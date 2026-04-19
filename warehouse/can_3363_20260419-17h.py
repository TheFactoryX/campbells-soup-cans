"""
Campbell's Soup Can #3363
Produced: 2026-04-19 17:53:40
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

def ansi_color(text, code):
    """Wrap text in ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

# Woody Allen‑style philosophical quote (original)
quote = "I’m not terrified of the void; I’m just terrified of showing up to the void without snacks."

# Pretty box characters
top_border    = "╔" + "═" * (len(quote) + 4) + "╗"
bottom_border = "╚" + "═" * (len(quote) + 4) + "╝"
side          = "║"

# Color cycle: red, yellow, green, cyan, magenta, blue
color_cycle = itertools.cycle([31, 33, 32, 36, 35, 34])

# Print top border with a subtle color
sys.stdout.write(ansi_color(top_border, 90) + "\n")
sys.stdout.flush()
time.sleep(0.1)

# Print left side, then animate the quote character‑by‑character
sys.stdout.write(side + "  ")
sys.stdout.flush()
time.sleep(0.1)

for ch in quote:
    sys.stdout.write(ansi_color(ch, next(color_cycle)))
    sys.stdout.flush()
    time.sleep(0.04)  # typing speed

# Finish the line with right side and bottom border
sys.stdout.write("  " + side + "\n")
sys.stdout.flush()
time.sleep(0.1)
sys.stdout.write(ansi_color(bottom_border, 90) + "\n")

# Optional tiny neurotic footer
footer = "(If you’re reading this, you’ve already wasted precious existential time.)"
sys.stdout.write("\n" + ansi_color(footer, 2) + "\n")