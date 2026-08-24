"""
Campbell's Soup Can #4807
Produced: 2026-08-24 10:04:04
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

def typewriter(text, delay=0.07):
    """Print text character‑by‑character with random colors, no newline."""
    for ch in text:
        color = random.choice([31, 32, 33, 34, 35, 36, 37])  # ANSI foreground colors
        sys.stdout.write(f"\033[{color}m{ch}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

def main():
    quote = "I spend my life searching for meaning, only to discover that the remote control was under the couch all along."
    # Width of the box (quote + padding)
    width = len(quote) + 4

    # Top border (cyan)
    sys.stdout.write("\033[36m" + "╔" + "═" * (width - 2) + "╝\n".replace("╝", "╗") + "\033[0m")
    # Actually replace just to avoid confusion:
    sys.stdout.write("\033[36m" + "╔" + "═" * (width - 2) + "╗\n" + "\033[0m")

    # Left border, space, then the quote with typewriter effect, then space and right border
    sys.stdout.write("\033[36m║\033[0m ")
    typewriter(quote, delay=0.06)
    sys.stdout.write(" \033[36m║\033[0m\n")

    # Bottom border (cyan)
    sys.stdout.write("\033[36m" + "╚" + "═" * (width - 2) + "╝\n" + "\033[0m")

    # A goofy Woody‑Allen‑inspired ASCII bunny (magenta)
    bunny = r"""
      (\_/)
      (='.'=)   This is Woody Allen's spirit animal:
      (")_(")   A neurotic bunny contemplating existence.
    """
    for line in bunny.splitlines():
        if line.strip():
            sys.stdout.write("\033[35m" + line + "\033[0m\n")
        else:
            print()

    # Blinking underscore cursor for a bit of fun
    for _ in range(3):
        sys.stdout.write("\033[32m_\033[0m")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
        time.sleep(0.5)

    print()  # final newline

if __name__ == "__main__":
    main()