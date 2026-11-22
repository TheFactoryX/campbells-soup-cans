"""
Campbell's Soup Can #5268
Produced: 2026-11-22 15:17:53
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style neurotic quote generator — pure Python, colorful & animated."""

import time, sys

# The quote, Woody-esque neurotic philosophy
QUOTE = (
    "I spend so much time contemplating the meaning of existence "
    "that by the time I figure it out, I'm too tired to care. "
    "Which, I suppose, is the meaning."
)

# ANSI color codes (no external deps)
C = {
    "R": "\033[0m",    # reset
    "B": "\033[1m",    # bold
    "G": "\033[92m",   # bright green
    "Y": "\033[93m",   # bright yellow
    "C": "\033[96m",   # bright cyan
    "M": "\033[95m",   # magenta
}

# ---- Magenta ASCII "neurotic" header ----
print(C["M"] + "      ... ... ... ... ...      " + C["R"])
print(C["M"] + "   ... ... ... ... ...   " + C["R"])
print(C["M"] + "  ... ... ... ... ...  " + C["R"])
print()

# ---- Colored box framing the quote ----
W = 72                                                    # box width
top = C["C"] + "+" + "-" * W + C["R"]                    # top border
print(top)

q = C["G"] + QUOTE + C["R"]                               # quote with green color
centered = q.center(W - 4)                                # center it inside
mid = C["C"] + "| " + centered + " |" + C["R"]          # bordered line
print(mid)
print(top)

# ---- Slight "thinking" animation ----
print("Thinking", end="", flush=True)
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print()                                                    # nice newline after dots

# ---- Neurotic footer ----
print(C["Y"] + "Life's pretty great—if you ignore the existential dread." + C["R"])