"""
Campbell's Soup Can #2477
Produced: 2026-02-28 06:56:43
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys

# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "magenta": "\033[95m",
    "bright_red": "\033[91m",
}

def color(text, name):
    return COLORS.get(name, "") + text + COLORS["reset"]

# Woody Allen‑style existential joke
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a colorful ASCII box around the quote
WIDTH = 66
top    = color("╔" + "═" * (WIDTH - 2) + "╗", "cyan")
bottom = color("╚" + "═" * (WIDTH - 2) + "╝", "cyan")
inside = f"║ {quote.center(WIDTH - 4)} ║"
middle = color(inside, "magenta")

# Print the framed quote
sys.stdout.write(color(top, "cyan") + "\n")
sys.stdout.write(color(middle, "yellow") + "\n")
sys.stdout.write(color(bottom, "cyan") + "\n")