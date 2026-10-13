"""
Campbell's Soup Can #5102
Produced: 2026-10-13 21:15:09
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
CYAN  = "\033[36m"
RESET = "\033[0m"

# The Woody Allen‑style quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Box dimensions
width = 100                # total width of the box (including '+' corners)
inner_width = width - 2    # space between the '+' signs

# Center the quote inside the box
quote_len = len(quote)
pad = (inner_width - quote_len) // 2
centered_quote = " " * pad + quote + " " * (inner_width - quote_len - pad)

# Build each line of the box
border = GREEN + "+" + "=" * inner_width + RESET
top    = CYAN + "|" + " " * inner_width + "|" + RESET
middle = CYAN + "|" + YELLOW + centered_quote + RESET + CYAN + "|" + RESET
bottom = CYAN + "|" + " " * inner_width + "|" + RESET
footer = GREEN + "+" + "=" * inner_width + RESET

# Print with a tiny pause for a simple animation effect
print(border)
time.sleep(0.1)
print(top)
time.sleep(0.1)
print(middle)
time.sleep(0.1)
print(bottom)
time.sleep(0.1)
print(footer)