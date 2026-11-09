"""
Campbell's Soup Can #5224
Produced: 2026-11-09 06:31:18
Worker: Crouton Alpha (stealth/crouton-alpha)
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
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"


def slow_print(text, color=WHITE, delay=0.025):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()


def rain(seconds=0.9):
    chars = "|'.,:;:-~"
    end = time.time() + seconds
    while time.time() < end:
        line = "".join(
            random.choice(chars) if random.random() < 0.07 else " "
            for _ in range(70)
        )
        print(f"{DIM}{CYAN}{line}{RESET}")
        time.sleep(0.05)


def main():
    quote = (
        "I don't fear death - I fear that in the afterlife, "
        "I'll still have to make small talk, and God will know "
        "I'm faking it."
    )

    # Clean screen
    print("\033[2J\033[H", end="")

    # Manhattan rain intro
    rain()

    slow_print("  ***  NEUROTIC PHILOSOPHY  ***  ", MAGENTA + BOLD, 0.04)
    print()

    # Signature glasses
    glasses = [
        "      .--------.       .--------.",
        "     /          \\_____/          \\",
        "    |   (o)           |           (o)   |",
        "     \\_______________/     \\_______________/",
    ]
    for line in glasses:
        print(f"{CYAN}{line}{RESET}")
        time.sleep(0.09)
    print()

    slow_print("  Woody whispers, overthinking as usual...", DIM + ITALIC, 0.03)
    print()

    width = 70
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "-" * (width - 2) + "+"

    # Flashing rainbow border
    for color in [RED, YELLOW, GREEN, CYAN, MAGENTA, YELLOW]:
        sys.stdout.write(f"\r{color}{top}{RESET}")
        sys.stdout.flush()
        time.sleep(0.12)
    print()

    # Type the quote inside the box
    wrapped = textwrap.wrap(quote, width=width - 6)
    for line in wrapped:
        sys.stdout.write(f"{YELLOW}| {RESET}{CYAN}")
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.022)
        padding = " " * (width - 4 - len(line))
        sys.stdout.write(f"{RESET}{padding}{YELLOW}|{RESET}\n")

    print(f"{YELLOW}{bottom}{RESET}")
    print()

    attribution = "- a neurotic in Manhattan, probably"
    print(f"{DIM}{ITALIC}{attribution.center(width)}{RESET}")
    print()

    slow_print("  Death approaching in: 3... 2... 1... (just kidding. It's therapy.)", DIM, 0.02)


if __name__ == "__main__":
    main()