"""
Campbell's Soup Can #4133
Produced: 2026-07-09 01:02:35
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

# ANSI color codes (foreground)
COLORS = [31, 32, 33, 34, 35, 36, 37]  # red, green, yellow, blue, magenta, cyan, white


def color_text(ch: str, code: int) -> str:
    """Return a single character wrapped in ANSI color code."""
    return f"\033[{code}m{ch}\033[0m"


def print_animated(line: str, delay: float = 0.04) -> None:
    """Print a line character‑by‑character with cycling colors."""
    for idx, ch in enumerate(line):
        sys.stdout.write(color_text(ch, COLORS[idx % len(COLORS)]))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def main() -> None:
    # Woody Allen‑style quote (original)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    padding = 2  # one space on each side inside the box
    inner_width = len(quote) + padding
    top_border = "╔" + "═" * inner_width + "╗"
    bottom_border = "╚" + "═" * inner_width + "╝"
    quoted_line = " " + quote + " "

    # Animated output
    print_animated(top_border, 0.03)
    time.sleep(0.15)
    print_animated(quoted_line, 0.04)
    time.sleep(0.15)
    print_animated(bottom_border, 0.03)


if __name__ == "__main__":
    main()