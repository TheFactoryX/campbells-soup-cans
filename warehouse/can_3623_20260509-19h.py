"""
Campbell's Soup Can #3623
Produced: 2026-05-09 19:33:19
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

def typewriter(text, delay=0.05):
    """Print text with a typewriter effect, cycling through colors."""
    colors = [
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[96m",  # Cyan
        "\033[95m",  # Magenta
        "\033[94m",  # Blue
    ]
    color_cycle = iter(colors * ((len(text) // len(colors)) + 1))
    for ch in text:
        sys.stdout.write(next(color_cycle) + ch + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # Woody Allen‑style quote (original)
    quote = "Life is a tragic comedy written in small print, and I lost my glasses."

    # Box dimensions
    padding = 2
    width = len(quote) + 2 * padding
    top_bottom = "╔" + "═" * width + "╗"
    sides = "║" + " " * width + "║"

    # Print top border
    print(top_bottom)
    # Print empty line for vertical padding
    for _ in range(padding):
        print(sides)
    # Print the quote line with typewriter effect
    sys.stdout.write("║" + " " * padding)
    sys.stdout.flush()
    typewriter(quote, delay=0.07)
    sys.stdout.write(" " * padding + "║\n")
    sys.stdout.flush()
    # Print bottom padding lines
    for _ in range(padding):
        print(sides)
    # Print bottom border
    print(top_bottom)

if __name__ == "__main__":
    main()