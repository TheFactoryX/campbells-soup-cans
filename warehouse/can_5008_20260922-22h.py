"""
Campbell's Soup Can #5008
Produced: 2026-09-22 22:09:32
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import itertools

def color(text: str, code: str) -> str:
    """Wrap text in ANSI color code."""
    return f"\033[{code}m{text}\033[0m"

def main() -> None:
    # Woody Allen‑style quote (original)
    quote = "I'm not afraid of dying; I just don't want to be there when it happens."

    # Build a simple box around the quote
    width = len(quote)
    top    = "╔" + "═" * (width + 2) + "╗"
    middle = f"║  {quote}  ║"
    bottom = "╚" + "═" * (width + 2) + "╝"

    # --- Spinner intro (just for fun) ---
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    for _ in range(20):
        sys.stdout.write('\r' + color(next(spinner), '33'))  # yellow spinner
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write('\r' + ' ' * 10 + '\r')  # clear spinner
    sys.stdout.flush()

    # --- Print the box with cycling colors ---
    colors = ['31', '32', '33', '34', '35', '36']  # red, green, yellow, blue, magenta, cyan
    for i, line in enumerate([top, middle, bottom]):
        col = colors[i % len(colors)]
        print(color(line, col))
        time.sleep(0.12)  # slight pause for visual effect

if __name__ == "__main__":
    main()