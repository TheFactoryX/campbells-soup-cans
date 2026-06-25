"""
Campbell's Soup Can #4011
Produced: 2026-06-25 15:14:08
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
A tiny, colorful, animated tribute to Woody Allen's neurotic philosophy.
Run it in a terminal that supports ANSI escape codes.
"""

import sys
import time
import itertools

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"

# Some nice colors (foreground)
COLORS = [
    "\033[38;5;202m",  # orange
    "\033[38;5;45m",   # cyan
    "\033[38;5;208m",  # bright orange
    "\033[38;5;215m",  # peach
    "\033[38;5;33m",   # blue
    "\033[38;5;129m",  # purple
]

# The quote – neurotic, self‑deprecating, existential.
QUOTE = (
    f"{BOLD}I think, therefore I panic.{RESET}\n"
    f"{BOLD}— a Woody‑Allen‑ish confession about consciousness{RESET}"
)

# A simple frame for the quote
def framed(text, width=60):
    lines = text.splitlines()
    padded = [line.center(width) for line in lines]
    top    = "┌" + "─" * (width + 2) + "┐"
    bottom = "└" + "─" * (width + 2) + "┘"
    body   = "\n".join(f"│ {line} │" for line in padded)
    return f"{top}\n{body}\n{bottom}"

# Animated typewriter effect
def typewriter(message, delay=0.04):
    for ch in message:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Choose a rotating color for the frame
    color_cycle = itertools.cycle(COLORS)

    # Build the framed quote once (without colors)
    raw_frame = framed(QUOTE)

    # Print the animation line by line, changing the frame color each line
    for line in raw_frame.splitlines():
        col = next(color_cycle)
        typewriter(col + line + RESET, delay=0.02)

    # Hold the final picture for a moment
    time.sleep(2)

    # Fade out (clear screen line by line)
    sys.stdout.write("\033[2J\033[H")  # clear screen, move cursor home
    sys.stdout.flush()
    time.sleep(0.5)

if __name__ == "__main__":
    main()