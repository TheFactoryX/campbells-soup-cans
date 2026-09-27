"""
Campbell's Soup Can #5034
Produced: 2026-09-27 18:24:46
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

# ANSI color codes
MAGENTA_BOLD = "\033[35;1m"
CYAN_BOLD    = "\033[36;1m"
RESET        = "\033[0m"

def slow_print(text, delay=0.05):
    """Print text character‑by‑character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # Woody Allen‑style quote (original)
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    # Padding inside the box
    inner = " " + quote + " "
    box_width = len(inner)

    # Top border
    sys.stdout.write(MAGENTA_BOLD + "╔" + "═" * box_width + "╗" + RESET + "\n")
    # Left border
    sys.stdout.write(MAGENTA_BOLD + "║" + RESET)
    # Quote with typewriter effect in cyan
    for ch in inner:
        sys.stdout.write(CYAN_BOLD + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    # Right border and newline
    sys.stdout.write(MAGENTA_BOLD + "║" + RESET + "\n")
    # Bottom border
    sys.stdout.write(MAGENTA_BOLD + "╚" + "═" * box_width + "╝" + RESET + "\n")

if __name__ == "__main__":
    main()