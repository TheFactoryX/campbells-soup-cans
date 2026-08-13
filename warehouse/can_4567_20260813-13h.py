"""
Campbell's Soup Can #4567
Produced: 2026-08-13 13:48:05
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
import random

# ANSI color codes
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
}
RESET = "\033[0m"
BOLD = "\033[1m"

def type_print(text: str, color: str, delay: float = 0.03) -> None:
    """Print text character‑by‑character with a slight delay and given color."""
    sys.stdout.write(color + BOLD)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def draw_box(width: int, color: str) -> None:
    """Draw a simple ASCII box with the given width and color."""
    horiz = "═" * (width - 2)
    sys.stdout.write(color + "╔" + horiz + "╗\n" + RESET)
    sys.stdout.write(color + "║" + " " * (width - 2) + "║\n" + RESET)

def main() -> None:
    # A Woody Allen‑style neurotic, funny, philosophical quote
    quote = "I’m not afraid of dying; I just don’t want to be there when it happens."

    # Pick a random color for the quote
    quote_color = random.choice(list(COLORS.values()))
    box_color = random.choice([c for c in COLORS.values() if c != quote_color])

    # Determine box width (quote length + padding)
    padding = 4
    width = len(quote) + padding

    # Visual output: box, animated typing, then closing box
    draw_box(width, box_color)
    sys.stdout.write(box_color + "║" + " " * ((width - 2 - len(quote)) // 2) + RESET)
    type_print(quote, quote_color, delay=0.05)
    sys.stdout.write(box_color + "║" + " " * ((width - 2 - len(quote)) // 2) + RESET)
    sys.stdout.write("\n")
    draw_box(width, box_color)

if __name__ == "__main__":
    main()