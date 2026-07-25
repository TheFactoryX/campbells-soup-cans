"""
Campbell's Soup Can #4318
Produced: 2026-07-25 04:27:50
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
COLORS = {
    "reset": "\033[0m",
    "cyan": "\033[36m",
    "yellow": "\033[33m",
    "magenta": "\033[35m",
    "green": "\033[32m",
}

def typewriter(text: str, delay: float = 0.03, color: str = COLORS["reset"]) -> None:
    """Print text character by character with a slight delay and optional color."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(COLORS["reset"] + "\n")

def main() -> None:
    quote = [
        '"I\'m not afraid of dying; I just don\'t want to be there when it happens — ' +
        'especially if I have to wear socks with sandals."'
    ]

    width = max(len(line) for line in quote) + 4  # padding inside the box
    top_border = "+" + "-" * (width - 2) + "+"
    empty_line = "|" + " " * (width - 2) + "|"

    # Print top border
    typewriter(top_border, color=COLORS["cyan"])
    # Print empty line above quote
    typewriter(empty_line, color=COLORS["yellow"])
    # Print the quote line(s) with a slight pause between lines
    for line in quote:
        padded = "| " + line.ljust(width - 4) + " |"
        typewriter(padded, color=COLORS["magenta"])
    # Print empty line below quote
    typewriter(empty_line, color=COLORS["yellow"])
    # Print bottom border
    typewriter(top_border, color=COLORS["cyan"])

    # A little Woody Allen‑style neurotic flourish
    time.sleep(0.5)
    sys.stdout.write(COLORS["green"])
    typewriter(" — Woody Allen (probably, if he wore socks with sandals)", delay=0.02)
    sys.stdout.write(COLORS["reset"])

if __name__ == "__main__":
    main()