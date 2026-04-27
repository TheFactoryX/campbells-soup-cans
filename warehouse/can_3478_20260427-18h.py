"""
Campbell's Soup Can #3478
Produced: 2026-04-27 18:19:46
Worker: Tencent: Hy3 preview (free) (tencent/hy3-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Prints a Woody Allen-style philosophical quote with visual flair.
Uses ANSI colors and a typewriter effect inside a decorative box.
"""

import sys
import time

# ANSI escape codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J\033[H"

def main():
    # The quote (crafted in Woody Allen's neurotic, existential style)
    quote = "I've decided to embrace existentialism—mainly because it gives me an excuse to stay in bed."
    raw_len = len(quote)

    # Box dimensions: interior padding of one space on each side
    interior = raw_len + 2
    top = f"{CYAN}┌{'─'*interior}┐{RESET}"
    left = f"{CYAN}│{RESET} "          # left border + one space
    right = f" {CYAN}│{RESET}"        # one space + right border
    bottom = f"{CYAN}└{'─'*interior}┘{RESET}"

    # Clear the screen for a dramatic start
    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.flush()
    time.sleep(0.5)

    # Draw the top border
    print(top)
    time.sleep(0.2)

    # Draw the left border (no newline)
    sys.stdout.write(left)
    sys.stdout.flush()
    time.sleep(0.3)

    # Type the quote in yellow, character by character
    sys.stdout.write(YELLOW)
    for ch in quote:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.04)   # typing speed
    sys.stdout.write(RESET)
    sys.stdout.flush()

    # Add the right border and move to the next line
    print(right)   # includes newline
    time.sleep(0.2)

    # Draw the bottom border
    print(bottom)

    # Add a little breathing room
    print()

if __name__ == "__main__":
    main()