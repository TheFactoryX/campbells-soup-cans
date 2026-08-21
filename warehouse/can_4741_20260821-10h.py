"""
Campbell's Soup Can #4741
Produced: 2026-08-21 10:47:36
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""Woody Allen style philosophical quote — colorful & neurotic."""
import time
import sys

# ANSI escape codes for colors and formatting
RS = "\033[0m"   # reset
B  = "\033[1m"   # bold
CY = "\033[96m"  # cyan
YL = "\033[93m"  # yellow
GR = "\033[92m"  # green
RD = "\033[91m"  # red
MA = "\033[95m"  # magenta

# A Woody-ish, neurotic, existential one-liner
QUOTE = (
    "I'm not afraid of death. I'm just afraid it'll cut me off mid-thought, "
    "leaving me eternally awkward in the afterlife, forever asking "
    "'Wait, what was I saying?' and wondering if the cosmic WiFi has good enough signal."
)


def typewriter(text, colors, delay=0.02):
    """Print text with a color-cycling typewriter effect."""
    for i, ch in enumerate(text):
        if ch == " ":
            sys.stdout.write(" ")
            sys.stdout.flush()
            time.sleep(0.005)
            continue
        c = colors[i % len(colors)]
        sys.stdout.write(c + ch + RS)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    # Draw a colorful box border
    print(CY + B + "+" + "=" * 60 + "+" + RS)
    print(CY + B + "| " + " " * 58 + " |" + RS)
    print(CY + B + "|  " + " " * 4 + " NEUROTIC PHILOSOPHICAL QUOTE " + " " * 4 + " |" + RS)
    print(CY + B + "| " + " " * 58 + " |" + RS)
    print(CY + B + "+" + "=" * 60 + "+" + RS)
    print()

    # Palette of neurotic colors
    palette = [RD, GR, YL, MA, CY]

    # Reveal the quote with playful typewriter action
    typewriter(QUOTE, palette, 0.018)

    print()
    # Footer pun
    print(YL + B + "'Existential dread: now with 100% more WiFi anxiety!'" + RS)
    print()
    # Bottom border
    print(CY + B + "+" + "-" * 60 + "+" + RS)


if __name__ == "__main__":
    main()