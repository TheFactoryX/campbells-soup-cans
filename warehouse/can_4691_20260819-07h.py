"""
Campbell's Soup Can #4691
Produced: 2026-08-19 07:05:07
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen meets ANSI art: a neurotic, funny, philosophical quote in color."""
import sys, time

# ANSI color codes (bright palette)
C = {
    "end": "\033[0m",
    "red": "\033[91m",
    "grn": "\033[92m",
    "yel": "\033[93m",
    "blu": "\033[94m",
    "mag": "\033[95m",
    "cyn": "\033[96m",
}
palette = [C["red"], C["grn"], C["yel"], C["blu"], C["mag"], C["cyn"]]

# The quote — Woody's neurotic existentialism
quote = (
    "I spend half my life anxious about things that haven't happened yet, "
    "and the other half depressed they might never happen. "
    "At least the worry gives me something to do while I'm waiting for nothing."
)

# Color each word cyclically through the palette
words = quote.split()
colored = ""
for i, w in enumerate(words):
    clr = palette[i % len(palette)]
    colored += clr + w + " " + C["end"]

# Typewriter effect
def typew(text, delay=0.006):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Top decorative border in cyan
print(C["cyn"] + "-" * 62 + C["end"])

# Typewrite the colorful quote
typew(colored, 0.005)

# Bottom decorative border in cyan
print(C["cyn"] + "-" * 62 + C["end"])

# Neurotic ASCII companion in magenta
print(C["mag"] + r"(\_/)  wondering why I'm here" + C["end"])