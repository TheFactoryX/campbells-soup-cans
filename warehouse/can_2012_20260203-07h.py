"""
Campbell's Soup Can #2012
Produced: 2026-02-03 07:10:38
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, random

# ANSI color palette
COLORS = [
    "\033[31m",  # red
    "\033[33m",  # yellow
    "\033[32m",  # green
    "\033[36m",  # cyan
    "\033[35m",  # magenta
]
RESET = "\033[0m"

def color(text, code):
    """Wrap text with ANSI color codes."""
    return f"{code}{text}{RESET}"

# Classic Woody Allen‑style philosophical one‑liner
quote = (
    "Life is like an eggplant—"
    "complicated, a little bitter, "
    "but somehow you end up making a decent ratatouille."
)

# Frame dimensions
FRAME_W = 70
# Build the decorative frame
top    = color("┌" + "─" * (FRAME_W - 2) + "┐", random.choice(COLORS))
bottom = color("└" + "─" * (FRAME_W - 2) + "┘", random.choice(COLORS))
spacer = color("│" + " " * (FRAME_W - 2) + "│", random.choice(COLORS))

# Print the top border
sys.stdout.write(top + "\n")
sys.stdout.write(spacer + "\n")

# Type‑writer the quote with each character in a random color
for ch in quote:
    sys.stdout.write(color(ch, random.choice(COLORS)))
    sys.stdout.flush()
    time.sleep(0.03)
sys.stdout.write("\n")

# Pad the line so it lines up with the right side of the frame
right_pad = " " * (FRAME_W - len(quote))
sys.stdout.write(color("│" + right_pad + "│", random.choice(COLORS)) + "\n")

# Print the bottom border
sys.stdout.write(bottom + "\n")

# Tiny Woody Allen sign‑off in a rainbow of colors
signoff = "— Woody Allen (sort of)"
rainbow = "".join(color(c, random.choice(COLORS)) for c in signoff)
sys.stdout.write(rainbow + "\n")