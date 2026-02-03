"""
Campbell's Soup Can #2017
Produced: 2026-02-03 11:50:44
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen style philosophical quote in a colorful box

# ANSI color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
RESET = '\033[0m'

# The quote (in classic Woody Allen neurotic existential style)
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Build a simple ASCII box that fits the quote
border_len = len(quote) + 4          # accounts for " | " on each side
border = "+" + "-" * border_len + "+"
mid_line = f"| {quote} |"

# Print the box with some color for visual fun
print(GREEN + border + RESET)
print(YELLOW + mid_line + RESET)
print(GREEN + border + RESET)