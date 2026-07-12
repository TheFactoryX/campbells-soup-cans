"""
Campbell's Soup Can #4176
Produced: 2026-07-12 21:06:31
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A tiny animated, colorful Woody‑Allen‑style philosophical quote.
Run it directly in a terminal that supports ANSI escape codes.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour helpers
# ----------------------------------------------------------------------
CSI = "\033["

def rgb(r, g, b, bright=False):
    """Return an ANSI colour code for given r,g,b (0‑255)."""
    return f"{CSI}{'1;' if bright else ''}38;2;{r};{g};{b}m"

RESET = f"{CSI}0m"

# A pastel palette that feels a bit neurotic‑yet‑soft
PALETTE = [
    rgb(255, 182, 193),   # Light pink
    rgb(173, 216, 230),   # Light blue
    rgb(152, 251, 152),   # Pale green
    rgb(255, 228, 181),   # Moccasin
    rgb(221, 160, 221),   # Plum
]

# ----------------------------------------------------------------------
# The quote – original Woody‑Allen‑ish neurotic wisdom
# ----------------------------------------------------------------------
quote = (
    "I’m terrified of meaninglessness, "
    "but even more terrified of the day I finally figure it out "
    "and realise it was just my Wi‑Fi that went out."
)

# ----------------------------------------------------------------------
# Animation utilities
# ----------------------------------------------------------------------
def typewriter(text, speed=0.04):
    """Yield progressively longer fragments of text, like a typewriter."""
    for i in range(1, len(text) + 1):
        yield text[:i]
        time.sleep(speed)

def bouncing_box(width, height, cycles=2, pause=0.1):
    """Yield a series of strings that draw a box moving up‑and‑down."""
    for _ in range(cycles):
        # go down
        for offset in range(height):
            lines = [""] * offset
            lines.append("+" + "-" * (width - 2) + "+")
            for _ in range(height - 2):
                lines.append("|" + " " * (width - 2) + "|")
            lines.append("+" + "-" * (width - 2) + "+")
            yield "\n".join(lines)
            time.sleep(pause)
        # go up
        for offset in reversed(range(height)):
            lines = [""] * offset
            lines.append("+" + "-" * (width - 2) + "+")
            for _ in range(height - 2):
                lines.append("|" + " " * (width - 2) + "|")
            lines.append("+" + "-" * (width - 2) + "+")
            yield "\n".join(lines)
            time.sleep(pause)

# ----------------------------------------------------------------------
# Main routine
# ----------------------------------------------------------------------
def main():
    # Choose a random colour for each letter, cycling through the palette
    colour_cycle = itertools.cycle(PALETTE)

    # Print a bouncing box while we type the quote inside it
    box_width = max(len(line) for line in quote.splitlines()) + 4
    box_height = 5

    box_gen = bouncing_box(box_width, box_height, cycles=1, pause=0.07)

    # Grab the first frame of the box to host the typing
    frame = next(box_gen)
    frame_lines = frame.splitlines()

    # We'll replace the middle line of the box with the typing text
    middle_index = len(frame_lines) // 2

    for partial in typewriter(quote):
        # colour each character
        coloured = "".join(
            next(colour_cycle) + ch + RESET if ch != " " else " "
            for ch in partial
        )
        # pad to box width
        padded = f" {coloured} ".ljust(box_width - 1)
        frame_lines[middle_index] = "|" + padded + "|"
        sys.stdout.write("\033[H\033[2J")  # clear screen
        sys.stdout.write("\n".join(frame_lines))
        sys.stdout.flush()
        # reset colour cycle for consistent rainbow effect
        colour_cycle = itertools.cycle(PALETTE)

    # hold the final picture for a moment
    time.sleep(2)

    # final flourish: flash the quote in bright neon
    for _ in range(3):
        sys.stdout.write("\033[H\033[2J")
        bright = rgb(255, 105, 180, bright=True)  # hot pink
        print("\n" * (box_height // 2))
        print(" " * ((box_width // 2) - len(quote)//2) + bright + quote + RESET)
        time.sleep(0.3)
        sys.stdout.write("\033[H\033[2J")
        time.sleep(0.2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(RESET)
        sys.exit(0)