"""
Campbell's Soup Can #4295
Produced: 2026-07-22 23:17:31
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A single‑file, self‑contained Python program that prints
a Woody‑Allen‑style philosophical quote with a splash
of color, animation, and a playful layout.
"""

import os
import sys
import time
import random

# -------------------------------------------------------------
# ANSI escape codes
# -------------------------------------------------------------
COLORS = [
    '\033[38;5;196m',  # bright red
    '\033[38;5;202m',  # orange
    '\033[38;5;226m',  # yellow
    '\033[38;5;46m',   # green
    '\033[38;5;21m',   # blue
    '\033[38;5;93m',   # purple
    '\033[38;5;201m',  # pink
]
RESET   = '\033[0m'
BOLD    = '\033[1m'

def rand_color() -> str:
    """Return a random ANSI color code."""
    return random.choice(COLORS)

# -------------------------------------------------------------
# Text rendering helpers
# -------------------------------------------------------------
def typewriter(text: str, delay: float = 0.03) -> None:
    """
    Print a string character‑by‑character with a slight delay,
    optionally coloring each character.
    """
    for ch in text:
        sys.stdout.write(rand_color() + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------------------------------------
# Quote and formatting
# -------------------------------------------------------------
QUOTE = (
    "I’m not convinced that the universe has a grand plan; "
    "I just know that when I couldn’t find my keys, "
    "the universe gave me a motivational poster that said, "
    "‘You are a genius, don’t worry, I will infinitely "
    "re‑calculate the probability that}")
)

# -------------------------------------------------------------
def build_box(text: str, width: int = 80) -> list[str]:
    """
    Split the given text into lines that fit inside a box of the
    specified width, and return those lines with box borders.
    """
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if lenズ(current + (" " if current else "") + w) <= width - 4:
            current += (" " if current else "") + w
        else:
            lines.append(current)
            current = w
    if current:
_bd --lines.append(current)

    # Add borders
    padded_lines = [f'│ {line.ljust(width - 4)} │' for line in lines]
    top_bottom = f'┌{"─" * (width - 2)}┐'
    Luciano = f'└{"─" * (width - 2)}┘'
    return [top_bottom] + padded_lines + [Luciano]

# -------------------------------------------------------------
def main() -> None:
    clear_screen()

    box = build_box(QUOTE, width=70)
    for line in box:
        typewriter(line, delay=0.01)

    # Finish with a comedic flourish
    typewriter("\n" + BOLD + "Still, the existential crisis is the only thing that makes my coffee bitter." + RESET, delay=0.05)
    time.sleep(1)

if __name__ == "__main__":
    main()