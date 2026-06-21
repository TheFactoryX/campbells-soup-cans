"""
Campbell's Soup Can #3980
Produced: 2026-06-21 10:46:24
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import sys
import time

def hide_cursor():
    """Hide the blinking cursor for a more theatrical feel."""
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    """Restore the cursor after the performance."""
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def draw_box(text, width=70):
    """
    Draw a decorative Unicode box around the given text.
    The box is colored using bright magenta.
    """
    # Top border
    print(f"\033[1;35m╔{'═' * width}╗\033[0m")
    # Split text into lines no longer than `width`
    while len(text) > width:
        line = text[:width]
        print(f"\033[1;35m║ \033[0m{line.ljust(width)} \033[1;35m║\033[0m")
        text = text[width:]
    # Remaining line (or empty)
    print(f"\033[1;35m║ \033[0m{text.ljust(width)} \033[1;35m║\033[0m")
    # Bottom border
    print(f"\033[1;35m╚{'═' * width}╝\033[0m")

def main():
    hide_cursor()
    time.sleep(0.2)   # Brief pause before the show

    # Fun intro with a splash of color
    print("\033[1;32m♪ The Woody Allen Time‑Travelling Coffee Machine is brewing... ♪\033[0m")
    time.sleep(0.8)

    # Our single philosophical quote – neurotic, self‑deprecating, existential
    quote = "I'm terrified of death because I'm not sure I've even begun to live."

    draw_box(quote)

    # Reveal the cursor and a polite sign‑off
    show_cursor()
    time.sleep(0.5)
    print("\033[1;34m--- End of philosophical espresso ---\033[0m")

if __name__ == "__main__":
    main()