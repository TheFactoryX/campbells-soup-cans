"""
Campbell's Soup Can #3463
Produced: 2026-04-26 15:57:46
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
import textwrap

# Woody Allen‑style quote (original)
QUOTE = (
    "I don't want to achieve immortality through my work; "
    "I want to achieve it by not dying — preferably while still wearing matching socks."
)

# ANSI color codes (bright foreground)
COLORS = [91, 92, 93, 94, 95, 96]  # red, green, yellow, blue, purple, cyan
RESET = "\x1b[0m"

def type_line(line: str, delay: float = 0.04):
    """Print a line character‑by‑character with random colors."""
    for ch in line:
        if ch == " ":
            sys.stdout.write(ch)
        else:
            color = random.choice(COLORS)
            sys.stdout.write(f"\x1b[{color}m{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def main():
    width = 58  # box inner width
    # Wrap the quote to fit inside the box
    wrapped = textwrap.wrap(QUOTE, width=width)

    # Top border
    top = "\x1b[95m╔" + "═" * (width + 2) + "╗" + RESET
    # Bottom border
    bottom = "\x1b[95m╚" + "═" * (width + 2) + "╝" + RESET

    print(top)
    for line in wrapped:
        # Add padding spaces inside the box
        padded = f" {line.ljust(width)} "
        type_line(padded, delay=0.03)
        time.sleep(0.1)  # slight pause between lines
    print(bottom)

if __name__ == "__main__":
    main()