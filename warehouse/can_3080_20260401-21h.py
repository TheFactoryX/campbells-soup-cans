"""
Campbell's Soup Can #3080
Produced: 2026-04-01 21:58:41
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Woody Allen‑style philosophical quotequote = "I'm not afraid of death; I just don't want to be there when it happens."
width = len(quote) + 4  # padding for the box borders

# Draw ASCII box borders
top_    = "┌" + "─" * width + "┐"
bottom_ = "└" + "─" * width + "┘"

# Simple ANSI color helper (uses only built‑in escape codes)
def col(txt, name):
    colors = {
        "reset":   "\033[0m",
        "cyan":    "\033[36m",
        "magenta": "\033[35m",
        "bright_cyan": "\033[96m",
        "bright_magenta": "\033[95m",
    }
    return colors.get(name, "") + txt + colors["reset"]

# Assemble the three lines of the box
lines = [top_, f"│ {quote} │", bottom_]

# Print with a tiny pause for a playful “animation”
for line in lines:
    print(col(line, "bright_cyan"))
    time.sleep(0.4)