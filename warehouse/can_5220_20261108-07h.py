"""
Campbell's Soup Can #5220
Produced: 2026-11-08 07:22:01
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A neurotic, colorful Woody Allen quote for your terminal."""
import sys
import re

# Woody's philosophical gem
quote = "I'm not afraid of death. I just don't want to be there when it happens, preferably while I'm still funny."

# ANSI palette (bright 9-bit colors)
R = "\033[0m"              # reset
C = {
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "bold": "\033[1m",
    "magenta": "\033[95m",
}

# Strip ANSI codes for accurate length calculations
clean = lambda s: re.sub(r"\033\[[0-9;]*m", "", s)

# Box width adapts to quote length (minimum 55)
w = max(len(clean(quote)) + 6, 55)

# Top border
top = f"{C['cyan']}╔{'═' * (w - 2)}╗{R}"

# Center the quote inside the box
padding = w - 4 - len(clean(quote))
left = padding // 2
right = padding - left
mid = (
    f"{C['cyan']}║{R}"
    f"{' ' * left}"
    f"{C['yellow']}{C['bold']}{quote}{R}"
    f"{' ' * right}"
    f"{C['cyan']} ║{R}"
)

# Bottom border
bot = f"{C['cyan']}╚{'═' * (w - 2)}╝{R}"

# Render
print(top)
print(mid)
print(bot)