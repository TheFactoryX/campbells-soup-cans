"""
Campbell's Soup Can #3335
Produced: 2026-04-18 05:50:30
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[97m",  # White
]
RESET = "\033[0m"

# Woody Allen‑style philosophical quote (split into two lines for fun)
quote_lines = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "It's terrible for my social life and even worse for my LinkedIn profile."
]

# Clear screen and move cursor to home
sys.stdout.write("\033[2J\033[H")
sys.stdout.flush()

# Determine box width based on longest line (+4 for padding and borders)
max_len = max(len(line) for line in quote_lines)
width = max_len + 4  # 2 spaces padding each side + 2 borders

# Build top and bottom borders using box‑drawing characters
top_border = "╔" + "═" * (width - 2) + "╕"  # Using ╕ for a playful twist
bottom_border = "╚" + "═" * (width - 2) + "╝"

# Print top border
sys.stdout.write(top_border + "\n")
sys.stdout.flush()

# Print each line with a typing‑like animation and random colors
for line in quote_lines:
    sys.stdout.write("║")  # left border
    sys.stdout.flush()
    # Center the text inside the inner width (width-2)
    inner = line.center(width - 2)
    for ch in inner:
        color = random.choice(COLORS)
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(0.03)  # typing delay
    sys.stdout.write("║\n")  # right border + newline
    sys.stdout.flush()

# Print bottom border
sys.stdout.write(bottom_border + "\n")
sys.stdout.flush()