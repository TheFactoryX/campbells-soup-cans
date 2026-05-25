"""
Campbell's Soup Can #3785
Produced: 2026-05-25 17:57:57
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen‑style philosophical quote with a splash of color and a gentle typewriter effect.
"""

import sys
import time
import random

# ANSI color codes
COLORS = [
    "\033[38;5;226m",  # bright yellow
    "\033[38;5;214m",  # orange
    "\033[38;5;208m",  # bright orange
    "\033[38;5;202m",  # red-orange
    "\033[38;5;196m",  # bright red
    "\033[38;5;220m",  # gold
    "\033[38;5;11m",   # bright cyan
    "\033[38;5;15m",   # white
]

RESET = "\033[0m"
BOLD = "\033[1m"

def colorize(text):
    """Return text wrapped in a random color from COLORS."""
    return f"{random.choice(COLORS)}{text}{RESET}"

def typewriter_line(line, delay=0.03):
    """Print a line character‑by‑character with a slight delay."""
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def draw_box(width, height, quote_lines):
    """Draw a colored box around the quote."""
    # Top border
    print(colorize("╔" + "═" * (width - 2) + "╗"))
    # Upper padding
    for _ in range((height - len(quote_lines)) // 2):
        print(colorize("║" + " " * (width - 2) + "║"))
    # Quote lines (centered)
    for line in quote_lines:
        padded = line.center(width - 2)
        print(colorize("║") + padded + colorize("║"))
    # Lower padding
    for _ in range(height - len(quote_lines) - (height - len(quote_lines)) // 2 - 2):
        print(colorize("║" + " " * (width - 2) + "║"))
    # Bottom border
    print(colorize("╚" + "═" * (width - 2) + "╝"))

def main():
    quote = [
        "I'm constantly torn between wanting to understand the universe",
        "and wanting a nap; unfortunately, the universe doesn't come with",
        "a snooze button… so I just stare at the ceiling and wonder if",
        "the void has Wi‑Fi and if I’ll miss my notifications."
    ]

    # Determine box size
    max_len = max(len(line) for line in quote)
    width = max_len + 4          # padding inside box
    height = len(quote) + 4      # top/bottom borders + vertical padding

    # Optional: clear screen (works on most terminals)
    print("\033[2J\033[H", end="")

    # Animate the box drawing
    time.sleep(0.2)
    draw_box(width, height, quote)

    # Now type‑write the quote inside the box (already printed, but we can redo with effect)
    # For simplicity, we'll just re‑print the quote with typewriter effect inside the box.
    # We'll move cursor back to the inner area and rewrite.
    # Compute start row for quote lines (after top border and top padding)
    start_row = 1 + (height - len(quote)) // 2
    for i, line in enumerate(quote):
        # Position cursor at beginning of the line inside the box
        sys.stdout.write(f"\033[{start_row + i};{2}H")  # row, column (1‑based)
        sys.stdout.flush()
        typed = line.center(width - 2)
        for ch in typed:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.03)
        # Ensure line ends with spaces to clear any leftovers
        sys.stdout.write(" " * (width - 2 - len(typed)))
        sys.stdout.flush()
    # Final newline
    print()
    time.sleep(0.5)

if __name__ == "__main__":
    main()