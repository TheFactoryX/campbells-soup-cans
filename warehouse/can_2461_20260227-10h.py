"""
Campbell's Soup Can #2461
Produced: 2026-02-27 10:58:47
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
One funny philosophical quote in Woody Allen's style.
Visually styled with ASCII art, colorful animation and a small finale.
Run directly – no external dependencies required.
"""

import sys
import time
import random

def random_color():
    """Return a random ANSI color code (31‑36)."""
    return f"\033[3{random.randint(1, 6)}m"

def flush():
    """Force immediate output."""
    sys.stdout.flush()

def animate(text, delay=0.01):
    """Print each character of `text` with a random color and a tiny delay."""
    for ch in text:
        print(random_color() + ch, end='', flush=flush)
        time.sleep(delay)
    print("\033[0m")  # reset all colors

def ascii_art():
    """Print a minimalist ‘philosopher’ silhouette with a little flair."""
    silhouette = [
        "   .---.   ",
        "  /     \\  ",
        " |       | ",
        " |  (•)  | ",
        " | (   ) | ",
        " |  (•)  | ",
        "  \\_____/  ",
        "    \\|/"
    ]
    for line in silhouette:
        print(random_color() + line + "\033[0m")
        time.sleep(0.12)

def main():
    # Header – the witty graphic
    ascii_art()

    # Quote – Woody Allen style
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    print("\n\033[1;35m>>> " + quote + " <<<\033[0m")

    # Animated reveal
    animate(quote, delay=0.006)

    # Final flourish – a burst of stars
    print("\n\n\033[4m* * * * * * * * * * * * * * * * * * * * * * * * * * * * *\033[0m")
    print("\033[1;30m...and then the universe sighed.\033[0m")

if __name__ == "__main__":
    main()