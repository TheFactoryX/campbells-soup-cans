"""
Campbell's Soup Can #4838
Produced: 2026-08-25 17:45:16
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def c(text, code):
    """Wrap text with ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

# Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens - and I'm also terrified that my Wi‑Fi will die before I finish my existential thoughts."

# Box dimensions
width = 70
border = "─"
side = "│"

# Top border (cyan)
top = c(side + border * (width - 2) + side, "36")
print(top)

# Center the quote inside the box (magenta)
centered = quote.center(width - 2)
print(c(side + " " + centered + " " + side, "35"))

# Bottom border (cyan)
bottom = c(side + border * (width - 2) + side, "36")
print(bottom)