"""
Campbell's Soup Can #3775
Produced: 2026-05-24 17:16:10
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

def typewriter(text: str, color: str = WHITE, delay: float = 0.05) -> None:
    """Print text character by character with a slight delay (typewriter effect)."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the whole string

def main() -> None:
    # Woody Allen‑style philosophical quote (original)
    quote = "I'm not afraid of dying; I just don't want to be there when it happens, especially if there's no Wi‑Fi."

    # Create a simple box around the quote
    inner_width = len(quote) + 4          # 2 spaces on each side + the quote
    horizontal = "═" * (inner_width - 2)  # minus the two corner characters
    top_border = f"╔{horizontal}╗"
    bottom_border = f"╚{horizontal}╝"
    quote_line = f"║  {quote}  ║"

    # Display with colors and a typewriter effect
    typewriter(top_border, CYAN, 0.001)
    typewriter(quote_line, YELLOW, 0.05)
    typewriter(bottom_border, CYAN, 0.001)

if __name__ == "__main__":
    main()