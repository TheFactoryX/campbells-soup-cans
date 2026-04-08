"""
Campbell's Soup Can #3193
Produced: 2026-04-08 14:02:22
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
A tiny, colorful, self‑deprecating Woody‑Allen‑style quote generator.
Run it in a terminal that understands ANSI escape sequences.
"""

import sys
import time
import itertools

# ------------------------------------------------------------
# ANSI colour helpers
# ------------------------------------------------------------
RESET = "\033[0m"
BOLD = "\033[1m"

# Some pleasant pastel colours
COLORS = [
    "\033[38;5;208m",  # orange
    "\033[38;5;221m",  # yellow
    "\033[38;5;159m",  # light cyan
    "\033[38;5;182m",  # light green
    "\033[38;5;141m",  # lilac
]

def colour_cycle():
    """Yield colours endlessly."""
    while True:
        for c in COLORS:
            yield c

def slow_print(text, delay=0.04, colour=""):
    """Print text character‑by‑character for a typing‑animation effect."""
    for ch in text:
        sys.stdout.write(colour + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# ------------------------------------------------------------
# The quote (Woody‑Allen style)
# ------------------------------------------------------------
QUOTE = (
    f"{BOLD}I think, therefore I’m terrified.{RESET} "
    "Existence is a very long, very boring lecture "
    "and I’m the only student who never took the "
    "attendance roll."
)

# ------------------------------------------------------------
# Pretty box drawing
# ------------------------------------------------------------
def framed(text, padding=2):
    """Return a string that puts *text* inside a nice ASCII box."""
    lines = text.split("\n")
    width = max(len(line) for line in lines) + padding * 2
    top = "╔" + "─" * width + "╗"
    bottom = "╚" + "─" * width + "╝"
    middle = []
    for line in lines:
        spaces = " " * (width - len(line) - padding)
        middle.append(
            "║"
            + " " * padding
            + line
            + spaces
            + " " * padding
            + "║"
        )
    return "\n".join([top] + middle + [bottom])

# ------------------------------------------------------------
# Main animation
# ------------------------------------------------------------
def main():
    # Create a colour iterator for a subtle rainbow effect
    col_it = colour_cycle()

    # Build the framed quote
    box = framed(QUOTE, padding=3)

    # Print line by line with a colour change every line
    for line in box.split("\n"):
        colour = next(col_it)
        slow_print(line, delay=0.02, colour=colour)
        # tiny pause between lines makes the "animation" smoother
        time.sleep(0.15)

    # Final splash – flash all colours quickly
    for _ in range(3):
        for colour in COLORS:
            sys.stdout.write(colour + BOLD + "★" * 5 + RESET + " ")
        sys.stdout.write("\r")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()