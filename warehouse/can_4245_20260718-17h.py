"""
Campbell's Soup Can #4245
Produced: 2026-07-18 17:15:40
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# A single, self‑contained Python script that prints a colorful, Woody Allen‑style
# philosophical one‑liner with a decorative ASCII box.

# ANSI colour codes (no external libraries needed)
CYAN  = '\033[36m'
YELLOW = '\033[33m'
RESET = '\033[0m'

# Woody Allen‑style quote
quote = "I’m not scared of death; I just don’t want to be there when it happens."

# Dimensions of the decorative box
BOX_WIDTH = 78                     # inner width (excluding side borders)
TOP_LEFT  = "╔"
TOP_RIGHT = "╗"
BOTTOM_LEFT = "╚"
BOTTOM_RIGHT = "╝"
SIDE = "║"

# Build the centred inner line
pad_len = (BOX_WIDTH - len(quote)) // 2
inner = " " * pad_len + quote + " " * (BOX_WIDTH - pad_len - len(quote))

# Print the coloured box
print(CYAN + TOP_LEFT + "═" * BOX_WIDTH + TOP_RIGHT + RESET)
print(CYAN + SIDE + RESET + YELLOW + inner + RESET + CYAN + SIDE + RESET)
print(CYAN + SIDE + RESET + YELLOW + inner + RESET + CYAN + SIDE + RESET)
print(CYAN + SIDE + RESET + YELLOW + inner + RESET + CYAN + SIDE + RESET)
print(CYAN + BOTTOM_LEFT + "═" * BOX_WIDTH + BOTTOM_RIGHT + RESET)

# Ensure colour is reset for any subsequent terminal output
print(RESET, end="")