"""
Campbell's Soup Can #3088
Produced: 2026-04-02 11:10:42
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

# ANSI escape codes for colors and effects
RESET   = "\033[0m"
BOLD    = "\033[1m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def typewriter(text, color=WHITE, delay=0.03):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the quote

def main():
    clear_screen()

    # Simple ASCII art: a neurotic brain/cloud
    art_lines = [
        "          .-.          ",
        "         (   )         ",
        "          '-'          ",
        "        .-´ `-.        ",
        "       /       \\       ",
        "      |  o   o  |      ",
        "      |    ^    |      ",
        "      |   '-'   |      ",
        "       \\  '-'  /       ",
        "        '-.....-'      "
    ]

    # Print the art with a slight delay, cycling colors
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
    for i, line in enumerate(art_lines):
        sys.stdout.write(colors[i % len(colors)] + line + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.07)

    print()  # space before quote

    # Woody Allen‑style philosophical quote
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "That's the part that makes me nervous — like showing up late to your own funeral."
    )

    # Typewriter effect in bright white on a dark background (inverse video)
    sys.stdout.write("\033[7m")  # invert colors
    typewriter(quote, color=WHITE, delay=0.05)
    sys.stdout.write(RESET)      # reset invert

if __name__ == "__main__":
    main()