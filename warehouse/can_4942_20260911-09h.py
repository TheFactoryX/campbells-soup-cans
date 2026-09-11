"""
Campbell's Soup Can #4942
Produced: 2026-09-11 09:42:13
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
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Woody Allen‑style quote (original)
QUOTE = (
    "I've come to the conclusion that the universe is indifferent, "
    "which is comforting—because it means I don't have to feel guilty "
    "about stealing the last cookie."
)

# Simple neurotic face ASCII art
FACE = [
    "   (\_/)",
    "  ( •_•)",
    "   >⌐■-■",
    "  (⌐■_■)",
]

def color_cycle(text, colors):
    """Return text with each character colored cyclically from colors."""
    if not colors:
        return text
    colored = []
    for i, ch in enumerate(text):
        colored.append(colors[i % len(colors)] + ch)
    colored.append(RESET)
    return "".join(colored)

def print_with_delay(line, delay=0.05):
    print(line, flush=True)
    time.sleep(delay)

def main():
    # Determine box width based on quote length + padding
    padding = 4
    width = len(QUOTE) + padding

    # Choose colors for each part
    top_color = RED
    face_color = YELLOW
    quote_color = CYAN
    border_color = MAGENTA

    # Top border
    top_border = border_color + "╔" + "═" * (width - 2) + "═╗" + RESET
    print_with_delay(top_border, 0.07)

    # Animated face
    for line in FACE:
        padded = line.center(width - 2)
        print_with_delay(face_color + "║" + padded + "║" + RESET, 0.07)

    # Quote line (centered)
    quote_line = QUOTE.center(width - 2)
    print_with_delay(border_color + "║" + quote_color + quote_line + RESET + border_color + "║" + RESET, 0.07)

    # Bottom border
    bottom_border = border_color + "╚" + "═" * (width - 2) + "═╝" + RESET
    print_with_delay(bottom_border, 0.07)

    # Optional: a little footer in green
    footer = GREEN + BOLD + " — Think about it… or don’t." + RESET
    print_with_delay(footer, 0.1)

if __name__ == "__main__":
    main()