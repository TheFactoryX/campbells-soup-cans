"""
Campbell's Soup Can #4275
Produced: 2026-07-21 03:48:19
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

def type_text(text, delay=0.07):
    """Print text with a type‑writer effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # finish with a newline

def main():
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"

    # Clear the terminal screen
    print("\033[2J\033[H", end="")

    width = 58  # interior width of the box

    # Top border
    print(CYAN + BOLD + "╔" + "═" * width + "╗" + RESET)
    # Empty line inside box
    print(CYAN + BOLD + "║" + " " * width + "║" + RESET)

    # Woody Allen‑style quote
    quote = "I’m not afraid of death; I just don’t want to be the punchline."
    type_text(MAGENTA + BOLD + quote + RESET, delay=0.06)

    # Empty line inside box
    print(CYAN + BOLD + "║" + " " * width + "║" + RESET)
    # Bottom border
    print(CYAN + BOLD + "╚" + "═" * width + "╝" + RESET)

if __name__ == "__main__":
    main()