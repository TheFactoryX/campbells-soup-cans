"""
Campbell's Soup Can #2185
Produced: 2026-02-12 16:09:44
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# -------------------------------------------------
# ASCII art box (fixed width 70 characters)
# -------------------------------------------------
def print_box(width: int = 70) -> None:
    top    = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"
    middle = "║" + " " * (width - 2) + "║"
    sys.stdout.write(top + "\n")
    sys.stdout.write(middle + "\n")
    sys.stdout.write(middle + "\n")
    sys.stdout.write(middle + "\n")
    sys.stdout.write(bottom + "\n")
    sys.stdout.flush()


# -------------------------------------------------
# Typewriter‑style print with random foreground colors
# -------------------------------------------------
def colorful_print(text: str) -> None:
    fg = [30, 31, 32, 33, 34, 35, 36, 37]          # ANSI colors
    words = text.split()
    colored_words = [
        f"\033[{random.choice(fg)}m{word}\033[0m"
        for word in words
    ]
    line = " ".join(colored_words)
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.02)  # slow‑type effect


# -------------------------------------------------
# Main routine
# -------------------------------------------------
def main() -> None:
    # Clear the terminal screen
    sys.stdout.write("\033[2J")
    sys.stdout.flush()

    # Draw the decorative box
    print_box()

    # Header + the Woody‑Allen style quote
    sys.stdout.write("\nWoody Allen's philosophical gem:\n")
    sys.stdout.flush()

    quote = (
        "I'm not a pessimist; I'm just a realist with a very bad sense of humor "
        "about the universe."
    )
    colorful_print(quote)

    # Keep the final picture for a beat before exiting
    time.sleep(1)
    sys.stdout.flush()


if __name__ == "__main__":
    main()