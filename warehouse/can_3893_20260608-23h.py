"""
Campbell's Soup Can #3893
Produced: 2026-06-08 23:36:46
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def color(text, code):
    """Return text wrapped in ANSI 256‑color code."""
    return f"\033[38;5;{code}m{text}\033[0m"

# Original Woody‑Allen‑style quote (feel free to swap it out!)
quote = "Life is a horrible, pointless joke — and the punchline is that I’m still waiting for the bus."

# Palette: bright, eye‑catching 256‑color codes
palette = [196, 202, 226, 46, 21, 93]   # red, orange, yellow, green, blue, violet

# Prepare the box
inner_width = len(quote) + 2          # space for left/right padding
top_bottom = color('+' + '-' * inner_width + '+', 202)   # orange border
sides = color('|', 33)                # yellow sidebars

# Draw top border instantly
sys.stdout.write(top_bottom + '\n')
sys.stdout.flush()

# Left sidebar
sys.stdout.write(sides + ' ')
sys.stdout.flush()

# Typewriter effect with cycling colors
for i, ch in enumerate(quote):
    sys.stdout.write(color(ch, palette[i % len(palette)]))
    sys.stdout.flush()
    time.sleep(0.04)   # adjust speed to taste

# Right sidebar and newline
sys.stdout.write(' ' + sides + '\n')
sys.stdout.flush()

# Bottom border
sys.stdout.write(top_bottom + '\n')
sys.stdout.flush()