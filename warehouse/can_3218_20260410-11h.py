"""
Campbell's Soup Can #3218
Produced: 2026-04-10 11:12:42
Worker: OpenAI: gpt-oss-120b (free) (openai/gpt-oss-120b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A single‑file, dependency‑free Python program that prints one
Woody‑Allen‑style philosophical quip with a splash of color
and a playful type‑writer animation.
"""

import sys
import time
import itertools

# ----------------------------------------------------------------------
# ANSI colour utilities
# ----------------------------------------------------------------------
RESET = "\033[0m"

# A few soothing (and slightly neurotic) colours
COLORS = {
    "dark": "\033[38;5;236m",   # dark gray
    "pink": "\033[38;5;205m",   # hot pink
    "cyan": "\033[38;5;45m",    # cyan
    "yellow": "\033[38;5;226m", # bright yellow
}

def colour(text: str, name: str) -> str:
    """Wrap *text* in the given colour name."""
    return f"{COLORS.get(name, '')}{text}{RESET}"

# ----------------------------------------------------------------------
# Animation helpers
# ----------------------------------------------------------------------
def typewriter(text: str, delay: float = 0.04):
    """Print *text* character‑by‑character."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def blink_border(frames, period=0.3, repeats=6):
    """Draw a simple blinking border around the quote."""
    for _ in range(repeats):
        for frame in frames:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(period)
    sys.stdout.write("\n")

# ----------------------------------------------------------------------
# The quote
# ----------------------------------------------------------------------
quote = (
    "I told my therapist I’m terrified of the meaning of life. "
    "She said, “Don’t worry, you’ll never figure it out anyway.”"
)

# ----------------------------------------------------------------------
# Build a colourful ASCII “box” around the quote
# ----------------------------------------------------------------------
def build_box(q: str) -> str:
    lines = q.split("\n")
    width = max(len(line) for line in lines) + 4  # padding
    top    = colour("╔" + "═" * width + "╗", "cyan")
    bottom = colour("╚" + "═" * width + "╝", "cyan")
    middle = []
    for line in lines:
        padded = f"  {line.ljust(width-2)}  "
        middle.append(colour("║", "cyan") + colour(padded, "pink") + colour("║", "cyan"))
    return "\n".join([top] + middle + [bottom])

# ----------------------------------------------------------------------
# Main animation routine
# ----------------------------------------------------------------------
def main():
    box = build_box(quote)

    # Prepare a simple “heartbeat” border animation
    frames = [
        colour(box, "dark"),
        colour(box, "yellow")
    ]

    # Show the blinking border a few times before the typewriter effect
    blink_border(frames, period=0.4, repeats=4)

    # Now print the quote inside the box with a typewriter effect
    # (we re‑print the whole box line by line to keep the colours)
    for line in box.split("\n"):
        typewriter(line, delay=0.02)

    # A final wink
    sys.stdout.write(colour("\n*wink*\n", "cyan"))
    sys.stdout.flush()

if __name__ == "__main__":
    main()