"""
Campbell's Soup Can #3638
Produced: 2026-05-10 19:33:32
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3# Woody Allen style philosophical quote in a colorful box

# ANSI color codes
CYAN  = "\033[36m"
RESET = "\033[0m"

# The quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."
inner_width = len(quote) + 4   # width for the top/bottom border

# Build the top and bottom borders
top    = CYAN + "╔" + "═" * inner_width + "╗" + RESET
bottom = CYAN + "╚" + "═" * inner_width + "╝" + RESET

# Colored left side (includes a trailing space)
side_start = CYAN + "║ "   # colored "║ "

# Closing part: a space then "║"
side_end   = " ║"

# Compute filler spaces so the quote is nicely padded
filler_spaces = " " * (inner_width - len(quote) - 2)   # -2 accounts for side_start length

# Print the box
print()
print(top)
print(side_start + quote + filler_spaces + side_end)
print(bottom)
print()