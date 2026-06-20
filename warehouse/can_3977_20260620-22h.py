"""
Campbell's Soup Can #3977
Produced: 2026-06-20 22:34:48
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

# ANSI escape codes for colors and styles
RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
BLUE    = "\033[1;34m"
CYAN    = "\033[1;36m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

# The philosophical quote in a classic Woody Allen vein
quote = "\"I'm not afraid of death; I just don't want to be there when it happens.\""
author = "— Woody Allen (sort of)"

# Width of the ASCII box (adjustable)
width = 70

def draw_box():
    """Draw a decorative ASCII box around the quote and author."""
    top = CYAN + "╔" + ("═" * width) + "╗" + RESET
    middle_empty = CYAN + "║" + (" " * width) + "║" + RESET
    bottom = CYAN + "╚" + ("═" * width) + "╝" + RESET

    # Top border
    print(top)

    # Quote line (centered)
    padding = (width - len(quote)) // 2
    line1 = (CYAN + "║" + RESET +
             " " * padding +
             BOLD + GREEN + quote + RESET +
             " " * (width - len(quote) - padding) +
             CYAN + "║" + RESET)
    print(line1)

    # Empty line inside the box
    print(middle_empty)

    # Author line (centered)
    auth_padding = (width - len(author)) // 2
    line2 = (CYAN + "║" + RESET +
             " " * auth_padding +
             YELLOW + author + RESET +
             " " * (width - len(author) - auth_padding) +
             CYAN + "║" + RESET)
    print(line2)

    # Bottom border
    print(bottom)

def animate_print(text, delay=0.03):
    """Print text character by character for a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    # Clear the screen (works on most ANSI terminals)
    print("\033[2J", end="")
    time.sleep(0.2)

    # Show a title with a little animation
    animate_print(BOLD + BLUE + "=== WOODY'S WISDOM ===\n" + RESET, 0.05)

    # Reveal the quote box
    draw_box()

    # Conclude with a witty line
    print("\n")
    animate_print(GREEN + "And that's the depth of your existence, folks!" + RESET, 0.05)

if __name__ == "__main__":
    main()