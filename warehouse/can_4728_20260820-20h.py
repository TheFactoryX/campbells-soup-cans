"""
Campbell's Soup Can #4728
Produced: 2026-08-20 20:46:38
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import sys
import time

# ANSI escape codes for colors
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\033[2J")
    sys.stdout.write("\033[H")
    sys.stdout.flush()

def animated_print(text, delay=0.05, color=""):
    """
    Print the given text character by character with a short delay
    between characters, applying the specified color.
    """
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    # Optionally clear the screen for a clean start
    clear_screen()

    # Top border of the box
    top_border = GREEN + "╔════════════════════════════════════════════════════════════╗" + RESET
    print(top_border)

    # Empty line for spacing
    print()

    # The Woody‑Allenesque philosophical quote, wrapped in a colored frame
    quote = (
        f'{YELLOW}'
        f'{BOLD}"'
        f"I don't want the peace of mind that comes from not caring; "
        f"I want the peace of mind that comes from caring about everything, "
        f"even though it will drive me crazy."
        f'{BOLD}"'
        f'{RESET}'
    )
    animated_print(quote, delay=0.02, color=YELLOW)

    # Bottom border of the box
    print()
    bottom_border = GREEN + "╚════════════════════════════════════════════════════════════╝" + RESET
    print(bottom_border)

    # Keep the output visible briefly
    time.sleep(0.5)
    sys.stdout.flush()

if __name__ == "__main__":
    main()