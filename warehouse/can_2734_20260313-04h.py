"""
Campbell's Soup Can #2734
Produced: 2026-03-13 04:55:13
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import timeimport random

# ANSI color codes
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m",  # Bright Cyan
]
RESET = "\033[0m"

def main():
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    # Calculate box width: 2 spaces + quote + 2 spaces
    width = len(quote) + 4
    top_border = "╔" + "═" * (width - 2) + "╗"
    bottom_border = "╚" + "═" * (width - 2) + "╝"

    # Print top border in bright cyan
    print("\033[96m" + top_border + RESET)

    # Left border
    sys.stdout.write("\033[96m║ " + RESET)

    # Print each character of the quote with a random color and a typewriter delay
    for ch in quote:
        color = random.choice(COLORS)
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.06)  # typing speed

    # Right border and newline
    sys.stdout.write(" ║" + RESET)
    print()  # move to next line after the box content

    # Bottom border in bright cyan    print("\033[96m" + bottom_border + RESET)

if __name__ == "__main__":
    main()