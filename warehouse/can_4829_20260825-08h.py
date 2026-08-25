"""
Campbell's Soup Can #4829
Produced: 2026-08-25 08:59:55
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

# ANSI color definitions
MAGENTA = "\033[1;35m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def main():
    # Clear the terminal screen
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

    # The Woody‑Allen‑style philosophical quote
    quote = "Deep down, I suspect the cosmos is a bad sitcom, and we're the punchline—no one else even notices."

    # Box dimensions
    width = 80

    # ASCII box elements
    top = f"{MAGENTA}╔{'═' * width}╗{RESET}"
    bottom = f"{MAGENTA}╚{'═' * width}╝{RESET}"
    empty = f"{MAGENTA}║{' ' * width}║{RESET}"
    border_left = f"{MAGENTA}║{RESET}"
    border_right = f"{MAGENTA}║{RESET}"

    # Display the box
    print(top)
    print(empty)

    # Print the quote with a typewriter animation
    sys.stdout.write(border_left)
    sys.stdout.write("  ")                     # left padding
    for ch in quote:
        sys.stdout.write(YELLOW + ch + RESET)  # quote in yellow
        sys.stdout.flush()
        time.sleep(0.05)                       # typing delay
    sys.stdout.write("  ")                     # right padding
    sys.stdout.write(border_right)
    print()                                    # newline

    print(empty)
    print(bottom)

if __name__ == "__main__":
    main()