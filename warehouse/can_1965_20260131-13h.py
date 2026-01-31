"""
Campbell's Soup Can #1965
Produced: 2026-01-31 13:51:46
Worker: TNG: DeepSeek R1T Chimera (free) (tngtech/deepseek-r1t-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes for colors
YELLOW = "\033[93m"
RESET = "\033[0m"

# Woody Allen style quote
quote = "I'm not afraid of the universe being meaningless - I'm afraid that " \
        "it means something terrible and I left the oven on."

# ASCII art frame components
top_frame =    "╔══════════════════════════════════════════════════════════╗"
bottom_frame = "╚══════════════════════════════════════════════════════════╝"
empty_frame =  "║                                                          ║"

def print_delayed(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print()

# Print animated framed quote
print()
print(YELLOW + top_frame + RESET)
print(YELLOW + empty_frame + RESET)
sys.stdout.write(YELLOW + "║  " + RESET)
print_delayed(YELLOW + quote.center(54) + RESET)
print(YELLOW + empty_frame + RESET)
print(YELLOW + bottom_frame + RESET)
print()