"""
Campbell's Soup Can #1092
Produced: 2025-12-21 23:30:27
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI color codes
COLORS = [
    '\033[31m',  # red
    '\033[32m',  # green
    '\033[33m',  # yellow
    '\033[34m',  # blue
    '\033[35m',  # magenta
    '\033[36m',  # cyan
]
RESET = '\033[0m'

# Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

def colored_print(text, color_idx):
    """Print text wrapped in the specified ANSI color."""
    sys.stdout.write(COLORS[color_idx % len(COLORS)] + text + RESET)

def animate_print(s, delay=0.04):
    """Type‑writer style print with a random color for each character."""
    for _ in s:
        color = random.randint(0, len(COLORS) - 1)
        colored_print(_, color)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# Fancy border made of Unicode box‑drawing characters
border = "╔═══════════════════════════════════════════════════════════╗"
top    = "║ " + quote[:42] + " ║"
bottom = "╚═══════════════════════════════════════════════════════════╝"

# Print the bordered frame
print(border)
print(top)
print(bottom)

# Animate the quote itself
animate_print(quote + "\n")