"""
Campbell's Soup Can #5240
Produced: 2026-11-14 03:16:32
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"

def slow_print(text: str, color: str = None, delay: float = 0.04) -> None:
    """Print text character by character with an optional color."""
    for ch in text:
        sys.stdout.write(color + ch + RESET if color else ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main() -> None:
    # Set box width (must be larger than the quote)
    width = 100

    # Woody‑Allen‑style quote (self‑deprecating, neurotic, existential)
    quote = "\"I'm terrified of silence; it's like the universe is on a coffee break, and I'm left to contemplate my own existence while the planets revolve around my mediocrity.\""

    # --- Top decorative line ---
    print(CYAN + "═" * width + RESET)

    # --- Coffee cup ASCII art (Woody's favorite fuel) ---
    coffee = [
        "   /\\   ",
        "  /  \\  ",
        "  |[]|  ",
        "  |__|  "
    ]
    for line in coffee:
        print(GREEN + line + RESET)

    # --- Separator ---
    print(CYAN + "─" * width + RESET)

    # --- Boxed quote ---
    # Build left/right padding to center the quote inside the box
    padding_needed = width - 2 - len(quote)
    left_pad = " " * (padding_needed // 2)
    right_pad = " " * (padding_needed - len(left_pad))

    # Top border of the quote box
    print(CYAN + "+" + "-" * width + "+" + RESET)

    # Print the quote with a subtle typing effect
    print(CYAN + "|" + RESET, end="")
    slow_print(left_pad + YELLOW + quote + RESET + right_pad, color=None)
    print(CYAN + "|" + RESET)

    # Bottom border of the quote box
    print(CYAN + "+" + "-" * width + "+" + RESET)

    # --- Concluding line (animated pondering) ---
    print()
    print(RED + "— (or at least someone who wishes they were a bit more philosophical)" + RESET)
    sys.stdout.write(" pondering" + RESET)
    for i in range(3):
        sys.stdout.write("." * (i + 1))
        sys.stdout.flush()
        time.sleep(0.5)
    print(RESET)

if __name__ == "__main__":
    main()