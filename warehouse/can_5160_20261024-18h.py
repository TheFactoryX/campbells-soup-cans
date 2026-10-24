"""
Campbell's Soup Can #5160
Produced: 2026-10-24 18:09:41
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

# ANSI color palette
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

QUOTE = (
    "I don't believe in an afterlife, although I am bringing a change of "
    "underwear just in case. Also, I'd like the universe to know that I'm "
    "available for commitment—just not to anything that requires effort."
)

ATTRIBUTION = "— Woody Allen (probably, if he wore better socks)"

WIDTH = 62


def slow_type(text, color, delay=0.025):
    """Print text character by character like a neurotic typewriter."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    # Neurotic ASCII face montage
    faces = [
        (CYAN, "   (o.o)   "),
        (MAGENTA, "   (>.<)   "),
        (YELLOW, "   (o.O)   "),
        (RED, "   (x.x)   "),
    ]

    print(BOLD + CYAN + "╔══════════════════════════════════════════════╗" + RESET)
    for color, face in faces:
        print(color + BOLD + face.center(46) + RESET)
        time.sleep(0.2)
    print(BOLD + CYAN + "╚══════════════════════════════════════════════╝" + RESET)
    print()

    # Existential spinner
    spins = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(25):
        sys.stdout.write(f"\r{MAGENTA}{spins[i % len(spins)]} Contemplating mortality...{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")

    # Box the quote
    wrapped = textwrap.wrap(QUOTE, width=WIDTH - 4)
    box_lines = wrapped + ["", ATTRIBUTION]

    print(YELLOW + "╔" + "═" * (WIDTH - 2) + "╗" + RESET)
    for line in box_lines:
        padded = line.ljust(WIDTH - 2)
        print(f"{YELLOW}║{RESET}{WHITE}{padded}{RESET}{YELLOW}║{RESET}")
    print(YELLOW + "╚" + "═" * (WIDTH - 2) + "╝" + RESET)

    print()
    slow_type("Existential dread successfully packaged. ", GREEN, delay=0.03)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "Aborted by user. Even the void needs a timeout." + RESET)
        sys.exit(0)