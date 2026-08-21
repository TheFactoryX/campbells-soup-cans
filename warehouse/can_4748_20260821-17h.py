"""
Campbell's Soup Can #4748
Produced: 2026-08-21 17:45:05
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

# Box drawing characters
TOP_LEFT = "╔"
TOP_RIGHT = "╗"
BOTTOM_LEFT = "╚"
BOTTOM_RIGHT = "╝"
HORIZONTAL = "═"
VERTICAL = "║"

def typewriter(text: str, color: str = WHITE, delay: float = 0.03) -> None:
    """Print text with a typewriter effect."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def main() -> None:
    width = 60  # inner width of the box
    quote = (
        "Life is like a poorly written script: you keep hoping for a plot twist, "
        "but all you get is more existential dread and free refills."
    )
    # Center the quote within the inner width
    pad_left = (width - len(quote)) // 2
    pad_right = width - len(quote) - pad_left
    inner_quote_line = " " * pad_left + quote + " " * pad_right
    empty_line = " " * width

    # Top border
    sys.stdout.write(CYAN + TOP_LEFT + HORIZONTAL * width + TOP_RIGHT + RESET + "\n")
    time.sleep(0.2)

    # First empty line
    sys.stdout.write(CYAN + VERTICAL + RESET)
    typewriter(empty_line, color=WHITE, delay=0.001)
    sys.stdout.write(CYAN + VERTICAL + RESET + "\n")
    time.sleep(0.2)

    # Quote line
    sys.stdout.write(CYAN + VERTICAL + RESET)
    typewriter(inner_quote_line, color=YELLOW, delay=0.02)
    sys.stdout.write(CYAN + VERTICAL + RESET + "\n")
    time.sleep(0.2)

    # Second empty line
    sys.stdout.write(CYAN + VERTICAL + RESET)
    typewriter(empty_line, color=WHITE, delay=0.001)
    sys.stdout.write(CYAN + VERTICAL + RESET + "\n")
    time.sleep(0.2)

    # Bottom border
    sys.stdout.write(CYAN + BOTTOM_LEFT + HORIZONTAL * width + BOTTOM_RIGHT + RESET + "\n")

if __name__ == "__main__":
    main()